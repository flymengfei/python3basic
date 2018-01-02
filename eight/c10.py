# -*- coding: utf-8 -*-

# c = 10  # 全局变量
# def demo():
#     c = 50  # 局部变量
#     print(c)
# print(c)
# demo()

def demo():
    c = 50
    # a = ''
    #块级作用域（python没有）
    for i in range(0,9):
        a = 'a'
        c += 1
    print(c)
    print(a)  # for循环可以引用内部代码

demo()
