import requests
from lxml import etree
import json
import time
import random

s = requests.Session()

class busSpider():
    def __init__(self, city):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
        self.baseUrl = 'https://{}.8684.cn'.format(city)
        self.detailsPageList = []
        self.city = city

    #导航栏
    def navigetionHandler(self):
        '''
        功能：爬取主导航栏并返回所有指向副导航栏的a链接href属性，以列表的方式返回
        '''
        #发送get请求
        r = s.get(self.baseUrl, headers=self.headers)
        #解析内容，获取导航链接
        tree = etree.HTML(r.text)
        #查找以数字开头的链接
        naviList_href_number = tree.xpath('//div[@class="bus_kt_r1"]/a/@href')
        #查找以字母开头的链接
        naviList_href_letter = tree.xpath('//div[@class="bus_kt_r2"]/a/@href')
        #将需要爬取的所有链接返回
        return naviList_href_number + naviList_href_letter

    #副导航栏
    def subNavigetionHandler(self, naviList):
        '''
         功能：遍历访问所有a链接显示所有副导航栏中指向详情页的a链接href属性,以列表的方式返回
        '''
        subNaviList = []
        for item in naviList:
            url = self.baseUrl + item
            r = s.get(url=url, headers = self.headers)
            tree = etree.HTML(r.text)
            subNaviList += tree.xpath('//div[@id="con_site_1"]/a/@href')
            time.sleep(random.random()*10)
        return subNaviList

    #详情页
    def detailsPageHandler(self, subNaviList):
        '''
        遍历访问所有的副导航栏链接，获取详情页信息列表，列表元素为每个详情页信息的字典
        '''
        n = 1
        for item in subNaviList:
            url = self.baseUrl + item
            r = s.get(url=url, headers = self.headers)
            tree = etree.HTML(r.text)
            # xpath的测试
            # with open('innerTest.html', 'w', encoding='utf8') as f:
            #     f.write(r.text)
            print('开始爬取{}'.format(tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0]))
            print(url)
            try:
                downwardRoute_totalStationNumber = tree.xpath('//span[@class="bus_line_no"]/text()')[1]
                downwardRoute = tree.xpath('//div[@class="bus_site_layer"]')[1].xpath('./div/a/text()')
            except IndexError:
                downwardRoute_totalStationNumber = ''
                downwardRoute = []
            detailsPageDict = {
                '公交车号': tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0],
                '运行时间': tree.xpath('//p[@class="bus_i_t4"][1]/text()')[0].split('：', 1)[-1],
                '票价信息': tree.xpath('//p[@class="bus_i_t4"][2]/text()')[0].split('：', 1)[-1],
                '公交公司': tree.xpath('//p[@class="bus_i_t4"][3]/a/text()')[0].split('：', 1)[-1],
                '最后更新': tree.xpath('//p[@class="bus_i_t4"][4]/text()')[0].split('：', 1)[-1],
                '上行总站数': tree.xpath('//span[@class="bus_line_no"]/text()')[0],
                '上行站台': tree.xpath('//div[@class="bus_site_layer"]')[0].xpath('./div/a/text()'),
                '下行总站数': downwardRoute_totalStationNumber,
                '下行站台':downwardRoute,
            }
            self.detailsPageList.append(detailsPageDict)
            print('爬取第{}条数据'.format(n))
            time.sleep(random.random()*10)
            n += 1

    #爬虫执行
    def run(self):
        #爬取主导航栏并返回所有指向副导航栏的a链接href属性，以列表的方式返回
        naviList = self.navigetionHandler()
        #遍历访问所有a链接显示所有副导航栏中指向详情页的a链接href属性,以列表的方式返回
        subNaviList = self.subNavigetionHandler(naviList)
        #遍历访问所有的副导航栏链接，获取详情页信息列表，列表元素为每个详情页信息的字典
        self.detailsPageHandler(subNaviList)
        #将字典转化为json并保存文件
        jsonData = json.dumps(self.detailsPageList, ensure_ascii=False)
        with open('{}_busInfo.json'.format(self.city), 'w', encoding='utf8') as f:
            f.write(jsonData)

def main():
    city = input('输入城市拼音：')
    spider = busSpider(city)
    spider.run()

if __name__ == '__main__':
    main()