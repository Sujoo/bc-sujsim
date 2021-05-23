from unittest import TestCase

from sujsim.ai.decision_model import FireballSpam, ArcaneBlastSpam, DoNothing, FakeTestingSpam, ArcaneMissleSpam, EvocateSpam
from sujsim.core.spells.buff_database import combat_buffs, player_buffs
from sujsim.core.items.gear_database import head, neck, back, wrist, weapon, off_hand, hands, wand, legs, feet, ring, waist, shoulder, chest, trinket
from sujsim.core.stats.gear_stats import GearStats
from sujsim.core.character.character import Character
from sujsim.core.character.race import Race
from sujsim.core.talents.mage_talents import MageTalents
from sujsim.sim.actor import Actor
from sujsim.sim.simulation import Simulation


def get_character(talents='-5-') -> Character:
    gear_stats = GearStats(head=head.INCANTERS_COWL,
                           neck=neck.BROOCH_OF_HEIGHTENED_POTENTIAL,
                           shoulder=shoulder.INCANTERS_PAULDRONS,
                           back=back.CLOAK_OF_WOVEN_ENERGY,
                           chest=chest.INCANTERS_ROBE,
                           wrist=wrist.CRIMSON_BRACERS_OF_GLOOM,
                           main_hand=weapon.GREATSWORD_OF_HORRID_DREAMS,
                           off_hand=off_hand.LAMP_OF_PEACEFUL_RADIANCE,
                           wand=wand.NETHER_CORES_CONTROL_ROD,
                           hands=hands.INCANTERS_GLOVES,
                           waist=waist.ADALS_GIFT,
                           legs=legs.INCANTERS_TROUSERS,
                           feet=feet.SIGIL_LACED_BOOTS,
                           ring_1=ring.MANASTORM_BAND,
                           ring_2=ring.RING_OF_CONFLICT_SURVIVAL,
                           trinket_1=trinket.FIGURINE_LIVING_RUBY_SERPENT,
                           trinket_2=trinket.SHIFFARS_NEXUS_HORN)
    return Character(name='Sujoo', race=Race.UNDEAD, gear_stats=gear_stats, mage_talents=MageTalents(talents), buffs=[player_buffs.MAGE_ARMOR])


def get_boss() -> Character:
    return Character(name='Boss', race=Race.UNDEAD, gear_stats=GearStats(), mage_talents=MageTalents('--'), buffs=[])


class ActorTest(TestCase):
    def test_actor(self):
        character = get_character()
        actor = Actor(character=character, decision_model_class=FireballSpam)
        actor.setup(logs=[], end_of_simulation=4, boss=None)
        self.assertEqual(4, len(actor.event_queue))

    def test_actor_add_buff(self):
        character = get_character()
        actor = Actor(character=character, decision_model_class=FireballSpam)
        actor.add_buff(combat_buffs.ARCANE_BLAST)
        self.assertEqual(['Mage Armor', 'Arcane Blast'], [buff.name for buff in actor.character.buffs])
        self.assertEqual(combat_buffs.ARCANE_BLAST.db_id, actor.character.buffs[1].db_id)

    def test_actor_stack_buff(self):
        character = get_character()
        actor = Actor(character=character, decision_model_class=FireballSpam)
        actor.add_buff(combat_buffs.ARCANE_BLAST)
        actor.add_buff(combat_buffs.ARCANE_BLAST)
        actor.add_buff(combat_buffs.ARCANE_BLAST)
        actor.add_buff(combat_buffs.ARCANE_BLAST)
        self.assertEqual(2, len(actor.character.buffs))
        self.assertEqual(3, actor.character.buffs[1].stacks)
        self.assertEqual(1, combat_buffs.ARCANE_BLAST.stacks)  # Ensure original object is not modified

    def test_actor_remove_buff(self):
        character = get_character()
        actor = Actor(character=character, decision_model_class=FireballSpam)
        actor.add_buff(combat_buffs.ARCANE_BLAST)
        actor.add_buff(combat_buffs.ARCANE_BLAST)
        actor.add_buff(combat_buffs.PRESENCE_OF_MIND)
        actor.remove_buff(combat_buffs.ARCANE_BLAST)
        actor.add_buff(combat_buffs.PRESENCE_OF_MIND)
        self.assertEqual(2, len(actor.character.buffs))
        self.assertEqual(combat_buffs.PRESENCE_OF_MIND.db_id, actor.character.buffs[1].db_id)


class SimulatorTest(TestCase):
    def test_sim_fireball(self):
        expected = ['[0.0] LOG_BUFF: GCD[1] gained',
                    '[0.0] LOG_BUFF: Casting 5 Second Rule[1] gained',
                    '[1.5] LOG_BUFF: GCD lost',
                    '[2.0] LOG_MANA: 28 Mana Regen',
                    "[3.0] LOG_SPELL: Sujoo's Fireball is a MISS",
                    '[3.0] LOG_MANA: 465 Mana Lost',
                    '[3.0] LOG_BUFF: GCD[1] gained',
                    '[3.0] LOG_BUFF: Casting 5 Second Rule[1] refreshed',
                    '[4.0] LOG_MANA: 28 Mana Regen',
                    '[4.5] LOG_BUFF: GCD lost',
                    '[5.0] LOG_WAIT: Waiting',
                    "[6.0] LOG_SPELL: Sujoo's Fireball is a HIT",
                    '[6.0] LOG_MANA: 465 Mana Lost',
                    '[6.0] LOG_BUFF: GCD[1] gained',
                    "[6.0] LOG_DAMAGE: Sujoo's Fireball HITs Boss for 1270",
                    '[6.0] LOG_MANA: 28 Mana Regen',
                    '[6.0] LOG_BUFF: Casting 5 Second Rule[1] refreshed',
                    '[7.5] LOG_BUFF: GCD lost',
                    '[8.0] LOG_MANA: 28 Mana Regen',
                    "[9.0] LOG_SPELL: Sujoo's Fireball is a CRIT",
                    '[9.0] LOG_MANA: 465 Mana Lost',
                    "[9.0] LOG_DAMAGE: Sujoo's Fireball CRITs Boss for 2079",
                    '[10.0] LOG_WAIT: Waiting',
                    '[10.0] LOG_MANA: 28 Mana Regen']
        player = get_character(talents='05-505002012003-003')
        player.add_buff(combat_buffs.DEBUG)
        player = Actor(character=player, decision_model_class=FireballSpam)
        boss = Actor(character=get_boss(), decision_model_class=DoNothing)
        sim = Simulation(player=player, boss=boss, end_of_simulation=15, seed=8)
        sim.run()

        self.assertEqual(expected, [str(log_entry) for log_entry in sim.logs])
        self.assertEqual(7173, player.character.stats.current_mana)

    def test_sim_arcane(self):
        expected = ['[0.0] LOG_BUFF: GCD[1] gained',
                    '[0.0] LOG_BUFF: Casting 5 Second Rule[1] gained',
                    '[1.5] LOG_BUFF: GCD lost',
                    '[2.0] LOG_MANA: 28 Mana Regen',
                    '[2.5] LOG_BUFF: Arcane Blast[1] gained',
                    "[2.5] LOG_SPELL: Sujoo's Arcane Blast is a HIT",
                    '[2.5] LOG_MANA: 195 Mana Lost',
                    '[2.5] LOG_BUFF: GCD[1] gained',
                    "[2.5] LOG_DAMAGE: Sujoo's Arcane Blast HITs Sujoo for 840",
                    '[2.5] LOG_BUFF: Casting 5 Second Rule[1] refreshed',
                    '[4.0] LOG_BUFF: GCD lost',
                    '[4.0] LOG_MANA: 28 Mana Regen',
                    '[4.67] LOG_BUFF: Arcane Blast[2] gained',
                    "[4.67] LOG_SPELL: Sujoo's Arcane Blast is a HIT",
                    '[4.67] LOG_MANA: 341 Mana Lost',
                    '[4.67] LOG_BUFF: GCD[1] gained',
                    "[4.67] LOG_DAMAGE: Sujoo's Arcane Blast HITs Sujoo for 1022",
                    '[4.67] LOG_BUFF: Casting 5 Second Rule[1] refreshed',
                    '[5.0] LOG_WAIT: Waiting',
                    '[6.0] LOG_MANA: 28 Mana Regen',
                    '[6.17] LOG_BUFF: GCD lost',
                    '[6.5] LOG_BUFF: Arcane Blast[3] gained',
                    "[6.5] LOG_SPELL: Sujoo's Arcane Blast is a CRIT",
                    '[6.5] LOG_MANA: 488 Mana Lost',
                    '[6.5] LOG_BUFF: GCD[1] gained',
                    "[6.5] LOG_DAMAGE: Sujoo's Arcane Blast CRITs Sujoo for 1559",
                    '[6.5] LOG_BUFF: Casting 5 Second Rule[1] refreshed',
                    '[8.0] LOG_BUFF: GCD lost',
                    '[8.0] LOG_MANA: 28 Mana Regen',
                    '[8.0] LOG_BUFF: Arcane Blast[3] refreshed',
                    "[8.0] LOG_SPELL: Sujoo's Arcane Blast is a HIT",
                    '[8.0] LOG_MANA: 634 Mana Lost',
                    '[8.0] LOG_BUFF: GCD[1] gained',
                    "[8.0] LOG_DAMAGE: Sujoo's Arcane Blast HITs Sujoo for 1092",
                    '[8.0] LOG_BUFF: Casting 5 Second Rule[1] refreshed',
                    '[9.5] LOG_BUFF: GCD lost',
                    '[9.5] LOG_BUFF: Arcane Blast[3] refreshed',
                    "[9.5] LOG_SPELL: Sujoo's Arcane Blast is a HIT",
                    '[9.5] LOG_MANA: 634 Mana Lost',
                    '[9.5] LOG_BUFF: GCD[1] gained',
                    "[9.5] LOG_DAMAGE: Sujoo's Arcane Blast HITs Sujoo for 1117",
                    '[9.5] LOG_BUFF: Casting 5 Second Rule[1] refreshed',
                    '[10.0] LOG_WAIT: Waiting',
                    '[10.0] LOG_MANA: 28 Mana Regen',
                    '[11.0] LOG_BUFF: GCD lost',
                    '[11.0] LOG_BUFF: Arcane Blast[3] refreshed',
                    "[11.0] LOG_SPELL: Sujoo's Arcane Blast is a CRIT",
                    '[11.0] LOG_MANA: 634 Mana Lost',
                    "[11.0] LOG_DAMAGE: Sujoo's Arcane Blast CRITs Sujoo for 1648",
                    '[12.0] LOG_MANA: 28 Mana Regen']
        character = get_character()
        player = Actor(character=character, decision_model_class=ArcaneBlastSpam)
        character = get_character()
        boss = Actor(character=character, decision_model_class=DoNothing)
        sim = Simulation(player=player, boss=boss, end_of_simulation=12, seed=5)
        sim.run()

        self.assertEqual(expected, [str(log_entry) for log_entry in sim.logs])
        self.assertEqual(5670, player.character.stats.current_mana)

    def test_sim_gcd(self):
        expected = ['[0.0] LOG_BUFF: GCD[1] gained',
                    '[0.0] LOG_BUFF: Casting 5 Second Rule[1] gained',
                    "[1.0] LOG_SPELL: Sujoo's GCD Spell is a HIT",
                    '[1.0] LOG_MANA: 0 Mana Lost',
                    "[1.0] LOG_DAMAGE: Sujoo's GCD Spell HITs Sujoo for 0",
                    '[1.05] LOG_WAIT: Waiting',
                    '[1.1] LOG_WAIT: Waiting',
                    '[1.15] LOG_WAIT: Waiting',
                    '[1.2] LOG_WAIT: Waiting',
                    '[1.25] LOG_WAIT: Waiting',
                    '[1.3] LOG_WAIT: Waiting',
                    '[1.35] LOG_WAIT: Waiting',
                    '[1.4] LOG_WAIT: Waiting',
                    '[1.45] LOG_WAIT: Waiting',
                    '[1.5] LOG_BUFF: GCD lost',
                    '[1.5] LOG_WAIT: Waiting']
        character = get_character()
        player = Actor(character=character, decision_model_class=FakeTestingSpam)
        character = get_character()
        boss = Actor(character=character, decision_model_class=DoNothing)
        sim = Simulation(player=player, boss=boss, end_of_simulation=1.9)
        sim.run()

        self.assertEqual(expected, [str(log_entry) for log_entry in sim.logs])
        self.assertEqual(8456, player.character.stats.current_mana)

    def test_sim_arcane_missiles(self):
        expected = ['']
        character = get_character()
        player = Actor(character=character, decision_model_class=ArcaneMissleSpam)
        boss = Actor(character=get_boss(), decision_model_class=DoNothing)
        sim = Simulation(player=player, boss=boss, end_of_simulation=11)
        sim.run()

        self.assertEqual(expected, [str(log_entry) for log_entry in sim.logs])
        self.assertEqual(8456, player.character.stats.current_mana)

    def test_sim_evocation(self):
        expected = ['']
        character = get_character()
        player = Actor(character=character, decision_model_class=EvocateSpam)
        boss = Actor(character=get_boss(), decision_model_class=DoNothing)
        sim = Simulation(player=player, boss=boss, end_of_simulation=60)
        sim.run()

        self.assertEqual(expected, [str(log_entry) for log_entry in sim.logs])
        self.assertEqual(8456, player.character.stats.current_mana)
