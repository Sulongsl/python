# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 下午3:46
# @Author  : Sulong
# @File    : dateTimeBasics.py

# python3 datetime模块

# @Software: PyCharm

import datetime,time

# 1.date 对象
  # 构成 year 年份 ，mouth月份 ， day日期 构成
date = datetime.date.today()
print(date)
print(date.year) # .mouth  .day
print("***********************************************")

# 2. 用于比较日期大小的方法
date2017 = datetime.date(2017,3,1)
date2018 = datetime.date(2018,3,15)

if date2017.__eq__(date2018):
	print("__eq__ 比较两个日期是否相等",date2018.__eq__(date2017))
else:
	print(date2017.__eq__(date2018))
# 比较月份
if date2017.month.__eq__(date2018.month):
	print("__eq__ 比较两个日期是否相等",date2018.month.__eq__(date2017.month))
else:
	print(date2017.__eq__(date2018))


 # 同理   __ge__  大于等于
 #       __gt__   大于
	#    __le__   小于等于
	#    __lt__   小于
	#    __ne__   不等于

print("***********************************************")

# 3. 比较相差几天的方法

# 返回值类型为datetime.timedelta
print(date2018.__sub__(date2017))

# 4.常用方法与属性

# 4.1 fromtimestamp(...)：根据给定的时间戮，返回一个date对象
# 获取当前 时间戳
time.time()
print(time.time())  # 1523960234.48987
# 输出当前日期
print(datetime.date.fromtimestamp(time.time()))
# 4.2 today(...)  获取当前日期
print(datetime.date.today())
# 4.3 日期对象 转化为 固定格式的 字符串对象
print(date2017.__format__('%Y-%m-%d'))
print(date2017.__format__('%Y/%m/%d'))
print(date2017.__format__('%y/%m/%d'))
#  普通转化为字符串
print(date2017.__str__())

# 获得ctime样式的格式
print(date2018.ctime())

# 5. time类
# time类由hour小时、minute分钟、second秒、microsecond毫秒和tzinfo五部分组成

# 比较时间大小与与日期类相似

# 5.1 时间的字符串输出
# 定义时间
time_now = datetime.time(12,59,59,899)
print(time_now.__str__())

print("***********************************************")

# 6.datetime类
date_time_now = datetime.datetime.now()
print(date_time_now)
# date(…)：返回datetime对象的日期部分
print(date_time_now.date())
# time(…)：返回datetime对象的时间部分：
print(date_time_now.time())
# combine(…)：将一个date对象和一个time对象合并生成一个datetime对象
print(datetime.datetime.combine(date2018,time_now))
# now(…)：返回当前日期时间的datetime对象
# strptime(…)：根据string, format 2个参数，返回一个对应的datetime对象：
cc = datetime.datetime.strptime('2017-3-22 15:25','%Y-%m-%d %H:%M')
print(cc)

# str 类型 转化为date 对象 与 time对象  以及 datetime对象


# if __name__ == '__main__':
	# print(getyesterday())
