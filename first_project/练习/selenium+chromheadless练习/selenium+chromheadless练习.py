from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

#设置谷歌的无头浏览器
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#创建无头浏览器对象
path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, options=options)

#打开百度
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)

#在框中输入内容
search_input = browser.find_element_by_id('kw') #找到输入框
search_input.send_keys('美女')
time.sleep(1)

#输入关闭后点击搜索按钮
search_button = browser.find_elements_by_class_name('s_btn')[0]
search_button.click()
time.sleep(3)

#点击指定一张图片
meivn_img = browser.find_element_by_xpath('//*[@id="1"]/div[2]/div[2]/a[3]/img')
meivn_img.click()
time.sleep(5)

#浏览器截图
browser.save_screenshot('meinv.png')

time.sleep(3)
browser.quit() #退出浏览器