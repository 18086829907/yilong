# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import quote
from seleniumChromeDrverTest.items import SeleniumchromedrvertestItem

class A1688Spider(scrapy.Spider):
    name = '1688'
    allowed_domains = ['www.1688.com']
    base_urls = 'https://s.1688.com/selloffer/offer_search.htm?keywords='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.base_urls + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page':page}, dont_filter=True)

    def parse(self, response):
        pass
