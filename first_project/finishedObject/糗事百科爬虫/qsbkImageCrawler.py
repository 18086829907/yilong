import urllib.request
import urllib.parse
import re
import os
import time

def handler_request(url, page):
    url = url + str(page) + '/'
    headers = {
        'Host': 'www.qiushibaike.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '_ga=GA1.2.1859399017.1556469673; _qqq_uuid_="2|1:0|10:1562045710|10:_qqq_uuid_|56:YThmNzAxYjdlM2QyM2IxN2QxNDY5NTlhYWViMjYyY2ViMzlhYjI2Mg==|1ac500ef6d6b8091a8fd15272d0a1160d99ce14135163829ebc13e922e4b084c"; _gid=GA1.2.1959390664.1562045710; _xsrf=2|4e038820|33b1b9f7fd0de31d055be13f8384d0a1|1562052790; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1562045710,1562052791; _gat=1; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1562052980',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def download_image(content):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', re.S)
    lt = pattern.findall(content)
    # 遍历列表，下载图片
    for image_src in lt:
        # 先处理image_src
        image_src = 'https:' + image_src
        # 发送请求，下载图片
        # 创建文件件
        dirname = 'qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        # 图片的名字叫啥
        filename = image_src.split('/')[-1]
        filepath = dirname + '/' + filename
        print('%s图片正在下载...' % filename)
        urllib.request.urlretrieve(image_src, filepath)
        print('%s图片下载结束...' % filename)
        time.sleep(1)

def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page+1):
        print('第%s页开始下载...' % page)
        # 生成请求对象
        request = handler_request(url, page)
        # 发送请求对象，获取响应内容
        content = urllib.request.urlopen(request).read().decode()
        # 解析下载内容，提取所有的图片链接，下载图片
        download_image(content)
        print('第%s页开始下载结束' % page)
        time.sleep(2)

if __name__ == '__main__':
    main()