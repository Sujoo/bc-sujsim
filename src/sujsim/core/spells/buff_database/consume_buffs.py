from sujsim.core.spells.buff import Buff
from sujsim.core.stats.item_stats import ItemStats
from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.stats.spell_stats import SpellStats

ELIXIR_DRAENIC_WISDOM = Buff(db_id=-1, name='', stats=ItemStats(intellect=30, spirit=30))
FLASK_DISTILLED_WISDOM = Buff(db_id=-1, name='', stats=ItemStats(intellect=65))
FOOD_SPELL_POWER = Buff(db_id=-1, name='', stats=ItemStats(spirit=20, spell_power=23))
FOOD_SPELL_CRIT = Buff(db_id=-1, name='', stats=ItemStats(spirit=20, spell_crit_rating=20))
ELIXIR_MAJOR_MAGEBLOOD = Buff(db_id=-1, name='', stats=ItemStats(mp_5=16))
OIL_SUPERIOR_MANA = Buff(db_id=-1, name='', stats=ItemStats(mp_5=14))
OIL_BRILLIANT_WIZARD = Buff(db_id=-1, name='', stats=ItemStats(spell_power=36, spell_crit_rating=14))
OIL_SUPERIOR_WIZARD = Buff(db_id=-1, name='', stats=ItemStats(spell_power=42))
OIL_BLESSED_WIZARD = Buff(db_id=-1, name='', stats=ItemStats(spell_power=60))
FLASK_SUPREME_POWER = Buff(db_id=-1, name='', stats=ItemStats(spell_power=70))
FLASK_BLINDING_LIGHT = Buff(db_id=-1, name='', stats=ItemStats(spell_power=80, impacted_schools=[MagicSchool.ARCANE, MagicSchool.HOLY, MagicSchool.NATURE]))
FLASK_PURE_DEATH = Buff(db_id=-1, name='', stats=ItemStats(spell_power=80, impacted_schools=[MagicSchool.FIRE, MagicSchool.FROST, MagicSchool.SHADOW]))
ELIXIR_ADEPTS = Buff(db_id=-1, name='', stats=ItemStats(spell_power=24, spell_crit_rating=24))
ELIXIR_GREATER_ARCANE = Buff(db_id=-1, name='', stats=ItemStats(spell_power=35))
ELIXIR_MAJOR_FIREPOWER = Buff(db_id=-1, name='', stats=ItemStats(spell_power=55, impacted_schools=[MagicSchool.FIRE]))

DESTRUCTION_POTION = Buff(db_id=28508, name='Destruction', duration=15, stats=ItemStats(spell_power=120, spell_crit_rating=SpellStats.ONE_CRIT * 2))
