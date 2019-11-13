#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from lxml import etree
import os
import urllib.request

browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('https://www.mzitu.com/197634')
try:
    time.sleep(3)
    html = browser.page_source
    html_obj = etree.HTML(html)
    img = str(html_obj.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')[0])
    page = html_obj.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')[0]
    title = str(html_obj.xpath('/html/body/div[2]/div[1]/h2/text()')[0])
    browser.quit()
    imgs = []
    for i in range(1,10):
        img = img[0:-5] + str(i) + '.jpg'
        imgs.append(img)
    for j in range(10,int(page)+1):
        img = img[0:-6] + str(j) + '.jpg'
        imgs.append(img)
    dirName = os.path.join('C:\妹子图', title)
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        n = 0
        for image_src in imgs:
            browser.get(image_src)
            image = browser.page_source
            print(image)
            # absPath = os.path.join(dirName, str(n) + '.jpg')
            # with open(absPath, 'wb') as f:
            #     f.write(image)
            time.sleep(3)

finally:
    browser.quit()