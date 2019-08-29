# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxxcxjcCrawl.items import WxxcxjccrawlItem

class WxappspiderSpider(CrawlSpider):
    name = 'wxappSpider'
    # allowed_domains = ['wxapp-union.com/']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        # Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-\d+-1\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = WxxcxjccrawlItem()
        item['title'] = response.xpath('//h1[@class="ph"]/text()').extract_first()
        item['author'] = response.xpath('//p[@class="authors"]/a/text()').extract_first()
        item['datetime'] = response.xpath('//span[@class="time"]/text()').extract_first()
        item['content'] = response.xpath('//td[@id="article_content"]/p//text()').extract()
        yield item
