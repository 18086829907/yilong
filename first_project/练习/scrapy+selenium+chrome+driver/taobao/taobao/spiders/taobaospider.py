# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import quote
from taobao.items import TaobaoItem
import time

class TaobaospiderSpider(scrapy.Spider):
    name = 'taobaospider'
    allowed_domains = ['www.taobao.com']
    base_urls = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.base_urls + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page':page}, dont_filter=True)
                break

    def parse(self, response):
        products = response.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class,"item")]')
        for product in products:
            item = TaobaoItem()
            item['picture'] = ''.join(product.xpath('.//div[@class="pic"]//img[contains(@class,"img")]/@data-src').extract())
            item['price'] = ''.join(product.xpath('.//div[contains(@class,"price")]//text').extract()).strip()
            # item['salesVolume'] = product.xpath('').extract_first()
            # item['title'] = product.xpath('').extract_first()
            # item['shop'] = product.xpath('').extract_first()
            # item['address'] = product.xpath('').extract_first()
            print(item)
