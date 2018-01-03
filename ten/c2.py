# -*- coding: utf-8 -*-

import re

a = 'C0C++7Java8C#9Python6Javascript'
# for in

r = re.findall('PHP',a)  # 常量表达式
# 规则
if len(r) != 0:
    print('字符串中包含PHP')
else:
    print('No')
# print(r)
# print(a.index('Python')>-1)

# print('Python' in a)
