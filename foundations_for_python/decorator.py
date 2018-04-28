# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 上午11:17
# @Author  : Sulong
# @File    : decorator.py
# @Software: PyCharm

import time

'''
# 装饰器用来增强 函数 的功能  但是不改变其原有的结构与功能 。 在代码运行期间 动态的添加功能 称为 装饰器
# 本质上，装饰器就是一个返回函数的高阶函数
'''

def log(func):
	def wrapper(*args, **kw):
		print('传入函数为: %s' % func.__name__)
		return func(*args, **kw)
	return wrapper

# *args 传入可变任意参数 tuple
# **kw  传入 关键字参数  dict
#
# def jump():
# 	print('我正在蹦跶')

def rainbow(main):   # 传入一个函数作为参数 ra(main())
	def make_rainbow(*args,**kwargs):
		print('你被挂上了彩虹：%s'%(main.__name__))
		return main(*args,**kwargs)
	return make_rainbow

@rainbow
def jump():
	print('我正在蹦跶')

# now


# 用于任何函数上，并打印该函数的执行时间：
def log_time(func):
	def aaa(*args, **kwargs):
		time1 = time.time()
		func(*args, **kwargs)
		time2 = time.time()
		time3 = time2-time1
		return time3
	return aaa()




'''
迭代器
实现 迭代迭代器协议的 容器对象
注：
	访问者无需关注迭代器内部  仅需要通过 next() 方法  去取下一个内容
	不能随机访问 集合中的某个值 只能从头到尾访问
	访问到一半时 不能往回退
	便于循环较大的数据集合 节省内存
'''
a  = iter([1,2,3,4,5,555,666])


'''
生成器
一个函数调用时返回一个迭代器，那这个函数就叫做生成器
如果函数中包含yield语法，那这个函数就会变成生成器
'''
def create():
	yield 1
	yield 2
	print('sr')
	yield 3

# 使用 yield 书写一个斐波那契 函数
#1.常规版本
def fab(max):
	n,a,b = 0,0,1
	while n <max:
		print(b)
		a,b,=b,a+b
		n =n+1

from inspect import isgeneratorfunction

if __name__ == '__main__':
	print(isgeneratorfunction(fab))
	# 用于任何函数上，并打印该函数的执行时间：
# 	@log_time
# 	def bbb():
# 		print('begin')
# 		time.sleep(3)
# 		print('end')
#
# # 装饰器
# 	@log
# 	def now():
# 		print('2018.04.23 Even Liu going')
# 	# 迭代器
# 	print(a.__iter__())
# 	print(a.__next__())
# 	print(a.__next__())
# 	print(a.__next__())
# 	print(a.__next__())
# 	print(a.__next__())
# 	print(a.__next__())
# 	print(a.__next__())
#
# 	# 生成器
# 	ret = create()
# 	# print(ret)     <generator object create at 0x101925ca8>
# 	print(ret.__next__())
# 	print(ret.__next__())
# 	ret.close()