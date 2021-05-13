from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats

# Pre-BIS

# Phase 1
SPELLSTRIKE_PANTS = Gear(db_id=24262, name="Spellstrike Pants", sockets=['b', 'y', 'r'],
                         stats=ItemStats(intellect=8, spell_power=46, spell_crit_rating=26, spell_hit_rating=22))
LEGGINGS_OF_THE_SEVENTH_CIRCLE = Gear(db_id=30734, name="Leggings of the Seventh Circle", sockets=['r', 'y', 'y'], bonus=ItemStats(spell_power=5),
                                      stats=ItemStats(intellect=22, spell_power=50, spell_crit_rating=25, spell_hit_rating=18))
TRIAL_FIRE_TROUSERS = Gear(db_id=28594, name="Trial-Fire Trousers", sockets=['y', 'y', 'y'], bonus=ItemStats(spell_power=5),
                           stats=ItemStats(intellect=40, spell_power=49))
BREECHES_OF_THE_OCCULTIST = Gear(db_id=30531, name="Breeches of the Occultist", sockets=['b', 'y', 'y'], bonus=ItemStats(spell_power=5),
                                 stats=ItemStats(intellect=22, spell_power=36, spell_crit_rating=23))
LEGWRAPS_OF_THE_ALDOR = Gear(db_id=29078, name="Legwraps of the Aldor", stats=ItemStats(intellect=40, spell_power=49, spell_hit_rating=24))
KIRIN_TOR_MASTERS_TROUSERS = Gear(db_id=30532, name="Kirin Tor Master's Trousers", sockets=['r', 'y', 'b'], bonus=ItemStats(spell_hit_rating=4),
                                  stats=ItemStats(intellect=29, spell_power=36))
ARANS_SORCEROUS_SLACKS = Gear(db_id=28212, name="Aran's Sorcerous Slacks", sockets=['r', 'y', 'b'], bonus=ItemStats(spell_power=5),
                              stats=ItemStats(intellect=28, spell_power=23, spell_crit_rating=21))
KHADGARS_KILT_OF_ABJURATION = Gear(db_id=28185, name="Khadgar's Kilt of Abjuration", sockets=['y', 'b', 'b'], bonus=ItemStats(spell_power=5),
                                   stats=ItemStats(intellect=22, spell_power=36))
BATTLECAST_PANTS = Gear(db_id=24263, name="Battlecast Pants", sockets=['r', 'b'], bonus=ItemStats(spell_crit_rating=3), stats=ItemStats(
    intellect=27,
    spell_power=46))
PANTALOONS_OF_FLAMING_WRATH = Gear(db_id=30709, name="Pantaloons of Flaming Wrath", stats=ItemStats(intellect=28, spell_power=33, spell_crit_rating=42))
DEVIL_STITCHED_LEGGINGS = Gear(db_id=28338, name="Devil-Stitched Leggings", sockets=['r', 'y', 'b'], bonus=ItemStats(spell_power=5),
                               stats=ItemStats(intellect=28, spell_power=29))
INCANTERS_TROUSERS = Gear(db_id=27838, name="Incanter's Trousers", stats=ItemStats(intellect=30, spirit=17, spell_power=42, spell_crit_rating=18))
MANA_ETCHED_PANTALOONS = Gear(db_id=27907, name="Mana-Etched Pantaloons", stats=ItemStats(intellect=32, spell_power=33, spell_crit_rating=21))
LEGGINGS_OF_POLARITY = Gear(db_id=23070, name="Leggings of Polarity", stats=ItemStats(intellect=14, spell_power=44, spell_crit_rating=28))
FROSTFIRE_LEGGINGS = Gear(db_id=22497, name="Frostfire Leggings", stats=ItemStats(intellect=26, spell_power=46, spell_hit_rating=8))

# Phase 2
LEGGINGS_OF_TIRISFAL = Gear(db_id=30207, name="Leggings of Tirisfal", sockets=['y'], bonus=ItemStats(spell_hit_rating=2), phase=2, stats=ItemStats(
    intellect=36, spell_power=54, spell_crit_rating=17, spell_hit_rating=26))
TROUSERS_OF_THE_ASTROMANCER = Gear(db_id=29972, name="Trousers of the Astromancer", sockets=['b', 'y', 'b'], bonus=ItemStats(spell_power=5), phase=2,
                                   stats=ItemStats(intellect=36, spell_power=54))
MERCILESS_GLADIATORS_SILK_TROUSERS = Gear(db_id=32051, name="Merciless Gladiator's Silk Trousers", phase=2,
                                          stats=ItemStats(intellect=36, spell_power=49, spell_crit_rating=29))

# Phase 3
LEGGINGS_OF_CHANNELED_ELEMENTS = Gear(db_id=30916, name="Leggings of Channeled Elements", sockets=['y', 'y', 'b'], bonus=ItemStats(spell_power=5), phase=3,
                                      stats=ItemStats(intellect=28, spell_power=59, spell_crit_rating=34, spell_hit_rating=18))
LEGGINGS_OF_THE_TEMPEST = Gear(db_id=31058, name="Leggings of the Tempest", sockets=['b'], bonus=ItemStats(spell_power=2), phase=3, stats=ItemStats(
    intellect=47, spell_power=62, spell_crit_rating=29, spell_hit_rating=20))
LEGGINGS_OF_DEVASTATION = Gear(db_id=32367, name="Leggings of Devastation", sockets=['y', 'y', 'b'], bonus=ItemStats(spell_power=5), phase=3,
                               stats=ItemStats(intellect=42, spell_power=60, spell_hit_rating=26))

# Phase 4
PANTALOONS_OF_ARCANE_ANNIHILATION = Gear(db_id=33584, name="Pantaloons of Arcane Annihilation", phase=4,
                                         stats=ItemStats(intellect=35, spell_power=54, spell_haste_rating=45))

# Phase 5
LEGGINGS_OF_CALAMITY = Gear(db_id=34181, name="Leggings of Calamity", sockets=['r', 'r', 'y'], bonus=ItemStats(spell_power=5), phase=5,
                            stats=ItemStats(intellect=41, spell_power=71, spell_crit_rating=33, spell_haste_rating=32))
PANTALOONS_OF_GROWING_STRIFE = Gear(db_id=34386, name="Pantaloons of Growing Strife", sockets=['r', 'y', 'y'], bonus=ItemStats(spell_power=5), phase=5,
                                    stats=ItemStats(intellect=36, spell_power=71, spell_haste_rating=42))
CORRUPTED_SOULCLOTH_PANTALOONS = Gear(db_id=34937, name="Corrupted Soulcloth Pantaloons", sockets=['y', 'b'], bonus=ItemStats(spell_power=4), phase=5,
                                      stats=ItemStats(intellect=33, spell_power=61, spell_crit_rating=43))
LEGWRAPS_OF_SWELTERING_FLAME = Gear(db_id=34918, name="Legwraps of Sweltering Flame", sockets=['y', 'b'], bonus=ItemStats(spell_power=4), phase=5,
                                    stats=ItemStats(intellect=36, spell_power=62, spell_hit_rating=25))
