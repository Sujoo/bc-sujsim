import copy
from typing import List

from sujsim.ai.decision_model import DecisionModel
from sujsim.core.character.character import Character
from sujsim.core.spells.buff import Buff
from sujsim.core.spells.buff_database import debuffs
from sujsim.core.spells.buff_database.debuffs import create_gcd, CASTING_5_SECOND_RULE
from sujsim.core.spells.spell_database.mage_spells import GCD_SPELL
from sujsim.sim.event import MageCastEvent, Event, ManaRegenEvent, GainBuffEvent, LoseBuffEvent, DotEvent
from sujsim.sim.sim_log import LogEntry


class Actor:
    def __init__(self,
                 character: Character,
                 decision_model_class: DecisionModel):
        self.character = character
        self.decision_model_class = decision_model_class
        self.decision_model = None
        self.current_time = 0.0
        self.end_of_simulation = -1
        self.logs = []  # List[LogEntry]
        self.event_queue = []  # List[Event]

    def setup(self, logs: List[LogEntry], end_of_simulation: int, boss, start_mana_regen: bool = True):
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
        if event.time <= self.end_of_simulation:
            if execute_now:
                event.execute()
            else:
                # Reset the DoT before reapplying
                if isinstance(event, DotEvent):
                    self.remove_dot_event_from_queue(event)
                self.event_queue.append(event)
                self.event_queue.sort(key=lambda x: x.time)

                # When you start casting, check if the spell being cast sets off the GCD
                if isinstance(event, MageCastEvent) and event.spell.does_trigger_gcd:
                    self.add_to_queue(GainBuffEvent(buff=create_gcd(duration=self.character.calculate_cast_time(GCD_SPELL)),
                                                    source_actor=event.source_actor,
                                                    target_actor=event.source_actor), execute_now=True)
                    self.add_to_queue(GainBuffEvent(buff=CASTING_5_SECOND_RULE,
                                                    source_actor=event.source_actor,
                                                    target_actor=event.source_actor))

    def remove_lose_buff_event_from_queue(self, event: GainBuffEvent):
        found_event = None
        for search_event in self.event_queue:
            if isinstance(search_event, LoseBuffEvent) and search_event.buff.db_id == event.buff.db_id:
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
