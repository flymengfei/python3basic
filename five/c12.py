# -*- coding: utf-8 -*-

# 集合是无序的，元组是有序的
a = 1
b = 2
a == b  # 值
a is b  # 身份
# 类型 type 判断
# 对象 三个特征 一切都是对象
a = 'hello'
type(a) == int

isinstance(a,str)  # 判断类型
isinstance(a,(int,str,float))  # 判断a是否在后面元组三种类型中，返回bool型

# 对象的三个特征 id、value、type
# is,==,isinstance