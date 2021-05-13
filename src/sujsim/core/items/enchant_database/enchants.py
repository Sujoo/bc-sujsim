from sujsim.core.items.enchant import Enchant
from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.stats.item_stats import ItemStats

# Weapon
SUNFIRE = Enchant(db_id=46540, name="Sunfire", stats=ItemStats(spell_power=50, impacted_schools=[MagicSchool.ARCANE, MagicSchool.FIRE]))
"""
weapon: [
        { id: 46540, title: "Sunfire", sp_arcane: 50, sp_fire: 50 },
        { id: 46538, title: "Soulfrost", sp_frost: 54 },
        { id: 46533, title: "Major Spellpower", sp: 40 },
    ],
    head: [
        { id: 35447, title: "Glyph of Power", sp: 22, hit: 14 },
        { id: 24164, title: "Presence of Sight", sp: 18, hit: 8, q: "rare" },
    ],
    shoulder: [
        { id: 35406, title: "Greater Inscription of Discipline (Aldor)", sp: 18, crit: 10, q: "rare" },
        { id: 35437, title: "Greater Inscription of the Orb (Scryer)", sp: 12, crit: 15, q: "rare" },
        { id: 29467, title: "Power of the Scourge", sp: 15, crit: 14, q: "epic" },
        { id: 35405, title: "Inscription of the Orb (Aldor)", sp: 15 },
        { id: 35436, title: "Inscription of the Orb (Scryer)", crit: 13 },
    ],
    chest: [
        { id: 46502, title: "Exceptional Stats", int: 6, spi: 6 },
        { id: 46504, title: "Major Spirit", spi: 15 },
    ],
    wrist: [
        { id: 46498, title: "Spellpower", sp: 15 },
        { id: 46496, title: "Major Intellect", int: 12 },
        { id: 46497, title: "Restore Mana Prime", mp5: 6 },
    ],
    hands: [
        { id: 46514, title: "Major Spellpower", sp: 20 },
        { id: 46516, title: "Spell Strike", hit: 15 },
        { id: 46512, title: "Blasting", crit: 10 },
    ],
    legs: [
        { id: 31372, title: "Runic Spellthread", sp: 35, q: "epic" },
        { id: 31371, title: "Mystic Spellthread", sp: 25, q: "rare" },
        { id: 24164, title: "Presence of Sight", sp: 18, hit: 8, q: "epic" },
    ],
    feet: [
        { id: 46470, title: "Boar's Speed", q: "rare" },
        { id: 32399, title: "Magister's Armor Kit", mp5: 3, q: "common" },
        { id: 20024, title: "Spirit", spi: 5 },
    ],
    finger: [
        { id: 46518, title: "Spellpower", sp: 12 },
    ],
"""