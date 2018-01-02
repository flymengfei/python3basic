# -*- coding: utf-8 -*-

# 4.可变参数

print('a','b','c')

# (),[]

def demo(*param):
    print(param)
    print(type(param))

a = (1,2,3,4,5,6)
demo(*a)

def demo(param1,param2=2,*param):  # 必须参数，默认参数，可变参数
    print(param1)
    print(param2)
    print(param)
    # print(type(param))

demo('a',1,2,3)

def demo(param1,*param,param2=2):  # 必须参数，默认参数，可变参数
    print(param1)
    print(param)
    print(param2)
    # print(type(param))

demo('a',1,2,3,'param')
demo('a',1,2,3,param2 = 'param')
# 参数列表不要设置这么复杂
