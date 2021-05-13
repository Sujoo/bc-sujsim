from __future__ import annotations
from typing import TYPE_CHECKING

from sujsim.core.spells.magic_school import MagicSchool

if TYPE_CHECKING:
    from sujsim.sim.actor import Actor

import random
from sujsim.core.items.gear_database import trinket
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
        self.spell = spell
        self.spell_target = spell_target

    def execute(self):
        super().execute()

        # TODO: make channeling spells work
        cast_spell = self.source_actor.character.calculate_cast_spell(spell=self.spell, target=self.target_actor)
        # Apply self-buffs from spell execution
        if self.spell.spell_type == MageSpells.ARCANE_BLAST:
            self.source_actor.add_to_queue(GainBuffEvent(buff=combat_buffs.ARCANE_BLAST,
                                                         target_actor=self.target_actor,
                                                         source_actor=self.target_actor),
                                           execute_now=True)
            """
            if (config->tirisfal_4set && spell->result == spell::CRIT)
                onBuffGain(make_shared<buff::ArcaneMadness>());
            """
        super().add_log(log_type=LogType.LOG_SPELL, text="{}'s {} is a {}".format(self.source_actor.character.name,
                                                                                  cast_spell.spell_type.value,
                                                                                  cast_spell.result))
        self.source_actor.add_to_queue(ManaEvent(target_actor=self.target_actor,
                                                 source_actor=self.target_actor,
                                                 amount=cast_spell.mana_cost,
                                                 gain=False),
                                       execute_now=True)
        if cast_spell.result == SpellResult.MISS:
            if self.source_actor.character.gear_stats.has_trinket(trinket.EYE_OF_MAGTHERIDON):
                self.source_actor.add_to_queue(GainBuffEvent(buff=trinket.EYE_OF_MAGTHERIDON.buff,
                                                             target_actor=self.target_actor,
                                                             source_actor=self.target_actor),
                                               execute_now=True)
        else:
            self.spell_target.add_to_queue(HealthEvent(source_actor=self.source_actor, target_actor=self.spell_target, gain=False, cast_spell=cast_spell),
                                           execute_now=True)
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
            """
            if (spell->school == SCHOOL_FROST && player->talents.winters_chill) {
                if (player->talents.winters_chill == 5 || random<int>(0, 4) < player->talents.winters_chill)
                    onDebuffGain(make_shared<debuff::WintersChill>());
            }

            if (spell->id == spell::FIREBALL)
                pushDot(make_shared<dot::Fireball>());
            if (spell->id == spell::PYROBLAST)
                pushDot(make_shared<dot::Pyroblast>());

            // 5% proc rate ?
            if (hasTrinket(TRINKET_QUAGMIRRANS_EYE) && !state->hasCooldown(cooldown::QUAGMIRRANS_EYE) && random<int>(0, 19) == 0) {
                onCooldownGain(make_shared<cooldown::QuagmirransEye>());
                onBuffGain(make_shared<buff::QuagmirransEye>());
            }
            // 15% proc rate
            if (hasTrinket(TRINKET_MARK_OF_DEFIANCE) && !state->hasCooldown(cooldown::MARK_OF_DEFIANCE) && random<int>(0, 99) < 15) {
                onCooldownGain(make_shared<cooldown::MarkOfDefiance>());
                onManaGain(random<double>(128, 173), "Mana Restore (Mark of Defiance)");
            }
            // 5% proc rate ?
            if (config->spellstrike_set && random<int>(0, 19) == 0)
                onBuffGain(make_shared<buff::Spellstrike>());
            // 10% proc rate
            if (config->eternal_sage && !state->hasCooldown(cooldown::ETERNAL_SAGE) && random<int>(0, 9) == 0) {
                onCooldownGain(make_shared<cooldown::EternalSage>());
                onBuffGain(make_shared<buff::EternalSage>());
            }
            // 5% proc rate, cannot refresh itself while up
            if (config->wrath_of_cenarius && !state->hasCooldown(cooldown::SPELL_BLASTING) && random<int>(0, 19) == 0) {
                onCooldownGain(make_shared<cooldown::SpellBlasting>());
                onBuffGain(make_shared<buff::SpellBlasting>());
            }
            // 2% proc rate, mana-etched 4-set bonus
            if (config->mana_etched_4set && random<int>(0, 49) == 0) {
                onBuffGain(make_shared<buff::SpellPowerBonus>());
            }
            // 50% proc rate
            if (config->judgement_of_wisdom && random<int>(0, 1) == 1)
                onManaGain(74, "Judgement of Wisdom");

            if (hasTrinket(TRINKET_DARKMOON_CRUSADE))
                onBuffGain(make_shared<buff::DarkmoonCrusade>());

            if (spell->result == spell::CRIT) {
                // 20% proc rate
                if (hasTrinket(TRINKET_UNSTABLE_CURRENTS) && !state->hasCooldown(cooldown::UNSTABLE_CURRENTS) && random<int>(0, 4) == 0) {
                    onCooldownGain(make_shared<cooldown::UnstableCurrents>());
                    onBuffGain(make_shared<buff::UnstableCurrents>());
                }
                // 20% proc rate
                if (hasTrinket(TRINKET_NEXUS_HORN) && !state->hasCooldown(cooldown::CALL_OF_THE_NEXUS) && random<int>(0, 4) == 0) {
                    onCooldownGain(make_shared<cooldown::CallOfTheNexus>());
                    onBuffGain(make_shared<buff::CallOfTheNexus>());
                }
                // 100% proc rate
                if (hasTrinket(TRINKET_LIGHTNING_CAPACITOR) && !state->hasCooldown(cooldown::LIGHTNING_CAPACITOR))
                    onBuffGain(make_shared<buff::LightningCapacitor>());
                // 50% proc rate
                if (hasTrinket(TRINKET_ASHTONGUE_TALISMAN) && random<int>(0, 1) == 0)
                    onBuffGain(make_shared<buff::AshtongueTalisman>());

                if (spell->school == SCHOOL_FIRE && player->talents.ignite)
                    addIgnite(spell);
                if ((spell->school == SCHOOL_FIRE || spell->school == SCHOOL_FROST) && player->talents.master_of_elements)
                    onManaGain(spell->cost * 0.1 * player->talents.master_of_elements, "Master of Elements");
            """

        # Check for buffs to remove and new procs
        self._execute_clearcasting()
        if cast_spell.mana_cost > 0:
            self._execute_presence_of_mind()
        self._execute_insightful_earthstorm_gem_proc()
        self._execute_blue_dragon_trinket_proc()

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


class ManaEvent(Event):
    def __init__(self, source_actor: Actor, target_actor: Actor, amount: int, gain: bool):
        super().__init__(time=0, target_actor=target_actor, source_actor=source_actor)
        self.amount = amount
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
    def __init__(self, source_actor: Actor, target_actor: Actor, cast_spell: CastSpell, gain: bool):
        super().__init__(time=0, target_actor=target_actor, source_actor=source_actor)
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
                                                                                         self.cast_spell.result,
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
