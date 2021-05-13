from sujsim.core.character.character import Character
from sujsim.sim.actor import Actor


class Simulation:
    def __init__(self,
                 player: Actor,
                 boss: Actor,
                 end_of_simulation: int):
        self.logs = []  # List[LogEntry]
        self.player = player
        self.boss = boss

        self.player.setup(self.logs, end_of_simulation, boss=boss)
        self.boss.setup(self.logs, end_of_simulation, boss=boss)

    def run(self):
        while len(self.player.event_queue) > 0:
            event = self.player.event_queue.pop(0)
            event.execute()
