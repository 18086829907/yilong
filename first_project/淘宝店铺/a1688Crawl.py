# -*- coding: utf-8 -*-
import scrapy


class A1688crawlSpider(scrapy.Spider):
    name = '1688Crawl'
    allowed_domains = [''https://detail.1688.com/offer/602220466194.html?'']
    start_urls = ['http://'https://detail.1688.com/offer/602220466194.html?'/']

    def parse(self, response):
        pass
