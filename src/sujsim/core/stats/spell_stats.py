from typing import Dict

from sujsim.core.spells.magic_school import MagicSchool


class SpellStats:
    ONE_HIT = 12.62
    ONE_CRIT = 22.08
    ONE_INT_CRIT = 68.51
    ONE_HASTE = 15.77

    def __init__(self, magic_school):
        self.magic_school = magic_school
        self.spell_power = 0
        self.spell_hit_rating = 0
        self.spell_crit_rating = 0
        self.spell_haste_rating = 0

        self.spell_hit_chance = 0.0
        self.spell_crit_chance = 0.0
        self.spell_haste = 0.0

    def set_int_crit_rating(self, intellect: int):
        self.spell_crit_rating += (intellect / self.ONE_INT_CRIT) * self.ONE_CRIT

    def calculate_chances(self):
        self.spell_hit_chance = min(83.0 + (self.spell_hit_rating / self.ONE_HIT), 99.0) / 100
        self.spell_crit_chance = (self.spell_crit_rating / self.ONE_CRIT) / 100
        self.spell_haste = 1 + (self.spell_haste_rating / self.ONE_HASTE) / 100

    @property
    def spell_hit_rating(self):
        return self._spell_hit_rating

    @spell_hit_rating.setter
    def spell_hit_rating(self, value):
        self._spell_hit_rating = round(value)

    @property
    def spell_crit_rating(self):
        return self._spell_crit_rating

    @spell_crit_rating.setter
    def spell_crit_rating(self, value):
        self._spell_crit_rating = round(value)

    @property
    def spell_haste_rating(self):
        return self._spell_haste_rating

    @spell_haste_rating.setter
    def spell_haste_rating(self, value):
        self._spell_haste_rating = round(value)

    @property
    def spell_hit_chance(self):
        return self._spell_hit_chance

    @spell_hit_chance.setter
    def spell_hit_chance(self, value):
        self._spell_hit_chance = round(value, 2)

    @property
    def spell_crit_chance(self):
        return self._spell_crit_chance

    @spell_crit_chance.setter
    def spell_crit_chance(self, value):
        self._spell_crit_chance = round(value, 2)

    @property
    def spell_haste(self):
        return self._spell_haste

    @spell_haste.setter
    def spell_haste(self, value):
        self._spell_haste = round(value, 2)


def get_new_spell_stats_dict() -> Dict[MagicSchool, SpellStats]:
    return {MagicSchool.FROST: SpellStats(MagicSchool.FROST),
            MagicSchool.FIRE: SpellStats(MagicSchool.FIRE),
            MagicSchool.ARCANE: SpellStats(MagicSchool.ARCANE),
            MagicSchool.SHADOW: SpellStats(MagicSchool.SHADOW),
            MagicSchool.HOLY: SpellStats(MagicSchool.HOLY),
            MagicSchool.NATURE: SpellStats(MagicSchool.NATURE)}


def merge_spell_stats_dict(spell_stats_dict_1: Dict[MagicSchool, SpellStats],
                           spell_stats_dict_2: Dict[MagicSchool, SpellStats],
                           modifier: int = 1):
    # Modified is used by buffs, it is the count of buff stacks
    for magic_shool, spell_stats_1 in spell_stats_dict_1.items():
        spell_stats_2 = spell_stats_dict_2[magic_shool]
        spell_stats_1.spell_power += spell_stats_2.spell_power * modifier
        spell_stats_1.spell_hit_rating += spell_stats_2.spell_hit_rating * modifier
        spell_stats_1.spell_crit_rating += spell_stats_2.spell_crit_rating * modifier
        spell_stats_1.spell_haste_rating += spell_stats_2.spell_haste_rating * modifier
