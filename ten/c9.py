# -*- coding: utf-8 -*-

# 边界匹配
import re
qq = '100000001'
# 4~8
# r = re.findall('^\d{4,8}$',qq)
r = re.findall('000$',qq)
print(r)

# ^开始位置匹配  $末尾位置匹配  占位符