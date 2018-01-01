# -*- coding: utf-8 -*-

a = 1
b = 2

if a > b:
    print('go to left')
else:
    print('go to right')

account = 'qiyue'
password = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if user_account == account:
    if user_password == password:
        print('success')
else:
    print('fail')
