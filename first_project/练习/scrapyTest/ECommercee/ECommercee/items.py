# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EcommerceeItem(scrapy.Item):
    # define the fields for your item here like:
    firstType = scrapy.Field()
    secondType = scrapy.Field()
    thirdType = scrapy.Field()
    pictrue = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()
    shop = scrapy.Field()
    tag = scrapy.Field()
    title = scrapy.Field()
    framePageUrl = scrapy.Field()
