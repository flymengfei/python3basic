# -*- coding: utf-8 -*-

a = 1
b = 2
c = 3

a,b,c = 1,2,3

d = 1,2,3
print(type(d))

a,b,c = d  # 序列解包 元素个数相等

a,b,c = [1,2,3]

a = 1
b = 1
c = 1

a,b,c = 1,1,1
a=b=c=1
print(a,b,c)
# 链式赋值
