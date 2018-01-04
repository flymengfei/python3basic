# -*- coding: utf-8 -*-

from enum import Enum
from enum import IntEnum,unique

@unique  # 装饰器，枚举类型不能实例化
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4

# 23种设计模式 单例模式