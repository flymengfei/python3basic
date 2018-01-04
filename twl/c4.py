# -*- coding: utf-8 -*-

from functools import reduce

# 连续计算，连续调用lambda
list_x = ['1','2','3','4','5','6','7','8']
r = reduce(lambda x,y:x+y,list_x,'aaa')  # 10为初始值
print(r)

(((1+2)+3)+4)+5

# map/reduce 编程模型 映射 归约 并行计算
# 函数式编程
