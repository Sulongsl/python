# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 上午10:20
# @Author  : Sulong
# @File    : with_key_word.py

# 浅析 with 关键字
# https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/
# @Software: PyCharm

# with 语句适用于
		# 对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。

# 上下文管理协议（Context Management Protocol）：包含方法 __enter__() 和 __exit__()，
# 支持该协议的对象要实现这两个方法。

# 上下文管理协议（Context Management Protocol）：包含方法 __enter__() 和 __exit__()，
# 支持该协议的对象要实现这两个方法。