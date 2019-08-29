from myClass.headers import Headers
import urllib.request
import time
import re
import pickle

# 糗事百科爬虫
def jockCrawler(url):
    headers = Headers()
    headersDict = headers.allHeaders()
    res = urllib.request.Request(url, headers=headersDict)
    response = urllib.request.urlopen(res)
    time.sleep(10)
    HTML = response.read().decode('utf-8')
    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat, re.S)  # 如果编码urf-8和正则表达式都没问题，任然出现提取零数据，则让.匹配换行
    divList = re_joke.findall(HTML)
    jokeDict = {}
    num = 0
    for div in divList:
        time.sleep(5)
        # 用户名
        patH2 = r'<h2>(.*?)</h2>'
        reH2 = re.compile(patH2, re.S)
        reName = reH2.findall(div)[0]
        reName = reName.replace('\n', '')

        # 段子
        patSpan = r'<div class="content">\n<span>(.*?)</span>'  # html显示了换行就有换行符
        reSpan = re.compile(patSpan, re.S)
        reContent = reSpan.findall(div)[0]
        reContent = reContent.replace('\n', '')
        # 存字典
        num += 1
        print('成功爬取{}条'.format(num))
        jokeDict[reName] = reContent
    return jokeDict


# 执行糗事百科爬虫
def jockCrawlerMain():
    List = []
    for page in range(1, 14):
        url = r'https://www.qiushibaike.com/text/page/{}/'.format(page)
        jokeDict = jockCrawler(url)
        List.append(jokeDict)
        print('成功爬取第{}页'.format(page))

    path = r'D:\qian_feng_education\first_project\myClass\糗事百科\jock.txt'
    with open(path, 'wb') as f:
        pickle.dump(List, f)

if __name__=='__main__':
    jockCrawlerMain()