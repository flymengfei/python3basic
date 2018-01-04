# -*- coding: utf-8 -*-

def f1():
    a = 10
    def f2():
        # a此时被认为是局部变量
        # a = 20
        return a
    return f2

f = f1()
print(f)
print(f.__closure__)
# 闭包只是思维方式，面向对象