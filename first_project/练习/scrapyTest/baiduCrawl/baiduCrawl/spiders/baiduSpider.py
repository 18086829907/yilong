# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

lua = """
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end
"""

class BaiduspiderSpider(scrapy.Spider):
    name = 'baiduSpider'
    allowed_domains = ['http://www.baidu.com/']
    start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], callback=self.parse, endpoint='execute', args={'lua_source': lua, 'wait':7})

    def parse(self, response):
        print(response.text)


