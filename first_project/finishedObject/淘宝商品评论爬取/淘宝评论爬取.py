import urllib.request
import urllib.parse
import time
import random
import json
import re

class taobaoSpider():
    def __init__(self, page):
        self.page = page
        self.url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=589815124915&spuId=1182940081&sellerId=2838892713&order=3&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvvvvRvpWvjQCkvvvvvjiPRFqhtjYnn2dv0jYHPmPvtjYPRLcwQjiEnLSWAjQtvpvhvvvvvUhCvCLwjvz%2FVaMwzn1FkDSSjNsbzUC4946CvvyvmRCoHBZvQH%2FrvpvEvv3R6DHBvbma2QhvCvvvMMGEvpCWvvbqvvw%2BdbmDYCywaZRQ0f0DW3CQog0HsXZpVcIUDajxALwpEcqh1jc6%2Bul08qknIOZtIoYbDpcBIb8rwZHlibmxdX3z8SoxfwoOdIyCvvOUvvVva6RivpvUvvmvrNdsxWRtvpvIvvvvvhCvvvvvvvUDphvW8QvvvAivpC29vvv28yCvhhvvvvWuphvppvhCvvOvCvvvphvtvpvhvvvvv8wCvvpvvUmm3QhvCvvhvvmrvpvEvv3EZeYSvnBf&needFold=0'
        self.t = str(time.time()).split('.')
        self.get_data = {
            'currentPageNum': page,
            '_ksTS': '{}_{}'.format(self.t[0], self.t[1]),
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        }

    def handler_request(self):
        get_data = urllib.parse.urlencode(self.get_data)
        url = self.url + get_data
        request = urllib.request.Request(url=url, headers=self.headers)
        return request

    def run(self):
        request = self.handler_request()
        json_txt = urllib.request.urlopen(request).read().decode()
        #通过strip(' ()\r\n\t')去除json两端的非法字符
        json_txt = json_txt.strip(' ()\r\n\t')
        #通过正则去除json格式字符串的两端的小括号,此时json格式字符串两端有空白字符
        json_txt = re.sub(r'\(', '', json_txt)
        json_txt = re.sub(r'\)', '', json_txt)
        #将json格式字符串转化为python对象，lodas方法会自动去掉json格式字符串两端的空白字符
        lis = json.loads(json_txt)

def main():
    start_page = int(input('开始页码：'))
    end_page = int(input('结束页码：'))
    for page in range(start_page, end_page+1):
        spider = taobaoSpider(page)
        spider.run()
        time.sleep(random.random()*5)

if __name__ == '__main__':
    main()
