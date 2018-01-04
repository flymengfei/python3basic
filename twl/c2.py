# -*- coding: utf-8 -*-

list_x = [1,2,3,4,5,6,7,8]
list_y = [1,4,9,16,25,36,49,64]

def square(x,y):
    return x * y

# for x in list_x:
#     square(x)

r = map(square,list_x,list_y)
print(r)
print(list(r))
