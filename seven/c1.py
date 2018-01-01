# -*- coding: utf-8 -*-

# 循环 穷举
# 循环语句 while for

# while condition:
#     pass

condition = True

while condition:
    print('I am While')
# ctrl+c 结束死循环

counter = 0

while counter:
    counter += 1
    print(counter)

counter = 1

while counter:
    counter += 1
    print(counter)

counter = 1
# LOL 给自己设定一个目标，递归用while
while counter <= 10:
    counter += 1
    print(counter)
else:
    print('EOF')