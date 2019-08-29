# -*- coding: utf-8 -*-
import scrapy.spiders
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cbrc.items import CbrcItem

class YbjhxzcfSpider(CrawlSpider):
    name = 'ybjhxzcf' #银保监会行政处罚
    allowed_domains = ['www.cbrc.gov.cn']
    start_urls = ['http://www.cbrc.gov.cn/cn/list/9103/910305/ybjfjcf/1.html']    #第一次发送文件

    #url规则定义
    rules = (
        #Rule：是一个类，Rule()在做实例化，得到的一条实例就是一条url规则
        Rule(LinkExtractor(allow=r'/cn/doc/9103/910305/ybjfjcf/\w*?\.html'), callback='parse_item', follow=False),
        #LinkExtractor：链接提取器，提取url地址
        # Rule(LinkExtractor(allow=r'\d+\.html'), callback='parse_item', follow=True),
        #allow：定义正则表达式
        #callback：提取出来的url地址的response会交个callback处理
    )

    #parse函数其实还是存在的，当我们用正则提取出url后，url会传到父类的parse函数中，发送请求
    #因此这里不能用parse命名函数，否则会重写父类方法

    def parse_item(self, response):
        item = CbrcItem()
        item['companyName'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/table/tbody/tr[3]/td[3]/p/span[1]/text()').extract_first()
        item['legalRepresentative'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/table/tbody/tr[4]/td[2]/p/span[1]/text()').extract_first()
        item['violationOffacts'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/table/tbody/tr[5]/td[2]/p/span[2]/text()').extract_first()
        item['punishmentBasis'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/table/tbody/tr[6]/td[2]/p/span[1]/text()').extract_first()
        item['penaltyDecision'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/table/tbody/tr[7]/td[2]/p//text()').extract_first()
        item['agencyName'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/table/tbody/tr[8]/td[2]/p/span[1]/text()').extract_first()
        item['date'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/table/tbody/tr[9]/td[2]/p/span[1]/text()').extract_first()
        print(item)

        return item