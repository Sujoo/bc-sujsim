from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.spells.magic_school import MagicSchool

# Pre-BIS

# Phase 1
SPELLFIRE_BELT = Gear(db_id=21846, name="Spellfire Belt", sockets=['y', 'b'],
                      stats=ItemStats(intellect=18, spell_crit_rating=18, spell_power=50, impacted_schools=[MagicSchool.ARCANE, MagicSchool.FIRE]))
GIRDLE_OF_RUINATION = Gear(db_id=24256, name="Girdle of Ruination", sockets=['r', 'y'], stats=ItemStats(intellect=13, spell_power=39, spell_crit_rating=20))
BELT_OF_DIVINE_INSPIRATION = Gear(db_id=28799, name="Belt of Divine Inspiration", sockets=['b', 'y'], bonus=ItemStats(spell_power=4),
                                  stats=ItemStats(intellect=26, spell_power=43))
GLYPH_LINED_SASH = Gear(db_id=27843, name="Glyph-Lined Sash", sockets=['y', 'y'], bonus=ItemStats(spell_power=4),
                        stats=ItemStats(intellect=23, spell_power=30, spell_crit_rating=9))
MALEFIC_GIRDLE = Gear(db_id=28654, name="Malefic Girdle", stats=ItemStats(intellect=26, spell_power=37, spell_crit_rating=21))
ADALS_GIFT = Gear(db_id=31461, name="A'dal's Gift", stats=ItemStats(intellect=25, spell_power=34, spell_crit_rating=21))
BELT_OF_DEPRAVITY = Gear(db_id=29241, name="Belt of Depravity", stats=ItemStats(intellect=27, spell_power=34, spell_hit_rating=17))
MINDFIRE_WAISTBAND = Gear(db_id=24395, name="Mindfire Waistband", sockets=['y', 'b'], bonus=ItemStats(spell_hit_rating=3), stats=ItemStats(intellect=14,
                                                                                                                                           spell_power=21,
                                                                                                                                           spell_hit_rating=11))
SASH_OF_ARCANE_VISIONS = Gear(db_id=29257, name="Sash of Arcane Visions", stats=ItemStats(intellect=23, spell_power=28, spell_crit_rating=22))
SASH_OF_SEALED_FATE = Gear(db_id=31283, name="Sash of Sealed Fate", stats=ItemStats(intellect=15, spell_power=35, spell_crit_rating=23))
EYESTALK_WAIST_CORD = Gear(db_id=22730, name="Eyestalk Waist Cord", stats=ItemStats(intellect=9, spell_power=41, spell_crit_rating=14))
FROSTFIRE_BELT = Gear(db_id=22502, name="Frostfire Belt", stats=ItemStats(intellect=21, spell_power=28, spell_hit_rating=8))

# Phase 2
BELT_OF_BLASTING = Gear(db_id=30038, name="Belt of Blasting", sockets=['b', 'y'], bonus=ItemStats(spell_power=4), phase=2,
                        stats=ItemStats(spell_power=50, spell_crit_rating=30, spell_hit_rating=23))
CORD_OF_SCREAMING_TERRORS = Gear(db_id=30064, name="Cord of Screaming Terrors", sockets=['y', 'y'], phase=2,
                                 stats=ItemStats(intellect=15, spell_power=50, spell_hit_rating=24))
VETERANS_SILK_BELT = Gear(db_id=32807, name="Veteran's Silk Belt", phase=2, stats=ItemStats(intellect=27, spell_power=32, spell_crit_rating=27))

# Phase 3
NETHERONS_NOOSE = Gear(db_id=30888, name="Anetheron's Noose", sockets=['y', 'b'], bonus=ItemStats(spell_power=4), phase=3,
                       stats=ItemStats(intellect=23, spell_power=55, spell_crit_rating=24))
WAISTWRAP_OF_INFINITY = Gear(db_id=32256, name="Waistwrap of Infinity", phase=3, stats=ItemStats(intellect=22, spell_power=56, spell_haste_rating=32))
VINDICATORS_SILK_BELT = Gear(db_id=33912, name="Vindicator's Silk Belt", phase=3, stats=ItemStats(intellect=30, spell_power=35, spell_crit_rating=28))

# Phase 4
VOODOO_WOVEN_BELT = Gear(db_id=33291, name="Voodoo-woven Belt", phase=4,
                         stats=ItemStats(intellect=22, spell_power=40, spell_crit_rating=33, spell_hit_rating=17))

# Phase 5
BELT_OF_THE_TEMPEST = Gear(db_id=34557, name="Belt of the Tempest", sockets=['y'], bonus=ItemStats(spell_power=2), phase=5, stats=ItemStats(intellect=29,
                                                                                                                                            spell_power=50,
                                                                                                                                            spell_crit_rating=17,
                                                                                                                                            spell_hit_rating=14,
                                                                                                                                            spell_haste_rating=29))
