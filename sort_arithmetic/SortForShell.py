# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 下午6:10
# @Author  : Sulong
# @File    : SortForShell.py
# @Software: PyCharm

# 希尔排序的算法思想：将待排序数组按照步长gap进行分组，然后将每组的元素利用直接插入排序的方法进行排序；
# 每次将gap折半减小，循环上述操作；当gap=1时，利用直接插入，完成排序
def instert_shell(L):
	# 定义初始值
	gap = (int)(len(L)/2)
	# 依次改变gap值 对列表分组
	while (gap >=1):
		# 直接插入排序
		# 从gap开始
		for x in range(gap,len(L)):
			# range(x-gap,-1,-gap):从x-gap开始与选定元素开始倒序比较，每个比较元素之间间隔gap
			for i in range(x-gap,-1,-gap):
				if L[i] > L[i+gap]:
					temp = L[i+gap]
					L[i+gap] = L[i]
					L[i] = temp
		# while循环条件折半
		gap = (int)(gap/2)

if __name__ == '__main__':
	List = [2,1,4,9,7,6,0,3,5,8,10]
	instert_shell(List)
	List1 =[2,1,4,9,7,6,0,3,5,8,10,11]
	for s in List:
		print(List[s])