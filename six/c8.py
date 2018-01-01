# -*- coding: utf-8 -*-
'''
    一段小程序
'''

account = 'qiyue'
password = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('fail')

# constant 常量（在python里并非正真意义上的常量）大写
# 一个文件就是一个模块
# 变量在函数、类里
