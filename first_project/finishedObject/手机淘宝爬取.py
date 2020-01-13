import re
import requests
import json
import time
t=time.time()
t=int(t)
print(t)
proxy = {'HTTP': 'HTTP://1.198.72.168:9999'}
# url="https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.4.11&appKey=12574478&t=1566286087111&sign=1aaae5ad812434bff3bd50be8c126db9&api=mtop.taobao.detail.getdetail&v=6.0&ttid=2017%40htao_h5_1.0.0&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22exParams%22%3A%22%7B%5C%22countryCode%5C%22%3A%5C%22CN%5C%22%7D%22%2C%22itemNumId%22%3A%22544895066973%22%7D"
url = "https://alisitecdn.m.taobao.com/pagedata/shop/index?pathInfo=shop/index&userId=1013371554&shopId=109405357&pageId=221322055"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
data = requests.get(url, headers=headers, proxies=proxy).content.decode('utf-8')

print(data)

s = re.findall(r'mtopjsonp1\((.+?}}}})', data)
print(s)
# print(s[0])
date1=json.loads(s[0])
print(type(date1))
# print(date1)
item=date1["data"]["item"]
title= item["title"]
img_list=item["images"]
commentCount=item["commentCount"]
guige=date1["data"]["props"]

print(title)
print(img_list)
print(commentCount)
print(guige)