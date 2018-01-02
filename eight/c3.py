# -*- coding: utf-8 -*-

# R Skill1 Skill2

def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1,damage2

# damages = damage(3,6)

skill1_damage,skill2_damage = damage(3,6)
# 序列解包

# print(damages[0],damages[1])
# print(type(damages))

print(skill1_damage,skill2_damage)
