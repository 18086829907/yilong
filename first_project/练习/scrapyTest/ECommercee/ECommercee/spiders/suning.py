# -*- coding: utf-8 -*-
import scrapy
from ECommercee.items import EcommerceeItem

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['list.suning.com']
    start_urls = ['http://list.suning.com/']

    def parse(self, response):
        firstTypeList = response.xpath('//div[@class="menu-item"]/dl/dt/h3/a')
        for firstType in firstTypeList:
            item = EcommerceeItem()
            item['firstType'] = firstType.xpath('./text()').extract_first()
            secondTypeList = response.xpath('//p[@class="submenu-item"]/a')
            for secondType in secondTypeList:
                item['secondType'] = secondType.xpath('./text()').extract_first()
                thirdTypeList = response.xpath('//ul[@class="book-name-list clearfix"]/li/a')
                for thirdType in thirdTypeList:
                    item['thirdType'] = thirdType.xpath('./text()').extract_first()
                    item['framePageUrl'] = thirdType.xpath('./@href').extract_first()
                    yield scrapy.Request(item['framePageUrl'], meta={'item':item}, callback=self.frameParse)

    def frameParse(self, response):
        item = response.meta['item']
