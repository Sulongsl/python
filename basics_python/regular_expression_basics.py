# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 下午7:46
# @Author  : Sulong
# @File    : regular_expression.py

# python3 正则表达式
# 		  re模块

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000

# @Software: PyCharm

import re
# 判断一个字符串是否是合法的Email

# 1. 字符表示
#     \d可以匹配一个数字
#     \w可以匹配一个字母或数字
# 	  \s可以匹配一个空格 包括 Tab等空白符
# 	  '\'转义
# eg：
# '00\d'可以匹配'007'，但无法匹配'00A'；
# '\d\d\d'可以匹配'010'；
# '\w\w\d'可以匹配'py3'；
# .可以匹配任意字
# 2. 字符长度
# 	  *表示任意个字符（包括0个
#	  +表示至少一个字符
# 	  ?表示0个或1个字符
# 	  {n}表示n个字符
# 	  {n,m}表示n-m个字符
# 3.
#  	  $表示行的结束  \d$表示必须以数字结束
#  	  ^表示行的开头  ^\d表示必须以数字开头
#  	  [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
# 4.正则匹配默认是贪婪匹配 匹配尽可能多的字符

# 提取的分组（Group）

# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
m = re.match(r'(\d{3})-(\d{3,8})$','010-987654')

print(m.group(0))
print(m.group(1))
# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串


a = r'ABC\\-001'
print(a)
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
name = input("What is your name?")
names = int(name)
print(type(names))
if re.match(r'[a-zA-Z]', name):
    print('ok')
else:
    print('failed')

# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：

# 1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错R；

# 2.用编译后的正则表达式去匹配字符串。

# 验证Email地址的正则表达式
e1 =r'someone@gmail.com'
e2 =r'billgates@microsoft.com'

def emial(s):
	re_email = re.compile(r'[\w]{0,20}@[\w]{0,20}.[com]')
	if re.match(re_email, s):
		print('ok')
		# print(re_email.match(s).group())  未定义如何分组
	else:
		print('failed')
emial(e2)