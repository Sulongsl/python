# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 下午4:10
# @Author  : Sulong
# @File    : sortBubble.py
# @Software: PyCharm

# 冒泡排序
# 1.将序列当中的左右元素，依次比较，保证右边的元素始终大于左边的元素；
#  （第一轮结束后，序列最后一个元素一定是当前序列的最大值；）
# 2.对序列当中剩下的n-1个元素再次执行步骤1。
# 3.对于长度为n的序列，一共需要执行n-1轮比较
#  （利用while循环可以减少执行次数）

def bubble_sort(L):
	length = len(L)
	for x in range(1,length):
		for i in range(0,length -x):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = temp

if __name__ == '__main__':
	List = [2,5,4,7,9,2673,44,726,145,741,486,6,10]
	bubble_sort(List)
	for x in List:
		print(x)