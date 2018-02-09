# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 下午3:30
# @Author  : Sulong
# @File    : LinkedList.py
# @Software: PyCharm

# 用python写一个单链表
#
# 创建单链表中每个值的元素 包含值和指向
class Node(object):
	def __init__(self, data, next):
		self.data = data
		self.next = next


# 链表的实现
class LianBiao(object):
	def __init__(self):
		self.root = None

	# 获取链表大小
	def size(self):
		con = 0
		if self.root == None:
			return con
		else:
			conself = self.root
			while conself != None:
				con = con + 1
				conself = conself.next
			return con

	# 给单链表添加元素节点
	def addNode(self, data):
		# 为空链表
		if self.root == None:
			self.root = Node(data=data, next=None)
			return self.root
		# 不为空 需要遍历到尾部节点，进行链表增加操作
		else:
			endData = self.root
			# 寻找最后一个元素
			while endData.next != None:
				endData = endData.next
			endData.next = Node(data=data, next=None)
			return self.root

	# 给链表末增加元素 底层调用
	def addEndNode(self, value):
		self.addNode(data=value)

	# 给链表首增加元素
	def prepend(self, value):
		if self.root == None:
			self.root = Node(data=value, next=None)
		else:
			newroot = Node(data=value, next=None)
			# 首元素增加next
			newroot.next = self.root

			self.root = newroot

	# 给链表指定位置增加元素
	def insert(self, index, value):
		# 链表为空无法处理 应该走 给链表首增加元素的方法
		if self.root == None:
			return
		if index < 0 or index > self.size():
			print("index非法")
			return
		# 如果index正好比当前链表长度大一，则添加在尾部即可
		elif index == self.size() + 1:
			self.addNode(data=value)
		else:
			conNum = 2
			pre = self.root
			prenext = self.root.next
			while prenext != None:
				# ##
				if conNum == index:
					temp = Node(data=value, next=None)
					pre.next = temp
					temp.next = prenext
					break
				else:
					conNum = conNum + 1
					pre = prenext
					prenext = prenext.next
				# Node 的 next 是一个Node 指针

	# 删除指定位置上的节点
	def delNode(self, index):
		if self.root == None:
			return
		if index < 0 or index > self.size():
			print("index非法")
			return
		# 删除第1个元素 则
		if index==1:
			self.root=self.root.next
		else:
			pre=self.root
			cursor=pre.next
			counter=2
			while cursor!=None:
				if index==counter:
					print("can be here!")
					pre.next=cursor.next
					break
				else:
					pre=cursor
					cursor=cursor.next
					counter+=1
	# 删除值为value的链表节点元素
	def delValue(self,value):
		if self.root == None:
			return
		# 对第一个 节点元素 做匹配 if true 替换第一个元素为第二个节点元素
		if self.root.data == value:
			self.root = self.root.next
		# else
		else:
			pre = self.root
			cursor =pre.next
			while cursor!=None:
				if cursor.data ==value:
					pre.next=cursor.next
					cursor = cursor.next
					continue
				else:
					pre =cursor
					cursor=cursor.next

	# 判断链表是否为空
	def isempty(self):
		if self.root.data == None or self.size()==0:
			return True
		else:
			return False

	# 删除 链表及其内部所有元素 如上判空 =None
	# 单链表的逆序实现
	def reverse(self):
		if self.root is None:
			return
		if self.size()==1:
			return
		else:
			pre = None
			cursor = self.root
			while cursor is not None:
				# 实现逆序
				post = cursor.next
				cursor.next=pre
				pre = cursor
				cursor=post
			# 把逆序后的头结点赋值给root，否则无法正确显示
			self.root=pre
	# 删除链表中的重复元素
	def delDuplecate(self):
		dic ={}
		if self.root==None:
			return
		if self.size()==1:
			return
		pre = self.root
		cursor = pre.next
		temp=self.root
		while temp !=None:
			dic[str(temp.data)]=0
			temp =temp.next
		temp = None






	# 删除值为value的链表



if __name__ == '__main__':
	lianbiao = LianBiao()
	print(lianbiao.size())