from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats

# Pre-BIS

# Phase 1
SPELLSTRIKE_HOOD = Gear(db_id=24266, name="Spellstrike Hood", sockets=['b', 'y', 'r'],
                        stats=ItemStats(intellect=12, spell_power=46, spell_crit_rating=24, spell_hit_rating=16))
COWL_OF_THE_GRAND_ENGINEER = Gear(db_id=29986, name="Cowl of the Grand Engineer", sockets=['y', 'y', 'b'], bonus=ItemStats(spell_power=5), stats=ItemStats(
    intellect=27,
    spell_power=53, spell_crit_rating=35, spell_hit_rating=16))
COLLAR_OF_THE_ALDOR = Gear(db_id=29076, name="Collar of the Aldor", sockets=['m', 'b'], bonus=ItemStats(spell_power=5), stats=ItemStats(intellect=35,
                                                                                                                                        spell_power=41,
                                                                                                                                        spell_crit_rating=27))
UNI_MIND_HEADDRESS = Gear(db_id=28744, name="Uni-Mind Headdress", stats=ItemStats(intellect=40, spell_power=46, spell_crit_rating=25, spell_hit_rating=19))
EVOKERS_HELMET_OF_SECOND_SIGHT = Gear(db_id=31104, name="Evoker's Helmet of Second Sight", sockets=['b', 'b', 'y'], bonus=ItemStats(spell_power=5),
                                      stats=ItemStats(intellect=15, spell_power=35, spell_crit_rating=24))
GNOMISH_POWER_GOGGLES = Gear(db_id=23828, name="Gnomish Power Goggles", stats=ItemStats(intellect=21, spell_power=59, spell_crit_rating=28))
WICKED_WITCHS_HAT = Gear(db_id=28586, name="Wicked Witch's Hat", stats=ItemStats(intellect=38, spell_power=43, spell_crit_rating=32))
MANA_BINDERS_COWL = Gear(db_id=32089, name="Mana-Binders Cowl", sockets=['m', 'y'], bonus=ItemStats(spell_power=5), stats=ItemStats(intellect=29,
                                                                                                                                    spell_power=34,
                                                                                                                                    spell_crit_rating=15))
INCANTERS_COWL = Gear(db_id=28278, name="Incanter's Cowl", sockets=['m', 'y'], bonus=ItemStats(spirit=4),
                      stats=ItemStats(intellect=27, spirit=17, spell_power=29, spell_crit_rating=19))
HOOD_OF_OBLIVION = Gear(db_id=28415, name="Hood of Oblivion", sockets=['m', 'b'], bonus=ItemStats(spell_power=5), stats=ItemStats(intellect=32, spell_power=40))
MANA_ETCHED_CROWN = Gear(db_id=28193, name="Mana-Etched Crown", sockets=['m', 'r'], stats=ItemStats(intellect=20, spell_power=34))
MAGHARI_RITUALISTS_HORNS = Gear(db_id=28169, name="Mag'hari Ritualist's Horns",
                                stats=ItemStats(intellect=16, spell_power=50, spell_crit_rating=15, spell_hit_rating=12))
FROSTFIRE_CIRCLET = Gear(db_id=22498, name="Frostfire Circlet", stats=ItemStats(intellect=23, spell_power=35, spell_crit_rating=28, spell_hit_rating=8))

# Phase 2
COWL_OF_TIRISFAL = Gear(db_id=30206, name="Cowl of Tirisfal", sockets=['m', 'y'], bonus=ItemStats(spell_hit_rating=4), phase=2, stats=ItemStats(intellect=36,
                                                                                                                                                spell_power=55,
                                                                                                                                                spell_crit_rating=24))
MERCILESS_GLADIATORS_SILK_COWL = Gear(db_id=32048, name="Merciless Gladiator's Silk Cowl", sockets=['m', 'r'], phase=2,
                                      stats=ItemStats(intellect=26, spell_power=42, spell_crit_rating=20))

# Phase 3
COWL_OF_THE_ILLIDARI_HIGH_LORD = Gear(db_id=32525, name="Cowl of the Illidari High Lord", sockets=['m', 'b'], bonus=ItemStats(spell_power=5), phase=3,
                                      stats=ItemStats(intellect=31, spell_power=64, spell_crit_rating=47, spell_hit_rating=21))
COWL_OF_THE_TEMPEST = Gear(db_id=31056, name="Cowl of the Tempest", sockets=['m', 'y'], phase=3,
                           stats=ItemStats(intellect=40, spell_power=62, spell_crit_rating=29, spell_hit_rating=13))
DESTRUCTION_HOLO_GOGS = Gear(db_id=32494, name="Destruction Holo-gogs", sockets=['m', 'b'], bonus=ItemStats(spell_power=5), phase=3, stats=ItemStats(
    intellect=24, spell_power=64, spell_crit_rating=29))
VENGEFUL_GLADIATORS_SILK_COWL = Gear(db_id=33758, name="Vengeful Gladiator's Silk Cowl", sockets=['m', 'r'], phase=3,
                                     stats=ItemStats(intellect=23, spell_power=47, spell_crit_rating=24))

# Phase 4
HOOD_OF_HEXING = Gear(db_id=33453, name="Hood of Hexing", sockets=['r', 'y', 'b'], bonus=ItemStats(spell_power=5), phase=4, stats=ItemStats(intellect=33,
                                                                                                                                            spell_power=56,
                                                                                                                                            spell_crit_rating=24,
                                                                                                                                            spell_hit_rating=31))

# Phase 5
DARK_CONJURORS_COLLAR = Gear(db_id=34340, name="Dark Conjuror's Collar", sockets=['m', 'b'], bonus=ItemStats(spell_power=5), phase=5,
                             stats=ItemStats(intellect=42, spell_power=75, spell_crit_rating=38, spell_haste_rating=30))
ANNIHILATOR_HOLO_GOGS = Gear(db_id=34847, name="Annihilator Holo-Gogs", sockets=['m', 'b'], bonus=ItemStats(spell_power=5), phase=5,
                             stats=ItemStats(intellect=37, spell_power=81, spell_crit_rating=42))
HELM_OF_ARCANE_PURITY = Gear(db_id=34405, name="Helm of Arcane Purity", sockets=['m', 'r'], bonus=ItemStats(spell_power=5), phase=5,
                             stats=ItemStats(intellect=42, spell_power=75, spell_crit_rating=30))
BRUTAL_GLADIATORS_SILK_COWL = Gear(db_id=35097, name="Brutal Gladiator's Silk Cowl", sockets=['m', 'r'], phase=5,
                                   stats=ItemStats(intellect=29, spell_power=54, spell_crit_rating=30))
