from typing import List


class MageTalents():
    def __init__(self, wowhead_calculator_string: str):
        # Arcane
        self.arcane_subtlety = 0
        self.arcane_focus = 0
        self.improved_arcane_missiles = 0
        self.wand_specialization = 0
        self.magic_absorption = 0
        self.arcane_concentration = 0
        self.magic_attunement = 0
        self.arcane_impact = 0
        self.arcane_fortitude = 0
        self.improved_mana_shield = 0
        self.improved_counterspell = 0
        self.arcane_meditation = 0
        self.improved_blink = 0
        self.presence_of_mind = 0
        self.arcane_mind = 0
        self.prismatic_cloak = 0
        self.arcane_instability = 0
        self.arcane_potency = 0
        self.empowered_arcane_missiles = 0
        self.arcane_power = 0
        self.spell_power = 0
        self.mind_mastery = 0
        self.slow = 0
        # Fire
        self.imp_fireball = 0
        self.ignite = 0
        self.incinerate = 0
        self.pyroblast = 0
        self.imp_scorch = 0
        self.master_of_elements = 0
        self.playing_with_fire = 0
        self.critical_mass = 0
        self.fire_power = 0
        self.pyromaniac = 0
        self.combustion = 0
        self.molten_fury = 0
        self.empowered_fireball = 0
        # Frost
        self.imp_frostbolt = 0
        self.elemental_precision = 0
        self.ice_shards = 0
        self.piercing_ice = 0
        self.icy_veins = 0
        self.frost_channeling = 0
        self.cold_snap = 0
        self.winters_chill = 0
        self.arctic_winds = 0
        self.empowered_frostbolt = 0

        talent_tree_ints = parse_wowhead_calculator_string(wowhead_calculator_string)
        arcane_talent_ints = talent_tree_ints[0]
        for i, arcane_talent_int in enumerate(arcane_talent_ints):
            if i == 0:
                self.arcane_subtlety = arcane_talent_int
            elif i == 1:
                self.arcane_focus = arcane_talent_int
            elif i == 2:
                self.improved_arcane_missiles = arcane_talent_int
            elif i == 3:
                self.wand_specialization = arcane_talent_int
            elif i == 4:
                self.magic_absorption = arcane_talent_int
            elif i == 5:
                self.arcane_concentration = arcane_talent_int
            elif i == 6:
                self.magic_attunement = arcane_talent_int
            elif i == 7:
                self.arcane_impact = arcane_talent_int
            elif i == 8:
                self.arcane_fortitude = arcane_talent_int
            elif i == 9:
                self.improved_mana_shield = arcane_talent_int
            elif i == 10:
                self.improved_counterspell = arcane_talent_int
            elif i == 11:
                self.arcane_meditation = arcane_talent_int
            elif i == 12:
                self.improved_blink = arcane_talent_int
            elif i == 13:
                self.presence_of_mind = arcane_talent_int
            elif i == 14:
                self.arcane_mind = arcane_talent_int
            elif i == 15:
                self.prismatic_cloak = arcane_talent_int
            elif i == 16:
                self.arcane_instability = arcane_talent_int
            elif i == 17:
                self.arcane_potency = arcane_talent_int
            elif i == 18:
                self.empowered_arcane_missiles = arcane_talent_int
            elif i == 19:
                self.arcane_power = arcane_talent_int
            elif i == 20:
                self.spell_power = arcane_talent_int
            elif i == 21:
                self.mind_mastery = arcane_talent_int
            elif i == 22:
                self.slow = arcane_talent_int

        fire_talent_ints = talent_tree_ints[1]
        for i, fire_talent_ints in enumerate(fire_talent_ints):
            if i == 0:
                self.imp_fireball = fire_talent_ints
            elif i == 2:
                self.ignite = fire_talent_ints
            elif i == 5:
                self.incinerate = fire_talent_ints
            elif i == 7:
                self.pyroblast = fire_talent_ints
            elif i == 9:
                self.imp_scorch = fire_talent_ints
            elif i == 11:
                self.master_of_elements = fire_talent_ints
            elif i == 12:
                self.playing_with_fire = fire_talent_ints
            elif i == 13:
                self.critical_mass = fire_talent_ints
            elif i == 16:
                self.fire_power = fire_talent_ints
            elif i == 17:
                self.pyromaniac = fire_talent_ints
            elif i == 18:
                self.combustion = fire_talent_ints
            elif i == 19:
                self.molten_fury = fire_talent_ints
            elif i == 20:
                self.empowered_fireball = fire_talent_ints

        frost_talent_ints = talent_tree_ints[2]
        for i, frost_talent_ints in enumerate(frost_talent_ints):
            if i == 1:
                self.imp_frostbolt = 0
            elif i == 2:
                self.elemental_precision = 0
            elif i == 3:
                self.ice_shards = 0
            elif i == 7:
                self.piercing_ice = 0
            elif i == 8:
                self.icy_veins = 0
            elif i == 11:
                self.frost_channeling = 0
            elif i == 14:
                self.cold_snap = 0
            elif i == 17:
                self.winters_chill = 0
            elif i == 19:
                self.arctic_winds = 0
            elif i == 20:
                self.empowered_frostbolt = 0


def parse_wowhead_calculator_string(wowhead_calculator_string: str) -> List[List[int]]:
    talent_tree_strings = wowhead_calculator_string.split('-')
    talent_tree_ints = []
    for talent_tree_string in talent_tree_strings:
        talent_ints = []
        for number in talent_tree_string:
            talent_ints.append(int(number))
        talent_tree_ints.append(talent_ints)
    return talent_tree_ints
