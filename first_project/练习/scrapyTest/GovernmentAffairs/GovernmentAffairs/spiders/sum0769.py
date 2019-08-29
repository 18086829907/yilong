# -*- coding: utf-8 -*-
import scrapy
from GovernmentAffairs.items import GovernmentaffairsItem
import logging
logger = logging.getLogger(__name__)

class Sum0769Spider(scrapy.Spider):
    name = 'sum0769'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']

    def parse(self, response):
        trList = response.xpath('//div[@class="greyframe"]/table[2]/tr/td/table/tr')
        for tr in trList:
            item = GovernmentaffairsItem()
            item['problemType'] = tr.xpath('./td[2]/a[1]/text()').extract_first() # 问题类型
            item['title'] = tr.xpath('./td[2]/a[2]/text()').extract_first()  # 标题
            item['innerUrl'] = tr.xpath('./td[2]/a[2]/@href').extract_first() # 内页url
            item['department'] = tr.xpath('./td[2]/a[3]/text()').extract_first()  # 部门
            item['status'] = tr.xpath('./td[3]/span/text()').extract_first()  # 状态
            item['netizen'] = tr.xpath('./td[4]/text()').extract_first()  # 网友
            item['datetime'] = tr.xpath('./td[5]/text()').extract_first()  # 日期时间
            yield scrapy.Request(item['innerUrl'], callback=self.innerParse, meta={'item':item})
        # next_url = response.xpath('//a[text()=">"]/@href').extract_first()
        # if next_url is not None:
        #     yield scrapy.Request(next_url, callback=self.parse)

    def innerParse(self, response):
        item = response.meta['item']
        item['content_image'] = response.xpath('//td[@class="txt16_3"]//img/@src').extract()
        if item['content_image'] is not None:
            item['content_image'] = ['http://wz.sun0769.com' + i for i in item['content_image']]
        else:
            item['content_image'] = None
        item['content'] = response.xpath('//td[@class="txt16_3"]//text()').extract() #内容
        # print(item)
        yield item
