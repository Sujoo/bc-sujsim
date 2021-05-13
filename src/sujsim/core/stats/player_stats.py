import math
from typing import List

from sujsim.core.spells.buff import Buff
from sujsim.core.spells.buff_database.player_buffs import BLESSING_OF_KINGS, IMPROVED_DIVINE_SPIRIT
from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.stats.gear_stats import GearStats
from sujsim.core.character.race import Race
from sujsim.core.stats.item_stats import ItemStats, merge_item_stats
from sujsim.core.stats.spell_stats import get_new_spell_stats_dict, merge_spell_stats_dict, SpellStats
from sujsim.core.talents.mage_talents import MageTalents


class PlayerStats:
    def __init__(self,
                 intellect: int = 0,
                 stamina: int = 0,
                 spirit: int = 0,
                 fire_resistance: int = 0,
                 frost_resistance: int = 0,
                 arcane_resistance: int = 0,
                 shadow_resistance: int = 0,
                 nature_resistance: int = 0,
                 magic_penetration: int = 0,
                 mp_5: int = 0,
                 base_health: int = 0,
                 max_health: int = 0,
                 current_health: int = 0,
                 base_mana: int = 0,
                 max_mana: int = 0,
                 current_mana: int = 0):
        self.intellect = intellect
        self.stamina = stamina
        self.spirit = spirit
        self.mp_5 = mp_5

        self.base_health = base_health
        self.max_health = max_health
        self.current_health = current_health
        self.base_mana = base_mana
        self.max_mana = max_mana
        self.current_mana = current_mana

        self.spell_stats_dict = get_new_spell_stats_dict()

        self.fire_resistance = fire_resistance
        self.frost_resistance = frost_resistance
        self.arcane_resistance = arcane_resistance
        self.shadow_resistance = shadow_resistance
        self.nature_resistance = nature_resistance
        self.magic_penetration = magic_penetration

    def finalize(self, race: Race, mage_talents: MageTalents, gear_stats: GearStats, buffs: List[Buff]):
        merge_item_stats(self, gear_stats.stats)
        self.merge_mage_talents(mage_talents)
        for buff in buffs:
            merge_item_stats(self, buff.stats, modifier=buff.stacks)

        # Finalize Attribute Multipliers
        self.intellect *= 1.0 + mage_talents.arcane_mind * 0.03
        if race == Race.GNOME:
            self.intellect *= 1.05
        if race == Race.HUMAN:
            self.spirit *= 1.1
        if BLESSING_OF_KINGS in buffs:
            self.intellect *= 1.1
            self.spirit *= 1.1
            self.stamina *= 1.1
        if gear_stats.has_ember_skyfire_meta_gem():
            self.intellect *= 1.02

        for spell_stats in self.spell_stats_dict.values():
            spell_stats.set_int_crit_rating(self.intellect)
            if mage_talents.mind_mastery > 0:
                spell_stats.spell_power += self.intellect * (mage_talents.mind_mastery * 0.05)
            if gear_stats.has_spellfire_set():
                spell_stats.spell_power += self.intellect * 0.07
            if IMPROVED_DIVINE_SPIRIT in buffs:
                spell_stats.spell_power += self.spirit * 0.1
            if race == Race.DRAENEI:
                spell_stats.spell_hit_rating += SpellStats.ONE_HIT

        self.max_mana = self.base_mana + (self.intellect * 15)
        self.current_mana = self.max_mana
        self.max_health = self.base_health + (self.stamina * 10)
        self.current_health = self.max_health

        for spell_stats in self.spell_stats_dict.values():
            spell_stats.calculate_chances()

    def get_mp_1(self):
        return self.mp_5 / 5

    def get_mp_spirit(self):
        return 0.001 + self.spirit * 0.009327 * math.sqrt(self.intellect)

    def merge_mage_talents(self, mage_talents: MageTalents):
        for spell_stats in self.spell_stats_dict.values():
            spell_stats.spell_crit_rating += mage_talents.arcane_instability * SpellStats.ONE_CRIT
            if spell_stats.magic_school == MagicSchool.ARCANE:
                spell_stats.spell_hit_rating += (mage_talents.arcane_focus * 2) * SpellStats.ONE_HIT
            if spell_stats.magic_school == MagicSchool.FIRE or spell_stats.magic_school == MagicSchool.FROST:
                """
                // This is supposedly bugged for binary spells to give 2% hit each point
                // They say it was actually that way in TBC so we'll keep it like this for now
                if (spell->school == SCHOOL_FIRE || spell->school == SCHOOL_FROST) {
                    if (spell->binary && player->talents.elemental_precision)
                        hit+= player->talents.elemental_precision*2.0;
                    else if (player->talents.elemental_precision)
                        hit+= player->talents.elemental_precision;
                """
                spell_stats.spell_hit_rating += mage_talents.elemental_precision * SpellStats.ONE_HIT

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

    @property
    def mp_5(self):
        return self._mp5

    @mp_5.setter
    def mp_5(self, value):
        self._mp5 = round(value)

    @property
    def current_mana(self):
        return self._current_mana

    @current_mana.setter
    def current_mana(self, value):
        self._current_mana = round(min(value, self.max_mana))
