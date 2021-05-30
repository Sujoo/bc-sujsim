from sujsim.core.spells.buff import Buff
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.stats.spell_stats import SpellStats

ARCANE_INTELLECT = Buff(db_id=27126, name='Arcane Intellect', stats=ItemStats(intellect=40))
MAGE_ARMOR = Buff(db_id=27125, name='Mage Armor', stats=ItemStats(fire_resistance=18, frost_resistance=18,
                                                                  shadow_resistance=18, arcane_resistance=18, nature_resistance=18))
MOLTEN_ARMOR = Buff(db_id=-1, name='', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT * 3))

DIVINE_SPIRIT = Buff(db_id=25312, name='Divine Spirit', stats=ItemStats(spirit=40))
IMPROVED_DIVINE_SPIRIT = Buff(db_id=33182, name='Improved Divine Spirit')
POWER_WORD_FORTITUDE = Buff(db_id=25389, name='Power Word: Fortitude', stats=ItemStats(stamina=79))
MARK_OF_THE_WILD = Buff(db_id=26990, name='Mark of the Wild', stats=ItemStats(intellect=14, spirit=14, stamina=14,
                                                                              fire_resistance=25, frost_resistance=25, shadow_resistance=25,
                                                                              arcane_resistance=25, nature_resistance=25))
BLESSING_OF_KINGS = Buff(db_id=20217, name='Blessing of Kings')
BLESSING_OF_WISDOM = Buff(db_id=27142, name='Blessing of Wisdom', stats=ItemStats(mp_5=41))  # 45, with 1 imp talent, 49 with 2 talent points

WRATH_OF_AIR = Buff(db_id=3738, name='Wrath of Air Totem', stats=ItemStats(spell_power=101))
TOTEM_OF_WRATH = Buff(db_id=30706, name='Totem of Wrath', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT * 3, spell_hit_rating=SpellStats.ONE_HIT * 3))

ATIESH_WARLOCK = Buff(db_id=22589, name='Atiesh, Greatstaff of the Guardian', stats=ItemStats(spell_power=33))
ATIESH_MAGE = Buff(db_id=22630, name='Atiesh, Greatstaff of the Guardian', stats=ItemStats(spell_crit_rating=28))

MOONKIN_AURA = Buff(db_id=24907, name='', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT * 5))

EYE_OF_THE_NIGHT = Buff(db_id=24116, name='Eye of the aNight', stats=ItemStats(spell_power=34), duration=1800)  # 30 minutes
JADE_PENDANT_OF_BLASTING = Buff(db_id=20966, name='Jade Pendant of Blasting', stats=ItemStats(spell_power=15), duration=900)  # 15 minutes
CHAIN_OF_THE_TWILIGHT_OWL = Buff(db_id=24121, name='Chain of the Twilight Owl', stats=ItemStats(spell_crit_rating=SpellStats.ONE_CRIT * 2), duration=1800)
INSPIRING_PRESENCE = Buff(db_id=28878, name='Inspiring Presence', stats=ItemStats(spell_hit_rating=SpellStats.ONE_HIT))
