from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.spells.magic_school import MagicSchool

# Pre-BIS

# Phase 1

ADORNMENT_OF_STOLEN_SOULS = Gear(db_id=28762, name="Adornment of Stolen Souls", stats=ItemStats(intellect=20, spell_power=28, spell_crit_rating=23))
BROOCH_OF_UNQUENCHABLE_FURY = Gear(db_id=28530, name="Brooch of Unquenchable Fury", stats=ItemStats(intellect=21, spell_power=26, spell_hit_rating=15))
BROOCH_OF_HEIGHTENED_POTENTIAL = Gear(db_id=28134, name="Brooch of Heightened Potential",
                                      stats=ItemStats(intellect=14, spell_power=22, spell_crit_rating=14, spell_hit_rating=9))
NATASHAS_EMBER_NECKLACE = Gear(db_id=31692, name="Natasha's Ember Necklace", stats=ItemStats(intellect=15, spell_power=29, spell_crit_rating=10))
TORC_OF_THE_SETHEKK_PROPHET = Gear(db_id=29333, name="Torc of the Sethekk Prophet", stats=ItemStats(intellect=18, spell_power=19, spell_crit_rating=21))
LUMINOUS_PEARLS_OF_INSIGHT = Gear(db_id=24462, name="Luminous Pearls of Insight", stats=ItemStats(intellect=15, spell_power=25, spell_crit_rating=11))
EYE_OF_THE_NIGHT = Gear(db_id=24116, name="Eye of the Night", stats=ItemStats(spell_crit_rating=26, spell_hit_rating=16))
CHAIN_OF_THE_TWILIGHT_OWL = Gear(db_id=24121, name="Chain of the Twilight Owl", stats=ItemStats(intellect=19, spell_power=21))
JADE_PENDANT_OF_BLASTING = Gear(db_id=20966, name="Jade Pendant of Blasting", stats=ItemStats(intellect=3, spell_power=8))
CHARLOTTES_IVY = Gear(db_id=31338, name="Charlotte's Ivy", stats=ItemStats(intellect=19, spell_power=23))
AMULET_OF_VEKNILASH = Gear(db_id=21608, name="Amulet of Vek'nilash", stats=ItemStats(intellect=5, spell_power=27, spell_crit_rating=14))
GEM_OF_TRAPPED_INNOCENTS = Gear(db_id=23057, name="Gem of Trapped Innocents", stats=ItemStats(intellect=7, spell_power=15, spell_crit_rating=28))
CHOKER_OF_THE_FIRE_LORD = Gear(db_id=18814, name="Choker of the Fire Lord", stats=ItemStats(intellect=7, spell_power=34))

# Phase 2
THE_SUN_KINGS_TALISMAN = Gear(db_id=30015, name="The Sun King's Talisman", phase=2, stats=ItemStats(intellect=16, spell_power=41, spell_crit_rating=24))
VETERANS_PENDANT_OF_CONQUEST = Gear(db_id=33067, name="Veteran's Pendant of Conquest", sockets=['y'], phase=2,
                                    stats=ItemStats(intellect=12, spell_power=21, spell_crit_rating=18))
PENDANT_OF_THE_LOST_AGES = Gear(db_id=30008, name="Pendant of the Lost Ages", phase=2, stats=ItemStats(intellect=17, spell_power=36))

# Phase 3
TRANSLUCENT_SPELLTHREAD_NECKLACE = Gear(db_id=32349, name="Translucent Spellthread Necklace", phase=3,
                                        stats=ItemStats(spell_power=46, spell_crit_rating=24, spell_hit_rating=15))
HELLFIRE_ENCASED_PENDANT = Gear(db_id=32589, name="Hellfire-Encased Pendant", phase=3, stats=ItemStats(intellect=17, spell_crit_rating=24, spell_power=51,
                                                                                                       impacted_schools=[MagicSchool.FIRE]))
VINDICATORS_PENDANT_OF_CONQUEST = Gear(db_id=33920, name="Vindicator's Pendant of Conquest", sockets=['y'], phase=3,
                                       stats=ItemStats(intellect=15, spell_power=25, spell_crit_rating=21))

# Phase 4
BROOCH_OF_NATURES_MERCY = Gear(db_id=33281, name="Brooch of Nature's Mercy", phase=4, stats=ItemStats(intellect=24, spell_power=25, spell_haste_rating=33))
LOOP_OF_CURSED_BONES = Gear(db_id=33466, name="Loop of Cursed Bones", phase=4, stats=ItemStats(intellect=20, spell_power=32, spell_haste_rating=27))

# Phase 5
PENDANT_OF_SUNFIRE = Gear(db_id=34359, name="Pendant of Sunfire", sockets=['y'], bonus=ItemStats(spell_power=2), phase=5, stats=ItemStats(intellect=19,
                                                                                                                                          spell_power=34,
                                                                                                                                          spell_crit_rating=25,
                                                                                                                                          spell_haste_rating=25))
AMULET_OF_UNFETTERED_MAGICS = Gear(db_id=34204, name="Amulet of Unfettered Magics", phase=5,
                                   stats=ItemStats(intellect=17, spell_power=39, spell_hit_rating=15, spell_haste_rating=32))
GUARDIANS_PENDANT_OF_SUBJUGATION = Gear(db_id=37928, name="Guardian's Pendant of Subjugation", sockets=['y'], phase=5,
                                        stats=ItemStats(intellect=18, spell_power=28, spell_haste_rating=24))
SINDOREI_PENDANT_OF_CONQUEST = Gear(db_id=35290, name="Sin'dorei Pendant of Conquest", sockets=['b'], bonus=ItemStats(spell_power=2), phase=5,
                                    stats=ItemStats(intellect=19, spell_power=34, spell_crit_rating=19))
