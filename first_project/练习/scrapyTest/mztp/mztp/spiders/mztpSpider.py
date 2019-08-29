# -*- coding: utf-8 -*-
import scrapy
import scrapy
from mztp.items import MztpItem
import time
import random
from scrapy_splash import SplashRequest

lua = """
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  splash.scroll_position={y=10000}
  assert(splash:wait(args.wait))
  splash.scroll_position={y=10000}
  assert(splash:wait(args.wait))
  splash.scroll_position={y=10000}
  assert(splash:wait(args.wait))
  return splash:html()
end
"""


class MztpspiderSpider(scrapy.Spider):
    name = 'mztpSpider'
    allowed_domains = ['mzt.com']
    start_urls = ['https://www.mzitu.com/tag/youhuo/']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], callback=self.parse, endpoint='execute', args={'lua_source':lua, 'wait':5}, dont_filter=True)

    def parse(self, response):
        innerList = response.xpath('//ul[@id="pins"]/li')
        for inner in innerList:
            item = MztpItem()
            innerUrl = inner.xpath('./a/@href').extract_first()
            yield SplashRequest(innerUrl, callback=self.parse1, endpoint='execute', meta={'item':item.copy()}, args={'lua_source':lua, 'wait':5}, dont_filter=True)
        next_outPage = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        if next_outPage:
            yield SplashRequest(next_outPage, callback=self.parse, endpoint='execute', args={'lua_source': lua, 'wait': 5}, dont_filter=True)

    def parse1(self, response):
        item = response.meta['item']
        item['title'] = response.xpath('//h2/text()').extract_first()
        item['picture'] = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
        yield item
        next_innerPage = response.xpath('//div[@class="pagenavi"]/a/span[contains(text(),"下一页")]/../@href')
        if next_innerPage:
            yield SplashRequest(next_innerPage, callback=self.parse1, endpoint='execute', args={'lua_source': lua, 'wait': 5}, dont_filter=True)
