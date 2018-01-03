# -*- coding: utf-8 -*-

# 匹配模式参数
import re
lanuage = 'PythonC#\nJavaPHP'
r = re.findall('c#.{1}',lanuage,re.I | re.S)
print(r)
# re.I 忽略大小写
