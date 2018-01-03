# -*- coding: utf-8 -*-

# json    python
# object  dict
# array   list
# string  str
# number  int
# number  float
# true    True
# false   False
# null    None

# 类c语言

# 序列化
import json
student = [
             {'name':'mf','age':18,'flag':False},
             {'name':'mf','age':18}
          ]

# NOSQL MongoDB
json_str = json.dumps(student)
print(type(json_str))
print(json_str)

# JSON对象、JSON、JSON字符串

# ECMASCRIPT ActionScript JSON Typescript
