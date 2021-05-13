from sujsim.core.stats.item_stats import ItemStats


class Enchant():
    def __init__(self,
                 db_id: int,
                 name: str,
                 stats: ItemStats,
                 phase: int = 1):
        self.db_id = db_id
        self.name = name
        self.stats = stats
        self.phase = phase
