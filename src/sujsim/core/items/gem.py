from sujsim.core.stats.item_stats import ItemStats


class Gem():
    def __init__(self,
                 db_id: int,
                 name: str,
                 stats: ItemStats,
                 color: str,
                 is_unique: bool = False,
                 phase: int = 1):
        self.db_id = db_id
        self.name = name
        self.stats = stats
        self.color = color
        self.is_unique = is_unique
        self.phase = phase
