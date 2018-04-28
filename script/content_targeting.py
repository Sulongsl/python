# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 上午10:14
# @Author  : Sulong
# @File    : content_targeting.py
# @Software: PyCharm

'''
朱丽叶健康：
  内容定向表 对cms文章(物理删除) 做比对 检索已删除文章 删 除 更改 contentTargeting表中 articleExist 为 false
  												未删除则不做任何操作
'''
# from pymongo import MongoClient
from pymongo import MongoClient
import requests
import socket

def link_mongo(name):
	if name == 'test':
		client = MongoClient('10.162.201.58', 3717)
		db = client.zlydata  # client['zlydata']
		db.authenticate("opadmin", "opadmin_2016")
		collection = db.contentTargeting
		return collection
	if name == 'official':
		client = MongoClient('10.162.201.58', 3728)
		db = client.zlydata  # client['zlydata']
		db.authenticate("opadmin", "MLN8v22BXG9YOCq7")
		collection = db.contentTargeting
		return collection

# 获取contentTargeting list
def get_content_list():
	contentTargeting = []
	db = link_mongo('test')
	for i in db.find({'isDeleted': False, 'articleExist': True}):
		# print(i['_id'])
		contentTargeting.append(i['articleId'])
	return contentTargeting

# 根据获取contentTargetinglist 获取 cms list
def get_cms_list(list,name):
	cms_list=[]
	if name =='test':
		cms_list = requests.get(url='http://articles_exists()', params={list})  # 带参数的GET请求
		return cms_list
	if name =='official':
		cms_list = requests.get(url='http://articles_exists()', params={list})  # 带参数的GET请求
		return cms_list

if __name__ == '__main__':
	link_mongo('test')
	# print(l)
	# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# host = '10.174.89.71'
	# port = 8181
	# conn = s.connect((host,port))
	# print('connected to server %s' % host)
	# # msg = s.recv(1024)
	# conn.use_service(['add'])
	# err, res = conn.add(1, 2)
	# print('result: %s' % str(res))
	# conn.disconnect()
	# print('disconnected from server %s' % host)
	# s.close()