# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from lxml import etree
from pymongo import MongoClient

class AjxxgkPipeline(object):
    def open_spider(self, spider):
        self.conn = MongoClient(spider.settings.get('MONGODB_HOST'), spider.settings.get('PORT'))
        db = self.conn.mydb
        self.collection = db.qqs

    def process_item(self, item, spider):
        rule = re.compile('<!--文书内容 开始 -->(.*?)<!--文书内容 结束 -->', re.S)
        tree = etree.HTML(rule.findall(item['content'])[0])
        contentList = [re.sub(r'\n|\t|\xa0', '', item) for item in tree.xpath('//p/text()')]
        content = [i for i in contentList if len(i) > 0]
        item['content'] = content
        self.collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.conn.close()