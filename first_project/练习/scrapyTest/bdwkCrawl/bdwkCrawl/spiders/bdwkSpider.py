# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from bdwkCrawl.items import BdwkcrawlItem

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

class BdwkspiderSpider(scrapy.Spider):
    name = 'bdwkSpider'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/view/f4f29a1ca300a6c30c229f9e.html']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], dont_filter=True, callback=self.parse, endpoint='execute', args={'lua_source':lua, 'wait':7})

    def parse(self, response):
        print(response.xpath('//title/text()').extract_frist())
        item = BdwkcrawlItem()
        item['content'] = response.xpath('//div[@class="ie-fix"]/p/text()')
        yield item
