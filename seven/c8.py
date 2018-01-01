# -*- coding: utf-8 -*-

import c7   # import只能导入模块
print(c7.a)

from c7 import a   # form import可以导入变量，也可以导入模块
print(a)

from c7 import *

print(a)
print(c)
print(d)

