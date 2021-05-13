import copy
from typing import List

from sujsim.core.items.enchant import Enchant
from sujsim.core.items.gem import Gem
from sujsim.core.spells.buff import Buff
from sujsim.core.stats.item_stats import ItemStats, merge_item_stats


class Gear:
    def __init__(self,
                 db_id: int,
                 name: str,
                 stats: ItemStats,
                 phase: int = 1,
                 buff: Buff = None,
                 sockets: List = None,
                 bonus: ItemStats = None,
                 is_two_hand: bool = False,
                 is_unique: bool = False):
        self.db_id = db_id
        self.name = name
        self.stats = stats
        self.phase = phase
        self.buff = buff
        self.sockets = [] if sockets is None else sockets
        self.bonus = bonus
        self.is_two_hand = is_two_hand
        self.is_unique = is_unique

    def add_gems(self, gems: List[Gem]):
        item = copy.deepcopy(self)

        if len(gems) > len(item.sockets):
            raise ValueError('{} gems, but only {} sockets'.format(len(gems), len(item.sockets)))
        matches_socket = True
        for gem, socket in zip(gems, item.sockets):
            if socket is 'm' and gem.color is not 'm':
                raise ValueError('Only meta gem may be placed in meta gem socket')
            if socket is 'r' and (gem.color is not 'r' or gem.color is not 'p' or gem.color is not 'o'):
                matches_socket = False
            if socket is 'y' and (gem.color is not 'y' or gem.color is not 'g' or gem.color is not 'o'):
                matches_socket = False
            if socket is 'b' and (gem.color is not 'b' or gem.color is not 'g' or gem.color is not 'p'):
                matches_socket = False

        # Add gem socket bonus if the colors match
        if matches_socket:
            merge_item_stats(item.stats, item.bonus)

        # Add the gem stats
        for gem in gems:
            merge_item_stats(item.stats, gem.stats)
        return item

    def add_enchant(self, enchants: List[Enchant]):
        item = copy.deepcopy(self)

        # Add the enchant stats
        for enchant in enchants:
            merge_item_stats(item.stats, enchant.stats)

        return item
