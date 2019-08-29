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

#打开百度
url = 'https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0xf3b67be0000a3ece&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=02003390_5_hao_pg&rsv_enter=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100'
browser.get(url)
time.sleep(3)

#保存截图
browser.save_screenshot('./ipImg/ip.png')
time.sleep(3)

#退出浏览器
browser.quit()