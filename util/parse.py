# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 上午10:01
# @Author  : Sulong
# @File    : parse.py
# 获取一个模块或者类中的所有方法及参数列表
# @Software: PyCharm
import re

def parse(filepath,repattern):
	with open(filepath,'rb') as f:
		lines=f.readlines()
	# 解析正则表达式
	rep=re.compile(repattern)
	result=[]
	for line in lines:
		res=re.findall(rep,str(line))
		# print("{}的匹配结果{}".format(str(line), res))
		if len(res)!=0 or res is not None:
			result.append(res)
		else:
			continue
	return [item for item in result if item !=[]]

if __name__=='__main__':
	repattern = "def (.[^_0-9]+\(.*?\)):"
	filepath = '/Users/sulong/dataStructure-for-python/dataStructure/LinkedList.py'
	result = parse(filepath, repattern)
	for item in result:
		print(str(item))