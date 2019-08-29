# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cl.items import ClItem


class ClsqSpider(CrawlSpider):
    name = 'clsq'
    allowed_domains = ['www.t66y.coms']
    start_urls = ['https://t66y.coms.live/thread0806.php?fid=8']

    rules = (
        Rule(LinkExtractor(allow=r'htm_data/1907/8/\d+\.html'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'thread0806.php?fid=8&search=&page=/d+'), follow=True),
    )

    def parse_item(self, response):
        item = ClItem()
        item['images'] = response.xpath('//p[@align="center"]/input/@src').extract()
        yield item
