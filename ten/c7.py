# -*- coding: utf-8 -*-

# 字符串
import re
s = 'abc,acc,adc,aec,afc,ahc'

r = re.findall('a[c-f]c',s)
print(r)
