# -*- coding: utf-8 -*-

import time

def decorator(func):
    # key word
    def wrapper(*args,**kw):  # args通用叫法
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator  # 装饰器的一个语法糖 @符号
def f1(func_name):
    print('This is a function named ' + func_name)

@decorator
def f2(func_name1,func_name2):
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)

@decorator
def f3(func_name1,func_name2,**kw):  # 关键字参数
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)
    print(kw)

f3('test func1','test func2',a=1,b=2)
f1('test func')
f2('test func1','hha')
