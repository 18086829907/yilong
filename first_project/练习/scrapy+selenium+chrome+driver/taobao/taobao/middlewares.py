from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import requests

class ProxyUserAgentMiddleware():
    def __init__(self, proxy_url):
        self.logger = getLogger(__name__)
        self.proxy_url = proxy_url

    def get_random_proxy(self):
        try:
            response=requests.get(self.proxy_url)
            proxy = response.text
            return proxy
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        proxy = self.get_random_proxy()
        uri = 'https://{}'.format(proxy)
        request.meta['proxy']=uri

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(proxy_url=settings.get('PROXY_URL'))

class SeleniumMiddleware():
    def __init__(self, timeout=None):
        self.timeout = timeout
        self.logger = getLogger(__name__)

    def process_request(self, request, spider):
        proxy = request.meta['proxy']
        chrome_options = webdriver.ChromeOptions()
        self.logger.debug('启用代理'+proxy)
        chrome_options.add_argument('-proxy-server=' + proxy)
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.set_window_size(1400,700)
        browser.set_page_load_timeout(self.timeout)
        wait = WebDriverWait(browser, self.timeout)
        self.logger.debug('chromeDriver is Starting')
        page = request.meta.get('page', 1)
        try:
            browser.get(request.url)
            if page > 1:
                input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
                submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
                input.clear()
                input.send_keys(page)
                submit.click()
            wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'), str(page)))
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
            browser.quit()
            return HtmlResponse(url=request.url, body=browser.page_source, request=request, encoding='utf-8', status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(timeout=settings.get('SELENIUM_TIMEOUT'))