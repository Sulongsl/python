# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 上午10:41
# @Author  : Sulong
# @File    : function_key_word.py

# 定义函数中的关键字

# @Software: PyCharm

# 1.默认参数
# 在定义函数时 直接给定
def enroll(name,age,city='BeiJing'):
	print("name",name)
	print("age",age)
	print("city",city)

# enroll("Tom",44)

# 这里是个坑  默认函数也是一个变量 在函数定义出的时候就已经被定义出来了
def down(L=[]):
	L.append("END")
	return L
# L这个函数看似是给传入的一个list添加元素
# print(down([1,2,3]))
print(down())  #['END']     函数返回的L是   ['END']
print(down())  #['END', 'END']    无参时 默认传入L  然而L已经被定义 所以第二个返回的 L 是['END', 'END']
print(down())  #['END', 'END', 'END']  t同理

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
# str 和 None 对象都是不可变对象 该内部数据结构不会变
print("**************************************************")


# 2.可变参数
def add_n(*n): # 参数 n 接收的是一个tuple元组  (5),(8,9)
	sum = 0
	for s in n:
		sum = sum+s
	return sum
print(add_n(5,6,9))
# 当有一个List 或  tuple 时  可以直接传入
LL = [9,6,8,43,21,8]
print(add_n(*LL))
print("**************************************************")


#3.关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kr):
	print("name:",name,"age:",age,"other:",kr)
person("tony",88,city="BeiJing")

extra = {'city': 'Beijing', 'job': 'Engineer'} # 同理 可直接传入dict
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kr参数，kr将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kr的改动不会影响到函数外的extra
person('Jack',99,**extra)
print("**************************************************")

# 4.命名关键字参数
# 限制关键字参数的名字，就 用命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person_1(name,age,*,city,job): # 只接收 附加key w为 city 和job 的 dict
	print(name,age,city,job)

# 5.参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def more(a,b,c='222',*d,**ee):
	print(a,b,c)
	sum = 0
	for i in d:
		sum=sum+i
	print(d)
	print(sum)
	print(ee)
more(1,2,"dddd",2,3,ee={'x':3})
print("**************************************************")

tuple = (2,3,4,5)
dict = {'x':3,'y':'&'}
more(*tuple)
print("**************************************************")

more(*tuple,**dict)
