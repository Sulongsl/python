# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dingdian.dingdian.items import DingdianItem
from dingdian.dingdian.mysqlpipelines.sql import Sql

class DingdianPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,DingdianItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)
            if ret[0] ==1:
                print('已经存在了')
                pass
            else:
                xs_name = item['xs_name']
                xs_author= item['xs_author']
                category = item['category']
                Sql.inster_dd_name(xs_name,xs_author,category,name_id)
                print('开始存储小说')

