# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from myClass.mySql import MySql
import re

class BosscrawlPipeline(object):
    def open_spider(self, spider):
        self.mySql = MySql(spider.settings['MYSQL_HOST'], spider.settings['MYSQL_USER'], spider.settings['MYSQL_PASSWORD'], spider.settings['MYSQL_DATABASE'])
        self.mySql.connect()

    def process_item(self, item, spider):
        item['content'] = self.process_content(item['content'])
        self.mySql.insert('market_demand_job', dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r'\xa0|\s|\n', '', i) for i in content]
        content = [i for i in content if len(i) > 0]
        return str(content)
