# -*- coding: utf-8 -*-

# filter 过滤
list_x = [1,0,1,0,0,1]
list_u = ['a','B','c','F','e']
# r = filter(lambda x: True if x==1 else False,list_x)
r = filter(lambda x: x,list_x)
print(r)  # 返回集合类型
print(list(r))
