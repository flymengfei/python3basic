# -*- coding: utf-8 -*-

(1+1)*2
type((1))  # (1)python3当作数学运算

type((1,))  # tuple

type([1])  # list

# int,float,bool,str,list,tuple
# 序列：str,list,tuple

'hello,world'[2]
[1,2,3][2]
# 序列都会被分配到一个序号

# 切片
[1,2,3,4][0:3]
"hello,world"[0:8:2]

3 in [1,2,3,4,5,6]
3 not in [1,2,3,4,5,6]

len([1,2,3,4,5,6])
len("hello,world")

max([1,2,3,4,5,6])
min([1,2,3,4,5,6])
max("hello,world")
min("hello,world")

ord('w')
ord('d')
ord(',')