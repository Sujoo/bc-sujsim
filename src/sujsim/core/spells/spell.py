from enum import Enum, auto

from sujsim.core.spells.dot import Dot
from sujsim.core.spells.magic_school import MagicSchool


class MageSpells(Enum):
    GCD = 'GCD Spell'
    ARCANE_BLAST = 'Arcane Blast'
    FIREBALL = 'Fireball'
    FROSTBOLT = 'Frostbolt'
    SCORCH = 'Scorch'
    PYROBLAST = 'Pyroblast'
    FIRE_BLAST = 'Fire Blast'
    FAKE = 'Fake'
    ARCANE_MISSILES = 'Arcane Missiles'


class Spell:
    def __init__(self,
                 spell_type: MageSpells,
                 rank: int,
                 min_damage: int,
                 max_damage: int,
                 cast_time: float,
                 coefficient: float,
                 mana_cost: int,
                 magic_school: MagicSchool,
                 ticks: int = 0,
                 dot: Dot = None,
                 is_aoe: bool = False,
                 is_channeling: bool = False,
                 does_trigger_gcd: bool = True,
                 is_binary: bool = False,
                 should_ignore_clearcast: bool = False):
        self.spell_type = spell_type
        self.rank = rank
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.variance = self.max_damage - self.min_damage
        self.cast_time = float(cast_time)
        self.coefficient = float(coefficient)
        self.mana_cost = mana_cost
        self.magic_school = magic_school
        self.ticks = ticks
        self.dot = dot
        self.is_aoe = is_aoe
        self.is_channeling = is_channeling
        self.does_trigger_gcd = does_trigger_gcd
        self.is_binary = is_binary
        self.should_ignore_clearcast = should_ignore_clearcast


class SpellResult(Enum):
    MISS = auto()
    HIT = auto()
    CRIT = auto()


class CastSpell:
    def __init__(self,
                 spell_type: MageSpells,
                 rank: int,
                 result: SpellResult,
                 damage: float,
                 resist: float,
                 mana_cost: int,
                 magic_school: MagicSchool,
                 ticks: int = 0,
                 dot: Dot = None,
                 is_aoe: bool = False,
                 is_channeling: bool = False,
                 does_trigger_gcd: bool = False,
                 is_binary: bool = False,
                 should_ignore_clearcast: bool = False):
        self.spell_type = spell_type
        self.rank = rank
        self.result = result
        self.damage = damage
        self.resist = resist
        self.mana_cost = mana_cost
        self.magic_school = magic_school
        self.ticks = ticks
        self.dot = dot
        self.is_aoe = is_aoe
        self.is_channeling = is_channeling
        self.does_trigger_gcd = does_trigger_gcd
        self.is_binary = is_binary
        self.should_ignore_clearcast = should_ignore_clearcast
