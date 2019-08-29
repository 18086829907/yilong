import urllib.request
import re
import time
import random

def http_image(src):
    url_img = src.group(1) + 'http://www.yikexun.cn/' + src.group(2) + src.group(3)
    return url_img

def get_text(url):
    #创建内容请求体
    request = handler_request(url)
    #发送请求
    response = urllib.request.urlopen(request).read().decode()
    #解析内容
    #提取内容
    pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
    content = pattern.findall(response)[0]
    #替换全部图片内容为完整url
    content = re.sub(r'(<img.*?src=")(.*?)(".*?>)', http_image, content)
    return content

def parse_content(content):
    pat = r'<h3><a href="(/lizhi/qianming/\d+\.html)"><b>(.*?)</b></a></h3>'
    pattern = re.compile(pat)
    #返回的标题是一个列表，列表中的元素都是元组，元素中第一个元素就是正则中第一个小括号匹配到的内容，元素中的二个元素就是正则中第二个小括号匹配到的内容
    lis = pattern.findall(content)
    #遍历列表
    for href_title in lis:
        #获取内容的链接
        a_href = 'http://www.yikexun.cn' + href_title[0]
        #获取标题
        title = href_title[1]
        #向a_href发送请求，获取响应内容
        content = get_text(a_href)
        #写入到html文件中
        string = '<h1>{}</h1>{}'.format(title, content)
        with open('lizhi.html', 'a') as f:
            f.write(string)
        # time.sleep(random.randint(10, 30))

def handler_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_{}.html'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page+1):
        #根据url和page去生成指定的request
        url = url.format(page)
        request = handler_request(url)
        #发送请求
        content = urllib.request.urlopen(request).read().decode()
        #解析内容
        parse_content(content)
        # time.sleep(random.randint(10,30))

if __name__=='__main__':
    main()