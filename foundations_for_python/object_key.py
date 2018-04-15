# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 下午7:44
# @Author  : Sulong
# @File    : object_key.py

# 面向对象编程
# 继承，多态 多重继承，枚举类
# @Software: PyCharm
# 1.类与实例

class Student(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def course(self):
		pass

	def introduce(self):
		print("我叫%s,今年%s岁" % (self.name, self.age))


student_1 = Student("Tom", 16)
# student_1.name='Tom'
print(student_1.name, student_1.age)
student_1.introduce()
print("**************************************************")


# 2.数据封装
# 实例本身存在的属性 不在外部的函数去访问  直接在类的内部定义访问数据的函数 --数据封装
def introduce_wai(student_1):
	print("外部函数调用;introduce_wai")
	print("我叫%s,今年%s岁" % (student_1.name, student_1.age))


# print ("His name is %s"%("Aviad"))
introduce_wai(student_1)
print("类的内部调用; introduce")
student_1.introduce()
print("**************************************************")

# 3.访问限制
# 上述类 Student 中的 name age 可以访问/ 更改  作为一个类的属性 有时 不需要该规则 或 不允许直接访问或改动  可以把属性的名称前加上两个下划线__ 就变成了类的 私有变量 只有内部可以访问 外部不允许访问
student_2 = Student("Tony", 14)
print(student_2.name)
student_2.name = 'Tony2'
print(student_2.name)


# 定义一个 teacher类
class Teacher(object):
	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	def introduce(self):
		print("师名%s,贵庚%s" % (self.__name, self.__age))

	# 当类的属性不允许访问时 则类内部需要给出 get set 方法  原因是 在方法中，可以对参数做检查，避免传入无效的参数
	def get_name(self):
		return self.__name

	def get_age(self):
		return self.__age

	def set__name(self, name):
		self.__name = name

	def set__age(self, age):
		if 0 <= age <= 100:
			self.__age = age
		else:
			raise ValueError('bad age')


techer_1 = Teacher("汉文", 66)
# 对techer_1 的属性做更改
try:
	# print(techer_1.age)
	# 不允许访问可以更改  更改后可以访问  ？ 还是 换了一个对象
	# 更改的是这个实例的 属性 并不是 同一个变量 而是外部代码给对象实例新增了一个age变量
	techer_1.age = 67
	print(techer_1.age)
except:
	print("出错！！！")
print(techer_1.get_age())
print("**************************************************")


# 4.继承与多态
class Animal(object):
	def run(self):
		print("Animal is runing")


# 两个雷继承Animal
class Dog(Animal):
	# 重写
	def run(self):
		print("Dog is runing")


class Cat(Animal):
	# 自雷的run()方法 覆盖 了父类的run()，在代码运行的时候，总是会调用子类的run()
	def run(self):
		print("Cat is runing")


dog = Dog()
dog.run()
cat = Cat()
cat.run()
animal = Animal()
# 判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
# Dog可以看成Animal，但Animal不可以看成Dog
print(isinstance(animal, Dog))


def run_twice(animal):
	animal.run()
	animal.run()


run_twice(animal)
run_twice(dog)


# 定义一个带有run的类  也可以传入run_twice  动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
class Run(object):
	def run(self):
		print("only runing")


run_twice(Run())
# type 获取对象类型
print(type(dog))
print(isinstance(dog, Animal))
# 获取对象的所有方法 和 属性 反会一个List
print(dir(dog))

print("**************************************************")

# 5.__slots__ 限制实例属性
# python 中是可以给实例绑定属性 和 方法

# 绑定属性
dog.sex = 1
print(dog.sex)


# 绑定方法
def charge_sex(self, sex):
	if sex != 1 and sex != 0:
		return ValueError('bad sex')
	elif sex == 1:
		self.sex = 0
	else:
		self.sex = 1
	print(self.sex)


# 绑定 方法
from types import MethodType

dog.ch_sex = MethodType(charge_sex, dog)
dog.ch_sex(1)


# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Student(object):
	__slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

print("**************************************************")



# 6.枚举类

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
# @unique装饰器 检查保证没有重复值
#