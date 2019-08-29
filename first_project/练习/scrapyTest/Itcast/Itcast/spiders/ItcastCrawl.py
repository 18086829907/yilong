# -*- coding: utf-8 -*-
import scrapy
from Itcast.items import ItcastItem


#命令scrapy genspider生成爬虫文件时，引擎就能获得此爬虫文件的文件名，便可生成爬虫名
#当使用scrapy crawl命令执行这个爬虫名字时，会读取此类的类属性，即要爬取的url列表
#这些列表会给到调度器去重入队列出队列，调度器会将这个url给到下载器进行数据爬取，返回网页的整个html
#response会通过引擎再次给到爬虫文件的parse方法，paser方法即可进行xpath处理
#将解析得到的数据用ItcastItem类的实例化对象来保存，通过yield将实例化对象item返回给items.py中的,引擎
#引擎会根据配置文件中的管道类配置和优先级参数，来依次调用这些类中process_item方法，并且将itme传给这些process_item方法
#当process_item处理完毕之后会返回信号，通知引擎我已经处理完毕，引擎在向爬虫文件的生成器索取下一个itme


class ItcastcrawlSpider(scrapy.Spider):
    #爬虫名，启动爬虫时需要的参数*必须，
    name = 'ItcastCrawl'
    #爬取域范围，允许爬虫在这个域名下进行爬取*可选
    allowed_domains = ['http://www.itcast.cn']
    #qishiurl列表，爬虫执行后第一批请求，将从这个列表里获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath('//div[@class="li_txt"]')
        for node in node_list:
            #创建item字典对象，用来存储信息
            item = ItcastItem()
            #.extract()方法将SelectorList对象转化成列表以及将Selector对象转换为文字
            name = node.xpath('./h3/text()')[0].extract()
            title = node.xpath('./h4/text()')[0].extract()
            info = node.xpath('./p/text()')[0].extract()
            item['name'] = name #将name添加到item字典对象中，以key为'name'，value为name的字典方式存储
            item['title'] = title
            item['info'] = info
            yield item #生成一个item数据生成器，此时会调用管道文件中的ItcastPipeline类的process_item方法来回去生成器中的数据，并且会处理该条item数据，当处理完数据后process_item方法会返回一个信号，告诉生成器给我下一条数据时，yield会继续执行for循环取下一条数据

