from sujsim.core.spells.buff import Buff
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.stats.spell_stats import SpellStats

ARCANE_INTELLECT = Buff(db_id=-1, name='', stats=ItemStats(intellect=40))
MAGE_ARMOR = Buff(db_id=27125, name='Mage Armor', stats=ItemStats(fire_resistance=18, frost_resistance=18,
                                                                  shadow_resistance=18, arcane_resistance=18, nature_resistance=18))
DIVINE_SPIRIT = Buff(db_id=-1, name='', stats=ItemStats(spirit=40))
IMPROVED_DIVINE_SPIRIT = Buff(db_id=-1, name='')
POWER_WORD_FORTITUDE = Buff(db_id=-1, name='', stats=ItemStats(stamina=79))
MARK_OF_THE_WILD = Buff(db_id=-1, name='', stats=ItemStats(intellect=14, spirit=14, stamina=14,
                                                           fire_resistance=25, frost_resistance=25, shadow_resistance=25, arcane_resistance=25,
                                                           nature_resistance=25))
BLESSING_OF_KINGS = Buff(db_id=20217, name='Blessing of Kings')
BLESSING_OF_WISDOM = Buff(db_id=27142, name='Blessing of Wisdom', stats=ItemStats(mp_5=41))  # 45, with 1 imp talent, 49 with 2 talent points
WRATH_OF_AIR = Buff(db_id=-1, name='', stats=ItemStats(spell_power=101))
ATIESH_WARLOCK = Buff(db_id=-1, name='', stats=ItemStats(spell_power=33))
ATIESH_MAGE = Buff(db_id=-1, name='', stats=ItemStats(spell_crit_rating=28))
EYE_OF_THE_NIGHT = Buff(db_id=-1, name='', stats=ItemStats(spell_power=34))
JADE_PENDANT_OF_BLASTING = Buff(db_id=-1, name='', stats=ItemStats(spell_power=15))
JUDGEMENT_OF_THE_CRUSADER = Buff(db_id=-1, name='', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT*3))
MOONKIN_AURA = Buff(db_id=-1, name='', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT*5))
TOTEM_OF_WRATH = Buff(db_id=-1, name='', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT*3, spell_hit_rating=SpellStats.ONE_HIT*3))
MOLTEN_ARMOR = Buff(db_id=-1, name='', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT*3))
CHAIN_OF_THE_TWILIGHT_OWL = Buff(db_id=-1, name='', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT*2))
INSPIRING_PRESENCE = Buff(db_id=-1, name='', stats=ItemStats(spell_hit_rating=SpellStats.ONE_HIT))
