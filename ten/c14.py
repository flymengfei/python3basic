# -*- coding: utf-8 -*-

import re
language = 'PythonC#JavaC#PHPC#'

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'

r = re.sub('C#',convert,language)
# language = language.replace('C#','GO')  # 内置函数
print(r)
# 字符串是不可变的
# 把函数当参数
