# -*- coding: utf-8 -*-

# 组（）
import re
a = 'PythonPythonPythonPythonPython'
r = re.findall('(Python){3}(JS)',a)
# [abc] 或关系
# (abc) 且关系
print(r)
