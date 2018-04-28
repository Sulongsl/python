# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 下午3:27
# @Author  : Sulong
# @File    : SortArithmetic.py
# @Software: PyCharm

# 直接插入
# 将数组中的所有元素 依次 与前面排序好的元素 相比较
# 如 选择元素 比 已排元素 小 则交换  知道全部元素比较完成
# 如 选择元素 比 已排元素 大 则进行下一个未排序元素 与全部元素比较
def insert_sort(L):
	# 遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
	# 0  < - 1 ---- len(L)
	for x in range(1,len(L)):
		# range(x-1,-1,-1) : 从x-1 倒循环 倒 0
		for i in range(x-1,-1,-1):
			if  L[i] > L[i+1]:
				temp = L[i+1]
				L[i+1] = L[i]
				L[i] = temp


if __name__ == '__main__':
	List=[2,5,4,7,9,2673,44,726,145,741,486,6,10]
	# 直接插入排序
	insert_sort(List)
	# for i in range(len(List)):
	# 	print(List[i])
	# range(len(List),-1,-1) 正常的List长度 为 0 ~ len(List)-1 写成这样会抛出异常
	for s in range(len(List)-1,-1,-1):
		print(List[s])
		# 函数返回的结果是一个整数序列的对象，而不是列表
	print(type(range(10)))
	for i in range(1,5):
		print(i)
# 知识点 python内置函数 range
# 语法 range(start,stop,step)
# start:计数从 start 开始。默认是从 0 开始   eg:range(5) = range(0,5)
# stop :计数到 stop 结束，但不包括 stop  	  eg:range(5) = [0,1,2,3,4] 没有5
# step :步长 默认为1 正序  -1 倒叙

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少
d = []
for a in range(1,5):
	for b in range(1,5):
		for c in range(1,5):
			if (a!=b) and (b!=c) and (a!=c):
				d.append([a,b,c])
print("总数量=" +str(len(d)))
print(d)

# def insertion2(L):
# 	for i in range(0,len(L)):
# 		for x in range()