# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github']
    start_urls = ['https://github.com/login/']    #开始url是登录界面

    def parse(self, response):
        #构造post请求的formdata
        post_data = {
            'login': "18086829907",
            'password': "135cylpsx",
            'authenticity_token': response.xpath(r'//*[@id="login"]/form/input[2]/@value').extract_first(),
            'utf8': response.xpath(r'//*[@id="login"]/form/input[1]/@value').extract_first(),
            'commit': response.xpath(r'//*[@id="login"]/form/div[3]/input[4]/@value').extract_first(),
            'webauthn-support': response.xpath(r'//*[@id="login"]/form/div[3]/input[3]/@value').extract_first(),
        }
        #携带post数据向接口地址发送post请求
        yield scrapy.FormRequest('https://github.com/session', formdata=post_data, callback=self.after_login, dont_filter=True)
    #处理返回数据
    def after_login(self, response):
        print(re.findall('justin', response.text))    #验证是否有用户名，有多个即成功登录