import copy
import random

from sujsim.ai.decision_model import ArcaneMage, DoNothing
from sujsim.core.items.enchant_database import enchants
from sujsim.core.items.gem_database import gems
from sujsim.core.spells.buff_database import combat_buffs, player_buffs, debuffs
from sujsim.core.items.gear_database import head, neck, back, wrist, weapon, off_hand, hands, wand, legs, feet, ring, waist, shoulder, chest, trinket
from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.stats.gear_stats import GearStats
from sujsim.core.character.character import Character
from sujsim.core.character.race import Race
from sujsim.core.talents.mage_talents import MageTalents
from sujsim.sim.actor import Actor
from sujsim.sim.sim_log import LogType
from sujsim.sim.simulation import Simulation, SimulationSet

boss = Actor(character=Character(name='Boss', race=Race.UNDEAD, gear_stats=GearStats(), mage_talents=MageTalents('--'), buffs=[]),
             decision_model_class=DoNothing)
wisdom = copy.deepcopy(debuffs.JUDGEMENT_OF_WISDOM)
wisdom.duration = 3600
crusader_crit = copy.deepcopy(debuffs.IMPROVED_SEAL_OF_THE_CRUSADER)
crusader_crit.duration = 3600

boss.add_buff(wisdom)
boss.add_buff(crusader_crit)
boss.add_buff(debuffs.MISERY)
boss.add_buff(debuffs.CURSE_OF_ELEMENTS)

gear_stats = GearStats(head=head.INCANTERS_COWL.add_gems([gems.INSIGHTFUL_EARTHSTORM, gems.BRILLIANT_DAWNSTONE]).add_enchant(enchants.GLYPH_OF_POWER),
                       neck=neck.BROOCH_OF_HEIGHTENED_POTENTIAL,
                       shoulder=shoulder.SPAULDERS_OF_THE_TORN_HEART.add_enchant(enchants.GREATER_INSCRIPTION_OF_DISC),
                       back=back.CLOAK_OF_WOVEN_ENERGY,
                       chest=chest.INCANTERS_ROBE.add_gems([gems.INFUSED_FIRE_OPAL, gems.INFUSED_FIRE_OPAL, gems.RUNED_LIVING_RUBY]).add_enchant(
                           enchants.EXCEPTIONAL_STATS),
                       wrist=wrist.CRIMSON_BRACERS_OF_GLOOM.add_enchant(enchants.SPELLPOWER_WRIST),
                       main_hand=weapon.GREATSWORD_OF_HORRID_DREAMS.add_enchant(enchants.SUNFIRE),
                       off_hand=off_hand.LAMP_OF_PEACEFUL_RADIANCE,
                       wand=wand.NETHER_CORES_CONTROL_ROD,
                       hands=hands.INCANTERS_GLOVES.add_enchant(enchants.MAJOR_SPELLPOWER_HANDS),
                       waist=waist.ADALS_GIFT,
                       legs=legs.INCANTERS_TROUSERS.add_enchant(enchants.RUNIC_SPELLTHREAD),
                       feet=feet.SIGIL_LACED_BOOTS.add_gems([gems.RUNED_LIVING_RUBY, gems.INFUSED_FIRE_OPAL]).add_enchant(enchants.BOARS_SPEED),
                       ring_1=ring.MANASTORM_BAND.add_enchant(enchants.SPELLPOWER_RING),
                       ring_2=ring.SPECTRAL_BAND_OF_INNERVATION.add_enchant(enchants.SPELLPOWER_RING),
                       trinket_1=trinket.ICON_OF_THE_SILVER_CRESCENT,
                       trinket_2=trinket.SHIFFARS_NEXUS_HORN)
sujoo = Actor(character=Character(name='Sujoo',
                                  race=Race.UNDEAD,
                                  gear_stats=gear_stats,
                                  mage_talents=MageTalents('2500250300030150330125--053500031003001'),
                                  buffs=[player_buffs.MAGE_ARMOR,
                                         player_buffs.ARCANE_INTELLECT,
                                         player_buffs.DIVINE_SPIRIT,
                                         player_buffs.IMPROVED_DIVINE_SPIRIT,
                                         # player_buffs.MARK_OF_THE_WILD,
                                         player_buffs.BLESSING_OF_KINGS,
                                         player_buffs.BLESSING_OF_WISDOM]),
              decision_model_class=ArcaneMage)
print('Intellect: ', sujoo.character.stats.intellect)
print('Spirit: ', sujoo.character.stats.spirit)
print('Mp5: ', sujoo.character.stats.mp_5)
print('Max Mana: ', sujoo.character.stats.max_mana)
print('Spell Power, Arcane: ', sujoo.character.stats.spell_stats_dict[MagicSchool.ARCANE].spell_power)
print('Crit: ', sujoo.character.stats.spell_stats_dict[MagicSchool.ARCANE].spell_crit_chance)
print('Hit: ', sujoo.character.stats.spell_stats_dict[MagicSchool.ARCANE].spell_hit_rating)
print('Hit: ', sujoo.character.stats.spell_stats_dict[MagicSchool.ARCANE].spell_hit_chance)
print('Haste: ', sujoo.character.stats.spell_stats_dict[MagicSchool.ARCANE].spell_haste)

sim = SimulationSet(player=sujoo, boss=boss, end_of_simulation=25)
sim.run_simulations(count=5000)


"""
sim = Simulation(player=sujoo, boss=boss, end_of_simulation=25)
sim.run()
print('Damage: ', boss.damage_taken[sujoo])
print('DPS: ', sim.get_dps(sujoo))
print('Current Mana: ', sujoo.character.stats.current_mana)
for log in sujoo.logs:
    if log.log_type == LogType.LOG_DAMAGE:
        print(log)
"""

