from __future__ import annotations
from typing import List, Type
from collections import defaultdict

from sujsim.ai.decision_model import DecisionModel
from sujsim.core.character.character import Character
from sujsim.core.spells.buff import Buff
from sujsim.core.spells.buff_database import combat_buffs
from sujsim.core.spells.buff_database.debuffs import create_gcd
from sujsim.core.spells.spell_database.mage_spells import GCD_SPELL
from sujsim.sim.event import MageCastEvent, Event, ManaRegenEvent, GainBuffEvent, LoseBuffEvent, DotEvent
from sujsim.sim.sim_log import LogEntry


class Actor:
    def __init__(self,
                 character: Character,
                 decision_model_class: Type[DecisionModel]):
        self.character = character
        self.decision_model_class = decision_model_class
        self.decision_model = None
        self.current_time = 0.0
        self.end_of_simulation = -1
        self.logs = []  # List[LogEntry]
        self.event_queue = []  # List[Event]
        self.damage_taken = defaultdict(int)
        self.healing_given = defaultdict(int)
        self.mana_given = defaultdict(int)

    def setup(self, logs: List[LogEntry], end_of_simulation: int, boss: Actor, start_mana_regen: bool = True):
        self.logs = logs
        self.end_of_simulation = end_of_simulation
        self.decision_model = self.decision_model_class(player=self, boss=boss)
        if start_mana_regen:
            self.add_to_queue(ManaRegenEvent(2, source_actor=self, target_actor=self))
        self.queue_next_action()

    def queue_next_action(self):
        self.add_to_queue(self.decision_model.get_next_action())

    def add_to_queue(self, event: Event, execute_now: bool = False):
        if execute_now and event.time > 0:
            raise ValueError('You cannot execute an event now when the time of the event executing is > 0.')
        event.time += self.current_time  # This is the key to moving time forward
        if isinstance(event, GainBuffEvent):
            if (event.buff.stats is not None and event.buff.stats.mp_5 > 0) or any(buff == event.buff for buff in [combat_buffs.INNERVATE,
                                                                                                                   combat_buffs.MANA_TIDE]):
                self.reset_mana_regen_tick()
        if event.time <= self.end_of_simulation or isinstance(event, GainBuffEvent) or isinstance(event, LoseBuffEvent):
            if execute_now:
                event.execute()
            else:
                # Reset the DoT before reapplying
                if isinstance(event, DotEvent):
                    self.remove_dot_event_from_queue(event)
                self.event_queue.append(event)
                self.event_queue.sort(key=lambda x: (x.time, x.priority))

                # When you start casting, check if the spell being cast sets off the GCD
                if isinstance(event, MageCastEvent) and event.spell.does_trigger_gcd:
                    self.add_to_queue(GainBuffEvent(buff=create_gcd(duration=self.character.calculate_cast_time(GCD_SPELL)),
                                                    source_actor=event.source_actor,
                                                    target_actor=event.source_actor), execute_now=True)

    def reset_mana_regen_tick(self):
        """
        When a new mp generation event occurs, the current mana tick gives back mana immediately.
        E.g., if mana regen started at 0, it will tick at 2.  But if mana spring totem drops at 1,
        the mana regen will immediately tick and provide 1 second of mana regen. Then a new tick starts
        which will execute at 3.
        """
        old_mana_regen_event = self.remove_mana_regen_event_from_queue()
        time_until_mana_tick = old_mana_regen_event.time - self.current_time
        old_mana_regen_event.seconds_of_regen = time_until_mana_tick
        old_mana_regen_event.execute()

    def remove_mana_regen_event_from_queue(self):
        found_event = None
        for search_event in self.event_queue:
            if isinstance(search_event, ManaRegenEvent):
                found_event = search_event
        if found_event:
            self.event_queue.remove(found_event)
        return found_event

    def remove_lose_buff_event_from_queue(self, event: GainBuffEvent):
        found_event = None
        for search_event in self.event_queue:
            if isinstance(search_event, LoseBuffEvent) and search_event.buff.db_id == event.buff.db_id and search_event.buff.name == event.buff.name:
                found_event = search_event
                break
        if found_event:
            self.event_queue.remove(found_event)

    def remove_dot_event_from_queue(self, event: DotEvent):
        found_event = None
        for search_event in self.event_queue:
            if isinstance(search_event, DotEvent) and search_event.dot.db_id == event.dot.db_id and search_event.dot.name == event.dot.name:
                found_event = search_event
                break
        if found_event:
            self.event_queue.remove(found_event)

    def add_to_log(self, log_entry: LogEntry):
        self.logs.append(log_entry)

    def add_buff(self, buff) -> Buff:
        return self.character.add_buff(buff)

    def remove_buff(self, buff):
        self.character.remove_buff(buff)

    def has_buff(self, buff: Buff) -> bool:
        return self.character.has_buff(buff)

    def get_buff(self, buff: Buff) -> Buff:
        return self.character.get_buff(buff)
