 # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

#通过配置文件ITEM_PIPELINES = {'Itcast.pipelines.ItcastPipeline': 300,}来启用管代文件类
#管道文件可以是多个，都可以通过配置文件类启用
#启用的管道文件类process_item方法才会去获取生成器中的数据
#多个管道类的目的是将相同数据处理为不同格式，比如将数据以json格式保存到本地、字典格式、列表格式、csv、dataframe
#当管道文件中有多个管道类时，item数据会以管道文件的优先级来依次通过管道处理，直到进过所有的管道类，最终会返回给引擎，告诉引擎我们管道文件的处理工作结束了

class ItcastPipeline(object):
    def __init__(self):    #被引擎调用的第一次，初始化一个文件，并且只执行一次
        self.f = open('name.json', 'wb')

    def process_item(self, item, spider): #每次有item数据时，即在爬虫文件中的for循环中爬取到一个数据就调用一次
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content.encode('utf8'))
        return item #此处返回item给引擎，告诉引擎管道文件已经将内容处理完毕，并且告诉爬虫文件中的生成器，可以给我下一个item了

    def close_spider(self, spider): #爬虫结束时自动调用这个方法，本质为引擎在循环索取爬虫文件的生成器数据，当生成器中的数据为空时，捕捉到错误做为判断依据，停止循环并调用close_spider方法
        self.f.close()