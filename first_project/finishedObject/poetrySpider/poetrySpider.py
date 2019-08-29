import requests
from lxml import etree

class poetrySpider():
    s = requests.Session()
    def __init__(self, loginUrl, clickLoginUrl):
        self.loginUrl = loginUrl
        self.clickLoginUrl = clickLoginUrl
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
        self.innerGetUrl = 'https://so.gushiwen.org/user/collect.aspx?type=s&id=342290&sort=t'

    #完成登录后访问收藏夹内容
    def collection(self):
        # self.s.get(self.innerGetUrl)
        pass


    def manualInput(self):
        #get登录界面
        r1 = self.s.get(url=self.loginUrl, headers=self.headers)
        #获取需要的post参数
        tree = etree.HTML(r1.text)
        __VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
        __VIEWSTATEGENERATOR = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
        picture = 'https://so.gushiwen.org' + tree.xpath('//img[@id="imgCode"]/@src')[0]
        r2 = self.s.get(url=picture, headsers=self.headers)
        with open('picture.jpg', 'wb') as f:
            f.write(r2.content)
        code = input('请输入验证码：')
        #post参数
        post_data = {
            '__VIEWSTATE': __VIEWSTATE,
            '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
            'from': '',
            'email': '18086829907',
            'pwd': '135cylpsx',
            'code': code,
            'denglu': '登录',
        }
        r3 = self.s.post(self.clickLoginUrl, data=post_data, headers=self.headers)
        print(r3.text)
        #完成登录后访问收藏夹内容
        self.collection()

    def run(self):
        #手动下载图片验证登录
        self.manualInput()

def main():
    #登录界面的url
    loginUrl = 'https://so.gushiwen.org/user/login.aspx?'
    #点击登录后，post请求的url
    clickLoginUrl = 'https://so.gushiwen.org/user/login.aspx'
    spider = poetrySpider(loginUrl, clickLoginUrl)
    spider.run()

if __name__ == '__main__':
    main()