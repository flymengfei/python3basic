# -*- coding: utf-8 -*-

c = 1

def func1():
    c = 2
    def func2():
        # c = 3   # 优先使用局部变量
        print(c)
    func2()

func1()

# 局部变量的相对性
# 链式，作用域链