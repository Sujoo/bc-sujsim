import copy
import random
import pandas as pd

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
        self.end_of_simulation = end_of_simulation
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

    def get_dps(self, player: Actor) -> float:
        return self.boss.damage_taken[player] / self.end_of_simulation


class SimulationSet:
    def __init__(self,
                 player: Actor,
                 boss: Actor,
                 end_of_simulation: int):
        self.logs = []  # List[LogEntry]
        self.original_player = copy.deepcopy(player)
        self.original_boss = copy.deepcopy(boss)
        self.end_of_simulation = end_of_simulation

    def run_simulations(self, count: int):
        dps_list = []
        executed = 0
        while executed < count:
            executed += 1
            player = copy.deepcopy(self.original_player)
            sim = Simulation(player=player,
                             boss=copy.deepcopy(self.original_boss),
                             end_of_simulation=self.end_of_simulation)
            sim.run()
            dps_list.append(sim.get_dps(player))
        df = pd.Series(dps_list)
        print(df.min(), df.max(), df.mean())
