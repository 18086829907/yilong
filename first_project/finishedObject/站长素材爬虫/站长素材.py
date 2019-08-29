import urllib.request
import urllib.parse
from lxml import etree
import json
import time
import os

class zzscSipder():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian_{}.html'
    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
        self.contentList = []

    def download_image(self, image_src):
        dirPath = 'xingan'
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
        fileName = os.path.basename(image_src)
        filePath = os.path.join(dirPath, fileName)
        urllib.request.urlretrieve(image_src, filePath)


    def XPath(self, response):
        htmlelement = etree.HTML(response)
        pictureList = htmlelement.xpath('//div[@id="container"]/div/div/a/img/@src2')
        #遍历列表，依次下载图片
        for image_src in pictureList:
            self.download_image(image_src)
            time.sleep(1)


    def handler_request(self, page):
        #伪造url
        #设置不同的url
        if page != 1:
            url_new = self.url.format(page)
        else:
            url_new = 'http://sc.chinaz.com/tupian/xingganmeinvtupian.html'
        #伪造请求头
        headers = self.headers
        #构造请求体
        response = urllib.request.Request(url=url_new, headers=headers)
        return response

    def run(self):
        #构造请求体,根据输入的页面伪造url
        for page in range(self.start_page, self.end_page + 1):
            #构造请求体
            request = self.handler_request(page)
            #发送请求，获取响应
            response = urllib.request.urlopen(request).read().decode()
            #解析内容
            self.XPath(response)
            time.sleep(2)
        #保存数据
        string = json.dumps(self.contentList, ensure_ascii=False)
        with open('xgmv.txt', 'w', encoding='utf8') as f:
            f.write(string)
def main():
    #根据用户输入的开始页和结束页爬取对应页面内容
    start_page = int(input('请输入开始页码：'))
    end_page = int(input('请输入结束页码：'))
    #构造一个爬虫对象是
    zzsc = zzscSipder(start_page, end_page)
    zzsc.run()

if __name__=='__main__':
    main()

