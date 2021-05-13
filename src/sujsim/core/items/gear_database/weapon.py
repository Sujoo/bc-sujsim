from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats

# Pre-BIS

# Phase 1
GLADIATORS_WAR_STAFF = Gear(db_id=24557, name="Gladiator's War Staff", is_two_hand=True,
                            stats=ItemStats(intellect=35, spell_power=199, spell_crit_rating=36, spell_hit_rating=21))
GLADIATORS_SPELLBLADE = Gear(db_id=28297, name="Gladiator's Spellblade", stats=ItemStats(intellect=18, spell_power=199))
TALON_OF_THE_TEMPEST = Gear(db_id=30723, name="Talon of the Tempest", sockets=['y', 'y'], bonus=ItemStats(intellect=3), stats=ItemStats(intellect=10,
                                                                                                                                        spell_power=194,
                                                                                                                                        spell_crit_rating=19,
                                                                                                                                        spell_hit_rating=9))
STAFF_OF_INFINITE_MYSTERIES = Gear(db_id=28633, name="Staff of Infinite Mysteries", is_two_hand=True,
                                   stats=ItemStats(intellect=51, spell_power=185, spell_hit_rating=23))
NATHREZIM_MINDBLADE = Gear(db_id=28770, name="Nathrezim Mindblade", stats=ItemStats(intellect=18, spell_power=203, spell_crit_rating=23))
BLOODMAW_MAGUS_BLADE = Gear(db_id=28802, name="Bloodmaw Magus-Blade", stats=ItemStats(intellect=15, spell_power=203, spell_crit_rating=25))
ATIESH_GREATSTAFF_OF_THE_GUARDIAN = Gear(db_id=22589, name="Atiesh, Greatstaff of the Guardian", is_two_hand=True,
                                         stats=ItemStats(intellect=32, spell_power=150, spell_crit_rating=28, spell_hit_rating=16))
ETERNIUM_RUNED_BLADE = Gear(db_id=23554, name="Eternium Runed Blade", stats=ItemStats(intellect=19, spell_power=168, spell_crit_rating=21))
STORMCALLER = Gear(db_id=29155, name="Stormcaller", stats=ItemStats(intellect=12, spell_power=159, spell_crit_rating=21))
HIGH_WARLORDS_WAR_STAFF = Gear(db_id=28935, name="High Warlord's War Staff",
                               stats=ItemStats(intellect=30, spell_power=121, spell_crit_rating=30, spell_hit_rating=20))
WARPSTAFF_OF_ARCANUM = Gear(db_id=28341, name="Warpstaff of Arcanum", stats=ItemStats(intellect=38, spell_power=121, spell_crit_rating=26, spell_hit_rating=16))
BLOODFIRE_GREATSTAFF = Gear(db_id=28188, name="Bloodfire Greatstaff", stats=ItemStats(intellect=42, spell_power=121, spell_crit_rating=28))
GRAND_SCEPTER_OF_THE_NEXUS_KINGS = Gear(db_id=27842, name="Grand Scepter of the Nexus-Kings",
                                        stats=ItemStats(intellect=43, spell_power=121, spell_hit_rating=19))
GREATSWORD_OF_HORRID_DREAMS = Gear(db_id=27905, name="Greatsword of Horrid Dreams", stats=ItemStats(intellect=14, spell_power=130, spell_hit_rating=14))
STARLIGHT_DAGGER = Gear(db_id=27543, name="Starlight Dagger", stats=ItemStats(intellect=15, spell_power=121, spell_hit_rating=16))
RUNESONG_DAGGER = Gear(db_id=27868, name="Runesong Dagger", stats=ItemStats(intellect=11, spell_power=121, spell_crit_rating=20))
THE_WILLBREAKER = Gear(db_id=27512, name="The Willbreaker", stats=ItemStats(intellect=14, spell_power=121, spell_crit_rating=17))
MANA_WRATH = Gear(db_id=27899, name="Mana Wrath", stats=ItemStats(intellect=18, spell_power=126))
CONTINUUM_BLADE = Gear(db_id=29185, name="Continuum Blade", stats=ItemStats(intellect=11, spell_power=121, spell_hit_rating=8))

# Phase 2
THE_NEXUS_KEY = Gear(db_id=29988, name="The Nexus Key", is_two_hand=True, phase=2, stats=ItemStats(intellect=52, spell_power=236, spell_crit_rating=51))
MERCILESS_GLADIATORS_WAR_STAFF = Gear(db_id=32055, name="Merciless Gladiator's War Staff", is_two_hand=True, phase=2,
                                      stats=ItemStats(intellect=42, spell_power=225, spell_crit_rating=42, spell_hit_rating=24))
FANG_OF_THE_LEVIATHAN = Gear(db_id=30095, name="Fang of the Leviathan", phase=2, stats=ItemStats(intellect=20, spell_power=221, spell_crit_rating=21))
MERCILESS_GLADIATORS_SPELLBLADE = Gear(db_id=32053, name="Merciless Gladiator's Spellblade", phase=2,
                                       stats=ItemStats(intellect=18, spell_power=225, spell_hit_rating=15))

# Phase 3
ZHARDOOM_GREATSTAFF_OF_THE_DEVOURER = Gear(db_id=32374, name="Zhar'doom, Greatstaff of the Devourer", is_two_hand=True, phase=3,
                                           stats=ItemStats(intellect=47, spell_power=259, spell_crit_rating=36, spell_haste_rating=55))
VENGEFUL_GLADIATORS_BATTLE_STAFF = Gear(db_id=34540, name="Vengeful Gladiator's Battle Staff", is_two_hand=True, phase=3,
                                        stats=ItemStats(intellect=46, spell_power=247, spell_crit_rating=46, spell_hit_rating=28))
TEMPEST_OF_CHAOS = Gear(db_id=30910, name="Tempest of Chaos", phase=3,
                        stats=ItemStats(intellect=22, spell_power=259, spell_crit_rating=24, spell_hit_rating=17))
THE_MAELSTROMS_FURY = Gear(db_id=32237, name="The Maelstrom's Fury", phase=3, stats=ItemStats(intellect=21, spell_power=236, spell_crit_rating=22))
VENGEFUL_GLADIATORS_SPELLBLADE = Gear(db_id=33763, name="Vengeful Gladiator's Spellblade", phase=3,
                                      stats=ItemStats(intellect=20, spell_power=247, spell_hit_rating=17))

# Phase 4
BRUTAL_GLADIATORS_BATTLE_STAFF = Gear(db_id=34987, name="Brutal Gladiator's Battle Staff", is_two_hand=True, phase=4,
                                      stats=ItemStats(intellect=50, spell_power=266, spell_crit_rating=50, spell_hit_rating=32))
AMANI_DIVINING_STAFF = Gear(db_id=33494, name="Amani Divining Staff", is_two_hand=True, sockets=['r', 'y', 'b'], bonus=ItemStats(spell_power=5), phase=4,
                            stats=ItemStats(intellect=47, spell_power=217, spell_crit_rating=31))
BLADE_OF_TWISTED_VISIONS = Gear(db_id=33467, name="Blade of Twisted Visions", phase=4, stats=ItemStats(intellect=21, spell_power=229, spell_haste_rating=21))
WUBS_CURSED_HEXBLADE = Gear(db_id=33354, name="Wub's Cursed Hexblade", phase=4,
                            stats=ItemStats(intellect=21, spell_power=217, spell_crit_rating=20, spell_hit_rating=13))

# Phase 5
GRAND_MAGISTERS_STAFF_OF_TORRENTS = Gear(db_id=34182, name="Grand Magister's Staff of Torrents", is_two_hand=True, sockets=['y', 'y', 'y'], bonus=ItemStats(
    spell_power=5), phase=5, stats=ItemStats(intellect=52, spell_power=266, spell_crit_rating=49, spell_hit_rating=50))
SUNFLARE = Gear(db_id=34336, name="Sunflare", phase=5, stats=ItemStats(intellect=20, spell_power=292, spell_crit_rating=30, spell_haste_rating=23))
