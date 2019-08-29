from selenium import webdriver
import time
#创建一个模拟浏览器对象
path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)

#打开豆瓣电影
url = 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action='
browser.get(url)
time.sleep(3)

#让browser执行简单的js代码，滚动条滚动到底部，此时会一直发送ajax请求加载更多内容，加载过程需要时间
js = 'var q=document.documentElement.scrollTop=100000'
browser.execute_script(js)
time.sleep(10)



































#退出浏览器
time.sleep(3)
browser.quit()