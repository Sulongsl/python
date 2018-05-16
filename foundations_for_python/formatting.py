# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 下午8:17
# @Author  : Sulong
# @File    : formatting.py


'''Python格式化输出'''

# @Software: PyCharm

# 1. 打印字符串
print ("字符串用 %s。","His name is %s,age is %s"%("Aviad",88))

# 2.打印整数 %d表示的不是整数自动截取 不做舍入
print ("整数用 %d。","His name is %s,age is %d"%("Aviad",88.54))

# 3.打印浮点数
print ("浮点数用 %f。","His name is %s,age is %d,money have %f"%("Aviad",99.999,88.54))

# 4.打印浮点数（指定保留小数点位数）
print ("浮点数指定保留小数点位数 %.nf.","His height is %.4f m"%(1.83))

# 5.指定占位符宽度
print ("指定占位符宽度用 %ns/d/f 。","Name:%10s Age:%8d Height:%8.2f"%("Aviad",25,1.83))

#6.科学计数法
print("科学计数法用 .2e 。",format(0.0015,'.2e'))

