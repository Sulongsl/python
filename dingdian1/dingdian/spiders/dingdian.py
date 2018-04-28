# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 下午6:09
# @Author  : Sulong
# @File    : dingdian.py
# @Software: PyCharm
from scrapy.http import Request  # 一个单独的ruquest 需要跟进Url时用到
from bs4 import BeautifulSoup
from dingdian.dingdian.items import DingdianItem
import scrapy

'''

http://www.23us.so/list/1_1.html 玄幻魔法
http://www.23us.so/list/1_200.html 玄幻魔法分类下 第 200页
http://www.23us.so/list/2_1.html 武侠修真
http://www.23us.so/list/3_1.html 都市言情
http://www.23us.so/list/4_1.html 历史军事
http://www.23us.so/list/5_1.html 网友竞技
http://www.23us.so/list/6_1.html 科幻小说
http://www.23us.so/list/7_1.html 恐怖灵异
http://www.23us.so/list/8_1.html 女生小说
http://www.23us.so/list/9_1.html 其他小说
'''


# 继承自scrapy.Spider
class Myspider(scrapy.Spider):
	# name就是我们在entrypoint.py文件中的第三个参数！
	name = 'dingdian'
	allowed_domains = ['23us.so']
	bash_url = 'http://www.23us.so/list/'
	bashurl = '.html'

	def start_requests(self):
		for i in range(1, 10):
			url = self.bash_url + str(i) + '_1' + self.bashurl
			# 生成器
			yield Request(url, self.parse)

		# 返回的response作为参数传递给self.parse