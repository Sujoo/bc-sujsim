from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.spells.magic_school import MagicSchool

# Pre-BIS

# Phase 1
INCANTERS_ROBE = Gear(db_id=27738, name="Incanter's Robe", sockets=['y', 'y', 'r'], bonus=ItemStats(intellect=4), stats=ItemStats(stamina=24,
                                                                                                                                  intellect=22,
                                                                                                                                  spirit=22,
                                                                                                                                  spell_power=29,
                                                                                                                                  spell_crit_rating=8))
SPELLFIRE_ROBE = Gear(db_id=21848, name="Spellfire Robe", sockets=['y', 'b'],
                      stats=ItemStats(intellect=17, spell_crit_rating=28, spell_power=72, impacted_schools=[MagicSchool.FIRE, MagicSchool.ARCANE]))
FROZEN_SHADOWEAVE_ROBE = Gear(db_id=21871, name="Frozen Shadoweave Robe", sockets=['y', 'b'], bonus=ItemStats(spell_hit_rating=3),
                              stats=ItemStats(intellect=20, spell_power=72, impacted_schools=[MagicSchool.FROST]))
VESTMENTS_OF_THE_ALDOR = Gear(db_id=29077, name="Vestments of the Aldor", sockets=['y', 'b', 'b'], bonus=ItemStats(spell_power=5), stats=ItemStats(
    intellect=32,
    spell_power=49, spell_crit_rating=25))
AUCHENAI_ANCHORITES_ROBE = Gear(db_id=29341, name="Auchenai Anchorite's Robe", sockets=['y', 'y', 'r'], bonus=ItemStats(spell_crit_rating=4),
                                stats=ItemStats(intellect=24, spell_power=28, spell_hit_rating=23))
GLADIATORS_SILK_RAIMENT = Gear(db_id=25856, name="Gladiator's Silk Raiment", sockets=['y', 'y', 'r'], bonus=ItemStats(spell_crit_rating=4),
                               stats=ItemStats(intellect=18, spell_power=32, spell_crit_rating=25))
WILL_OF_EDWARD_THE_ODD = Gear(db_id=31340, name="Will of Edward the Odd", stats=ItemStats(intellect=30, spell_power=53, spell_crit_rating=30))
WARP_INFUSED_DRAPE = Gear(db_id=28342, name="Warp Infused Drape", sockets=['r', 'b', 'y'], bonus=ItemStats(spell_crit_rating=4),
                          stats=ItemStats(intellect=28, spell_power=30, spell_hit_rating=12))
MANA_ETCHED_VESTMENTS = Gear(db_id=28191, name="Mana-Etched Vestments", sockets=['r', 'b', 'y'], bonus=ItemStats(spell_power=5),
                             stats=ItemStats(intellect=25, spell_power=29, spell_crit_rating=17))
ANCHORITES_ROBES = Gear(db_id=29129, name="Anchorite's Robes", sockets=['y', 'b', 'y'], bonus=ItemStats(mp_5=2), stats=ItemStats(intellect=38,
                                                                                                                                 spell_power=29))
ROBE_OF_OBLIVION = Gear(db_id=28232, name="Robe of Oblivion", sockets=['r', 'y', 'b'], stats=ItemStats(intellect=20, spell_power=40))
FROSTFIRE_ROBE = Gear(db_id=22496, name="Frostfire Robe", stats=ItemStats(intellect=27, spell_power=47, spell_crit_rating=14, spell_hit_rating=8))

# Phase 2
ROBES_OF_TIRISFAL = Gear(db_id=30196, name="Robes of Tirisfal", sockets=['y', 'y', 'b'], bonus=ItemStats(spell_power=5), phase=2,
                         stats=ItemStats(intellect=35, spell_power=55, spell_crit_rating=19))
VESTMENTS_OF_THE_SEA_WITCH = Gear(db_id=30107, name="Vestments of the Sea-Witch", sockets=['y', 'y', 'b'], bonus=ItemStats(spell_power=5), phase=2,
                                  stats=ItemStats(intellect=28, spell_power=57, spell_crit_rating=31, spell_hit_rating=27))
ROBE_OF_HATEFUL_ECHOES = Gear(db_id=30056, name="Robe of Hateful Echoes", sockets=['r', 'y', 'y'], phase=2,
                              stats=ItemStats(intellect=36, spell_power=50, spell_crit_rating=25))
MERCILESS_GLADIATORS_SILK_RAIMENT = Gear(db_id=32050, name="Merciless Gladiator's Silk Raiment", sockets=['r', 'y', 'y'], bonus=ItemStats(spell_crit_rating=4),
                                         phase=2, stats=ItemStats(intellect=21, spell_power=35, spell_crit_rating=30))

# Phase 3
ROBES_OF_THE_TEMPEST = Gear(db_id=31057, name="Robes of the Tempest", sockets=['y', 'y', 'b'], bonus=ItemStats(spell_power=5), phase=3,
                            stats=ItemStats(intellect=39, spell_power=62, spell_crit_rating=23, spell_hit_rating=13))
ROBES_OF_RHONIN = Gear(db_id=30913, name="Robes of Rhonin", phase=3, stats=ItemStats(intellect=38, spell_power=81, spell_crit_rating=24, spell_hit_rating=27))
ROBE_OF_THE_SHADOW_COUNCIL = Gear(db_id=32327, name="Robe of the Shadow Council", phase=3, stats=ItemStats(intellect=36, spell_power=73, spell_crit_rating=28))
VENGEFUL_GLADIATORS_SILK_RAIMENT = Gear(db_id=33760, name="Vengeful Gladiator's Silk Raiment", sockets=['r', 'y', 'y'], bonus=ItemStats(spell_crit_rating=4),
                                        phase=3, stats=ItemStats(intellect=15, spell_power=39, spell_crit_rating=33))

# Phase 4
ROBE_OF_DEPARTED_SPIRITS = Gear(db_id=33317, name="Robe of Departed Spirits", phase=4, stats=ItemStats(intellect=31, spell_power=54, spell_haste_rating=35))

# Phase 5
SUNFIRE_ROBE = Gear(db_id=34364, name="Sunfire Robe", sockets=['r', 'r', 'r'], bonus=ItemStats(spell_power=5), phase=5, stats=ItemStats(intellect=34,
                                                                                                                                        spell_power=71,
                                                                                                                                        spell_crit_rating=40,
                                                                                                                                        spell_haste_rating=40))
ROBES_OF_GHOSTLY_HATRED = Gear(db_id=34399, name="Robes of Ghostly Hatred", sockets=['r', 'r', 'y'], bonus=ItemStats(spell_power=5), phase=5,
                               stats=ItemStats(intellect=40, spell_power=71, spell_crit_rating=26, spell_haste_rating=27))
FEL_CONQUERER_RAIMENTS = Gear(db_id=34232, name="Fel Conquerer Raiments", sockets=['r', 'y', 'y'], bonus=ItemStats(spell_power=5), phase=5,
                              stats=ItemStats(intellect=41, spell_power=71, spell_crit_rating=24, spell_haste_rating=33))
