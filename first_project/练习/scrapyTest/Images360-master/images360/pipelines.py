# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

#mongodb
class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def process_item(self, item, spider):
        name = item.collection
        self.db[name].insert(dict(item))
        return item
    def close_spider(self, spider):
        self.client.close()

#mysql
from mySql import MySql
class MysqlPipeline():
    def open_spider(self, spider):
        self.mySql = MySql(spider.settings['MYSQL_HOST'], spider.settings['MYSQL_USER'], spider.settings['MYSQL_PASSWORD'], spider.settings['MYSQL_DATABASE'])
        self.mySql.connect()
    def process_item(self, item, spider):
        self.mySql.insert('images', dict(item))
        return item
    def close_spider(self, spider):
        # self.mySql.close()    #因为insert会自动关闭mysql所以不用再关闭
        pass

#图片本地
class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item
    def get_media_requests(self, item, info):
        yield Request(item['url'])
