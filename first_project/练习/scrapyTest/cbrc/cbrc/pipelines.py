# -*- coding: utf-8 -*-
import json
import re
from pymongo import MongoClient
class CbrcPipeline(object):
    def open_spider(self, spider):      # 链接服务器
        self.conn = MongoClient(spider.settings.get('MONGODB_HOST'), spider.settings.get('PORT'))
        # 链接数据库
        db = self.conn.mydb
        # 获取集合
        self.collection = db.ybjhxzcf
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
    def close_spider(self, spider):
        # 断开服务
        self.conn.close()
