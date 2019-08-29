# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ajxxgk.items import AjxxgkItem

class QssSpider(CrawlSpider):
    name = 'qss'
    allowed_domains = ['ajxxgk']
    start_urls = ['http://www.ajxxgk.jcy.gov.cn/html/zjxflws/']

    rules = (
        Rule(LinkExtractor(allow=r'/html/20190723/2/\d+\.html'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'/html/zjxflws/\d+\.html'), follow=True),
    )

    def parse_item(self, response):
        item = AjxxgkItem()
        item['content'] = response.text
        yield item
