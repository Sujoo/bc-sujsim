from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sujsim.sim.actor import Actor

import abc

from sujsim.core.spells.buff_database import debuffs
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


class ArcaneSpam(DecisionModel):
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
        return WaitEvent(time=5, source_actor=self.player, target_actor=self.player)
