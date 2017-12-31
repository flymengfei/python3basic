# -*- coding: utf-8 -*-

type = 1
type(1)  # TypeError
print(type)

# int str tuple(不可改变) 值类型 list set dict(可变) 引用类型
a = 'hello'
a = a + 'python'
print(a)

b = 'hello'
id(b)
b = b + 'python'
id(b)

'python'[0]
'python'[0] = '0'  # TypeError