# -*- coding: utf-8 -*-

from enum import Enum
# 枚举其实是一个类
class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4
# 别名
class Common():
    YELLOW = 1
a = 1
print(VIP(a))
# if a == VIP.YELLOW:
#     print()
# if a == VIP.BLACK:
#     print()

# VIP.black VIP.green
print(VIP.YELLOW)
# VIP.YELLOW = 6

for v in VIP.__members__:
    print(v)
