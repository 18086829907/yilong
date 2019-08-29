# -*- coding: utf-8 -*-
import scrapy
import re
class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://www.github.com/login/']
    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, #自动从response中寻找from表单
            formdata={'login': '18086829907',    #<input name='login'...>, 用户名，即字典第一个key = input标签中name的值
                      'password': '135cylpsx'},    ##<input name='password'...>, 密码，即字典第二个key = input标签的name值
            callback=self.after_login,
            formxpath='//*[@id="login"]/form',    #xpath定位form表单，如果有两个及以上时使用
            dont_filter=False,    #不过滤这条请求
        )
    #处理返回数据
    def after_login(self, response):

        print(re.findall('justin', response.text))    #验证是否有用户名，有多个即成功登录