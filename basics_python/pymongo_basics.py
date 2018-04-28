# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 下午6:31
# @Author  : Sulong
# @File    : pymongo_basics.py
# @Software: PyCharm
import pymongo

'''
使用pymongo 操作MongoDB数据库
'''


# 1.连接 数据库 获取 集合对象
def link_mongo():
	# 连接数据库服务器,获取客户端对象
	client = pymongo.MongoClient('localhost', 27017)
	# 获取数据库对象
	db = client.db  # client['zlydata']
	# 用户
	# db.authenticate("root", "sulong")
	# 获取集合对象
	collection = db.users
	return collection


def init_mongo():
	db = link_mongo()
	tom = {'name': 'Tom', 'age': 18, 'sex': '男', 'hobbies': ['吃饭', '睡觉', '打豆豆']}
	alice = {'name': 'Alice', 'age': 19, 'sex': '女', 'hobbies': ['读书', '跑步', '弹吉他']}
	tom_id = db.insert(tom)
	alice_id = db.insert(alice)
	return tom_id, alice_id


def find_mongo():
	db = link_mongo()
	bson = db.find()
	'''
	条件查询：
	$ne：不等于(not equal)
    $gt：大于(greater than)
    $lt：小于(less than)
    $lte：小于等于(less than equal)
    $gte：大于等于(greater than equal)
    $or:   or
    $in:  in
    $nin: not in 
    None: 查讯字段是否存在 {'name':None}
    $regex: 正则
    limit:  用查询出的bson  bson.sort({}).limit(n)

	'''
	# 用字典指定获取字段
	# bson = db.find({},{'name':True})

	# 获取文档个数
	count = db.count()
	print(count)
	for i in bson:
		print(i)


def update_mongo():
	db = db = link_mongo()
	#  更新操作 只会更新单个文档
	db.update({'name': 'Alice'}, {'$set': {'hobbies': ['向Alice学习读书', '跟Alice一起跑步', '向Alice学习弹吉他']}})


# 不建议做物理删除
def delete_mongo():
	db = link_mongo()
	# db.remove()
	db.remove({'name': 'Tom'})


if __name__ == '__main__':
	find_mongo()
