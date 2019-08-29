# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
logger = logging.getLogger(__name__)
import json
import re
from pymongo import MongoClient

class GovernmentaffairsPipeline(object):
    def open_spider(self, spider):
        # 链接服务器
        self.conn = MongoClient(spider.settings.get('MONGODB_HOST'), spider.settings.get('PORT'))
        # 链接数据库
        db = self.conn.mydb
        # 获取集合
        self.collection = db.sum0769

    def process_item(self, item, spider):
        item['content'] = self.process_content(item['content'])
        self.collection.insert_one(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r'\xa0|\s','',i) for i in content]
        content = [i for i in content if len(i)>0]
        return content

    def close_spider(self, spider):
        # 断开服务
        self.conn.close()