# -*- coding: utf-8 -*-

# 装饰器
# 特性 注解
import time

def f1():
    print(time.time())
    print('This is a function')
# unix 时间戳
f1()

# 对修改是封闭的，对扩展是开发的

def f2():
    print('This is a function')

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)
