from sujsim.core.items.gem import Gem
from sujsim.core.stats.item_stats import ItemStats


# Phase 1
CHAOTIC_SKYFIRE = Gem(db_id=34220, name="Chaotic Skyfire Diamond", color="m", stats=ItemStats(spell_crit_rating=12))
EMBER_SKYFIRE = Gem(db_id=35503, name="Ember Skyfire Diamond", color="m", stats=ItemStats(spell_power=14))
INSIGHTFUL_EARTHSTORM = Gem(25901, name="Insightful Earthstorm Diamond", color="m", stats=ItemStats(intellect=12))
DESTRUCTIVE_SKYFIRE_DIAMOND = Gem(db_id=25890, name="Destructive Skyfire Diamond", color="m", stats=ItemStats(spell_power=14))
IMBUED_UNSTABLE_DIAMOND = Gem(db_id=32641, name="Imbued Unstable Diamond", color="m", stats=ItemStats(spell_power=14))
SWIFT_SKYFIRE_DIAMOND = Gem(db_id=28557, name="Swift Skyfire Diamond", color="m", stats=ItemStats(spell_power=12))

RUNED_ORNATE_RUBY = Gem(db_id=28118, name="Runed Ornate Ruby", color="r", stats=ItemStats(spell_power=12), is_unique=True)
RUNED_LIVING_RUBY = Gem(db_id=24030, name="Runed Living Ruby", color="r", stats=ItemStats(spell_power=9))

INFUSED_FIRE_OPAL = Gem(db_id=30551, name="Infused Fire Opal", color="o", stats=ItemStats(intellect=4, spell_power=6))
SHINING_FIRE_OPAL = Gem(db_id=30564, name="Shining Fire Opal", color="o", stats=ItemStats(spell_power=6, spell_hit_rating=5))
POTENT_FIRE_OPAL = Gem(db_id=30588, name="Potent Fire Opal", color="o", stats=ItemStats(spell_power=6, spell_crit_rating=4))
POTENT_ORNATE_TOPAZ = Gem(db_id=28123, name="Potent Ornate Topaz", color="o", stats=ItemStats(spell_power=6, spell_crit_rating=5), is_unique=True)
VEILED_NOBLE_TOPAZ = Gem(db_id=31867, name="Veiled Noble Topaz", color="o", stats=ItemStats(spell_power=5, spell_hit_rating=4))
POTENT_NOBLE_TOPAZ = Gem(db_id=24059, name="Potent Noble Topaz", color="o", stats=ItemStats(spell_power=5, spell_crit_rating=4))
UNSTABLE_TOPAZ = Gem(db_id=32638, name="Unstable Topaz", color="o", stats=ItemStats(spell_power=5, intellect=4), is_unique=True)

GLEAMING_ORNATE_DAWNSTONE = Gem(db_id=28120, name="Gleaming Ornate Dawnstone", color="y", stats=ItemStats(spell_crit_rating=10), is_unique=True)
GREAT_DAWNSTONE = Gem(db_id=31861, name="Great Dawnstone", color="y", stats=ItemStats(spell_hit_rating=8))
GLEAMING_DAWNSTONE = Gem(db_id=24050, name="Gleaming Dawnstone", color="y", stats=ItemStats(spell_crit_rating=8))
BRILLIANT_DAWNSTONE = Gem(db_id=24047, name="Brilliant Dawnstone", color="y", stats=ItemStats(intellect=8))

FLOURESCENT_TANZANITE = Gem(db_id=30600, name="Fluorescent Tanzanite", color="p", stats=ItemStats(spirit=4, spell_power=6))
GLOWING_TANZANITE = Gem(db_id=30555, name="Glowing Tanzanite", color="p", stats=ItemStats(spell_power=6))
GLOWING_NIGHTSEYE = Gem(db_id=24056, name="Glowing Nightseye", color="p", stats=ItemStats(spell_power=5))

SEERS_CHRYSOPRASE = Gem(db_id=30586, name="Seer's Chrysoprase", color="g", stats=ItemStats(intellect=4, spirit=5))
LAMBENT_CHRYSOPRASE = Gem(db_id=30606, name="Lambent Chrysoprase", color="g", stats=ItemStats(spell_hit_rating=5, mp_5=2))
RUNE_COVERED_CHRYSOPRASE = Gem(db_id=30560, name="Rune Covered Chrysoprase", color="g", stats=ItemStats(spell_crit_rating=5, mp_5=2))
DAZZLING_CHRYSOPRASE = Gem(db_id=30589, name="Dazzling Chrysoprase", color="g", stats=ItemStats(intellect=5, mp_5=2))
DAZZLING_TALASITE = Gem(db_id=24065, name="Dazzling Talasite", color="g", stats=ItemStats(intellect=4, mp_5=2))

SPARKLING_STAR_OF_ELUNE = Gem(db_id=24035, name="Sparkling Star of Elune", color="b", stats=ItemStats(spirit=8))
LUSTROUS_STAR_OF_ELUNE = Gem(db_id=24037, name="Lustrous Star of Elune", color="b", stats=ItemStats(mp_5=3))

# Phase 3
DON_JULIOS_HEART = Gem(db_id=33133, name="Don Julio's Heart", color="r", stats=ItemStats(spell_power=14), is_unique=True, phase=3)
RUNED_CRIMSON_SPINEL = Gem(db_id=32196, name="Runed Crimson Spinel", color="r", stats=ItemStats(spell_power=12), phase=3)

VEILED_PYRESTONE = Gem(db_id=32221, name="Veiled Pyrestone", color="o", stats=ItemStats(spell_power=6, spell_hit_rating=5), phase=3)
POTENT_PYRESTONE = Gem(db_id=32218, name="Potent Pyrestone", color="o", stats=ItemStats(spell_power=6, spell_crit_rating=5), phase=3)

BLOOD_OF_AMBER = Gem(db_id=33140, name="Blood of Amber", color="y", stats=ItemStats(spell_crit_rating=12), is_unique=True, phase=3)
GREAT_LIONSEYE = Gem(db_id=32210, name="Great Lionseye", color="y", stats=ItemStats(spell_hit_rating=10), phase=3)
GLEAMING_LIONSEYE = Gem(db_id=32207, name="Gleaming Lionseye", color="y", stats=ItemStats(spell_crit_rating=10), phase=3)
BILLIANT_LIONSEYE = Gem(db_id=32204, name="Brilliant Lionseye", color="y", stats=ItemStats(intellect=10), phase=3)

# Phase 5
RECKLESS_PYRESTONE = Gem(db_id=35760, name="Reckless Pyrestone", color="o", stats=ItemStats(spell_power=6, spell_haste_rating=5), phase=5)
QUICK_LIONSEYE = Gem(db_id=35761, name="Quick Lionseye", color="y", stats=ItemStats(spell_haste_rating=10), phase=5)