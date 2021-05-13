from sujsim.core.stats.item_stats import ItemStats


class Buff():
    def __init__(self,
                 db_id: int,
                 name: str,
                 stats: ItemStats = None,
                 phase: int = 1,
                 duration: float = 3600,  # default to 1 hour
                 stacks: int = 1,
                 max_stacks: int = 1,
                 is_hidden: bool = False):
        self.db_id = db_id
        self.name = name
        self.stats = stats
        self.phase = phase
        self.duration = duration
        self.stacks = stacks
        self.max_stacks = max_stacks
        self.is_hidden = is_hidden
        self.is_maxed = False

    def add_stack(self):
        if self.stacks == self.max_stacks:
            self.is_maxed = True
        self.stacks = min(self.stacks + 1, self.max_stacks)

