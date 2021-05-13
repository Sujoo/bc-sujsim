from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats

# Pre-BIS

# Phase 1
EREDAR_WAND_OF_OBLITERATION = Gear(db_id=28783, name="Eredar Wand of Obliteration", stats=ItemStats(intellect=11, spell_power=16, spell_crit_rating=14))
TIRISFAL_WAND_OF_ASCENDENCY = Gear(db_id=28673, name="Tirisfal Wand of Ascendency", stats=ItemStats(intellect=9, spell_power=15, spell_hit_rating=11))
THE_BLACK_STALK = Gear(db_id=29350, name="The Black Stalk", stats=ItemStats(spell_power=20, spell_crit_rating=11))
DOOMFINGER = Gear(db_id=22821, name="Doomfinger", stats=ItemStats(spell_power=16, spell_crit_rating=14))
NETHER_CORES_CONTROL_ROD = Gear(db_id=28386, name="Nether Core's Control Rod", stats=ItemStats(intellect=10, spell_power=13, spell_hit_rating=8))
NETHEKURSES_ROD_OF_TORMENT = Gear(db_id=25806, name="Nethekurse's Rod of Torment", stats=ItemStats(intellect=10, spell_power=11, spell_crit_rating=10))
ROD_OF_DIRE_SHADOWS = Gear(db_id=25808, name="Rod of Dire Shadows", stats=ItemStats(intellect=10, spell_power=11, spell_crit_rating=10))
GLADIATORS_TOUCH_OF_DEFEAT = Gear(db_id=28320, name="Gladiator's Touch of Defeat", stats=ItemStats(intellect=11, spell_power=14))
WAND_OF_THE_SEER = Gear(db_id=30859, name="Wand of the Seer", stats=ItemStats(intellect=8, spell_power=18))
WAND_OF_FATES = Gear(db_id=22820, name="Wand of Fates", stats=ItemStats(intellect=7, spell_power=12, spell_hit_rating=8))

# Phase 2
WAND_OF_THE_FORGOTTEN_STAR = Gear(db_id=29982, name="Wand of the Forgotten Star", phase=2,
                                  stats=ItemStats(spell_power=23, spell_crit_rating=14, spell_hit_rating=11))
MERCILESS_GLADIATORS_TOUCH_OF_DEFEAT = Gear(db_id=32962, name="Merciless Gladiator's Touch of Defeat", phase=2, stats=ItemStats(intellect=13, spell_power=16))

# Phase 3
WAND_OF_PRISMATIC_FOCUS = Gear(db_id=32343, name="Wand of Prismatic Focus", phase=3, stats=ItemStats(spell_power=25, spell_hit_rating=13))

# Phase 4
CARVED_WITCH_DOCTORS_STICK = Gear(db_id=33192, name="Carved Witch Doctor's Stick", sockets=['b'], bonus=ItemStats(spell_power=2), phase=4, stats=ItemStats(
    intellect=15,
    spell_power=18))

# Phase 5
WAND_OF_THE_DEMONSOUL = Gear(db_id=34347, name="Wand of the Demonsoul", sockets=['y'], bonus=ItemStats(spell_power=2), phase=5,
                             stats=ItemStats(intellect=10, spell_power=22, spell_haste_rating=18))
