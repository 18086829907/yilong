# -*- coding: utf-8 -*-
import scrapy
from bossCrawl.items import BosscrawlItem
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

class BossspiderSpider(scrapy.Spider):
    name = 'bossSpider'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=%E7%88%AC%E8%99%AB&page=1&ka=page-1']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], callback=self.parse, endpoint='execute', args={'lua_source':lua, 'wait':5}, dont_filter=True)

    def parse(self, response):
        for i in response.xpath('//div[@class="job-list"]/ul/li'):
            item = BosscrawlItem()
            item['source'] = 'Boss直聘'
            item['jobName'] = i.xpath('.//div[@class="job-title"]/text()').extract_first()
            item['price'] = i.xpath('.//span[@class="red"]/text()').extract_first()
            item['companyName'] = i.xpath('//div[@class="company-text"]/h3/a/text()').extract_first()
            item['address'] = i.xpath('//div[@class="info-primary"]/p/text()').extract_first()
            innerUrl = 'https://www.zhipin.com' + i.xpath('//div[@class="info-primary"]/h3/a/@href').extract_first()
            yield SplashRequest(innerUrl, callback=self.innerParse, endpoint='execute', meta={'item':item.copy()}, args={'lua_source': lua, 'wait': 5}, dont_filter=True)
        next_url = response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract_first()
        if next_url:
            yield SplashRequest('https://www.zhipin.com' + next_url, callback=self.parse, endpoint='execute', args={'lua_source': lua, 'wait': 5}, dont_filter=True)
        else:
            return

    def innerParse(self, response):
        item = response.meta['item']
        item['content'] = response.xpath('//div[@class="job-sec"]/div[@class="text"]/text()').extract()
        yield item
        randomtime = random.randint(1, 59)
        if time.strftime('%H:%M:%S', time.localtime()) == '9:{}:{}'.format(randomtime, randomtime):
            time.sleep(39600)
