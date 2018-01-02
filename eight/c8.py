# -*- coding: utf-8 -*-

def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
    print(sum)

squsum(1,2,3,4)

# def squsum(*param):
#     sum = 0
#     for i in param:
#         sum += i*i
#         print(sum)
#
# squsum(1,2,3,4)

# squsum(*{1,2,3,4})
# 任意关键字参数
# squsum('36c','42c','31c')

def city_temp(**param):
    for key,value in param.items():
        print(key,':',value)

a = {'bj':'32c','sh':'31c'}
# city_temp(bj='32c',xm='23c',sh='31c')
city_temp(**a)
# city_temp()
