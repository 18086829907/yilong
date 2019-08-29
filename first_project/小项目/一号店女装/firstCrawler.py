from myClass.headers import Headers
import urllib.request
import re
import os

# 一号店图片爬取
def fristiImageCrawler(url, toPath):
    headers = Headers()
    getHeaders = headers.allHeaders()
    res = urllib.request.Request(url, headers=getHeaders)
    response = urllib.request.urlopen(res)
    HTML = response.read().decode('utf-8')
    # html用wb写入文件时不需要.decode()，这样才不乱码
    # HTMLpath = r'D:\qian_feng_education\first_project\myClass\一号店女装\first.html'
    # with open(HTMLpath, 'wb') as f:
    # f.write(HTML)
    pat = r'<div style="position: relative">\n<img (src)|(original)="//(.*?)/>'
    re_imgList = re.compile(pat, re.S)
    imgList = re_imgList.findall(HTML)
    fileNum = 0
    for i in imgList:
        if i[2] != '':
            imageUrl = i[2].rstrip(' ').rstrip('\"')
            absPath = os.path.join(toPath, '{}.jpg'.format(fileNum))
            fileNum += 1
            # 把图片存入
            urllib.request.urlretrieve('http://' + imageUrl, filename=absPath)


# 执行一号店图片爬取
def fristImageCrawlerMain(url, toPath):
    fristiImageCrawler(url, toPath)

if __name__=='__main__':
    url = r'https://search.yhd.com/c9719-0-0/mbname-b/a-s1-v0-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E5%A5%B3%E8%A3%85/'
    toPath = r'D:\qian_feng_education\first_project\myClass\一号店女装\image'
    fristImageCrawlerMain(url, toPath)