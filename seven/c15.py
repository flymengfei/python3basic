# -*- coding: utf-8 -*-

import seven.t.t1.c9

# 代码调用路径
print('~~~~~~~~~~~C15~~~~~~~~~~')
print('name:'+__name__)
print('package:'+(__package__ or '当前模块不属于任何包'))
print('doc:'+(__doc__ or '当前模块没有文档注释'))
print('file:'+__file__)

# a = 5>3?1:0
# 作为一个普通的模块必须有包
# python -m seven.c15