# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 下午2:42
# @Author  : Sulong
# @File    : comic_spider.py
# @Software: PyCharm

import scrapy
import re
from scrapy import Selector
from cartoon.items import CartoonItem


class ComicSpider(scrapy.Spider):
	name = "comic"  # 自己定义的内容，在运行工程的时候需要用到的标识；

	def __init__(self):
		self.server_img = 'http://n2.1whour.com//'  # 图片链接server域名 这里根据实际情况修改为 n2
		self.server_link = 'http://comic.kukudm.com'  # 章节链接server域名 已参考网站对照
		self.allowed_domains = ['comic.kukudm.com']  # 允许爬虫访问的域名，防止爬虫跑飞 放置于列表中
		self.start_urls = ['http://comic.kukudm.com/comiclist/3/']  # 开始爬取的url，同样这个url链接也需要放在列表里
		self.pattern_img = re.compile(r'\+"(.+)\'><span')  # #匹配图片地址的正则表达式   这里不懂 需要测试todo

	def start_requests(self):
		yield scrapy.Request(url=self.start_urls[0], callback=self.parse1)

	'''解析response,获取张杰图片链接地址'''

	def parse1(self, response):
		hxs = Selector(response)
		items = []
		urls = hxs.xpath('//dd/a[1]/@href').extract()  # 章节连接地址
		dir_names = hxs.xpath('//dd/a[1]/text()').extract()  # 章节名
		for index in range(len(urls)):  # 保存章节连接和章节名
			item = CartoonItem()
			item['link_url'] = self.server_link + urls[index]
			item['dir_name'] = dir_names[index]
			items.append(item)
		# 根据每个章节的连接 ，发送Request请求，传递  item参数
		for item in items[-13:-1]:
			yield scrapy.Request(url=item['link_url'], meta={'item': item}, callback=self.parse2)

	'''解析获得章节第一页的页码数和图片链接'''

	def parse2(self, response):
		item = response.meta['item']  # 接受传递的item参数
		item['link_url'] = response.url  # 获取章节的第一页链接
		hxs = Selector(response)
		pre_img_url = hxs.xpath('//script/text()').extract()  # 获取章节第一页的图片链接
		img_url = [self.server_img + re.findall(self.pattern_img, pre_img_url[0])[0]]  # 这里返回的图片地址 应为列表
		item['img_url'] = img_url  # 将获取的章节第一页的图片链接保存至img_url中
		yield item  # 返回item 交给下载器下载图片
		page_num = hxs.xpath('//td[@valign="top"]/text()').re(u'共(\d+)页')[0]  # 获取章节页数
		# 根据页数 ，整理出本章节其他页码的连接
		pre_link = item['link_url'][:-5]
		for each_link in range(2, int(page_num) + 1):
			new_link = pre_link + str(each_link) + '.htm'
			# 根据本章节其他页码的连接发送Request请求  用于解析其他页码的图片链接,并传递item
			yield scrapy.Request(url=new_link, meta={'item': item}, callback=self.parse3)

	'''解析获得的本章节其他页面的图片链接'''

	def parse3(self, response):
		item = response.meta['item']  # 接收传递的item
		item['link_url'] = response.url  # 获取该页面的连接
		hxs = Selector(response)
		pre_img_url = hxs.xpath('//script/text()').extract()
		img_url = [self.server_img + re.findall(self.pattern_img, pre_img_url[0])[0]]  # 这里返回的图片地址 应为列表
		item['img_url'] = img_url  # 将获得的图片链接保存至 img_url 中
		yield item  # 返回item，交给item pipeline下载图片

	# def parse(self, response): # 测试输出部分
	# 	# 请求分析的糊掉函数，如果不定义 start_requests(self)  获取的请求直接从这个函数分析
	# 	# link_urls = response.xpath('//dd/a[1]/@href').extract()
	# 	dir_names = response.xpath('//dd/a[1]/text()').extract()
	# 	dir_image = re.compile(r'\+"(.+)\'><span')
	# 	for img in dir_image:
	# 		print(img)
	# 	# for each_name in dir_names:  # 输出章节名字
	# 	# 	print(each_name)
	# 	# for each_link in link_urls: # 输出连接
	# 	# 	print('http://comic.kukudm.com' + each_link)
