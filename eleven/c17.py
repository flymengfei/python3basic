# -*- coding: utf-8 -*-

origin = 0
# 函数式编程
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(5))