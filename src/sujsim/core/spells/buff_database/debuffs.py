import copy

from sujsim.core.spells.buff import Buff
from sujsim.core.stats.item_stats import ItemStats

GLOBAL_COOLDOWN = Buff(db_id=-100, name="GCD", duration=1.5, max_stacks=1)
CASTING_5_SECOND_RULE = Buff(db_id=-200, name="Casting 5 Second Rule", duration=5)
FIRE_VULNERABILITY = Buff(db_id=22959, name='Fire Vulnerability', duration=30, max_stacks=5)
WINTERS_CHILL = Buff(db_id=12579, name="Winter's Chill", duration=15, max_stacks=5)
MISERY = Buff(db_id=33195, name="Misery", duration=25)
CURSE_OF_ELEMENTS = Buff(db_id=27228, name="Curse of the Elements", stats=ItemStats(arcane_resistance=-88, fire_resistance=-88, frost_resistance=-88,
                                                                                    shadow_resistance=-88),  duration=300)


def create_gcd(duration: float = 1.5) -> Buff:
    gcd = copy.deepcopy(GLOBAL_COOLDOWN)
    gcd.duration = round(duration - 0.0001, 4)  # TODO: Double check the Event list ordering when GCD and Spell cast have the same duration
    return gcd
