from typing import List

from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.stats.spell_stats import get_new_spell_stats_dict, merge_spell_stats_dict


class ItemStats:
    def __init__(self,
                 intellect: int = 0,
                 stamina: int = 0,
                 spirit: int = 0,
                 spell_power: int = 0,
                 spell_hit_rating: int = 0,
                 spell_crit_rating: int = 0,
                 spell_haste_rating: int = 0,
                 fire_resistance: int = 0,
                 frost_resistance: int = 0,
                 arcane_resistance: int = 0,
                 shadow_resistance: int = 0,
                 nature_resistance: int = 0,
                 magic_penetration: int = 0,
                 mp_5: int = 0,
                 impacted_schools: List[MagicSchool] = None):
        self.intellect = intellect
        self.stamina = stamina
        self.spirit = spirit
        self.fire_resistance = fire_resistance
        self.frost_resistance = frost_resistance
        self.arcane_resistance = arcane_resistance
        self.shadow_resistance = shadow_resistance
        self.nature_resistance = nature_resistance
        self.magic_penetration = magic_penetration
        self.mp_5 = mp_5
        self.impacted_schools = list(MagicSchool) if impacted_schools is None else impacted_schools
        self.spell_stats_dict = get_new_spell_stats_dict()
        for magic_school in self.impacted_schools:
            self.spell_stats_dict[magic_school].spell_power += spell_power
            self.spell_stats_dict[magic_school].spell_hit_rating += spell_hit_rating
            self.spell_stats_dict[magic_school].spell_crit_rating += spell_crit_rating
            self.spell_stats_dict[magic_school].spell_haste_rating += spell_haste_rating

    @property
    def intellect(self):
        return self._intellect

    @intellect.setter
    def intellect(self, value):
        self._intellect = round(value)

    @property
    def spirit(self):
        return self._spirit

    @spirit.setter
    def spirit(self, value):
        self._spirit = round(value)

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        self._stamina = round(value)


def merge_item_stats(stats_1: ItemStats, stats_2: ItemStats, modifier: int = 1):
    # Modified is used by buffs, it is the count of buff stacks
    stats_1.intellect += stats_2.intellect * modifier
    stats_1.stamina += stats_2.stamina * modifier
    stats_1.spirit += stats_2.spirit * modifier
    stats_1.fire_resistance += stats_2.fire_resistance * modifier
    stats_1.frost_resistance += stats_2.frost_resistance * modifier
    stats_1.arcane_resistance += stats_2.arcane_resistance * modifier
    stats_1.shadow_resistance += stats_2.shadow_resistance * modifier
    stats_1.nature_resistance += stats_2.nature_resistance * modifier
    stats_1.magic_penetration += stats_2.magic_penetration * modifier
    stats_1.mp_5 += stats_2.mp_5
    merge_spell_stats_dict(stats_1.spell_stats_dict, stats_2.spell_stats_dict, modifier=modifier)
