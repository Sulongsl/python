# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 下午6:15
# @Author  : Sulong
# @File    : sql.py
# @Software: PyCharm

import pymysql
from dingdian.dingdian import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = pymysql.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor()

class Sql:
	# 关于@classmethod这个是一个修饰符；作用是我们不需要初始化类就可以直接调用类中的函数使用
	@classmethod
	def inster_dd_name(cls,xs_name,xs_aurhor,category,name_id):
		sql = 'INSERT INTO dd_name(`xs_name`,`xs_author`,`category`,`name_id`) VALUES (%(xs_name)s,%(xs_author)s,%(category)s,%(name_id)s)'
		value ={
			'xs_name':xs_name,
		    'xs_author':xs_aurhor,
		    'category':category,
		    'name_id':name_id}
		# 写个插入
		cur.execute(sql,value)
		cnx.close()
	@classmethod
	# 查找name_id这个字段，如果存在则会返回1
	# 不存在则会返回0
	def select_name(cls,name_id):
		sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
		value = {
			'name_id': name_id
		}
		cur.execute(sql,value)
		return cur.fetchall()[0]

# if __name__ == '__main__':
# 	a = Sql
# 	a.inster_dd_name('sss','sss','sss','sss')