# -*- coding: utf-8 -*-

# JSON:JavaScript对象标记，是一种轻量级的数据交换格式
# 字符串是JSON的表现形式
# {name: "mf"}
# JSON VS XML
# 跨语言交换数据

# 网站后台 ——> 浏览器

# 反序列化
import json

# JSON object array数组
json_str = '[{"name":"mf","age":18,"flag":false},{"name":"mf","age":18}]'  # 字符串

# dict
student = json.loads(json_str)
print(type(student))
print(student)
# print(student['name'])
# print(student['age'])
# dict [] ()
