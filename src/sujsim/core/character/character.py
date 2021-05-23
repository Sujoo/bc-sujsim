from __future__ import annotations
import copy
import random
from typing import List

from sujsim.core.spells.buff import Buff
from sujsim.core.spells.buff_database import combat_buffs, debuffs, player_buffs
from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.spells.spell import Spell, MageSpells, CastSpell, SpellResult
from sujsim.core.stats.gear_stats import GearStats
from sujsim.core.stats.player_stats import PlayerStats
from sujsim.core.character.race import Race
from sujsim.core.talents.mage_talents import MageTalents

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sujsim.sim.actor import Actor


class Character(object):
    def __init__(self, name: str, race: Race, gear_stats: GearStats, mage_talents: MageTalents, buffs: List[Buff]):
        self.name = name
        self.race = race
        self.gear_stats = gear_stats
        self.mage_talents = mage_talents
        self.buffs = []
        for buff in buffs:
            self.add_buff(buff)
        self.stats = self._init_player_stats()
        self.stats.finalize(race=self.race,
                            mage_talents=self.mage_talents,
                            gear_stats=self.gear_stats,
                            buffs=self.buffs)

    def _init_player_stats(self) -> PlayerStats:
        stats = PlayerStats()
        stats.stamina = 0  # idk what stamina is per race
        stats.base_health = 1650  # Undead defaults until I figure out the other races
        stats.base_mana = 1961  # Other code claims this is true for all races
        if self.race == Race.UNDEAD:
            stats.intellect = 149
            stats.spirit = 150
            stats.shadow_resistance += 10
        elif self.race == Race.TROLL:
            stats.intellect = 147
            stats.spirit = 146
        elif self.race == Race.BLOOD_ELF:
            stats.intellect = 155
            stats.spirit = 144
        elif self.race == Race.HUMAN:
            stats.intellect = 151
            stats.spirit = 145
        elif self.race == Race.GNOME:
            stats.intellect = 155
            stats.spirit = 145
        elif self.race == Race.DRAENEI:
            stats.intellect = 152
            stats.spirit = 147
        return stats

    def reset(self):
        self.stats = self._init_player_stats()
        self.stats.finalize(race=self.race,
                            mage_talents=self.mage_talents,
                            gear_stats=self.gear_stats,
                            buffs=self.buffs)

    def add_buff(self, buff: Buff) -> Buff:
        buff_to_add = None
        if self.has_buff(buff):
            buff_to_add = self.get_buff(buff)
            buff_to_add.add_stack()
        else:
            buff_to_add = copy.deepcopy(buff)
            self.buffs.append(buff_to_add)

        self.reset_stats_if_necessary(buff_to_add)

        return buff_to_add

    def remove_buff(self, buff: Buff):
        buff_to_remove = self.get_buff(buff)
        if buff_to_remove:
            self.buffs.remove(buff_to_remove)

        self.reset_stats_if_necessary(buff_to_remove)

    def reset_stats_if_necessary(self, buff: Buff):
        if buff.stats is not None:
            self.reset()

    def has_buff(self, buff: Buff) -> bool:
        if self.get_buff(buff):
            return True
        else:
            return False

    def get_buff(self, buff: Buff) -> Buff:
        for search_buff in self.buffs:
            if search_buff.db_id == buff.db_id and search_buff.name == buff.name:
                return search_buff
        return None

    def calculate_cast_time(self, spell: Spell) -> float:
        if self.has_buff(combat_buffs.PRESENCE_OF_MIND):
            return 0.0

        cast_time = spell.cast_time
        if spell.spell_type == MageSpells.ARCANE_BLAST and self.has_buff(combat_buffs.ARCANE_BLAST):
            cast_time -= self.get_buff(combat_buffs.ARCANE_BLAST).stacks / 3.0
        elif spell.spell_type == MageSpells.FROSTBOLT:
            cast_time -= self.mage_talents.imp_frostbolt * 0.1
        elif spell.spell_type == MageSpells.FIREBALL:
            cast_time -= self.mage_talents.imp_fireball * 0.1

        cast_time = round(cast_time * self.calculate_spell_haste(spell.magic_school), 2)

        """
        # As of 5/23/21 GCD can be less than 1 sec, so not using this code anymore
        if spell.spell_type == MageSpells.GCD:
            cast_time = max(1, cast_time)
        """

        return cast_time

    def calculate_spell_haste(self, magic_school: MagicSchool) -> float:
        spell_haste = self.stats.spell_stats_dict[magic_school].spell_haste

        if self.has_buff(combat_buffs.BLOODLUST):
            spell_haste *= 1.3
        if self.has_buff(combat_buffs.POWER_INFUSION):
            spell_haste *= 1.2
        if self.has_buff(combat_buffs.ICY_VEINS):
            spell_haste *= 1.2
        if self.has_buff(combat_buffs.BERSERKING):
            spell_haste *= 1.1
        return 1.0 / spell_haste

    def calculate_current_mana_regen_per_second(self) -> int:
        mp_1 = self.stats.get_mp_1()
        mp_spirit = self.stats.get_mp_spirit()

        mp_spirit_while_casting_regen_percent = 0
        if not self.has_buff(debuffs.CASTING_5_SECOND_RULE) or self.has_buff(combat_buffs.BLUE_DRAGON):
            mp_spirit_while_casting_regen_percent = 1.0
        elif self.has_buff(combat_buffs.INNERVATE):
            mp_spirit_while_casting_regen_percent = 1.0
            mp_spirit *= 5  # Increase regen by 400%
        else:
            mp_spirit_while_casting_regen_percent += self.mage_talents.arcane_meditation * 0.1
            if self.has_buff(player_buffs.MAGE_ARMOR):
                mp_spirit_while_casting_regen_percent += 0.3

        mp_1 += mp_spirit_while_casting_regen_percent * mp_spirit
        return round(mp_1)

    def calculate_cast_spell(self, spell: Spell, target: Actor) -> CastSpell:
        result = self.calculate_spell_result(spell, target)
        if result != SpellResult.MISS:
            damage = self.calculate_spell_damage(spell, target)

            if result == SpellResult.CRIT:
                damage *= self.calculate_crit_multipler(spell)

            resist = self.calculate_spell_resist(spell, damage)
            damage -= resist

            resist = round(resist)
            damage = round(damage)
        else:
            damage = 0
            resist = 0
        mana_cost = self.calculate_spell_cost(spell)
        return CastSpell(result=result,
                         damage=damage,
                         resist=resist,
                         mana_cost=mana_cost,
                         spell_type=spell.spell_type,
                         rank=spell.rank,
                         magic_school=spell.magic_school,
                         max_ticks=spell.max_ticks,
                         dot=spell.dot,
                         is_aoe=spell.is_aoe,
                         is_channeling=spell.is_channeling,
                         does_trigger_gcd=spell.does_trigger_gcd,
                         is_binary=spell.is_binary,
                         should_ignore_clearcast=spell.should_ignore_clearcast)

    def calculate_spell_result(self, spell: Spell, target: Actor) -> SpellResult:
        spell_stats = self.stats.spell_stats_dict[spell.magic_school]
        result = SpellResult.HIT
        if random.random() > spell_stats.spell_hit_chance:
            result = SpellResult.MISS
        elif random.random() <= self.calculate_spell_crit_chance(spell_stats.spell_crit_chance, spell, target):
            result = SpellResult.CRIT

        return result

    def calculate_spell_crit_chance(self, base_crit_chance: float, spell: Spell, target: Actor) -> float:
        final_crit_chance = base_crit_chance
        if spell.spell_type == MageSpells.ARCANE_BLAST:
            final_crit_chance += self.mage_talents.arcane_impact * 2
        if spell.spell_type == MageSpells.SCORCH:
            final_crit_chance += self.mage_talents.incinerate * 2
        if spell.spell_type == MageSpells.SCORCH:
            final_crit_chance += self.mage_talents.empowered_frostbolt

        if self.has_buff(combat_buffs.CLEARCAST):
            final_crit_chance += self.mage_talents.arcane_potency * 10
        if self.has_buff(combat_buffs.COMBUSTION) and spell.magic_school == MagicSchool.FIRE:
            final_crit_chance += self.get_buff(combat_buffs.COMBUSTION).stacks * 10

        if spell.magic_school == MagicSchool.FIRE:
            final_crit_chance += self.mage_talents.critical_mass * 2
            final_crit_chance += self.mage_talents.pyromaniac
        if spell.magic_school == MagicSchool.FROST and target.has_buff(debuffs.WINTERS_CHILL):
            final_crit_chance += target.get_buff(debuffs.WINTERS_CHILL).stacks * 2

        return final_crit_chance

    def calculate_spell_damage(self, spell: Spell, target: Actor) -> float:
        spell_stats = self.stats.spell_stats_dict[spell.magic_school]
        damage = random.randint(spell.min_damage, spell.max_damage)

        spell_power = spell_stats.spell_power
        spell_coefficient = spell.coefficient
        if spell.spell_type == MageSpells.ARCANE_MISSILES and self.mage_talents.empowered_arcane_missiles:
            spell_coefficient += self.mage_talents.empowered_arcane_missiles * 0.15
        if spell.spell_type == MageSpells.FIREBALL and self.mage_talents.empowered_fireball:
            spell_coefficient += self.mage_talents.empowered_fireball * 0.03
        if spell.spell_type == MageSpells.FROSTBOLT and self.mage_talents.empowered_frostbolt:
            spell_coefficient += self.mage_talents.empowered_frostbolt * 0.02

        if spell.is_channeling:
            spell_coefficient /= spell.max_ticks

        damage += spell_power * spell_coefficient

        return damage * self.calculate_damage_multiplier(spell, target)

    def calculate_damage_multiplier(self, spell: Spell, target: Actor) -> float:
        multiplier = 1.0

        if target.has_buff(debuffs.MISERY):
            multiplier *= 1.05
        if target.has_buff(debuffs.CURSE_OF_ELEMENTS) and (spell.magic_school == MagicSchool.FROST or spell.magic_school == MagicSchool.FIRE or
                                                           spell.magic_school == MagicSchool.ARCANE or spell.magic_school == MagicSchool.SHADOW):
            multiplier *= 1.1
        multiplier = 1 + self.mage_talents.playing_with_fire * 0.01
        if spell.magic_school == MagicSchool.FROST:
            multiplier *= 1 + self.mage_talents.piercing_ice * 0.02
            multiplier *= 1 + self.mage_talents.arctic_winds * 0.01
        if spell.magic_school == MagicSchool.FIRE:
            multiplier *= 1 + self.mage_talents.fire_power * 0.02
            if target.has_buff(debuffs.FIRE_VULNERABILITY):
                multiplier *= 1 + target.get_buff(debuffs.FIRE_VULNERABILITY).stacks * 0.03
        if target.character.stats.current_health < (target.character.stats.max_health * 0.2):
            multiplier *= 1 + self.mage_talents.molten_fury * 0.1

        if self.has_buff(combat_buffs.ARCANE_POWER):
            multiplier *= 1.3
        if spell.spell_type == MageSpells.ARCANE_BLAST and False:  # TODO: and config->tirisfal_2set
            multiplier *= 1.2

        if (spell.spell_type == MageSpells.ARCANE_MISSILES or spell.spell_type == MageSpells.FROSTBOLT or spell.spell_type == MageSpells.FIREBALL) and False:
            # and config->tempest_4set
            multiplier *= 1.05

        return multiplier

    def calculate_crit_multipler(self, spell: Spell) -> float:
        base = 1.5
        talents = 1.0

        if self.gear_stats.has_chaotic_skyfire_meta_gem():
            base *= 1.03

        talents += self.mage_talents.spell_power * 0.25

        if spell.magic_school == MagicSchool.FROST:
            talents += self.mage_talents.ice_shards * 0.2

        return (base - 1) * talents + 1

    def calculate_spell_resist(self, spell: Spell, damage: float) -> float:
        if spell.is_binary:
            return 0.0
        # No confirmed formulas or resistance tables can be found
        # This resistance table is based on data from Karazhan in TBC Beta uploaded to WCL
        # It results in about 6% mitigation
        resist = [83, 11, 5, 1]
        roll = random.randint(0, 99)

        resistance_multipler = 0.0
        for i, value in enumerate(resist):
            if roll < resist[i]:
                resistance_multipler = i * 0.25
                break
            roll -= resist[i]
        return damage * resistance_multipler

    def calculate_spell_cost(self, spell: Spell) -> int:
        if self.has_buff(combat_buffs.CLEARCAST) and not spell.should_ignore_clearcast:
            return 0

        spell_cost_multiplier = 1
        if spell.spell_type == MageSpells.ARCANE_BLAST and self.has_buff(combat_buffs.ARCANE_BLAST):
            spell_cost_multiplier += 0.75 * self.get_buff(combat_buffs.ARCANE_BLAST).stacks
            """
            TODO:
            if (config->tirisfal_2set):
                spell_cost_multiplier += 0.2
            """

        if spell.magic_school == MagicSchool.FROST and self.mage_talents.frost_channeling:
            spell_cost_multiplier -= self.mage_talents.frost_channeling * 0.05

        if spell.magic_school == MagicSchool.FIRE and self.mage_talents.pyromaniac:
            spell_cost_multiplier -= self.mage_talents.pyromaniac * 0.01

        if spell.spell_type == MageSpells.ARCANE_MISSILES and self.mage_talents.empowered_arcane_missiles:
            spell_cost_multiplier += self.mage_talents.empowered_arcane_missiles * 0.02

        if self.has_buff(combat_buffs.POWER_INFUSION):
            spell_cost_multiplier -= 0.2

        if self.has_buff(combat_buffs.ARCANE_POWER):
            spell_cost_multiplier += 0.3

        return round(spell.mana_cost * spell_cost_multiplier)
