from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats

# Pre-BIS

# Phase 1
ANCIENT_SPELLCLOAK_OF_THE_HIGHBORNE = Gear(db_id=30735, name="Ancient Spellcloak of the Highborne",
                                           stats=ItemStats(intellect=15, spell_power=36, spell_crit_rating=19))
RUBY_DRAPE_OF_THE_MYSTICANT = Gear(db_id=28766, name="Ruby Drape of the Mysticant", stats=ItemStats(intellect=21, spell_power=30, spell_hit_rating=18))
BRUTE_CLOAK_OF_THE_OGRE_MAGI = Gear(db_id=28797, name="Brute Cloak of the Ogre-Magi", stats=ItemStats(intellect=20, spell_power=28, spell_crit_rating=23))
CLOAK_OF_THE_NECROPOLIS = Gear(db_id=23050, name="Cloak of the Necropolis",
                               stats=ItemStats(intellect=11, spell_power=26, spell_crit_rating=14, spell_hit_rating=8))
SHADOW_CLOAK_OF_DALARAN = Gear(db_id=28570, name="Shadow-Cloak of Dalaran", stats=ItemStats(intellect=18, spell_power=36))
SHAWL_OF_SHIFTING_PROBABILITIES = Gear(db_id=29369, name="Shawl of Shifting Probabilities", stats=ItemStats(intellect=16, spell_power=21, spell_crit_rating=22))
OGRE_SLAYERS_COVER = Gear(db_id=25777, name="Ogre Slayer's Cover", stats=ItemStats(intellect=18, spell_power=20, spell_crit_rating=16))
SETHEKK_ORACLE_CLOAK = Gear(db_id=27981, name="Sethekk Oracle Cloak", stats=ItemStats(intellect=18, spell_power=22, spell_hit_rating=12))
CLOAK_OF_THE_DEVOURED = Gear(db_id=22731, name="Cloak of the Devoured", stats=ItemStats(intellect=10, spell_power=30, spell_hit_rating=8))
CLOAK_OF_WOVEN_ENERGY = Gear(db_id=29813, name="Cloak of Woven Energy", stats=ItemStats(intellect=13, spirit=3, spell_power=29, spell_crit_rating=6))

# Phase 2
ROYAL_CLOAK_OF_THE_SUNSTRIDERS = Gear(db_id=29992, name="Royal Cloak of the Sunstriders", phase=2, stats=ItemStats(intellect=22, spell_power=44))

# Phase 3
CLOAK_OF_THE_ILLIDARI_COUNCIL = Gear(db_id=32331, name="Cloak of the Illidari Council", phase=3,
                                     stats=ItemStats(intellect=16, spell_power=42, spell_crit_rating=25))
SHROUD_OF_THE_HIGHBORNE = Gear(db_id=32524, name="Shroud of the Highborne", phase=3, stats=ItemStats(intellect=23, spell_power=23, spell_haste_rating=32))

# Phase 4
SHADOWCASTERS_DRAPE = Gear(db_id=33591, name="Shadowcaster's Drape", phase=4, stats=ItemStats(intellect=20, spell_power=27, spell_haste_rating=25))
CLOAK_OF_ANCIENT_RITUALS = Gear(db_id=33592, name="Cloak of Ancient Rituals", phase=4, stats=ItemStats(intellect=20, spell_power=17, spell_haste_rating=25))

# Phase 5
TATTERED_CAPE_OF_ANTONIDAS = Gear(db_id=34242, name="Tattered Cape of Antonidas", sockets=['r'], bonus=ItemStats(spell_power=2), phase=5,
                                  stats=ItemStats(intellect=26, spell_power=42, spell_haste_rating=32))
