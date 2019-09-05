# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SeleniumchromedrvertestItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    volume = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    years = scrapy.Field()
    turnoverRate = scrapy.Field()
    shopType = scrapy.Field()

