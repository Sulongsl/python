# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 下午2:49
# @Author  : Sulong
# @File    : demo.py
# @Software: PyCharm

a = [1,2,3,4]
a.append([5,6,7,8])
print(a)


# (1)会被python认为是int类型，所以必须是（1,）
# python单下划线和双下划线的作用和区别。
a = [1,0]
a_1 =[2 for i in range(3)]
print(a_1)
