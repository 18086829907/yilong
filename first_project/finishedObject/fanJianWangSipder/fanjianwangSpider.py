import requests
from queue import Queue
import threading
from lxml import etree
import json
import time


#存放采集线程实例对象
g_crawl_list = []
#存放解析线程实例对象
g_parse_list = []
#存放解析后的数据
jsonList = []

#创建采集线程类
class CrawlThread(threading.Thread):
    def __init__(self, name, page_queue, html_queue):
        super(CrawlThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.html_queue = html_queue
        self.url = 'http://www.fanjian.net/jiantu-{}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60 Opera/8.0 (Windows NT 5.1; U; en)'}

    #采集类进程执行的函数
    def run(self):
        print('{}---线程启动'.format(self.name))
        while True:
            #判断页面队列为空时，采集线程结束
            if self.page_queue.empty():
                break
            #从页码队列中取出页码
            page = self.page_queue.get()
            #拼接url，发送请求，将响应内容存放网页队列中
            url = self.url.format(page)
            r = requests.get(url=url, headers=self.headers)
            #将响应内容放到html_queue中
            self.html_queue.put(r.text)
        print('{}---线程结束'.format(self.name))

#创建解析线程类
class parseThread(threading.Thread):
    def __init__(self, name, html_queue, lock):
        super(parseThread, self).__init__()
        self.name = name
        self.html_queue = html_queue
        self.lock = lock

    #解析类进程执行的函数
    def run(self):
        print('{}---线程启动'.format(self.name))
        while True:
            #判断页面队列为空时，采集线程结束
            try:
                # 在html_queue队列中取数据，并解析数据
                html = self.html_queue.get(True, 10)
                # 解析网页数据
                self.parse_content(html)
            except Exception as e:
                break
        print('{}---线程结束'.format(self.name))

    #网页内容解析
    def parse_content(self, html):
        tree = etree.HTML(html)
        #先查找所有的li，再从li里面查找自己的标题和url
        li_list = tree.xpath('//ul[@class="cont-list"]/li')
        dataList = []
        for oli in li_list:
            #获取标题
            title = oli.xpath('.//h2/a/text()')[0]
            #获取懒加载图片url
            img_url = oli.xpath('.//div[@class="cont-list-main"]/p[2]/img[@class="lazy"]/@data-src')
            dataDict = {
                '标题': title,
                '图片链接': img_url,
            }
            dataList.append(dataDict)
        #将dataList写到文件中
        self.lock.acquire()
        jsonList.extend(dataList)
        self.lock.release()

#实例采集线程
def create_crawlThread(page_queue, html_queue):
    crawl_name = ['采集线程1号','采集线程2号','采集线程3号']
    for name in crawl_name:
        #创建3个采集线程
        tcrawl = CrawlThread(name, page_queue, html_queue)
        #保存采集线程实例对象
        g_crawl_list.append(tcrawl)

#实例解析线程
def create_parseThread(html_queue, lock):
    parse_name = ['解析线程1号','解析线程2号','解析线程3号']
    for name in parse_name:
        #创建3个解析线程
        tparse = parseThread(name, html_queue, lock)
        #保存解析线程实例对象
        g_parse_list.append(tparse)

#创建队列
def create_queue():
    '''
    功能：创建页码队列和网页队列
    :return: 返回两个队列
    '''
    #创建页码队列
    page_queue = Queue()
    for page in range(1, 11):
        page_queue.put(page)

    #创建网页队列
    html_queue = Queue()
    return page_queue, html_queue

def main():
    #函数创建队列,
    page_queue, html_queue = create_queue()
    #打开一个文件
    fp = open('jian.json', 'w', encoding='utf8')
    #创建锁
    lock = threading.Lock()
    #函数创建线程——采集html类，解析html类
    create_crawlThread(page_queue, html_queue)
    time.sleep(3)
    create_parseThread(html_queue, lock)
    #启动所有采集线程
    for tcrawl in g_crawl_list:
        tcrawl.start()
    #启动所有解析线程
    for tparse in g_parse_list:
        tparse.start()
    #主线程等待子线程结束再结束
    for tcrawl in g_crawl_list:
        tcrawl.join()
    #主线程等待子线程结束再结束
    for tparse in g_parse_list:
        tparse.join()
    #写入json数据
    print(jsonList)
    fp.write(json.dumps(jsonList, ensure_ascii=False))
    #关闭文件
    fp.close()
    print('主线程子线程全部结束')

if __name__ == '__main__':
    main()