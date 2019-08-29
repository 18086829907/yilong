# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
from images360.items import ImageItem
from jsonpath import jsonpath

class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    def start_requests(self):
        urlBaes = 'https://image.so.com/zjl?ch=photography&sn={}&listtype=new&temp=1'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            url = urlBaes.format(page * 30)
            yield Request(url, self.parse)
    
    def parse(self, response):
        result = json.loads(response.text)
        for image in jsonpath(result, '$.list[*]'):
            item = ImageItem()
            item['id'] = jsonpath(image, '$.id')[0]
            item['url'] = jsonpath(image, '$.imgurl')[0]
            item['title'] = jsonpath(image, '$.title')[0]
            yield item
