# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class IpsipderSpider(scrapy.Spider):
    name = 'ipsipder'
    allowed_domains = ['ip.cn']
    start_urls = ['https://ip.cn/']

    lua='''
    function main(splash, args)
      assert(splash:go(args.url))
      assert(splash:wait(0.5))
      return html = splash:html()
    end
    '''
    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse, endpoint='execute', args={'lua_source':self.lua})

    def parse(self, response):
        print(response.text)