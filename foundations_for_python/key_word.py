#!/usr/local/bin/python2.7

# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 下午2:41
# @Author  : Sulong
# @File    : Keyword.py
# python 关键字用法
# @Software: PyCharm

# python 常用關鍵字
# and	not or else if pass import print
# del from while as elif global with assert yield break except class exec in raise contiue finally is return def for lambda try

# 1.and or
# 逻辑滚关系用词
# 2.del
# 删除变量 （接触变量对 值 的引用）
list = [1, 2, 3]
# 包含list[0],list[1],list[2]
# 并不包含数字1,2,3
# 3.from
from sys import argv
# 从sys中导入argv
from sys import *


# 将sys中所有东西都导入
# 4.golbal
# 声明全局变量 但 单个函数中出现同一变量名时 在单个函数中为局部变量
# 5.with
# with 用来处理异常
# with open("/Users/sulong/dataStructure-for-python/foundationsForPython/test.txt") as file:
# 	data = file.read()
# 6.assert
# 判定一个boolean值 是否为真
# 其布尔值必须为真的判定，如果发生异常就说明表达示为假。
# 7.yield
# yield的意思是生产，返回了一个生成器对象，每个生成器只能使用一次 用于迭代
def hhh(n):
	while n > 0:
		print("before yield")
		yield n  # 生成值 n
		n -= 1
		print('after yield')


c = hhh(5)  # 生成器 只有在执行__next__() 才会调用 执行里面的语句
# print(c.__next__()) # 此处输出5  第一次调用__next__方法时，并不会打印"after yield"
# 每次调用__next__()方法时，count函数会运行到语句yield n处为止
# print(c.__next__()) # 此处输出4

# 当 执行至无可迭代值时 程序会报错 一般使用for循环
# for i in hhh(5):
# 	print(i)
# 8.break  contiue
# Python break语句用来终止循环，用在while和for循环中！！直接跳出 整个 循环
# 嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码
# for letter in 'python':
# 	if letter == 'h':
# 		break
# 	print(u'当前字母为：',letter)

var = 10
# while var > 0:
# 	print(u'当前字母：',var)
# 	var = var -1
# 	if var ==5:
# 		break
# print('bye')

# continue是跳出当前循环
# while var > 0:
# 	# print(u'当前字母：', var)
# 	var = var - 1
# 	if var == 5:
# 		continue
# 	print(u'当前字母：', var)
# print('bye2')
# 9.try except finally
# try:
# <语句>        #运行别的代码
# except <名字>：
# <语句>        #如果在try部份引发了'name'异常
# except <名字>，<数据>:
# <语句>        #如果引发了'name'异常，获得附加的数据
# else:
# <语句>        #如果没有异常发生
# 10.raise
# 触发异常
# raise 触发异常后，后面的代码就不会再执行 但仍会执行 try except中的输出
# try:
# 	s = None
# 	if s is None:
# 		print("s will None") # 执行
# 		raise NameError
# 		print("s is None") # 该句并不会输出
#
# 	print(len(s))  # 该句并不会输出
# except:
# 	print("the None not have len")
# 11.exec eval execfile
# exec 用来执行储存在字符串或文件中的Python 语句 将字符串str当成有效的python代码来执行
# eval 与 execfile是python内置函数
# eval(str[globals[locals]])  将字符串str当成有效的python表达式来求值
# execfile(filename)函数可以用来执行文件
# 12. lambda   filte   map   reduce
# lambda 定义匿名函数 函数速写 他可以直接作为 列表活字典中的元素
inffo = [lambda  a:a**3,lambda b:b**3]