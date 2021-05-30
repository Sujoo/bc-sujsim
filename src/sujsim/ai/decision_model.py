from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sujsim.sim.actor import Actor

import abc

from sujsim.core.spells.buff_database import debuffs, combat_buffs
from sujsim.core.spells.spell_database import mage_spells
from sujsim.sim.event import Event, MageCastEvent, WaitEvent, GainBuffEvent


class DecisionModel(abc.ABC):
    def __init__(self, player: Actor, boss: Actor):
        self.player = player
        self.boss = boss

    @abc.abstractmethod
    def get_next_action(self) -> Event:
        pass


class FireballSpam(DecisionModel):
    def __init__(self, player: Actor, boss: Actor):
        super().__init__(player=player, boss=boss)

    def get_next_action(self) -> Event:
        return MageCastEvent(spell=mage_spells.FIREBALL_R14,
                             time=self.player.character.calculate_cast_time(mage_spells.FIREBALL_R14),
                             source_actor=self.player,
                             target_actor=self.player,
                             spell_target=self.boss)


class ArcaneMage(DecisionModel):
    def __init__(self, player: Actor, boss: Actor):
        super().__init__(player=player, boss=boss)

    def get_next_action(self) -> Event:
        if self.player.character.has_buff(debuffs.GLOBAL_COOLDOWN):
            return WaitEvent(time=0.05, source_actor=self.player, target_actor=self.player)
        if self.player.character.mage_talents.presence_of_mind > 0 and not self.player.has_buff(debuffs.PRESENCE_OF_MIND_COOLDOWN):
            # TODO: this should cast as a spell, it costs mana
            self.player.add_to_queue(GainBuffEvent(buff=combat_buffs.PRESENCE_OF_MIND,
                                                   target_actor=self.player,
                                                   source_actor=self.player),
                                     execute_now=True)
            self.player.add_to_queue(GainBuffEvent(buff=debuffs.PRESENCE_OF_MIND_COOLDOWN,
                                                   target_actor=self.player,
                                                   source_actor=self.player),
                                     execute_now=True)
            return WaitEvent(time=1.5, source_actor=self.player, target_actor=self.player)  # Wait for GCD
        if self.player.character.mage_talents.arcane_power > 0 and not self.player.has_buff(debuffs.ARCANE_POWER_COOLDOWN):
            self.player.add_to_queue(GainBuffEvent(buff=combat_buffs.ARCANE_POWER,
                                                   target_actor=self.player,
                                                   source_actor=self.player),
                                     execute_now=True)
            self.player.add_to_queue(GainBuffEvent(buff=debuffs.ARCANE_POWER_COOLDOWN,
                                                   target_actor=self.player,
                                                   source_actor=self.player),
                                     execute_now=True)

        return MageCastEvent(spell=mage_spells.ARCANE_BLAST_R1,
                             time=self.player.character.calculate_cast_time(mage_spells.ARCANE_BLAST_R1),
                             source_actor=self.player,
                             target_actor=self.player,
                             spell_target=self.boss)


class ArcaneBlastSpam(DecisionModel):
    def __init__(self, player: Actor, boss: Actor):
        super().__init__(player=player, boss=boss)

    def get_next_action(self) -> Event:
        if self.player.character.has_buff(debuffs.GLOBAL_COOLDOWN):
            return WaitEvent(time=0.05, source_actor=self.player, target_actor=self.player)
        return MageCastEvent(spell=mage_spells.ARCANE_BLAST_R1,
                             time=self.player.character.calculate_cast_time(mage_spells.ARCANE_BLAST_R1),
                             source_actor=self.player,
                             target_actor=self.player,
                             spell_target=self.boss)


class ArcaneMissleSpam(DecisionModel):
    def __init__(self, player: Actor, boss: Actor):
        super().__init__(player=player, boss=boss)

    def get_next_action(self) -> Event:
        if self.player.character.has_buff(debuffs.GLOBAL_COOLDOWN):
            return WaitEvent(time=0.05, source_actor=self.player, target_actor=self.player)
        return MageCastEvent(spell=mage_spells.ARCANE_MISSILES_R10,
                             time=self.player.character.calculate_cast_time(mage_spells.ARCANE_MISSILES_R10) / mage_spells.ARCANE_MISSILES_R10.max_ticks,
                             source_actor=self.player,
                             target_actor=self.player,
                             spell_target=self.boss)


class EvocateSpam(DecisionModel):
    def __init__(self, player: Actor, boss: Actor):
        super().__init__(player=player, boss=boss)

    def get_next_action(self) -> Event:
        if self.player.character.has_buff(debuffs.EVOCATION_COOLDOWN):
            return WaitEvent(time=15, source_actor=self.player, target_actor=self.player)
        return MageCastEvent(spell=mage_spells.EVOCATION,
                             time=self.player.character.calculate_cast_time(mage_spells.EVOCATION) / mage_spells.EVOCATION.max_ticks,
                             source_actor=self.player,
                             target_actor=self.player,
                             spell_target=self.boss)


class FakeTestingSpam(DecisionModel):
    def __init__(self, player: Actor, boss: Actor):
        super().__init__(player=player, boss=boss)

    def get_next_action(self) -> Event:
        if self.player.character.has_buff(debuffs.GLOBAL_COOLDOWN):
            return WaitEvent(time=0.05, source_actor=self.player, target_actor=self.player)
        return MageCastEvent(spell=mage_spells.FAKE_SPELL,
                             time=self.player.character.calculate_cast_time(mage_spells.FAKE_SPELL),
                             source_actor=self.player,
                             target_actor=self.player,
                             spell_target=self.boss)


class DoNothing(DecisionModel):
    def __init__(self, player: Actor, boss: Actor):
        super().__init__(player=player, boss=boss)

    def get_next_action(self) -> Event:
        return WaitEvent(time=1000000, source_actor=self.player, target_actor=self.player)
