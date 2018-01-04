# -*- coding: utf-8 -*-

from enum import Enum
# 枚举其实是一个类
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1
# VIP.black VIP.green
print(VIP.YELLOW.value)
print(type(VIP.YELLOW.name))
print(type(VIP.YELLOW))
print(VIP['GREEN'])

# 枚举类型、枚举的名字、枚举的值
# VIP.YELLOW = 6

for v in VIP:
    print(v)
