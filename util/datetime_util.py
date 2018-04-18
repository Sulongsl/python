# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 下午6:45
# @Author  : Sulong
# @File    : datetime_util.py
# @Software: PyCharm

# 日常工具类

import datetime, time  # 传入int 获取当天int时的13位时间戳 1521648000


# 24小时制
def get_int_time(x):
	a = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:00:00" % x
	timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
	timeStamp = int(time.mktime(timeArray) * 1000)
	return timeStamp


# 获取 昨天 当前日期的时间  时单位
def get_yesterday():
	now_time = datetime.datetime.now()
	yes_time = now_time + datetime.timedelta(days=-1)
	yes_time_nyr = yes_time.strftime('%Y-%m-%d %18:%000:%000')
	timeArray = time.strptime(yes_time_nyr, "%Y-%m-%d %H:%M:%S")
	timestamp = int(time.mktime(timeArray) * 1000)
	# print (timestamp)
	return timestamp


# 获取当前日期和时间 %Y-%m-%d %H:%M:%S
def get_now_datetime():
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


# datetime对象转换为String
def datetime_toString(dt):
	return dt.structtime("%Y-%m-%d-%H")


# 字符串转为 datetime
def string_toDatetime(string):
	return datetime.strptime(string, "%Y-%m-%d-%H")


# 把字符串转成时间戳形式
def string_toTimestamp(strTime):
	return time.mktime(string_toDatetime(strTime).timetuple())


# 把时间戳转成字符串形式
def timestamp_toString(stamp):
	return time.strftime("%Y-%m-%d", time.localtime(stamp))


# 把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTim):
	return time.mktime(dateTim.timetuple())

