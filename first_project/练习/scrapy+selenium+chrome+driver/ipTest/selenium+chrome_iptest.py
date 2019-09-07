from selenium import webdriver
import requests
response = requests.get('http://101.205.52.157:8000/random')
proxy = response.text
print('启用代理：'+proxy)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-proxy-server=http://'+proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')