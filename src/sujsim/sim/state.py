class State:
    def __init__(self,
                 time: float,
                 time_global_cooldown: float,
                 time_mana_spent: float,
                 mana: float,
                 damage: int,
                 regen_cycle: int,
                 innvervates: int,
                 mana_emerald: int,
                 mana_ruby: int,
                 combustion: int,
                 duration: int):
        self.time = time
        self.time_global_cooldown = time_global_cooldown
        self.time_mana_spent = time_mana_spent
        self.mana = mana
        self.damage = damage
        self.regen_cycle = regen_cycle
        self.innervates = innvervates
        self.mana_emerald = mana_emerald
        self.mana_ruby = mana_ruby
        self.combustion = combustion
        self.duration = duration
