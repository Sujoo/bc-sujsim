from unittest import TestCase

from sujsim.core.items.gear_database import head
from sujsim.core.items.enchant_database import enchants
from sujsim.core.spells.magic_school import MagicSchool


class EnchantTest(TestCase):
    def test_enchants(self):
        item_1 = head.INCANTERS_COWL
        item_2 = head.INCANTERS_COWL.add_enchant([enchants.SUNFIRE])
        self.assertEqual(29, item_1.stats.spell_stats_dict[MagicSchool.FIRE].spell_power)
        self.assertEqual(79, item_2.stats.spell_stats_dict[MagicSchool.FIRE].spell_power)
