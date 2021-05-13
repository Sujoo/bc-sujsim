from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.spells.magic_school import MagicSchool

# Pre-BIS

# Phase 1
SPELLFIRE_GLOVES = Gear(db_id=21847, name="Spellfire Gloves", sockets=['y', 'b'],
                        stats=ItemStats(intellect=10, spell_crit_rating=23, spell_power=50, impacted_schools=[MagicSchool.ARCANE, MagicSchool.FIRE]))
SOUL_EATERS_HANDWRAPS = Gear(db_id=28780, name="Soul-Eater's Handwraps", sockets=['y', 'b'], bonus=ItemStats(spell_power=4), stats=ItemStats(intellect=24,
                                                                                                                                             spell_power=36,
                                                                                                                                             spell_crit_rating=21))
ANGER_SPARK_GLOVES = Gear(db_id=30725, name="Anger-Spark Gloves", sockets=['r', 'r'], bonus=ItemStats(spell_crit_rating=3),
                          stats=ItemStats(spell_power=30, spell_crit_rating=25, spell_hit_rating=20))
HANDWRAPS_OF_FLOWING_THOUGHT = Gear(db_id=28507, name="Handwraps of Flowing Thought", sockets=['y', 'b'], bonus=ItemStats(spell_hit_rating=3), stats=ItemStats(
    intellect=22, spell_power=35, spell_hit_rating=14))
GLOVES_OF_THE_ALDOR = Gear(db_id=29080, name="Gloves of the Aldor", stats=ItemStats(intellect=22, spell_power=35, spell_crit_rating=19, spell_hit_rating=17))
MANA_ETCHED_GLOVES = Gear(db_id=27465, name="Mana-Etched Gloves", sockets=['r', 'y'], stats=ItemStats(intellect=17, spell_power=20, spell_crit_rating=16))
TEMPESTS_TOUCH = Gear(db_id=29317, name="Tempest's Touch", sockets=['b', 'b'], bonus=ItemStats(spell_crit_rating=3),
                      stats=ItemStats(intellect=20, spell_power=27))
MANASPARK_GLOVES = Gear(db_id=24450, name="Manaspark Gloves", sockets=['r', 'y'], bonus=ItemStats(spell_crit_rating=3), stats=ItemStats(
    intellect=14,
    spell_power=16, spell_hit_rating=15))
GLOVES_OF_THE_DEADWATCHER = Gear(db_id=27493, name="Gloves of the Deadwatcher", stats=ItemStats(intellect=24, spell_power=29, spell_hit_rating=18))
GLOVES_OF_PANDEMONIUM = Gear(db_id=31149, name="Gloves of Pandemonium",
                             stats=ItemStats(intellect=15, spell_power=25, spell_crit_rating=22, spell_hit_rating=10))
INCANTERS_GLOVES = Gear(db_id=27508, name="Incanter's Gloves", stats=ItemStats(intellect=24, spirit=12, spell_power=29, spell_crit_rating=14))
DARK_STORM_GAUNTLETS = Gear(db_id=21585, name="Dark Storm Gauntlets", stats=ItemStats(intellect=15, spell_power=37, spell_hit_rating=8))
FROSTFIRE_GLOVES = Gear(db_id=22501, name="Frostfire Gloves", stats=ItemStats(intellect=19, spell_power=36))

# Phase 2
GLOVES_OF_TIRISFAL = Gear(db_id=30205, name="Gloves of Tirisfal", phase=2, stats=ItemStats(intellect=27, spell_power=41, spell_crit_rating=27))
GAUNTLETS_OF_THE_SUN_KING = Gear(db_id=29987, name="Gauntlets of the Sun King", phase=2, stats=ItemStats(intellect=29, spell_power=42, spell_crit_rating=28))
GLOVES_OF_ARCANE_ACUITY = Gear(db_id=34808, name="Gloves of Arcane Acuity", sockets=['b', 'r'], bonus=ItemStats(spell_power=4), phase=2,
                               stats=ItemStats(intellect=20, spell_power=34, spell_hit_rating=18))
MERCILESS_GLADIATORS_SILK_HANDGUARDS = Gear(db_id=32049, name="Merciless Gladiator's Silk Handguards", phase=2,
                                            stats=ItemStats(intellect=20, spell_power=36, spell_crit_rating=19))

# Phase 3
GLOVES_OF_THE_TEMPEST = Gear(db_id=31055, name="Gloves of the Tempest", sockets=['y'], bonus=ItemStats(spell_power=2), phase=3, stats=ItemStats(intellect=26,
                                                                                                                                                spell_power=46,
                                                                                                                                                spell_crit_rating=19,
                                                                                                                                                spell_hit_rating=20))
VENGEFUL_GLADIATORS_SILK_HANDGUARDS = Gear(db_id=33759, name="Vengeful Gladiator's Silk Handguards", phase=3,
                                           stats=ItemStats(intellect=18, spell_power=40, spell_crit_rating=22))

# Phase 4
STUDIOUS_WRAPS = Gear(db_id=33586, name="Studious Wraps", sockets=['r', 'b'], bonus=ItemStats(spell_power=4), phase=4,
                      stats=ItemStats(intellect=22, spell_power=40, spell_crit_rating=25))

# Phase 5
HANDGUARDS_OF_DEFILED_WORLDS = Gear(db_id=34344, name="Handguards of Defiled Worlds", sockets=['y', 'r'], bonus=ItemStats(spell_power=4), phase=5,
                                    stats=ItemStats(intellect=32, spell_power=47, spell_hit_rating=27, spell_haste_rating=36))
GLOVES_OF_TYRIS_POWER = Gear(db_id=34406, name="Gloves of Tyri's Power", sockets=['y', 'r'], bonus=ItemStats(spell_power=4), phase=5,
                             stats=ItemStats(intellect=32, spell_power=47, spell_haste_rating=36))
SUNFIRE_HANDWRAPS = Gear(db_id=34366, name="Sunfire Handwraps", sockets=['r', 'r'], bonus=ItemStats(spell_power=4), phase=5,
                         stats=ItemStats(intellect=30, spell_power=53, spell_crit_rating=37))
BRUTAL_GLADIATORS_SILK_HANDGUARDS = Gear(db_id=35098, name="Brutal Gladiator's Silk Handguards", phase=5,
                                         stats=ItemStats(intellect=23, spell_power=44, spell_crit_rating=26))
