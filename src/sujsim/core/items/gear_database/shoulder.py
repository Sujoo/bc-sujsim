from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.spells.magic_school import MagicSchool

# Pre-BIS

# Phase 1
INCANTERS_PAULDRONS = Gear(db_id=27738, name="Incanter's Pauldrons", sockets=['y', 'r'], bonus=ItemStats(spell_hit_rating=3), stats=ItemStats(stamina=24,
                                                                                                                                              intellect=17,
                                                                                                                                              spirit=16,
                                                                                                                                              spell_power=20))
FROZEN_SHADOWEAVE_SHOULDERS = Gear(db_id=21869, name="Frozen Shadoweave Shoulders", sockets=['y', 'b'], bonus=ItemStats(spell_hit_rating=3),
                                   stats=ItemStats(intellect=15, spell_power=50, impacted_schools=[MagicSchool.FROST]))
PAULDRONS_OF_THE_ALDOR = Gear(db_id=29079, name="Pauldrons of the Aldor", sockets=['y', 'r'], bonus=ItemStats(spell_power=4), stats=ItemStats(intellect=26,
                                                                                                                                              spell_power=27,
                                                                                                                                              spell_crit_rating=15))
MANA_ETCHED_SPAULDERS = Gear(db_id=27796, name="Mana-Etched Spaulders", sockets=['y', 'r'], stats=ItemStats(intellect=17, spell_power=20, spell_crit_rating=16))
HIGH_WARLORDS_SILK_AMICE = Gear(db_id=28866, name="High Warlord's Silk Amice", sockets=['b', 'y'],
                                stats=ItemStats(intellect=16, spell_power=25, spell_crit_rating=8))
SPAULDERS_OF_OBLIVION = Gear(db_id=27778, name="Spaulders of Oblivion", sockets=['b', 'y'], bonus=ItemStats(spell_hit_rating=3),
                             stats=ItemStats(intellect=17, spell_power=29))
SPAULDERS_OF_THE_TORN_HEART = Gear(db_id=30925, name="Spaulders of the Torn-heart", stats=ItemStats(intellect=7, spell_power=40, spell_crit_rating=18))
MANTLE_OF_THREE_TERRORS = Gear(db_id=27994, name="Mantle of Three Terrors", stats=ItemStats(intellect=25, spell_power=29, spell_hit_rating=12))
RIME_COVERED_MANTLE = Gear(db_id=22983, name="Rime Covered Mantle", stats=ItemStats(intellect=12, spell_power=39, spell_crit_rating=14))
FROSTFIRE_SHOULDERPADS = Gear(db_id=22499, name="Frostfire Shoulderpads", stats=ItemStats(intellect=18, spell_power=36))
# Phase 2
MANTLE_OF_TIRISFAL = Gear(db_id=30210, name="Mantle of Tirisfal", sockets=['y', 'b'], bonus=ItemStats(spell_power=4), phase=2,
                          stats=ItemStats(intellect=24, spell_power=40, spell_crit_rating=17))
ILLIDARI_SHOULDERPADS = Gear(db_id=30079, name="Illidari Shoulderpads", sockets=['y', 'y'], bonus=ItemStats(spell_power=4), phase=2,
                             stats=ItemStats(intellect=23, spell_power=39, spell_crit_rating=16))
MANTLE_OF_THE_ELVEN_KINGS = Gear(db_id=30024, name="Mantle of the Elven Kings", phase=2,
                                 stats=ItemStats(intellect=18, spell_power=39, spell_crit_rating=25, spell_hit_rating=18))
MERCILESS_GLADIATORS_SILK_AMICE = Gear(db_id=32047, name="Merciless Gladiator's Silk Amice", sockets=['b', 'y'], phase=2,
                                       stats=ItemStats(intellect=15, spell_power=36, spell_crit_rating=14))

# Phase 3
HATEFURY_MANTLE = Gear(db_id=30884, name="Hatefury Mantle", sockets=['b', 'y'], bonus=ItemStats(spell_crit_rating=3), phase=3, stats=ItemStats(intellect=18,
                                                                                                                                               spell_power=55,
                                                                                                                                               spell_crit_rating=24))
MANTLE_OF_THE_TEMPEST = Gear(db_id=31059, name="Mantle of the Tempest", sockets=['y', 'b'], bonus=ItemStats(spell_power=4), phase=3,
                             stats=ItemStats(intellect=27, spell_power=46, spell_crit_rating=21))
BLOOD_CURSED_SHOULDERPADS = Gear(db_id=32338, name="Blood-cursed Shoulderpads", phase=3,
                                 stats=ItemStats(intellect=19, spell_power=55, spell_crit_rating=25, spell_hit_rating=18))
MANTLE_OF_NIMBLE_THOUGHT = Gear(db_id=32587, name="Mantle of Nimble Thought", phase=3, stats=ItemStats(intellect=26, spell_power=44, spell_haste_rating=38))
VENGEFUL_GLADIATORS_SILK_AMICE = Gear(db_id=33757, name="Vengeful Gladiator's Silk Amice", sockets=['b', 'y'], phase=3,
                                      stats=ItemStats(intellect=13, spell_power=40, spell_crit_rating=17))

# Phase 4
MANTLE_OF_ILL_INTENT = Gear(db_id=33489, name="Mantle of Ill Intent", phase=4, stats=ItemStats(intellect=24, spell_power=40, spell_haste_rating=33))

# Phase 5
AMICE_OF_THE_CONVOKER = Gear(db_id=34210, name="Amice of the Convoker", sockets=['r', 'y'], bonus=ItemStats(spell_power=4), phase=5,
                             stats=ItemStats(intellect=28, spell_power=53, spell_crit_rating=22, spell_haste_rating=30))
SHOULDERPADS_OF_KNOWLEDGES_PURSUIT = Gear(db_id=34393, name="Shoulderpads of Knowledge's Pursuit", sockets=['r', 'y'], bonus=ItemStats(spell_power=4), phase=5,
                                          stats=ItemStats(intellect=33, spell_power=53, spell_crit_rating=26))
BRUTAL_GLADIATORS_SILK_AMICE = Gear(db_id=35096, name="Brutal Gladiator's Silk Amice", sockets=['b', 'y'], phase=5,
                                    stats=ItemStats(intellect=18, spell_power=44, spell_crit_rating=21))
