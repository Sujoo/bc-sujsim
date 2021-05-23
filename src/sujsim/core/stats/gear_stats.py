from sujsim.core.items.gear import Gear
from sujsim.core.stats.item_stats import ItemStats, merge_item_stats


class GearStats(object):
    def __init__(self,
                 head: Gear = None,
                 neck: Gear = None,
                 shoulder: Gear = None,
                 back: Gear = None,
                 chest: Gear = None,
                 wrist: Gear = None,
                 hands: Gear = None,
                 waist: Gear = None,
                 legs: Gear = None,
                 feet: Gear = None,
                 ring_1: Gear = None,
                 ring_2: Gear = None,
                 trinket_1: Gear = None,
                 trinket_2: Gear = None,
                 main_hand: Gear = None,
                 off_hand: Gear = None,
                 wand: Gear = None):
        self.head = head
        self.neck = neck
        self.shoulder = shoulder
        self.back = back
        self.chest = chest
        self.wrist = wrist
        self.hands = hands
        self.waist = waist
        self.legs = legs
        self.feet = feet
        self.ring_1 = ring_1
        self.ring_2 = ring_2
        self.trinket_1 = trinket_1
        self.trinket_2 = trinket_2
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.wand = wand
        self.gear_list = [self.head, self.neck, self.shoulder, self.back, self.chest, self.wrist,
                          self.hands, self.waist, self.legs, self.feet,
                          self.ring_1, self.ring_2, self.trinket_1, self.trinket_2,
                          self.main_hand, self.off_hand, self.wand]
        self.stats = ItemStats()
        self.finalize()

    def finalize(self):
        self.validate_gear_stats()

        self.stats = ItemStats()
        for item in self.gear_list:
            if item is not None:
                merge_item_stats(self.stats, item.stats)

    def validate_gear_stats(self):
        if self.main_hand and self.main_hand.is_two_hand and self.off_hand is not None:
            raise ValueError("Main hand is 2H, but gear set includes an off-hand.  Remove the off-hand.")
        if self.ring_1 and self.ring_2 and self.ring_1.is_unique and self.ring_2.is_unique and self.ring_1.db_id == self.ring_2.db_id:
            raise ValueError("Unique ring equiped twice.  Replace one of the rings.")
        if self.trinket_1 and self.trinket_2 and self.trinket_1.db_id == self.trinket_2.db_id:
            raise ValueError("The same trinket is equiped twice.  Replace one of the trinkets.")

    def has_trinket(self, trinket: Gear) -> bool:
        if trinket.db_id == self.trinket_1.db_id or trinket.db_id == self.trinket_2.db_id:
            return True
        else:
            return False

    def has_ring(self, ring: Gear) -> bool:
        if ring.db_id == self.ring_1.db_id or ring.db_id == self.ring_2.db_id:
            return True
        else:
            return False

    def has_ember_skyfire_meta_gem(self) -> bool:
        return False

    def has_insightful_earthstorm_meta_gem(self) -> bool:
        return False

    def has_chaotic_skyfire_meta_gem(self) -> bool:
        return False

    def has_spellfire_set(self) -> bool:
        return False

    def has_spellstrike(self) -> bool:
        return False
