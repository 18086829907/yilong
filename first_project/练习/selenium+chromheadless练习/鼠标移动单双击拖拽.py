from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#设置谷歌的无头浏览器
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#创建无头浏览器对象
path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, options=options)

#打开豆瓣电影
url = 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action='
browser.get(url)
time.sleep(3)

# browser.maximizez-window()  # 最大化窗口
browser.get(url)
browser.save_screenshot('xxx.png') # 保存浏览器截图
browser.find_element_by_id() #返回对象
browser.find_elements_by_class() # 返回对象列表
browser.find_element_by_id('kw').send_kdy('搜索关键字')
browser.find_element_by_id('su').click()  # 点击选中对象
browser.find_element_by_class_name()  # 根据类名来筛选,类名只能写一个!!!
browser.page_source # 获取渲染后页面代码
browser.get_cookies() # 获取当前页面cookie
browser.find_element_by_di('kw').send_key(Keys.CONTROL, 'a')  # ctrl +a 全选输入框内容
browser.find_element_by_id('kw').send_key(Keys.RETURN)  # 模拟点击Enter回车键
browser.find_element_by_id('kw').clear()  # 清除输入框内容
browser.current_url # 当前请求的url
browser.close() # 关闭当前页面
browser.quit() # 退出浏览器
browser.forward()     #前进
browser.back()        # 后退

# 鼠标移动到 ac 位置
ac = browser.find_element_by_xpath('element')
ActionChains(browser).move_to_element(ac).perform()


# 在 ac 位置单击
ac = browser.find_element_by_xpath("elementA")
ActionChains(browser).move_to_element(ac).click(ac).perform()

# 在 ac 位置双击
ac = browser.find_element_by_xpath("elementB")
ActionChains(browser).move_to_element(ac).double_click(ac).perform()

# 在 ac 位置右击
ac = browser.find_element_by_xpath("elementC")
ActionChains(browser).move_to_element(ac).context_click(ac).perform()

# 在 ac 位置左键单击hold住
ac = browser.find_element_by_xpath('elementF')
ActionChains(browser).move_to_element(ac).click_and_hold(ac).perform()

# 将 ac1 拖拽到 ac2 位置
ac1 = browser.find_element_by_xpath('elementD')
ac2 = browser.find_element_by_xpath('elementE')
ActionChains(browser).drag_and_drop(ac1, ac2).perform()
