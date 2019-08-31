# -*- coding: utf-8 -*-

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from myClass.mySql import MySql
class JdcrawlPipeline(object):
    def open_spider(self, spider):
        self.mySql = MySql(spider.settings['MYSQL_HOST'], spider.settings['MYSQL_USER'], spider.settings['MYSQL_PASSWORD'], spider.settings['MYSQL_DATABASE'])
        self.mySql.connect()
    def process_item(self, item, spider):
        self.mySql.insert('goods', self.parseData(dict(item)))
        return item
    def parseData(self, item):
        for k, v in item.items():
            if v == []:
                v = ''
                item[k] = v
            elif type(v) == list:
                v = ','.join(v)
                item[k] = v
            elif v == None:
                v = ''
                item[k] = v
        return item
