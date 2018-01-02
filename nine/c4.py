# -*- coding: utf-8 -*-

# 模版
class Student():
    # sum = 0
    name = 'qiyue'
    age = 0

    # 实例方法
    def __init__(self,name,age):  # self 代表的是实例
        self.name = name
        self.age = age
        # print(age)
        # print(name)
        print(self.name)
        # print('student')

    # 行为 与 特征
    def do_homework(self):
        print('homework')

student1 = Student('haha',18)
print(student1.__dict__)
# print(student1.name) 寻找，先在实例中寻找，没有的话再在类中寻找
# print(Student.name)
print(Student.__dict__)