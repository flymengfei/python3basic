# -*- coding: utf-8 -*-

import t
print(t.sys.path)

# 包和模块是不会重复导入的

# 避免循环导入
# 当你导入一个模块时，就会运行该模块的源代码
# 入口文件的概念
