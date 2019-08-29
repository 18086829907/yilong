from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument("–proxy-server=http://120.132.18.138:8888")
# 创建无头浏览器对象
path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, options=options)
# 打开京东商品页
# url = 'https://item.jd.com/100001200571.html'
url = 'https://item.jd.com/100003827446.html'
browser.get(url)
time.sleep(3)
# 让browser执行简单的js代码，滚动条滚动到底部，此时会一直发送ajax请求加载更多内容，加载过程需要时间
for i in range(3):
    js = 'var q=document.documentElement.scrollTop=100000'
    browser.execute_script(js)
    time.sleep(2)
# 获取网页代码
html1 = browser.page_source
with open('textinner.html', 'w', encoding='utf8') as f:
    f.write(html1)
time.sleep(3)

#找到规格与包装标签并点击，再获取网页

# 退出浏览器
browser.quit()
