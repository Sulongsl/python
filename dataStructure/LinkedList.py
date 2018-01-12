# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 下午3:30
# @Author  : Sulong
# @File    : LinkedList.py
# @Software: PyCharm

# 用python写一个单链表
#
# 创建单链表中每个值的元素 包含值和指向
class Node(object):
	def __init__(self,data,next):
		self.data =data
		self.next =next

# 链表的实现
class LianBiao(object):
	def __init__(self):
		self.root = None

# 获取链表大小
	def size(self):
		con = 0
		if self.root ==None:
			return con
		else:
			conself = self.root
			while conself !=None:
				con = con+1
				conself = conself.next
			return con

	# 给单链表添加元素节点
	def addNode(self,data):
		# 为空链表
		if self.root ==None:
			self.root=Node(data=data,next=None)
			return self.root
		# 不为空 需要遍历到尾部节点，进行链表增加操作
		else:
			endData = self.root
			# 寻找最后一个元素
			while endData.next != None:
				endData = endData.next
			endData.next=Node(data=data,next=None)
			return self.root
	# 给链表末增加元素 底层调用
	def addEndNode(self,value):
		self.addNode(data=value)

	# 给链表首增加元素
	def prepend(self,value):
		if self.root == None:
			self.root = Node(data=value,next=None)
		else:
			newroot = Node(data=value,next=None)
			# 首元素增加next
			newroot.next= self.root

			self.root=newroot
	# 给链表指定位置增加元素
	def insert(self,index,value):
		# 链表为空无法处理
		if self.root ==None:
			return
		if index <0 or index> self.size():
			print("index非法")
			return
		# 如果index正好比当前链表长度大一，则添加在尾部即可
		elif index ==self.size()+1:
			self.addNode(data=value)
		else:
			conNum = 2
			pre = self.root
			prenext = self.root.next
			while prenext != None:
				# ##
				if conNum == index:
					temp = Node(data=value,next= None)
					pre.next = temp
					temp.next=prenext
					break
				else:
					conNum = conNum +1
					pre = prenext
					prenext = prenext.next
					# Node 的 next 也是一个Node 实例

