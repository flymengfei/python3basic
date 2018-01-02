# -*- coding: utf-8 -*-

# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象
# 类的名字首字母需要大写，不要像变量一样用下划线
# 实例化
# 类最基本的作用：封装
# 类和对象
class Student():
    sum = 0
    name = 'mf'  # 类变量
    age = 0
# '类变量' '实例变量'
    def __init__(self,name,age):  # 实例方法 对象
        # 构造函数
        # 初始化对象的属性
        self.name = name  # 实例变量
        self.age = age
        # print('student')

    # 行为 与 特征
    def do_homework(self):
        print('homework')

    @classmethod  # 装饰器 类方法 类本身
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

# 类就是一个印刷机、模版，类实例化可以产生很多个对象
# 类里面可以传入多个特征

# class Printer():
#     def print_file(self):
#         print('name: ' + self.name)
#         print('age: ' + str(self.age))

    # print_file()  类不负责执行代码，只负责定义

# class StudentHomework():
#     homework_name = ''

# 方法 和 函数的区别
# 方法：设计层面 函数：程序运行、过程式的一种称谓
# 数据成员 变量

# student = Student()  # 类实例化
# student.print_file()  # 调用类的方法
# 类实例化和调用不要放在定义类的文件里

student1 = Student('哈哈',18)
print(student1.name)

# a = student1.__init__()
# print(a)
# print(type(a))
# student2 = Student()
# student3 = Student()
#
# print(id(student1))
# print(id(student2))
# print(id(student3))
