# -*- coding: utf-8 -*-

a = [['apple','orange','banana','grape'],(1,2,3)]

for x in a:
    print(x)

for x in a:
    if 'banana' in x:
        break
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('fruit is gone')

# for each
# a = [1,2,3,4,5...]

for x in range(0,10):
    print(x)

# for target_list in expression_list:
#     pass
for x in range(0,10,2):  # 2步长
    print(x,end = ' | ')

for x in range(10,0,-2):  # -2步长
    print(x,end = ' | ')
