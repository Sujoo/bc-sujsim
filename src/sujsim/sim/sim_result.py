class SimulationResult:
    def __int__(self,
                damage: int,
                time: int,
                dps: float,
                log: str):
        self.damage = damage
        self.time = time
        self.dps = dps
        self.log = str


class SimulationResults:
    def __init__(self,
                 min_dps: float,
                 max_dps: float,
                 average_dps: float,
                 iterations: int,
                 histogram: str):
        self.min_dps = min_dps
        self.max_dps = max_dps
        self.average_dps = average_dps
        self.iterations = iterations
        self.histogram = histogram
