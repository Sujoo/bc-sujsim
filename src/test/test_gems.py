from unittest import TestCase

from sujsim.core.items.gear_database import head
from sujsim.core.items.gem_database import gems
from sujsim.core.spells.magic_school import MagicSchool


class GemTest(TestCase):
    def test_gems(self):
        item_1 = head.INCANTERS_COWL
        item_2 = head.INCANTERS_COWL.add_gems([gems.CHAOTIC_SKYFIRE, gems.RUNED_ORNATE_RUBY])
        self.assertEqual(29, item_1.stats.spell_stats_dict[MagicSchool.FIRE].spell_power)
        self.assertEqual(41, item_2.stats.spell_stats_dict[MagicSchool.FIRE].spell_power)
