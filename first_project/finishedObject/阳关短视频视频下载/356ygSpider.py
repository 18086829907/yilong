import requests
from lxml import etree
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import random

class YgSpider():
    s = requests.Session()
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}

    def handler_selenium(self, url, pages):
        print('启动无头浏览器')
        # 设置谷歌的无头浏览器
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # 创建无头浏览器对象
        # path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        path = r'E:\Anaconda3\Scripts\chromedriver.exe'
        browser = webdriver.Chrome(executable_path=path, options=options)
        # 打开365yg视频网站二级页面
        browser.get(url)
        time.sleep(2)
        #滚动条滚动到底部,50次
        for page in range(pages):
            js = 'var q=document.documentElement.scrollTop=100000' #模拟滚动条滚到底部
            browser.execute_script(js)
            browser.save_screenshot('./image/{}.png'.format(page))
            time.sleep(random.random() * 5)
        # 获得网页html
        html = browser.page_source
        # 关闭无头浏览器
        browser.quit()  # 退出浏览器
        print('关闭无头浏览器')
        return html

    def handler_fristPage(self, page):
        '''
        功能：使用无头浏览器访问一级页面，获取所有二级页面url列表
        :return: 完整的二级页面url
        '''
        #365yg视频网站一级页面
        url = 'http://www.365yg.com/'
        #启动无头浏览器，获取一级页面的html，滑动滚轮到底部page次
        html = self.handler_selenium(url, page)
        #解析源代码
        tree = etree.HTML(html)
        secondPageUrlList = tree.xpath('//div[@class="title-box"]/a/@href')
        secondPageCompleteUrlList = []
        for item in secondPageUrlList:
            completeUrl = 'http://www.365yg.com' + item
            secondPageCompleteUrlList.append(completeUrl)
        return secondPageCompleteUrlList

    def handler_secondPage(self, secondPageCompleteUrlList):
        '''
        功能：使用无头浏览器遍历访问每一个二级页面，并获取视频地址，并向视频地址发送get请求，保存视频到本地
        :param secondPageCompleteUrlList: 完成的二级页面url
        :return: 无
        '''
        n = 1
        for secondUrl in secondPageCompleteUrlList:
            #启动无头浏览器访问二级页面，并返回html
            html = self.handler_selenium(secondUrl, 1)
            #解析网站内页
            tree = etree.HTML(html)
            videoUrl = tree.xpath('//video/@src')[0]
            title = tree.xpath('//h1/text()')[0]
            r = requests.get(url=videoUrl, headers=self.headers)
            with open('./video/{}.mp4'.format(title), 'wb') as f:
                f.write(r.content)
            print('开始爬取视频{}：{}'.format(n, title))
            n += 1
            time.sleep(random.random()*10)

    def run(self):
        #使用无头浏览器访问一级页面，获取所有二级页面url列表,参数表示滑动5次滚轮，触发ajax加载更多二级页面链接
        secondPageCompleteUrlList = self.handler_fristPage(5)
        #使用无头浏览器遍历访问每一个二级页面，并获取视频地址，并向视频地址发送get请求，保存视频到本地
        self.handler_secondPage(secondPageCompleteUrlList)

def main():
    spider = YgSpider()
    spider.run()

if __name__ == '__main__':
    main()