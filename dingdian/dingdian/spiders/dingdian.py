# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 下午3:05
# @Author  : Sulong
# @File    : dingdian.py
# @Software: PyCharm

import scrapy
from bs4 import BeautifulSoup
from dingdian.dingdian.items import DingdianItem
from scrapy.http import Request  # 一个单独的ruquest 需要跟进Url时用到

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

	def parse(self, response):
		# print(response.text)
		max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
		bashurl = str(response.url)[:-7]
		for num in range(1, int(max_num) + 1):
			url = bashurl + '_' + str(num) + self.bashurl
			yield Request(url, callback=self.get_name)

	def get_name(self, response):
		tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
		for td in tds:
			novelname = td.find('a').get_text()
			novelurl = td.find('a')['href']
			yield Request(novelurl, callback=self.get_chapterurl, mata={'name': novelname,
																		'url': novelurl})

	def get_chapterurl(self, response):
		print(response.text)
		item = DingdianItem()
		item['name'] = str(response.meta['name']).replace('\xa0', '')
		item['novelurl'] = response.meta['url']
		category = BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
		author = BeautifulSoup(response.text,'lxml').find('table').find_all('td')[1].get_text()
		bash_url = BeautifulSoup(response.text,'lxml').find('p',class_='btnlinks').find('a',class_='read')['href']
		name_id = str(bash_url)[-6:-1].replace('/','')
		item['category'] = str(category).replace('/','')
		item['author'] = str(author).replace('/','')
		item['name_id'] = name_id
		return item