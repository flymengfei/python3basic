# -*- coding: utf-8 -*-

from c6 import Human

class Student(Human):
    sum = 0
    def __init__(self,school,name,age):
        self.school = school
        Human.__init__(self,name,age)
    #     self.__score = 0
    #     self.__class__.sum += 1

    def do_homework(self):
        print('english homework')

student1 = Student('人民小学','haha',18)
print(student1.sum)
print(Student.sum)
print(student1.name)
print(student1.age)
student1.get_name()
