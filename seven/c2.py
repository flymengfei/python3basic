# -*- coding: utf-8 -*-

# 主要用来遍历/循环 序列或者集合、字典
a = ['apple','orange','banana','grape']
for x in a:
    print(x)

a = [['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
        print(y)
else:
    print('fruit is gone')  # 循环结束后使用

a = [['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
        print(y,end='')

a = [1,2,3]
for x in a:
    if x == 2:  # x遍历2时终止
        break
    print(x)

a = [1,2,3]
for x in a:
    if x == 2:  # 只是跳过x=2
        continue
    print(x)

a = [1,2,3]
for x in a:
    if x == 2:
        break   # 不执行else语句
    print(x)
else:
    print('EOF')

a = [1,2,3]
for x in a:
    if x == 2:
        continue   # 执行else语句
    print(x)
else:
    print('EOF')

a = [['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('fruit is gone')
