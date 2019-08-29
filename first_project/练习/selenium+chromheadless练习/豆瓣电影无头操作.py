from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

#设置谷歌的无头浏览器的参数
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options .add_argument("–proxy-server=http://120.132.18.138:8888")# 一定要注意，等号两边不能有空格

#创建无头浏览器对象
path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, options=options)

#打开豆瓣电影
url = 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action='
browser.get(url)
time.sleep(3)
#给豆瓣电影排行榜界面拍照
browser.save_screenshot('豆瓣电影1.png')

#让browser执行简单的js代码，滚动条滚动到底部，此时会一直发送ajax请求加载更多内容，加载过程需要时间
js = 'var q=document.documentElement.scrollTop=100000'
browser.execute_script(js)
time.sleep(10)
#给豆瓣电影排行榜界面拍照
browser.save_screenshot('豆瓣电影2.png')

#获取网页代码，保存到文件中
html = browser.page_source
with open('豆瓣电影.html', 'w', encoding='utf8') as fp:
    fp.write(html)

time.sleep(3)
browser.quit() #退出浏览器































#退出浏览器
time.sleep(3)
browser.quit()