# -*- coding: utf-8 -*-

# a = x
#
# a = 1 print('apple')
# a = 2 print('orange')
# a = 3 print('banana')
#
# print('shopping')

a = input()
a = int(a)

if a == 1:
    print('apple')
else:
    if a == 2:
        print('orange')
    else:
        if a == 3:
            print('banana')
        else:
            print('shopping')

# elif:else if 不能单独使用，代码更加简洁
a = input()
a = int(a)

if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('banana')
else:
    print('shopping')
