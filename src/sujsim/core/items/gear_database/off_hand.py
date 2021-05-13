from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.spells.magic_school import MagicSchool

# Pre-BIS

# Phase 1
TALISMAN_OF_KALECGOS = Gear(db_id=29271, name="Talisman of Kalecgos", stats=ItemStats(intellect=14, spell_power=50, impacted_schools=[MagicSchool.ARCANE]))
TALISMAN_OF_NIGHTBANE = Gear(db_id=28603, name="Talisman of Nightbane", stats=ItemStats(intellect=19, spell_power=28, spell_crit_rating=17))
FLAMETONGUE_SEAL = Gear(db_id=29270, name="Flametongue Seal", stats=ItemStats(spell_crit_rating=17, spell_power=49, impacted_schools=[MagicSchool.FIRE]))
SAPPHIRONS_WING_BONE = Gear(db_id=29269, name="Sapphiron's Wing Bone", stats=ItemStats(spell_hit_rating=12, spell_power=51, impacted_schools=[
    MagicSchool.FROST]))
JEWEL_OF_INFINITE_POSSIBILITIES = Gear(db_id=28734, name="Jewel of Infinite Possibilities", stats=ItemStats(intellect=18, spell_power=23, spell_hit_rating=21))
KARABORIAN_TALISMAN = Gear(db_id=28781, name="Karaborian Talisman", stats=ItemStats(intellect=23, spell_power=35))
LAMP_OF_PEACEFUL_RADIANCE = Gear(db_id=28412, name="Lamp of Peaceful Radiance",
                                 stats=ItemStats(intellect=14, spell_power=21, spell_crit_rating=13, spell_hit_rating=12))
KHADGARS_KNAPSACK = Gear(db_id=29273, name="Khadgar's Knapsack", stats=ItemStats(spell_power=49))
SAPPHIRONS_LEFT_EYE = Gear(db_id=23049, name="Sapphiron's Left Eye", stats=ItemStats(intellect=8, spell_power=26, spell_crit_rating=14, spell_hit_rating=8))
GLADIATORS_ENDGAME = Gear(db_id=28346, name="Gladiator's Endgame", stats=ItemStats(intellect=14, spell_power=19))
MANUAL_OF_THE_NETHERMANCER = Gear(db_id=28260, name="Manual of the Nethermancer", stats=ItemStats(intellect=15, spell_power=21, spell_crit_rating=19))
STAR_HEART_LAMP = Gear(db_id=28187, name="Star-Heart Lamp", stats=ItemStats(intellect=18, spell_power=22, spell_hit_rating=12))

# Phase 2
FATHOMSTONE = Gear(db_id=30049, name="Fathomstone", phase=2, stats=ItemStats(intellect=12, spell_power=36, spell_crit_rating=23))
MERCILESS_GLADIATORS_ENDGAME = Gear(db_id=31978, name="Merciless Gladiator's Endgame", phase=2, stats=ItemStats(intellect=19, spell_power=33))

# Phase 3
CHRONICLE_OF_DARK_SECRETS = Gear(db_id=30872, name="Chronicle of Dark Secrets", phase=3,
                                 stats=ItemStats(intellect=12, spell_power=42, spell_crit_rating=23, spell_hit_rating=17))
BLIND_SEERS_ICON = Gear(db_id=32361, name="Blind-Seers Icon", phase=3, stats=ItemStats(intellect=16, spell_power=42, spell_hit_rating=24))

# Phase 4
FETISH_OF_THE_PRIMAL_GODS = Gear(db_id=33334, name="Fetish of the Primal Gods", phase=4, stats=ItemStats(intellect=17, spell_power=37, spell_haste_rating=17))

# Phase 5
HEART_OF_THE_PIT = Gear(db_id=34179, name="Heart of the Pit", phase=5, stats=ItemStats(intellect=21, spell_power=39, spell_haste_rating=32))
