# -*- coding: utf-8 -*-
import scrapy
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

class BaiduspiderSpider(scrapy.Spider):
    name = 'baiduSpider'
    allowed_domains = ['http://www.baidu.com/']
    start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], callback=self.parse, endpoint='execute', args={'lua_source': lua, 'wait':7})

    def parse(self, response):
        # print(response.text)
        print(response.xpath('//title/text()'))

