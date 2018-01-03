# -*- coding: utf-8 -*-

import re

s = '83C72D1D8E67'
# None
r = re.match('\d',s)
print(r.span())
r1 = re.search('\d',s)
print(r1.group())
r2 = re.findall('\d',s)
print(r2)
