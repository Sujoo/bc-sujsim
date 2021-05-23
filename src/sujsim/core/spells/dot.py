from sujsim.core.spells.magic_school import MagicSchool


class Dot:
    def __init__(self,
                 db_id: int,
                 name: str,
                 magic_school: MagicSchool,
                 damage: float,
                 max_ticks: int = 1,
                 current_tick: int = 0,
                 tick_interval: float = 3,
                 is_stackable: bool = False):
        self.db_id = db_id
        self.name = name
        self.magic_school = magic_school
        self.damage = damage
        self.max_ticks = max_ticks
        self.current_tick = current_tick
        self.tick_interval = tick_interval
        self.is_stackable = is_stackable

    def do_tick(self):
        self.current_tick += 1

    def stack(self):
        return


class Ignite(Dot):
    def __init__(self, damage: float):
        super(db_id=12848,
              name='Ignite',
              damage=damage,
              ticks=2,
              tick_interval=2,
              is_stackable=True)

    def stack(self, damage: float):
        if self.current_tick == 0:
            self.damage += damage
        elif self.current_tick == 1:
            self.damage = damage + round(self.damage / 2)
        else:
            self.damage
        tick = 0
