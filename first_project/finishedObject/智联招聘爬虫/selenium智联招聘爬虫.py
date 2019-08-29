from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from lxml import etree
from queue import Queue
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from pandas.io.json import json_normalize
import threading
lock = threading.Lock()
dataList = []

#采集线程类
class CrawlThread(threading.Thread):
    def __init__(self, crawlThreadName, url, htmlQueue, wk):
        super(CrawlThread, self).__init__()
        self.crawlThreadName = crawlThreadName
        self.url = url
        self.htmlQueue = htmlQueue
        self.wk = wk

    def handler_request(self):
        try:
            # 设置谷歌的无头浏览器的参数
            options = Options()
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # 创建无头浏览器对象
            path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
            browser = webdriver.Chrome(executable_path=path, options=options)
            # 打开智联招聘网站
            browser.get(self.url)
            #关闭弹窗
            time.sleep(1)
            adButtom = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div/div/button')))
            adButtom.click()
            # 等待搜索框的出现并写入关键字
            time.sleep(5)
            input_kw = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, r'//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div/div/input')))
            input_kw.send_keys(self.wk)
            time.sleep(3)
            input_kw.send_keys(Keys.ENTER)
            time.sleep(3)
            browser.switch_to.window(browser.window_handles[1])
            n = 1
            while True:
                # 让browser执行简单的js代码，滚动条滚动到底部，此时会一直发送ajax请求加载更多内容，加载过程需要时间
                for i in range(5):
                    js = 'var q=document.documentElement.scrollTop=100000'
                    browser.execute_script(js)
                    time.sleep(3)
                html = browser.page_source
                self.htmlQueue.put(html)
                print('成功抓取{}页'.format(n))
                try:
                    nextButtom = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, r'//div[@id="pagination_content"]/div/button[contains(text(), "下一页")]')))
                except TimeoutException as e:
                    print('无下一页')
                    break
                nextButtom.click()
                time.sleep(5)
                n += 1
        finally:
            browser.quit()  # 退出浏览器

    def run(self):
        print('{}开始'.format(self.crawlThreadName))
        #启动无头浏览器访问该url,并将返回的html存入htmlQueue
        self.handler_request()
        print('{}结束'.format(self.crawlThreadName))

#解析线程类
class ParseThread(threading.Thread):
    def __init__(self, parseThreadName, htmlQueue):
        super(ParseThread, self).__init__()
        self.parseThreadName = parseThreadName
        self.htmlQueue = htmlQueue

    def innerHandler_request(self, jobDetailsURL):
        #打开内页返回内页html
        try:
            # 设置谷歌的无头浏览器的参数
            options = Options()
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # 创建无头浏览器对象
            path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
            browser = webdriver.Chrome(executable_path=path, options=options)
            # 打开智联招聘岗位详情页
            browser.get(jobDetailsURL)

            # 让browser执行简单的js代码，滚动条滚动到底部，此时会一直发送ajax请求加载更多内容，加载过程需要时间
            for i in range(2):
                js = 'var q=document.documentElement.scrollTop=100000'
                browser.execute_script(js)
                time.sleep(1)
            innerHtml = browser.page_source
        finally:
            browser.quit()  # 退出浏览器
        return innerHtml

    #xpath解析岗位详情、工作地址
    def parseInner(self, innerHtml):
        tree = etree.HTML(innerHtml)
        jobDetails = '\n'.join(tree.xpath(r'//div[@class="describtion__detail-content"]//text()'))
        workingAddress = tree.xpath(r'//span[@class="job-address__content-text"]/text()')[0]
        return jobDetails, workingAddress

    #传入商品列表页，遍历每个商品，解析商品列表页的每个商品以及每个商品的内页
    def htmlParse(self, html, n):
        tree = etree.HTML(html)
        itemList = tree.xpath('//div[@id="listContent"]/div')
        for item in itemList:
            try:
                jobName = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[1]/div[1]/span/@title')[0]
                company = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[1]/div[2]/a/text()')[0]
                salary = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[2]/div[1]/p/text()')[0]
                jobCity = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[2]/div[1]/ul/li[1]/text()')[0]
                orkexperience = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[2]/div[1]/ul/li[2]/text()')[0].strip('\n\t ')
                eduLevel = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[2]/div[1]/ul/li[3]/text()')[0]
                companyType = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[2]/div[2]/span[1]/text()')[0]
                companySize = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[2]/div[2]/span[2]/text()')[0]
                welfare = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[3]/div[1]/div/text()')
                timeStatus = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[3]/div[2]/span/text()')[0]
                jobDetailsURL = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/@href')[0]
                companyUrl = item.xpath('.//a[@class="contentpile__content__wrapper__item__info"]/div[1]/div[2]/a/@href')[0]
            except IndexError as e:
                pass
            #打开岗位详情页并返回html
            innerHtml = self.innerHandler_request(jobDetailsURL)
            #解析内页数据，并返回岗位详情和工作地点
            jobDetails, workingAddress = self.parseInner(innerHtml)
            dataDict = {
                '岗位名称': jobName,
                '公司名字': company,
                '薪资待遇': salary,
                '工作城市': jobCity,
                '工作地址': workingAddress,
                '工作经验': orkexperience,
                '学历要求': eduLevel,
                '公司体制': companyType,
                '在职员工': companySize,
                '雇员福利': '、'.join(welfare),
                '岗位状态': timeStatus,
                '岗位详情URL': jobDetailsURL,
                '公司详情': companyUrl,
                '岗位详情': jobDetails,
                }
            dataList.append(dataDict)
            print('成功爬取岗位条数：{}条,'.format(n))
            with lock:
                n += 1

    #从htmlQueue中取出html，解析出需要的数据，保存为字典，添加到列表中，并返回
    def run(self):
        print('{}开始'.format(self.parseThreadName))
        n = 1
        while True:
            #从htmlQueue中取出html
            try:
                html = self.htmlQueue.get(True, 30)
            except Exception as e:
                print('等待60秒，html队列仍然没有数据，结束{}'.format(self.parseThreadName))
                break
            #创建html的解析函数
            self.htmlParse(html, n)

#智联招聘爬虫类
class ZlSpider():
    def __init__(self, city, wk):
        self.city = city
        self.url = 'https://www.zhaopin.com/{}/'.format(self.city)
        self.htmlQueue = Queue()
        self.wk = wk
    #开始采集线程和解析线程
    def createThread(self):
        # 创建采集线程名字
        crawlThreadsName = ['采集线程1']
        # 创建8个采集线程存放于下面列表中
        tCrawlThreadingList = []
        for crawlThreadName in crawlThreadsName:  # 遍历线程名称，传递给线程
            tCrawlThreading = CrawlThread(crawlThreadName, self.url, self.htmlQueue, self.wk)
            tCrawlThreadingList.append(tCrawlThreading)
        # 创建解析线程名字
        parseThreadsName = ['解析线程1']
        # 创建8个解析线程存放于下面列表中
        tParseThreadingList = []
        for parseThreadName in parseThreadsName:
            # 实例化解析线程
            tParseThreading = ParseThread(parseThreadName, self.htmlQueue)
            tParseThreadingList.append(tParseThreading)
        # 启动8个采集线程
        for tCrawlThreading in tCrawlThreadingList:  # 遍历8个线程，启动线程
            tCrawlThreading.start()
            # time.sleep(5)
        # 启动8个解析线程
        # 等待30秒，让采集线程先运行，避免html队列为空
        time.sleep(10)
        print('采集线程全部结束10秒后开启解析线程')
        for tParseThreading in tParseThreadingList:
            tParseThreading.start()
            time.sleep(5)
        # 子线程结束主线才程结束
        for tCrawlThreading in tCrawlThreadingList:  # 遍历8个线程，启动线程
            tCrawlThreading.join()
        # 子线程结束主线程才结束
        for tParseThreading in tParseThreadingList:
            tParseThreading.join()

    def run(self):
        #创建采集线程,将每一页岗位数据传递存放于htmlQueue中
        #创建解析线程，从htmlQueue中取出html，解析出需要的数据，保存为字典，添加到全局列表中
        self.createThread()
        #将json对象转化df
        df = json_normalize(dataList)
        df.to_excel('{}的{}岗位.xlsx'.format(self.city, self.wk), encoding='utf8')


def main():
    city = input('城市拼音：')
    wkList = input('搜索多个关键词用,号分割：').split(',')
    for wk in wkList:
        zlSpider = ZlSpider(city, wk)
        zlSpider.run()
#
if __name__ == '__main__':
    main()