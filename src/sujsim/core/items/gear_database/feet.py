from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.spells.magic_school import MagicSchool

# Pre-BIS

# Phase 1
BOOTS_OF_FORETELLING = Gear(db_id=28517, name="Boots of Foretelling", sockets=['r', 'y'], bonus=ItemStats(intellect=3), stats=ItemStats(intellect=23,
                                                                                                                                        spell_power=26,
                                                                                                                                        spell_crit_rating=19))
SIGIL_LACED_BOOTS = Gear(db_id=28406, name="Sigil-Laced Boots", sockets=['r', 'y'], bonus=ItemStats(intellect=3),
                         stats=ItemStats(intellect=18, spell_power=20, spell_crit_rating=17))
RUBY_SLIPPERS = Gear(db_id=28585, name="Ruby Slippers", stats=ItemStats(intellect=29, spell_power=35, spell_hit_rating=16))
BOOTS_OF_BLASPHEMY = Gear(db_id=29242, name="Boots of Blasphemy", stats=ItemStats(intellect=29, spell_power=36))
FROZEN_SHADOWEAVE_BOOTS = Gear(db_id=21870, name="Frozen Shadoweave Boots", sockets=['y', 'b'], bonus=ItemStats(spell_hit_rating=3),
                               stats=ItemStats(intellect=9, spell_power=57, impacted_schools=[MagicSchool.FROST, MagicSchool.SHADOW]))
EMBROIDERED_SPELLPYRE_BOOTS = Gear(db_id=27848, name="Embroidered Spellpyre Boots", stats=ItemStats(intellect=21, spell_power=41))
BOOTS_OF_ETHEREAL_MANIPULATION = Gear(db_id=29258, name="Boots of Ethereal Manipulation", stats=ItemStats(intellect=27, spell_power=33))
ETHEREAL_BOOTS_OF_THE_SKYSTRIDER = Gear(db_id=25957, name="Ethereal Boots of the Skystrider",
                                        stats=ItemStats(intellect=19, spell_power=26, spell_crit_rating=17))
SHATTRATH_JUMPERS = Gear(db_id=28179, name="Shattrath Jumpers", sockets=['b', 'y'], bonus=ItemStats(intellect=3), stats=ItemStats(intellect=17, spell_power=29))
GENERALS_SILK_FOOTGUARDS = Gear(db_id=28410, name="General's Silk Footguards", stats=ItemStats(intellect=23, spell_power=28, spell_crit_rating=24))
EXTRAVAGANT_BOOTS_OF_MALICE = Gear(db_id=27821, name="Extravagant Boots of Malice", stats=ItemStats(intellect=24, spell_power=30, spell_hit_rating=14))
BOOTS_OF_THE_INFERNAL_COVEN = Gear(db_id=28670, name="Boots of the Infernal Coven", stats=ItemStats(intellect=27, spell_power=34))
FROSTFIRE_SANDALS = Gear(db_id=22500, name="Frostfire Sandals", stats=ItemStats(intellect=18, spell_power=28, spell_crit_rating=14))
ENIGMA_BOOTS = Gear(db_id=21344, name="Enigma Boots", stats=ItemStats(intellect=15, spell_power=28, spell_hit_rating=8))

# Phase 2
VELVET_BOOTS_OF_THE_GUARDIAN = Gear(db_id=30067, name="Velvet Boots of the Guardian", phase=2,
                                    stats=ItemStats(intellect=21, spell_power=49, spell_crit_rating=24))
BOOTS_OF_BLASTING = Gear(db_id=30037, name="Boots of Blasting", phase=2,
                         stats=ItemStats(intellect=25, spell_power=39, spell_crit_rating=25, spell_hit_rating=18))
VETERANS_SILK_FOOTGUARDS = Gear(db_id=32795, name="Veteran's Silk Footguards", phase=2, stats=ItemStats(intellect=27, spell_power=32, spell_crit_rating=27))
VETERANS_DREADWEAVE_STALKERS = Gear(db_id=32787, name="Veteran's Dreadweave Stalkers", phase=2, stats=ItemStats(intellect=30, spell_power=36))

# Phase 3
SLIPPERS_OF_THE_SEACALLER = Gear(db_id=32239, name="Slippers of the Seacaller", sockets=['y', 'b'], bonus=ItemStats(spell_power=4), phase=3,
                                 stats=ItemStats(intellect=18, spell_power=44, spell_crit_rating=29))
BLUE_SUEDE_SHOES = Gear(db_id=30894, name="Blue Suede Shoes", phase=3, stats=ItemStats(intellect=32, spell_power=56, spell_hit_rating=18))

# Phase 4
FOOTPADS_OF_MADNESS = Gear(db_id=33357, name="Footpads of Madness", phase=4, stats=ItemStats(intellect=22, spell_power=50, spell_haste_rating=25))

# Phase 5
BOOTS_OF_THE_TEMPEST = Gear(db_id=34574, name="Boots of the Tempest", sockets=['y'], bonus=ItemStats(spell_power=2), phase=5,
                            stats=ItemStats(intellect=29, spell_power=50, spell_crit_rating=20, spell_hit_rating=15, spell_haste_rating=25))
BOOTS_OF_INCANTATIONS = Gear(db_id=34919, name="Boots of Incantations", sockets=['y'], bonus=ItemStats(spell_power=2), phase=5,
                             stats=ItemStats(intellect=26, spell_power=47, spell_hit_rating=17))
