# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 下午7:56
# @Author  : Sulong
# @File    : requests_basics.py

# python3 requests模块

# @Software: PyCharm

import requests
import urllib
import urllib3

# HTTP请求：GET、POST、PUT、DELETE、HEAD、OPTIONS

# r = requests.get(url ='http://www.itwhy.org')
# print(r)
url = 'articles_exists()'
data =['243644','243646']
# ip: 10.174
# .89
# .71
# port: 8181
# req = urllib3.Request(url = url,data =data)
# print(req)
# r = requests.get(url=url, article_ids=data)   #带参数的GET请求
# print(r.url)
# print(r.text)   #打印解码后的返回数据
print((85-72)/72)
# "His height is %.4f m"%(1.83)
print('%.3f'%((85-72)/72))