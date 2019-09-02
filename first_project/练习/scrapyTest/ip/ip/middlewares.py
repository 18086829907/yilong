# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import logging
import requests

class ProxyUserAgentMiddleware():
    def __init__(self, proxy_url):
        self.logger = logging.getLogger(__name__)
        self.proxy_url = proxy_url

    def get_random_proxy(self):
        try:
            response=requests.get(self.proxy_url)
            proxy = response.text
            return proxy
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        # if request.meta.get('retry_times'):
        #     proxy = self.get_random_proxy()
        #     if proxy:
        #         uri = 'https://{}'.format(proxy)
        #         request.meta['splash']['args']['proxy'] = uri
        #     userAgent = agent.allHeaders()
        #     request.headers['User_Agent'] = userAgent
        proxy = self.get_random_proxy()
        uri = 'https://{}'.format(proxy)
        request.meta['splash']['args']['proxy'] = uri
        # userAgent = agent.allHeaders()
        # request.headers['User_Agent'] = userAgent

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(proxy_url=settings.get('PROXY_URL'))
