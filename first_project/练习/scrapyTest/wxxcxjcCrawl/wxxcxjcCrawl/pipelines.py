# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WxxcxjccrawlPipeline(object):
    def process_item(self, item, spider):
        item['content'] = ''.join([x.strip('\n\t ') for x in dict(item)['content']])
        print(item)
        return item
