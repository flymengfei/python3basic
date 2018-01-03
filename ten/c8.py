# -*- coding: utf-8 -*-

# 数量词
# * 前面的字符匹配0次或者无限多次
# + 匹配1次或者无限多次
# ？匹配0次或者1次
import re
a = 'pytho0python1pythonn2'

r = re.findall('python?',a)
# r = re.findall('[a-z]{3,6}?',a)
# 贪婪 与 非贪婪?（一直到某一字符不符合）
print(r)
