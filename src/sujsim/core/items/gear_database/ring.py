from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats

# Pre-BIS

# Phase 1
RING_OF_CONFLICT_SURVIVAL = Gear(db_id=31922, name="Ring of Conflict Survival", stats=ItemStats(stamina=28, spell_power=23, spell_crit_rating=20))
VIOLET_SIGNET_OF_THE_ARCHMAGE = Gear(db_id=29287, name="Violet Signet of the Archmage", stats=ItemStats(intellect=23, spell_power=29, spell_crit_rating=17))
RING_OF_RECURRENCE = Gear(db_id=28753, name="Ring of Recurrence", stats=ItemStats(intellect=15, spell_power=32, spell_crit_rating=19))
BAND_OF_CRIMSON_FURY = Gear(db_id=28793, name="Band of Crimson Fury", stats=ItemStats(intellect=22, spell_power=28, spell_hit_rating=16))
VIOLET_SIGNET = Gear(db_id=29286, name="Violet Signet", stats=ItemStats(intellect=22, spell_power=28, spell_crit_rating=17))
SPARKING_ARCANITE_RING = Gear(db_id=28227, name="Sparking Arcanite Ring",
                              stats=ItemStats(intellect=14, spell_power=22, spell_crit_rating=14, spell_hit_rating=10))
RING_OF_CRYPTIC_DREAMS = Gear(db_id=29367, name="Ring of Cryptic Dreams", stats=ItemStats(intellect=17, spell_power=23, spell_crit_rating=20))
COBALT_BAND_OF_TYRIGOSA = Gear(db_id=29352, name="Cobalt Band of Tyrigosa", stats=ItemStats(intellect=17, spell_power=35))
EVOKERS_MARK_OF_THE_REDEMPTION = Gear(db_id=31075, name="Evoker's Mark of the Redemption", stats=ItemStats(intellect=15, spell_power=29, spell_crit_rating=10))
MANASTORM_BAND = Gear(db_id=30366, name="Manastorm Band", stats=ItemStats(intellect=15, spell_power=29, spell_crit_rating=10))
SPECTRAL_BAND_OF_INNERVATION = Gear(db_id=28510, name="Spectral Band of Innervation", stats=ItemStats(intellect=24, spell_power=29))
RYNGOS_BAND_OF_INGENUITY = Gear(db_id=28394, name="Ryngo's Band of Ingenuity", stats=ItemStats(intellect=14, spell_power=25, spell_crit_rating=14))
BAND_OF_DOMINION = Gear(db_id=31290, name="Band of Dominion", stats=ItemStats(spell_power=28, spell_crit_rating=21))
SCINTILLATING_CORAL_BAND = Gear(db_id=27784, name="Scintillating Coral Band", stats=ItemStats(intellect=15, spell_power=21, spell_crit_rating=17))
SEERS_SIGNET = Gear(db_id=29126, name="Seer's Signet", stats=ItemStats(spell_power=34, spell_crit_rating=12))
LOLAS_EVE = Gear(db_id=31339, name="Lola's Eve", stats=ItemStats(intellect=14, spell_power=29))
ASHYENS_GIFT = Gear(db_id=29172, name="Ashyen's Gift", stats=ItemStats(spell_power=23, spell_hit_rating=21))
BAND_OF_THE_GUARDIAN = Gear(db_id=29320, name="Band of the Guardian", stats=ItemStats(intellect=11, spell_power=23, spell_crit_rating=17))
WRATH_OF_CENARIUS = Gear(db_id=21190, name="Wrath of Cenarius", stats=ItemStats())
RING_OF_THE_FALLEN_GOD = Gear(db_id=21709, name="Ring of the Fallen God", stats=ItemStats(intellect=6, spell_power=37, spell_hit_rating=8))
FROSTFIRE_RING = Gear(db_id=23062, name="Frostfire Ring", stats=ItemStats(intellect=10, spell_power=30, spell_crit_rating=14))
BAND_OF_THE_INEVITABLE = Gear(db_id=23031, name="Band of the Inevitable", stats=ItemStats(spell_power=36, spell_hit_rating=8))
# Phase 2
RING_OF_ENDLESS_COILS = Gear(db_id=30109, name="Ring of Endless Coils", phase=2, stats=ItemStats(spell_power=37, spell_crit_rating=22))
BAND_OF_ALAR = Gear(db_id=29922, name="Band of Al'ar", phase=2, stats=ItemStats(intellect=23, spell_power=37))

# Phase 3
RING_OF_ANCIENT_KNOWLEDGE = Gear(db_id=32527, name="Ring of Ancient Knowledge", phase=3, stats=ItemStats(intellect=20, spell_power=39, spell_haste_rating=31))
RING_OF_CAPTURED_STORMS = Gear(db_id=32247, name="Ring of Captured Storms", phase=3, stats=ItemStats(spell_power=42, spell_crit_rating=29, spell_hit_rating=19))
BAND_OF_THE_ETERNAL_SAGE = Gear(db_id=29305, name="Band of the Eternal Sage", phase=3, stats=ItemStats(intellect=25, spell_power=34, spell_crit_rating=24))

# Phase 4
MANA_ATTUNED_BAND = Gear(db_id=33497, name="Mana Attuned Band", phase=4,
                         stats=ItemStats(intellect=19, spell_power=34, spell_hit_rating=18, spell_haste_rating=29))
SIGNET_OF_THE_QUIET_FOREST = Gear(db_id=33498, name="Signet of the Quiet Forest", phase=4, stats=ItemStats(intellect=17, spell_power=21, spell_haste_rating=30))
SIGNET_OF_ANCIENT_MAGICS = Gear(db_id=33293, name="Signet of Ancient Magics", sockets=['b'], bonus=ItemStats(spell_power=2), phase=4,
                                stats=ItemStats(intellect=17, spell_power=29))

# Phase 5
LOOP_OF_FORGED_POWER = Gear(db_id=34362, name="Loop of Forged Power", phase=5,
                            stats=ItemStats(intellect=28, spell_power=34, spell_hit_rating=19, spell_haste_rating=30))
RING_OF_OMNIPOTENCE = Gear(db_id=34230, name="Ring of Omnipotence", phase=5,
                           stats=ItemStats(intellect=14, spell_power=40, spell_crit_rating=22, spell_haste_rating=31))
FUSED_NETHERGON_BAND = Gear(db_id=34889, name="Fused Nethergon Band", phase=5, stats=ItemStats(intellect=19, spell_power=35, spell_hit_rating=28))
