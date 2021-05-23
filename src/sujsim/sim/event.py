from __future__ import annotations

import copy
from typing import TYPE_CHECKING

from sujsim.core.spells.magic_school import MagicSchool

if TYPE_CHECKING:
    from sujsim.sim.actor import Actor

import random
from sujsim.core.items.gear_database import trinket, ring
from sujsim.core.spells.buff_database import combat_buffs, debuffs
from sujsim.sim.sim_log import LogEntry, LogType
from sujsim.core.spells.buff import Buff
from sujsim.core.spells.cooldown import Cooldown
from sujsim.core.spells.dot import Dot
from sujsim.core.spells.spell import Spell, MageSpells, CastSpell, SpellResult


class Event:
    def __init__(self, time: float, source_actor: Actor, target_actor: Actor):
        self.time = time
        self.source_actor = source_actor
        self.target_actor = target_actor

    def execute(self):
        self.target_actor.current_time = self.time

    def add_log(self, log_type: LogType, text: str):
        log_entry = LogEntry(log_type=log_type,
                             text=text,
                             time=self.time)
        print(log_entry)
        self.target_actor.add_to_log(log_entry)


class WaitEvent(Event):
    def __init__(self, time: float, source_actor: Actor, target_actor: Actor):
        super().__init__(time=time, target_actor=target_actor, source_actor=source_actor)

    def execute(self):
        super().execute()
        self.target_actor.queue_next_action()
        super().add_log(log_type=LogType.LOG_WAIT, text='Waiting')


class MageCastEvent(Event):
    def __init__(self, time: float, spell: Spell, source_actor: Actor, target_actor: Actor, spell_target: Actor):
        super().__init__(time=time, target_actor=target_actor, source_actor=source_actor)
        self.spell = copy.deepcopy(spell)
        self.spell_target = spell_target

    def execute(self):
        super().execute()

        if self.spell.is_channeling:
            self.spell.current_ticks += 1
            self.spell.does_trigger_gcd = False

        if self.spell.spell_type == MageSpells.EVOCATION:
            self.source_actor.add_to_queue(ManaEvent(target_actor=self.target_actor,
                                                     source_actor=self.target_actor,
                                                     amount=self.target_actor.character.stats.max_mana * 0.15,
                                                     gain=True),
                                           execute_now=True)
            if self.spell.current_ticks == 1:
                self.source_actor.add_to_queue(GainBuffEvent(buff=debuffs.EVOCATION_COOLDOWN,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
            if self.spell.current_ticks < self.spell.max_ticks:
                self.source_actor.add_to_queue(MageCastEvent(spell=self.spell,
                                                             time=self.spell.cast_time / self.spell.max_ticks,
                                                             source_actor=self.source_actor,
                                                             target_actor=self.target_actor,
                                                             spell_target=self.spell_target))
        else:
            self.execute_spell_cast()

    def execute_spell_cast(self):
        cast_spell = self.source_actor.character.calculate_cast_spell(spell=self.spell, target=self.target_actor)
        # Spells only cost mana when they are cast, not when channeled spells tick
        if not self.spell.is_channeling or (self.spell.current_ticks == 1):
            self.source_actor.add_to_queue(ManaEvent(target_actor=self.target_actor,
                                                     source_actor=self.target_actor,
                                                     amount=cast_spell.mana_cost,
                                                     gain=False),
                                           execute_now=True)
        # Apply self-buffs from spell execution
        if self.spell.spell_type == MageSpells.ARCANE_BLAST:
            self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.ARCANE_BLAST,
                                                         target_actor=self.target_actor,
                                                         source_actor=self.target_actor),
                                           execute_now=True)
            # TODO
            """
            if config->tirisfal_4set and cast_spell.result == spell::CRIT)
                onBuffGain(make_shared<buff::ArcaneMadness>());
            """
        super().add_log(log_type=LogType.LOG_SPELL, text="{}'s {} is a {}".format(self.source_actor.character.name,
                                                                                  cast_spell.spell_type.value,
                                                                                  cast_spell.result.name))

        if cast_spell.result == SpellResult.MISS:
            if self.source_actor.character.gear_stats.has_trinket(trinket.EYE_OF_MAGTHERIDON):
                self.source_actor.add_to_queue(GainBuffEvent(buff=trinket.EYE_OF_MAGTHERIDON.buff,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
        else:
            self.spell_target.add_to_queue(HealthEvent(source_actor=self.source_actor,
                                                       target_actor=self.spell_target,
                                                       gain=False,
                                                       cast_spell=cast_spell,
                                                       time=self.time - self.spell_target.current_time))
            if cast_spell.dot is not None:
                dot = copy.deepcopy(cast_spell.dot)
                self.spell_target.add_to_queue(DotEvent(source_actor=self.source_actor,
                                                        target_actor=self.spell_target,
                                                        dot=dot,
                                                        time=(dot.tick_interval + self.time) - self.spell_target.current_time))
            # Do DoT checks
            # if spell has dot, add recurring health event to the boss, or add a cast event (can't be a cast event)
            # Combustion
            if cast_spell.magic_school == MagicSchool.FIRE and self.source_actor.has_buff(combat_buffs.COMBUSTION):
                if cast_spell.result == SpellResult.CRIT:
                    self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.COMBUSTION_CRITS,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)
                if self.source_actor.get_buff(combat_buffs.COMBUSTION_CRITS).stacks == combat_buffs.COMBUSTION_CRITS.max_stacks:
                    # TODO: Add Buff for Combustion Cooldown
                    self.source_actor.add_to_queue(LoseBuffEvent(buff=combat_buffs.COMBUSTION,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor,
                                                                 time=0),
                                                   execute_now=True)
                    self.source_actor.add_to_queue(LoseBuffEvent(buff=combat_buffs.COMBUSTION_CRITS,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor,
                                                                 time=0),
                                                   execute_now=True)
                else:
                    self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.COMBUSTION,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)
            if cast_spell.spell_type == MageSpells.SCORCH and self.source_actor.character.mage_talents.imp_scorch > 0:
                if self.source_actor.character.mage_talents.imp_scorch > 0 == 3 or random.randint(0, 2) < self.source_actor.character.mage_talents.imp_scorch:
                    self.spell_target.add_to_queue(GainBuffEvent(buff=debuffs.FIRE_VULNERABILITY,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)

                    if self.source_actor.character.gear_stats.has_trinket(trinket.DARKMOON_CARD_CRUSADE):
                        self.source_actor.add_to_queue(GainBuffEvent(buff=trinket.DARKMOON_CARD_CRUSADE.buff,
                                                                     target_actor=self.target_actor,
                                                                     source_actor=self.target_actor),
                                                       execute_now=True)
            if cast_spell.magic_school == MagicSchool.FROST and self.source_actor.character.mage_talents.winters_chill:
                if self.source_actor.character.mage_talents.winters_chill == 5 or random.randrange(0,
                                                                                                   4) < self.source_actor.character.mage_talents.winters_chill:
                    self.spell_target.add_to_queue(GainBuffEvent(buff=debuffs.WINTERS_CHILL,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)

            # 5% proc rate ?
            if self.source_actor.character.gear_stats.has_trinket(trinket.QUAGMIRRANS_EYE) and not self.source_actor.has_buff(
                    combat_buffs.QUAGMIRRANS_EYE) and random.randrange(0, 19) == 0:
                self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.QUAGMIRRANS_EYE,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
                self.source_actor.add_to_queue(GainBuffEvent(buff=debuffs.QUAGMIRRANS_EYE_COOLDOWN,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)

            # 15% proc rate
            if self.source_actor.character.gear_stats.has_trinket(trinket.MARK_OF_DEFIANCE) and not self.source_actor.has_buff(
                    debuffs.MARK_OF_DEFIANCE_COOLDOWN) and random.randrange(0, 99) < 15:
                self.source_actor.add_to_queue(GainBuffEvent(buff=debuffs.MARK_OF_DEFIANCE_COOLDOWN,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
                self.source_actor.add_to_queue(ManaEvent(target_actor=self.target_actor,
                                                         source_actor=self.target_actor,
                                                         amount=random.randrange(128, 173),
                                                         gain=True),
                                               execute_now=True)

            # 5% proc rate ?
            if self.source_actor.character.gear_stats.has_spellstrike() and random.randrange(0, 19) == 0:
                self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.SPELLSTRIKE,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
            # 10% proc rate
            if self.source_actor.character.gear_stats.has_ring(ring.BAND_OF_THE_ETERNAL_SAGE) and not self.source_actor.has_buff(combat_buffs.ETERNAL_SAGE) \
                    and random.randrange(0, 9) == 0:
                self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.ETERNAL_SAGE,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
                self.source_actor.add_to_queue(GainBuffEvent(buff=debuffs.ETERNAL_SAGE_COOLDOWN,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)

            # 5% proc rate, cannot refresh itself while up
            if self.source_actor.character.gear_stats.has_ring(ring.WRATH_OF_CENARIUS) and not self.source_actor.has_buff(
                    combat_buffs.SPELL_BLASTING) and random.randrange(0, 19) == 0:
                self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.SPELL_BLASTING,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
                self.source_actor.add_to_queue(GainBuffEvent(buff=debuffs.SPELL_BLASTING_COOLDOWN,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)

            # TODO
            """
            # 2% proc rate, mana-etched 4-set bonus
            if config->mana_etched_4set and random.randrange(0, 49) == 0:
                self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.SPELL_POWER_BONUS,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
            """

            # 50% proc rate
            if self.target_actor.has_buff(debuffs.JUDGEMENT_OF_WISDOM) and random.randrange(0, 1) == 1:
                self.source_actor.add_to_queue(ManaEvent(target_actor=self.target_actor,
                                                         source_actor=self.target_actor,
                                                         amount=74,
                                                         gain=True),
                                               execute_now=True)

            if self.source_actor.character.gear_stats.has_trinket(trinket.DARKMOON_CARD_CRUSADE):
                self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.DARKMOON_CRUSADE,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)

            if cast_spell.result == SpellResult.CRIT:
                # 20% proc rate
                if self.source_actor.character.gear_stats.has_trinket(trinket.SEXTANT_OF_UNSTABLE_CURRENTS) and not self.source_actor.has_buff(
                        combat_buffs.UNSTABLE_CURRENTS) and random.randrange(0, 4) == 0:
                    self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.UNSTABLE_CURRENTS,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)
                    self.source_actor.add_to_queue(GainBuffEvent(buff=debuffs.UNSTABLE_CURRENTS_COOLDOWN,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)
                # 20% proc rate
                if self.source_actor.character.gear_stats.has_trinket(trinket.SHIFFARS_NEXUS_HORN) and not self.source_actor.has_buff(
                        combat_buffs.CALL_OF_THE_NEXUS) and random.randrange(0, 4) == 0:
                    self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.CALL_OF_THE_NEXUS,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)
                    self.source_actor.add_to_queue(GainBuffEvent(buff=debuffs.CALL_OF_THE_NEXUS_COOLDOWN,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)
                # 100% proc rate
                if self.source_actor.character.gear_stats.has_trinket(trinket.THE_LIGHTNING_CAPACITOR) and not self.source_actor.has_buff(
                        combat_buffs.LIGHTNING_CAPACITOR):
                    self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.LIGHTNING_CAPACITOR,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)
                    # TODO: Add code to fireLightningCapacitor
                # 50% proc rate
                if self.source_actor.character.gear_stats.has_trinket(trinket.ASHTONGUE_TALISMAN_MAGE) and random.randrange(0, 1) == 0:
                    self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.ASHTONGUE_TALISMAN,
                                                                 target_actor=self.target_actor,
                                                                 source_actor=self.target_actor),
                                                   execute_now=True)

                if cast_spell.magic_school == MagicSchool.FIRE and self.source_actor.character.mage_talents.ignite:
                    # addIgnite(spell)
                    pass
                if cast_spell.magic_school == MagicSchool.FIRE or cast_spell.magic_school == MagicSchool.FROST and self.source_actor.character.mage_talents.master_of_elements:
                    self.source_actor.add_to_queue(ManaEvent(target_actor=self.target_actor,
                                                             source_actor=self.target_actor,
                                                             amount=round(cast_spell.mana_cost * 0.1 *
                                                                          self.source_actor.character.mage_talents.master_of_elements),
                                                             gain=True),
                                                   execute_now=True)

        # Check for buffs to remove and new procs
        self._execute_clearcasting()
        if cast_spell.mana_cost > 0:
            self._execute_presence_of_mind()
        self._execute_insightful_earthstorm_gem_proc()
        self._execute_blue_dragon_trinket_proc()

        if self.spell.is_channeling and self.spell.current_ticks < self.spell.max_ticks:
            self.source_actor.add_to_queue(MageCastEvent(spell=self.spell,
                                                         time=self.spell.cast_time / self.spell.max_ticks,
                                                         source_actor=self.source_actor,
                                                         target_actor=self.target_actor,
                                                         spell_target=self.spell_target))
        else:
            self.source_actor.queue_next_action()

    def _execute_clearcasting(self):
        if self.source_actor.has_buff(combat_buffs.CLEARCAST):
            self.source_actor.add_to_queue(LoseBuffEvent(buff=combat_buffs.CLEARCAST,
                                                         target_actor=self.target_actor,
                                                         source_actor=self.target_actor,
                                                         time=0),
                                           execute_now=True)
        if random.random() > 1 - (self.source_actor.character.mage_talents.arcane_concentration * 2) / 100:
            self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.CLEARCAST,
                                                         target_actor=self.target_actor,
                                                         source_actor=self.target_actor),
                                           execute_now=True)

    def _execute_presence_of_mind(self):
        if self.source_actor.has_buff(combat_buffs.PRESENCE_OF_MIND):
            LoseBuffEvent(buff=combat_buffs.PRESENCE_OF_MIND,
                          target_actor=self.target_actor,
                          source_actor=self.target_actor,
                          time=0)

    def _execute_pendant_violet_eye(self):
        if self.source_actor.has_buff(combat_buffs.PENDANT_VIOLET_EYE):
            self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.ENLIGHTENMENT,
                                                         target_actor=self.target_actor,
                                                         source_actor=self.target_actor),
                                           execute_now=True)

    def _execute_insightful_earthstorm_gem_proc(self):
        # 5% proc rate
        if self.source_actor.character.gear_stats.has_insightful_earthstorm_meta_gem() and random.random() > 0.8 and not self.source_actor.has_buff(
                combat_buffs.INSIGHTFUL_EARTHSTORM_COOLDOWN):
            self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.INSIGHTFUL_EARTHSTORM_COOLDOWN,
                                                         target_actor=self.target_actor,
                                                         source_actor=self.target_actor),
                                           execute_now=True)
            self.source_actor.add_to_queue(ManaEvent(source_actor=self.target_actor,
                                                     target_actor=self.target_actor,
                                                     amount=300,
                                                     gain=True))

    def _execute_blue_dragon_trinket_proc(self):
        # 2% proc rate
        if self.source_actor.character.gear_stats.has_trinket(trinket.DARKMOON_CARD_BLUE_DRAGON) and random.random() > 0.5:
            self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.BLUE_DRAGON,
                                                         target_actor=self.target_actor,
                                                         source_actor=self.target_actor),
                                           execute_now=True)


class DotEvent(Event):
    def __init__(self, time: int, source_actor: Actor, target_actor: Actor, dot: Dot):
        super().__init__(time=time, target_actor=target_actor, source_actor=source_actor)
        self.dot = dot

    def execute(self):
        super().execute()
        self.dot.current_tick += 1
        self.target_actor.add_to_queue(HealthEvent(source_actor=self.source_actor,
                                                   target_actor=self.target_actor,
                                                   gain=False,
                                                   cast_spell=CastSpell(spell_type=MageSpells.DOT,
                                                                        rank=1,
                                                                        result=SpellResult.HIT,
                                                                        damage=self.dot.damage,
                                                                        resist=0,
                                                                        mana_cost=0,
                                                                        magic_school=self.dot.magic_school),
                                                   time=0))
        if self.dot.current_tick <= self.dot.max_ticks:
            self.target_actor.add_to_queue(DotEvent(source_actor=self.source_actor,
                                                    target_actor=self.target_actor,
                                                    dot=self.dot,
                                                    time=self.dot.tick_interval))


class ManaEvent(Event):
    def __init__(self, source_actor: Actor, target_actor: Actor, amount: int, gain: bool):
        super().__init__(time=0, target_actor=target_actor, source_actor=source_actor)
        self.amount = round(amount)
        self.gain = gain

    def execute(self):
        super().execute()
        if self.gain:
            self.target_actor.character.stats.current_mana += self.amount
            super().add_log(log_type=LogType.LOG_MANA, text='{} Mana Gain'.format(self.amount))
        else:
            self.target_actor.character.stats.current_mana -= self.amount
            super().add_log(log_type=LogType.LOG_MANA, text='{} Mana Lost'.format(self.amount))


class HealthEvent(Event):
    def __init__(self, time, source_actor: Actor, target_actor: Actor, cast_spell: CastSpell, gain: bool):
        super().__init__(time=time, target_actor=target_actor, source_actor=source_actor)
        self.gain = gain
        self.cast_spell = cast_spell

    def execute(self):
        super().execute()
        if self.gain:
            self.target_actor.character.stats.current_health += self.cast_spell.damage
        else:
            self.target_actor.character.stats.current_health -= self.cast_spell.damage
        super().add_log(log_type=LogType.LOG_DAMAGE, text="{}'s {} {}s {} for {}".format(self.source_actor.character.name,
                                                                                         self.cast_spell.spell_type.value,
                                                                                         self.cast_spell.result.name,
                                                                                         self.target_actor.character.name,
                                                                                         self.cast_spell.damage))


class ManaRegenEvent(Event):
    def __init__(self, time: float, source_actor: Actor, target_actor: Actor):
        super().__init__(time=time, target_actor=target_actor, source_actor=source_actor)
        self.seconds_of_regen = time

    def execute(self):
        super().execute()

        mp_1 = self.target_actor.character.calculate_current_mana_regen_per_second()

        mana_to_add = mp_1 * self.seconds_of_regen
        self.target_actor.character.stats.current_mana += mana_to_add
        super().add_log(log_type=LogType.LOG_MANA, text='{} Mana Regen'.format(mana_to_add))

        self.target_actor.add_to_queue(ManaRegenEvent(2,
                                                      target_actor=self.target_actor,
                                                      source_actor=self.target_actor))


class GainBuffEvent(Event):
    def __init__(self, buff: Buff, source_actor: Actor, target_actor: Actor):
        super().__init__(time=0, target_actor=target_actor, source_actor=source_actor)
        self.buff = buff

    def execute(self):
        super().execute()

        self.target_actor.remove_lose_buff_event_from_queue(self)
        self.target_actor.add_to_queue(LoseBuffEvent(time=self.buff.duration,
                                                     target_actor=self.target_actor,
                                                     source_actor=self.target_actor,
                                                     buff=self.buff))  # Refresh the timer on the buff

        buff_added = self.target_actor.add_buff(self.buff)
        if buff_added.is_maxed:
            super().add_log(log_type=LogType.LOG_BUFF, text='{}[{}] refreshed'.format(buff_added.name, buff_added.stacks))
        else:
            super().add_log(log_type=LogType.LOG_BUFF, text='{}[{}] gained'.format(buff_added.name, buff_added.stacks))


class LoseBuffEvent(Event):
    def __init__(self, time: float, buff: Buff, source_actor: Actor, target_actor: Actor):
        super().__init__(time=time, target_actor=target_actor, source_actor=source_actor)
        self.buff = buff

    def execute(self):
        super().execute()
        self.target_actor.remove_buff(self.buff)
        if self.buff == combat_buffs.PENDANT_VIOLET_EYE:
            self.target_actor.add_to_queue(LoseBuffEvent(time=combat_buffs.ENLIGHTENMENT,
                                                         target_actor=self.target_actor,
                                                         source_actor=self.source_actor,
                                                         buff=self.buff))
        super().add_log(log_type=LogType.LOG_BUFF, text='{} lost'.format(self.buff.name))
