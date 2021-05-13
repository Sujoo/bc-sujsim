from unittest import TestCase

from sujsim.core.spells.buff_database import player_buffs, combat_buffs
from sujsim.core.items.gear_database import head, neck, back, wrist, weapon, off_hand, hands, wand, legs, feet, ring
from sujsim.core.items.gear_database import waist, shoulder, chest, trinket
from sujsim.core.spells.spell_database import mage_spells
from sujsim.core.stats.gear_stats import GearStats
from sujsim.core.character.character import Character
from sujsim.core.character.race import Race
from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.talents.mage_talents import MageTalents


class PlayerTest(TestCase):
    @staticmethod
    def get_gear_set() -> GearStats:
        return GearStats(head=head.INCANTERS_COWL,
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

    def test_init_player(self):
        player = Character(name='Sujoo', race=Race.UNDEAD, gear_stats=self.get_gear_set(), mage_talents=MageTalents('--'), buffs=[])
        self.assertEqual('Sujoo', player.name)
        self.assertEqual(Race.UNDEAD, player.race)
        self.assertEqual(8456, player.stats.max_mana)
        self.assertEqual(433, player.stats.intellect)
        self.assertEqual(87, player.gear_stats.stats.spirit)
        self.assertEqual(237, player.stats.spirit)
        self.assertEqual(492, player.stats.spell_stats_dict[MagicSchool.FIRE].spell_power)
        self.assertEqual(55, player.stats.spell_stats_dict[MagicSchool.FIRE].spell_hit_rating)
        self.assertEqual(0.87, player.stats.spell_stats_dict[MagicSchool.FIRE].spell_hit_chance)
        self.assertEqual(330, player.stats.spell_stats_dict[MagicSchool.FIRE].spell_crit_rating)
        self.assertEqual(14.95, player.stats.spell_stats_dict[MagicSchool.FIRE].spell_crit_chance)
        self.assertEqual(0, player.stats.spell_stats_dict[MagicSchool.FIRE].spell_haste_rating)
        self.assertEqual(0, player.stats.mp_5)

    def test_buffs_int(self):
        player = Character(name='Sujoo',
                           race=Race.UNDEAD,
                           gear_stats=self.get_gear_set(),
                           mage_talents=MageTalents('--'),
                           buffs=[player_buffs.ARCANE_INTELLECT])
        self.assertEqual(473, player.stats.intellect)
        self.assertEqual(9056, player.stats.max_mana)
        self.assertEqual(342, player.stats.spell_stats_dict[MagicSchool.ARCANE].spell_crit_rating)
        self.assertEqual(15.49, player.stats.spell_stats_dict[MagicSchool.ARCANE].spell_crit_chance)

    def test_buffs_spirit(self):
        player = Character(name='Sujoo',
                           race=Race.UNDEAD,
                           gear_stats=self.get_gear_set(),
                           mage_talents=MageTalents('--'),
                           buffs=[player_buffs.DIVINE_SPIRIT])
        self.assertEqual(277, player.stats.spirit)
        self.assertEqual(0, player.stats.mp_5)
        self.assertEqual(54, player.calculate_current_mana_regen_per_second())

    def test_buffs_kings(self):
        player = Character(name='Sujoo',
                           race=Race.UNDEAD,
                           gear_stats=self.get_gear_set(),
                           mage_talents=MageTalents('--'),
                           buffs=[player_buffs.BLESSING_OF_KINGS])
        self.assertEqual(476, player.stats.intellect)
        self.assertEqual(261, player.stats.spirit)

    def test_gcd_min(self):
        player = Character(name='Sujoo',
                           race=Race.UNDEAD,
                           gear_stats=self.get_gear_set(),
                           mage_talents=MageTalents('--'),
                           buffs=[combat_buffs.ICY_VEINS,
                                  combat_buffs.ARCANE_BLAST, combat_buffs.ARCANE_BLAST, combat_buffs.ARCANE_BLAST])
        player.calculate_cast_time(mage_spells.GCD_SPELL)
        player.calculate_cast_time(mage_spells.ARCANE_BLAST_R1)
        self.assertEqual('This test case is complete', 'No, but it would be good to have more test cases around spell cast calculations')
