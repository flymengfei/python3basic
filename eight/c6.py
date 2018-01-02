# -*- coding: utf-8 -*-

# 3.默认参数

def print_student_files(name,gender,age,college):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')

print_student_files('哈哈','男',18,'杨挂小学')

def print_student_files(name,gender='男',age=18,college='杨挂小学'):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')

print_student_files('哈哈')
print('~~~~~~~~~~~~~~~~~~~~~')
print_student_files('呵呵')
print('~~~~~~~~~~~~~~~~~~~~~')
print_student_files('呵呵','女',18)
print('~~~~~~~~~~~~~~~~~~~~~')
print_student_files('果果',age = 17,college = '光明小学',gender = '女')
# 实参会和形参对应起来

# 不能把参数放在默认参数后

