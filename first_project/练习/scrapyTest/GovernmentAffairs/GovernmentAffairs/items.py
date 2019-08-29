# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovernmentaffairsItem(scrapy.Item):
    # define the fields for your item here like:
    problemType = scrapy.Field() #问题类型
    title = scrapy.Field() #标题
    department = scrapy.Field() #部门
    status = scrapy.Field() #状态
    netizen = scrapy.Field() #网友
    datetime = scrapy.Field() #日期时间
    innerUrl = scrapy.Field() #内页url
    content = scrapy.Field() #内页内容
    content_image = scrapy.Field() #内页图片