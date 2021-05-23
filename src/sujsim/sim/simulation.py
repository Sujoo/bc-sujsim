import random

from sujsim.sim.actor import Actor


class Simulation:
    def __init__(self,
                 player: Actor,
                 boss: Actor,
                 end_of_simulation: int,
                 seed: int = None):
        self.logs = []  # List[LogEntry]
        self.player = player
        self.boss = boss
        self.actors = [player, boss]
        self.next_actor = None
        if seed:
            random.seed(seed)

        self.player.setup(self.logs, end_of_simulation, boss=self.boss)
        self.boss.setup(self.logs, end_of_simulation, boss=self.boss, start_mana_regen=False)

    def run(self):
        while self.has_next_actor():
            event = self.next_actor.event_queue.pop(0)
            event.execute()

    def has_next_actor(self) -> bool:
        self.next_actor = None
        next_time = None
        for actor in self.actors:
            if len(actor.event_queue) > 0:
                event = actor.event_queue[0]
                if next_time is None or event.time <= next_time:
                    next_time = event.time
                    self.next_actor = actor
        if self.next_actor:
            return True
        else:
            return False
