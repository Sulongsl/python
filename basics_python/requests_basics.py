# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 下午7:56
# @Author  : Sulong
# @File    : requests_basics.py

# python3 requests模块

# @Software: PyCharm

import requests

# HTTP请求：GET、POST、PUT、DELETE、HEAD、OPTIONS

# r = requests.get(url ='http://www.itwhy.org')
# print(r.status_code)
r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
print(r.url)
print(r.text)   #打印解码后的返回数据
