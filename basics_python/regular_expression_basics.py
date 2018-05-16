# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 下午7:46
# @Author  : Sulong
# @File    : regular_expression.py

# python3 正则表达式
# 		  re模块

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000

# @Software: PyCharm

import re

'''正则表达式是一个处理字符串强大的工具，在提供正则表达式的语言中 语法都是一样的
	匹配流程：
		1. 正则表达式引 将 正则表达式文本 编译为 正则表达式对象 （该对象中 包含如何进行匹配的信息）
		2. 正则表达式对象 匹配 需要匹配的文本 输出匹配结果 
			一旦有匹配不成功的字符则匹配失败
	贪婪模式与非贪婪模式：
		贪婪模式：总是尝试匹配尽可能多的字符；如 "ab" 匹配结果： "abbbc","abbb"
		非贪婪模式： 总是尝试匹配尽可能少的字符。
		
	re模块还提供了一个方法 escape(string)，用于将string中的正则表达式元字符如*/+/?等之前加上转义符再返回
	'''
'''一.re支持
   1.将正则表达式的字符串 编译 为 Pattern实例 
   2.使用 Pattern实例 处理文本并获得匹配结果（Match实例）
'''


def re_hello(re_str):
	# re.compile 将字符串形式的正则表达式编译为Pattern对象
	pattern = re.compile(r"hello")
	match = pattern.match(re_str)
	if match:
		yield match.group()


'''re.compile(strPattern[, flag]):
    第二个参数 flag 是匹配模式 如 re.I 忽略大小写 re.M 多行模式 改变 '^'和'$'的行为  可以使用按位或运算符'|'表示同时生效
    re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
	M(MULTILINE): 多行模式，       改变'^'和'$'的行为
	S(DOTALL):    点任意匹配模式，  改变'.'的行为
	L(LOCALE):    使预定字符类      \w \W \b \B \s \S 取决于当前区域设定
	U(UNICODE):   使预定字符类      \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
	X(VERBOSE):   详细模式。        这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释
    '''


def re_match():
	m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
	return m


'''二.Match
	Match对象是一次匹配的结果
	属性：
	1.string: 匹配时使用的文本
	2.re: 匹配时使用的Pattern对象
	3.pos : 文本中正则表达式开始搜索的索引
	4.endpos： 文本中正则表达式 结束搜索的索引 
	5.lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
	6.lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
	
	方法：
	1.group([group1, …]): 获得一个或多个分组截获的字符串，指定多个参数时将以元组形式返回
'''
if __name__ == '__main__':
	a = re_hello('hello world,hello')
	print(type(a))
	b = a.__next__()
	print(b)
	print("*****" * 10)
	m = re_match()
	print("m.string", m.string)
	print("m.re",m.re)
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
# m = re.match(r'(\d{3})-(\d{3,8})$', '010-987654')
#
# print(m.group(0))
# print(m.group(1))
# # 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
#
#
# a = r'ABC\\-001'
# print(a)
# # match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
# name = input("What is your year?")
# names = int(name)
# print(type(names))
# if re.match(r'[a-zA-Z]', name):
# 	print('ok')
# else:
# 	print('failed')
#
# # 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
#
# # 1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错R；
#
# # 2.用编译后的正则表达式去匹配字符串。
#
# # 验证Email地址的正则表达式
# e1 = r'someone@gmail.com'
# e2 = r'billgates@microsoft.com'
#
#
# def emial(s):
# 	re_email = re.compile(r'[\w]{0,20}@[\w]{0,20}.[com]')
# 	if re.match(re_email, s):
# 		print('ok')
# 	# print(re_email.match(s).group())  未定义如何分组
# 	else:
# 		print('failed')
#
#
# emial(e2)
