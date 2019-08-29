# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class RenrenwangSpider(CrawlSpider):
    name = 'renrenwang'
    allowed_domains = ['wwww.renren.com']
    start_urls = ['http://www.renren.com/971351636/profile']

    def start_requests(self):
        #这个cookey是在正确登录后，我的主页里面的cookie，没有token验证，即可直接携带正确的cookie模拟登录
        cookies = 'anonymid=jxl276snx7rdrl; _r01_=1; ln_uact=18086829907; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; _de=2E757325973CAD40D28173EB34A8CC93; jebe_key=22738ca2-ea84-4c1c-a594-4a186dcf246f%7Cd68038a7330c1c27a93e726b5b24a666%7C1562026527492%7C1%7C1563949661795; depovince=SC; JSESSIONID=abcSfk_6u-eYacP1Zi0Xw; ick_login=e0548aeb-4373-467f-be9b-4d5659e0e642; jebecookies=2fd2ab9c-bc60-41d9-82ed-89f16ae80b66|||||; p=a2a003c1f995f16053defe46452101076; first_login_flag=1; t=516809734be6077dfce136d80ccdb1726; societyguester=516809734be6077dfce136d80ccdb1726; id=971351636; xnsid=8bd9cd10; loginfrom=syshome; jebe_key=22738ca2-ea84-4c1c-a594-4a186dcf246f%7Cd68038a7330c1c27a93e726b5b24a666%7C1565316757615%7C1%7C1565316758911; wp_fold=0'
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')} #将cookies字符串转化为字典格式
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse_item,
            cookies=cookies
        )

    def parse_item(self, response):
        print(re.findall(r'新用户2', response.text))    #验证登录是否成功，即返回的响应中是否包含新用户
        yield scrapy.Request('http://www.renren.com/971351636/profile?v=info_timeline', callback=self.parse_item2, dont_filter=True)

    def parse_item2(self, response):
        print(re.findall(r'感情状态', response.text))