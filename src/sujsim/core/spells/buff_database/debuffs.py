import copy

from sujsim.core.spells.buff import Buff
from sujsim.core.stats.item_stats import ItemStats

GLOBAL_COOLDOWN = Buff(db_id=-100, name="GCD", duration=1.5, max_stacks=1)
CASTING_5_SECOND_RULE = Buff(db_id=-200, name="Casting 5 Second Rule", duration=5)
FIRE_VULNERABILITY = Buff(db_id=22959, name='Fire Vulnerability', duration=30, max_stacks=5)
WINTERS_CHILL = Buff(db_id=12579, name="Winter's Chill", duration=15, max_stacks=5)
JUDGEMENT_OF_WISDOM = Buff(db_id=27164, name='Judgement of Wisdom', duration=20)
MISERY = Buff(db_id=33195, name="Misery", duration=25)
CURSE_OF_ELEMENTS = Buff(db_id=27228, name="Curse of the Elements", stats=ItemStats(arcane_resistance=-88, fire_resistance=-88, frost_resistance=-88,
                                                                                    shadow_resistance=-88), duration=300)

NONE_COOLDOWN = Buff(db_id=0, name='', duration=120)
POTION_COOLDOWN = Buff(db_id=1, name='Potion Cooldown', duration=120)
CONJURED_COOLDOWN = Buff(db_id=2, name='Conjured Cooldown', duration=120)
EVOCATION_COOLDOWN = Buff(db_id=12051, name='Evocation Cooldown', duration=480)
COLD_SNAP_COOLDOWN = Buff(db_id=11958, name='Cold Snap Cooldown', duration=480)
BERSERKING_COOLDOWN = Buff(db_id=20554, name='Berserking Cooldown', duration=180)
ICY_VEINS_COOLDOWN = Buff(db_id=12472, name='Icy Veins Cooldowns', duration=180)
COMBUSTION_COOLDOWN = Buff(db_id=29977, name='Combustion Cooldown', duration=180)
ARCANE_POWER_COOLDOWN = Buff(db_id=12042, name='Arcane Power Cooldown', duration=180)
PRESENCE_OF_MIND_COOLDOWN = Buff(db_id=12043, name='Presence of Mind Cooldown', duration=180)
QUAGMIRRANS_EYE_COOLDOWN = Buff(db_id=33370, name='Quagmirrans Eye Cooldown', duration=45)
UNSTABLE_CURRENTS_COOLDOWN = Buff(db_id=38348, name='Unstable Currents Cooldown', duration=45)
ETERNAL_SAGE_COOLDOWN = Buff(db_id=35084, name='Eternal Sage Cooldown', duration=45)
SPELL_BLASTING_COOLDOWN = Buff(db_id=25906, name='Spell Blasting Cooldown', duration=10)
DRUMS_COOLDOWN = Buff(db_id=35476, name='Drums Cooldown', duration=120)
LIGHTNING_CAPACITOR_COOLDOWN = Buff(db_id=37657, name='Lightning Capcitor Cooldown', duration=2.5)
INSIGHTFUL_EARTHSTORM_COOLDOWN = Buff(db_id=27521, name='Insightful Earthstorm Cooldown', duration=15)
MARK_OF_DEFIANCE_COOLDOWN = Buff(db_id=33511, name='Mark of Defiance Cooldown', duration=15)
CALL_OF_THE_NEXUS_COOLDOWN = Buff(db_id=34320, name='Call of the Nexus Cooldown', duration=45)

TRINKET1_COOLDOWN = Buff(db_id=3, name='Trinket 1 Cooldown', duration=120)
TRINKET2_COOLDOWN = Buff(db_id=4, name='Trinket 2 Cooldown', duration=120)


def create_gcd(duration: float = 1.5) -> Buff:
    gcd = copy.deepcopy(GLOBAL_COOLDOWN)
    gcd.duration = round(duration - 0.0001, 4)  # TODO: Double check the Event list ordering when GCD and Spell cast have the same duration
    return gcd
