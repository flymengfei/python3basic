# -*- coding: utf-8 -*-

import re
s = 'A83C3721D86'

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

r = re.sub('\d',convert,s)
print(r)