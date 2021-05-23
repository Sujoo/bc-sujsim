from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats

# Pre-BIS

# Phase 1
GENERALS_SILK_CUFFS = Gear(db_id=28411, name="General's Silk Cuffs", sockets=['y'], bonus=ItemStats(spell_power=2), stats=ItemStats(intellect=17,
                                                                                                                                    spell_power=20,
                                                                                                                                    spell_crit_rating=12))
BRACERS_OF_HAVOK = Gear(db_id=24250, name="Bracers of Havok", sockets=['y'], bonus=ItemStats(spell_crit_rating=2), stats=ItemStats(intellect=12,
                                                                                                                                   spell_power=30))
BANDS_OF_NEFARIOUS_DEEDS = Gear(db_id=28515, name="Bands of Nefarious Deeds", stats=ItemStats(intellect=22, spell_power=32))
CRIMSON_BRACERS_OF_GLOOM = Gear(db_id=27462, name="Crimson Bracers of Gloom", stats=ItemStats(intellect=18, spell_power=22, spell_hit_rating=12))
BANDS_OF_NEGATION = Gear(db_id=29240, name="Bands of Negation", stats=ItemStats(intellect=22, spell_power=29))
SHATTRATH_WRAPS = Gear(db_id=28174, name="Shattrath Wraps", sockets=['r'], stats=ItemStats(intellect=15, spell_power=21))
HARBINGER_BANDS = Gear(db_id=28477, name="Harbinger Bands", stats=ItemStats(intellect=21, spell_power=26))
THE_SOUL_HARVESTERS_BINDINGS = Gear(db_id=23021, name="The Soul Harvester's Bindings", stats=ItemStats(intellect=11, spell_power=21, spell_crit_rating=14))
ROCKFURY_BRACERS = Gear(db_id=21186, name="Rockfury Bracers", stats=ItemStats(spell_power=27, spell_hit_rating=8))
# Phase 2
MINDSTORM_WRISTBANDS = Gear(db_id=29918, name="Mindstorm Wristbands", phase=2, stats=ItemStats(intellect=13, spell_power=36, spell_crit_rating=23))
VETERANS_SILK_CUFFS = Gear(db_id=32820, name="Veteran's Silk Cuffs", sockets=['y'], bonus=ItemStats(spell_power=2), phase=2,
                           stats=ItemStats(intellect=18, spell_power=22, spell_crit_rating=14))
VETERANS_DREADWEAVE_CUFFS = Gear(db_id=32811, name="Veteran's Dreadweave Cuffs", sockets=['y'], bonus=ItemStats(spell_power=2), phase=2,
                                 stats=ItemStats(intellect=16, spell_power=25))

# Phase 3
BRACERS_OF_NIMBLE_THOUGHT = Gear(db_id=32586, name="Bracers of Nimble Thought", phase=3, stats=ItemStats(intellect=20, spell_power=34, spell_haste_rating=28))
CUFFS_OF_DEVASTATION = Gear(db_id=30870, name="Cuffs of Devastation", sockets=['y'], phase=3,
                            stats=ItemStats(intellect=20, spell_power=34, spell_crit_rating=14))
FOCUSED_MANA_BINDINGS = Gear(db_id=32270, name="Focused Mana Bindings", phase=3, stats=ItemStats(intellect=20, spell_power=42, spell_hit_rating=19))
VINDICATORS_SILK_CUFFS = Gear(db_id=33913, name="Vindicator's Silk Cuffs", sockets=['y'], bonus=ItemStats(spell_power=2), phase=3,
                              stats=ItemStats(intellect=22, spell_power=27, spell_crit_rating=15))

# Phase 4
FURY_OF_THE_URSINE = Gear(db_id=33285, name="Fury of the Ursine", sockets=['y'], bonus=ItemStats(spell_power=2), phase=4,
                          stats=ItemStats(intellect=17, spell_power=29, spell_crit_rating=17))
RUNED_SPELL_CUFFS = Gear(db_id=33588, name="Runed Spell-cuffs", phase=4, stats=ItemStats(intellect=18, spell_power=29, spell_haste_rating=25))

# Phase 5
BRACERS_OF_THE_TEMPEST = Gear(db_id=34447, name="Bracers of the Tempest", sockets=['r'], bonus=ItemStats(spell_power=2), phase=5,
                              stats=ItemStats(intellect=17, spell_power=39, spell_crit_rating=11, spell_haste_rating=26))
