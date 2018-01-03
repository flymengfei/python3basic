# -*- coding: utf-8 -*-

# 概括字符集
# \d \D
# \w 单词字符[A-Za-z0-9_] \W
# \s 空白字符 \S
# . 匹配除换行符\n之外其他所有字符
import re
a = 'python 1111java&___678\nphp'

r = re.findall('\s',a)
print(r)
