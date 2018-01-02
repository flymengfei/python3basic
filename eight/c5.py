# -*- coding: utf-8 -*-

# 参数
# 1.必须参数:
# a.形式参数，形参
# b.实际参数，实参
# 2.关键字参数

def add(x,y):
    # 形式参数，形参
    result = x + y
    return result

c = add(y=3,x=2)  # 关键字参数
# 代码的可读性
# 区别在于函数的调用上
