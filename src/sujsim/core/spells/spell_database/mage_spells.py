from sujsim.core.spells.dot import Dot
from sujsim.core.spells.magic_school import MagicSchool
from sujsim.core.spells.spell import Spell, MageSpells

# Fake, for testing
FAKE_SPELL = Spell(spell_type=MageSpells.GCD, rank=1, min_damage=0, max_damage=0, cast_time=0.5, coefficient=0, mana_cost=0,
                   magic_school=MagicSchool.ARCANE)

# GCD "Spell"
GCD_SPELL = Spell(spell_type=MageSpells.GCD, rank=1, min_damage=0, max_damage=0, cast_time=1.5, coefficient=0, mana_cost=0,
                  magic_school=MagicSchool.ARCANE)

# Arcane
ARCANE_BLAST_R1 = Spell(spell_type=MageSpells.ARCANE_BLAST, rank=1, min_damage=668, max_damage=772, cast_time=2.5, coefficient=2.5 / 3.5, mana_cost=195,
                        magic_school=MagicSchool.ARCANE)

# Fireball
FIREBALL_R14 = Spell(spell_type=MageSpells.FIREBALL, rank=14, min_damage=717, max_damage=913, cast_time=3.5, coefficient=1.0, mana_cost=465,
                     magic_school=MagicSchool.FIRE,
                     dot=Dot(db_id=27070, name='{} R{} DoT'.format(MageSpells.FIREBALL.value, 14), tick_interval=2, ticks=4, damage=21))
FIREBALL_R13 = Spell(spell_type=MageSpells.FIREBALL, rank=13, min_damage=649, max_damage=821, cast_time=3.5, coefficient=1.0, mana_cost=425,
                     magic_school=MagicSchool.FIRE,
                     dot=Dot(db_id=27070, name='{} R{} DoT'.format(MageSpells.FIREBALL.value, 13), tick_interval=2, ticks=4, damage=21))
FIREBALL_R12 = Spell(spell_type=MageSpells.FIREBALL, rank=12, min_damage=611, max_damage=776, cast_time=3.5, coefficient=1.0, mana_cost=410,
                     magic_school=MagicSchool.FIRE,
                     dot=Dot(db_id=27070, name='{} R{} DoT'.format(MageSpells.FIREBALL.value, 12), tick_interval=2, ticks=4, damage=19))
FIREBALL_R11 = Spell(spell_type=MageSpells.FIREBALL, rank=11, min_damage=575, max_damage=730, cast_time=3.5, coefficient=1.0, mana_cost=395,
                     magic_school=MagicSchool.FIRE,
                     dot=Dot(db_id=27070, name='{} R{} DoT'.format(MageSpells.FIREBALL.value, 11), tick_interval=2, ticks=4, damage=18))
# Pyroblast
PYROBLAST_R10 = Spell(spell_type=MageSpells.PYROBLAST, rank=10, min_damage=939, max_damage=1191, cast_time=6.0, coefficient=1.0, mana_cost=500,
                      magic_school=MagicSchool.FIRE,
                      dot=Dot(db_id=27070, name='{} R{} DoT'.format(MageSpells.PYROBLAST.value, 10), tick_interval=3, ticks=4, damage=89))
# Scorch
SCORCH_R9 = Spell(spell_type=MageSpells.SCORCH, rank=9, min_damage=305, max_damage=361, cast_time=1.5, coefficient=1.5 / 3.5, mana_cost=180,
                  magic_school=MagicSchool.FIRE)

# Fireblast
FIRE_BLAST_RX = Spell(spell_type=MageSpells.FIRE_BLAST, rank=-1, min_damage=446, max_damage=524, cast_time=0, coefficient=0.4285, mana_cost=-1,
                      magic_school=MagicSchool.FIRE)
"""
          'Frostbolt': [440, 475, 2.5, 0.814, 260, FROST_SPELL],  # Rank 10
          'Frostbolt_r1': [20, 22, 1.5, 0.814, 25, FROST_SPELL],
          'Arcane Explosion': [249, 270, 1.5, 0.143, 390, ARCANE_AOE_SPELL],
          'Blast Wave': [462, 544, 1.5, 0.129, 545, FIRE_AOE_SPELL],
"""
