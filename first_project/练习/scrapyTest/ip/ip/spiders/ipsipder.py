# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class IpsipderSpider(scrapy.Spider):
    name = 'ipsipder'
    allowed_domains = ['ip.cn']
    start_urls = ['https://ip.cn/']

    lua='''
        function main(splash, args)
            splash.images_enabled = false    
            assert(splash:go(args.url))
            return splash:html()
        end
    '''
    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.myParse, endpoint='execute', args={'lua_source':self.lua})

    def myParse(self, response):
        print(response.text)
