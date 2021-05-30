from sujsim.core.items.enchant import Enchant
from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.stats.item_stats import ItemStats

# Weapon
SUNFIRE = Enchant(db_id=46540, name="Sunfire", stats=ItemStats(spell_power=50, impacted_schools=[MagicSchool.ARCANE, MagicSchool.FIRE]))
SOULFROST = Enchant(db_id=46538, name="Soulfrost", stats=ItemStats(spell_power=54, impacted_schools=[MagicSchool.FROST]))
MAJOR_SPELLPOWER_WEAPON = Enchant(db_id=27975, name="Sunfire", stats=ItemStats(spell_power=40))

# Head
GLYPH_OF_POWER = Enchant(db_id=35447, name="Glyph of Power", stats=ItemStats(spell_power=22, spell_hit_rating=14))
PRESENCE_OF_SIGHT = Enchant(db_id=24164, name="Presence of Sight", stats=ItemStats(spell_power=18, spell_hit_rating=8))

# Shoulder
GREATER_INSCRIPTION_OF_DISC = Enchant(db_id=35406, name="Greater Inscription of Discipline (Aldor)", stats=ItemStats(spell_power=18, spell_crit_rating=10))
GREATER_INSCRIPTION_OF_ORB = Enchant(db_id=35437, name="Greater Inscription of the Orb (Scryer)", stats=ItemStats(spell_power=12, spell_crit_rating=15))
POWER_OF_SCOURGE = Enchant(db_id=29467, name="Power of the Scourge", stats=ItemStats(spell_power=15, spell_crit_rating=14))
INSCRIPTION_OF_DISC = Enchant(db_id=35405, name="Inscription of the Orb (Aldor)", stats=ItemStats(spell_power=15))
INSCRIPTION_OF_ORB = Enchant(db_id=35436, name="Inscription of the Orb (Scryer)", stats=ItemStats(spell_crit_rating=13))

# Chest
EXCEPTIONAL_STATS = Enchant(db_id=46502, name="Exceptional Stats", stats=ItemStats(intellect=6, spirit=6, stamina=6))
MAJOR_SPIRIT = Enchant(db_id=46504, name="", stats=ItemStats(spirit=15))

# Wrist
SPELLPOWER_WRIST = Enchant(db_id=46498, name="Spellpower", stats=ItemStats(spell_power=15))
MAJOR_INTELLECT = Enchant(db_id=46496, name="Major Intellect", stats=ItemStats(intellect=12))
RESTORE_MANA_PRIMT = Enchant(db_id=46497, name="Restore Mana Prime", stats=ItemStats(mp_5=6))

# Hands
MAJOR_SPELLPOWER_HANDS = Enchant(db_id=46514, name="Major Spellpower", stats=ItemStats(spell_power=20))
SPELL_STRIKE = Enchant(db_id=46516, name="Spell Strike", stats=ItemStats(spell_hit_rating=15))
BLASTING = Enchant(db_id=46512, name="Blasting", stats=ItemStats(spell_crit_rating=10))

# Legs
RUNIC_SPELLTHREAD = Enchant(db_id=31372, name="Runic Spellthread", stats=ItemStats(spell_power=35))
MYSTIC_SPELLTHREAD = Enchant(db_id=31371, name="Mystic Spellthread", stats=ItemStats(spell_power=25))

# Feet
BOARS_SPEED = Enchant(db_id=46470, name="Boar's Speed")
MAGISTERS_ARMOR_KIT = Enchant(db_id=32399, name="Magister's Armor Kit", stats=ItemStats(mp_5=3))
SPIRIT = Enchant(db_id=20024, name="Spirit", stats=ItemStats(spirit=5))

# Finger
SPELLPOWER_RING = Enchant(db_id=46518, name="Spellpower", stats=ItemStats(spell_power=12))
