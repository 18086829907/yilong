import time
import random
from myClass import mySpider
url = 'http://bang.360.cn/youpin/search?from=index&pn={}'
urls = []
for i in range(84, 109):
    urls.append(url.format(i))

path = r'D:\qian_feng_education\first_project\finishedObject\同城帮数据爬取\htmls\{}.html'

num = 84
for i in urls:
    myCra = mySpider.MyCrawler()
    html = myCra.getHtmlBytes(i)
    myCra.writeFileHtmlBytes2Html(html, path.format(num))
    num += 1
    print('成功爬取第{}页'.format(num))
    time.sleep(random.randint(10,30))