# -*- coding: utf-8 -*-

import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator  # 装饰器的一个语法糖 @符号
def f1():
    print('This is a function')

f1()
# ES6 class
# @ AOP
# f = decorator(f1)
# f()
