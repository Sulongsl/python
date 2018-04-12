# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 下午2:36
# @Author  : Sulong
# @File    : sortSelect.py
# @Software: PyCharm

# 简单选择排序
# 思想 ： 比较 交换
# 1.从待排序序列中，找到关键字最小的元素；
# 2.如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换；s
# 3.从余下的 N - 1 个元素中，找出关键字最小的元素，重复(1)、(2)步，直到排序结束。
def select_sort(L):
	for x in range(0,len(L)):
		mins = L[x]
		for i in range(x+1,len(L)):
			if L[i] < mins:
				temp = L[i]
				L[i] = mins
				mins = temp
		L[x] = mins
if __name__ == '__main__':
	List = [2,5,4,7,9,2673,44,726,145,741,486,6,10]
	select_sort(List)
	for x in List:
		print(x)