#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 下午8:01
# @Author  : Sulong
# @File    : osBasics.py

#  python 3 os模块

# @Software: PyCharm

import os
print("操作系统类型："+ os.name) # 操作系统类型
print("详细的系统信息在这里:%s"% str(os.uname())) # 详细的系统信息
# print(os.environ) # 获取系统环境变量
# print(str(os.environ.get('PYTHONUNBUFFERED'))) # 获取系统中某个环境变量的值
print(os.path.abspath('.')) # 查看当前位置的绝对路径

# os.path.join()  用来拼接路径; os.path.split() 是把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名  因为不同的操作系统路径表示是不同的建议 以此调用
# print(os.path.join('/Users/sulong/dataStructure-for-python/basicsPython', 'testdir')) # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.mkdir('/Users/sulong/dataStructure-for-python/basicsPython/testdir')   # 创建这个路径目录 存在则抛出异常
# os.rmdir('/Users/sulong/dataStructure-for-python/basicsPython/testdir')   # 删除这个路径目录 不存在则抛出异常
# print(os.path.splitext('/Users/sulong/Documents/学无止境/shellSort.py')) # 获取文件扩展名 有点鸡肋
# os.rename('/Users/sulong/dataStructure-for-python/basicsPython/tesyyy.py','shellSort.py')  # 将改名文件移动至当前目录中


