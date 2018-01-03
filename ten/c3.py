# -*- coding: utf-8 -*-

import re

a = 'C0C++7Java8C#9Python6Javascript'

r = re.findall('\D',a)  # \d表示任意一个数字字符
print(r)

# 'Python' 普通字符 '\d' 元字符
# 根据自己的业务需求去找元字符去组成你想要的
