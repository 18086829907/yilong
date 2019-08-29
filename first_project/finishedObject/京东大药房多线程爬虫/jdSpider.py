# -*- coding: utf-8 -*
import time
from lxml import etree
import threading
from queue import Queue
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random
import re
import json
from myClass.mySql import MySql
from selenium.common.exceptions import TimeoutException

commodityList = []
#采集线程类
class CrawlThread(threading.Thread):
    def __init__(self, crawlThreadName, urlQueue, htmlQueue):
        super(CrawlThread, self).__init__()
        self.crawlThreadName = crawlThreadName
        self.urlQueue = urlQueue
        self.htmlQueue = htmlQueue

    # 启动无头浏览器访问该url,并将html存入htmlQueue
    def handler_request(self, url):
        print('{}启动无头浏览器'.format(self.crawlThreadName))
        # 设置谷歌的无头浏览器
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # options.add_argument("–proxy-server=http://120.132.18.138:8888")
        # 创建无头浏览器对象
        path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        browser = webdriver.Chrome(executable_path=path, options=options)
        try:
            try:
                # 打开京东商品页
                browser.get(url)
            except TimeoutException as e:
                print('开大此url超时：{}'.format(url))
            print('{}打开了京东页面，url:{}'.format(self.crawlThreadName, url))
            print('等待3秒')
            time.sleep(3)
            # 让browser执行简单的js代码，滚动条滚动到底部，此时会一直发送ajax请求加载更多内容，加载过程需要时间
            for i in range(5):
                js = 'var q=document.documentElement.scrollTop=100000'
                browser.execute_script(js)
                sleepTime = random.random()*20
                print('{}操作无头浏览器，向下滑动{}次，等待{}'.format(self.crawlThreadName, i+1, sleepTime))
                time.sleep(sleepTime)
            # 获取网页代码
            html = browser.page_source
            print('{}获取html,等待3秒'.format(self.crawlThreadName))
            time.sleep(3)
        finally:
            # 退出浏览器
            browser.quit()
            print('{}退出无头浏览器'.format(self.crawlThreadName))
        return html
        
    #在url队列中取值，并访问每个url，将返回值存放到htmlQueue
    def run(self):
        print('{}开始'.format(self.crawlThreadName))
        n = 1
        while True:
            if self.urlQueue.empty():
                break
            url = self.urlQueue.get()
            #启动无头浏览器访问该url,并将返回的html存入htmlQueue
            html = self.handler_request(url)
            self.htmlQueue.put(html)
            print('{}在htmlQueue中添加了{}条html'.format(self.crawlThreadName, n+1))
            n += 1
        print('{}结束'.format(self.crawlThreadName))

#解析线程类
class ParseThread(threading.Thread):
    def __init__(self, parseThreadName, htmlQueue):
        super(ParseThread, self).__init__()
        self.parseThreadName = parseThreadName
        self.htmlQueue = htmlQueue

    #返回内页的所有解析数据
    def innerParse(self, html):
        #解析：
            #商品介绍
                #子图列表、品牌、商品名称、商品编号、货号、
                #店铺、商品毛重、商品产地、（国产/进口、国别、）电源、分类、（类别、药品类别、）（特色、特性、特点、）
                #价位、规格、尺寸、原料、数量、用途、性质、尺码、裙长、面料、厚度、领型、流行元素、适用季节、是否有兜、
                #适用场景、适用人群、分子筛、调码方式、记忆功能、测量部位
                #智能警报、充电方式、压力范围、工作模式、压力模式、重量、（适用部位、部位、）电源方式、
                #（适用症状、症状、）、包装、蓝帽标识、款式、袖长、是否可外穿、形态、形状
                #使用方式、风格、材质、使用对象、选购热点、适用类型、（药品剂型、剂型、产品类型）
                #使用方法、主要成份、功效、功能、控制类型
            #商品详情图片、商品视频
            #规格与包装
                #医疗器械注册证编号或者备案凭证编号、医疗器械名称、型号、注册人或者备案人信息、生产企业、生产许可证或者备案凭证编号、高血压警示、语音播报、加压方式
                #测量时间、记忆功能（次）、测量范围、是否自动关闭、测量方法、测量时间、测量精度、产品尺寸（cm）、显示方式、结构及组成、适用范围、
                #通气模式、氧气浓度、氧气流量、功率（w）、雾化颗粒是否可调、雾化量是否可调、禁忌症、贮藏条件、压缩机寿命、雾化粒大小分布
                #容量、工作模式、治疗板尺寸、产品净重（kg）、最大载重（kg）、座宽（cm）、折叠后长*宽*高（cm）、前/后轮尺寸（cm）、
                # 轮胎类型、最小转弯半径（cm）、爬坡度数（°）、电机功率（w）、电池类型、电池容量（AH）、理论充电时间（H）、最大速率（KM/H）、额定续航（KM）
                #药品商品名、药品通用名、批准文号、产品规格、用法用量、有效期、适用症/功能主治、包装规格
                #库内是否按批号管理、库内是否按供应商管理、不良反应、适用人群
                #保质期、功用、款式
        #返回：
        tree = etree.HTML(html)
        ztlbList = tree.xpath('//div[@id="spec-list"]/ul/li[*]/img/@src') #子图列表
        ztlb = []
        for item in ztlbList:
            if 'https:' not in item:
                item = 'https:' + item
                ztlb.append(item)
        try:
            pinpai = tree.xpath('//ul[@id="parameter-brand"]/li/a/text()')[0] #品牌
        except IndexError as e:
            try:
                pinpai = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "品牌")]/a/text()')[0]
            except IndexError as e:
                pinpai = ''
        try:
            spmc = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "商品名称")]/text()')[0].split('：')[-1]
        except IndexError as e:
            spmc = ''
        try:
            spbh = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "商品编号")]/text()')[0].split('：')[-1]
        except IndexError as e:
            spbh = ''
        try:
            huohao = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "货号")]/text()')[0].split('：')[-1]
        except IndexError as e:
            huohao = ''
        try:
            dianpu = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "店铺")]/text()')[0].split('：')[-1]
        except IndexError as e:
            dianpu = ''
        try:
            spmz = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "商品毛重")]/text()')[0].split('：')[-1]
        except IndexError as e:
            spmz = ''
        try:
            spcd = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "商品产地")]/text()')[0].split('：')[-1]
        except IndexError as e:
            spcd = ''
        try:
            gcjk = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "国产/进口")]/text()')[0].split('：')[-1]
        except IndexError as e:
            gcjk = ''
        try:
            guobie = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "国别")]/text()')[0].split('：')[-1]
        except IndexError as e:
            guobie = ''
        gcjk = gcjk + guobie
        try:
            dianyuan = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "电源：")]/text()')[0].split('：')[-1]
        except IndexError as e:
            dianyuan = ''
        try:
            fenlei = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "分类")]/text()')[0].split('：')[-1]
        except IndexError as e:
            fenlei = ''
        try:
            leibie = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "类别")]/text()')[0].split('：')[-1]
        except IndexError as e:
            leibie = ''
        try:
            yplb = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "药品类别")]/text()')[0].split('：')[-1]
        except IndexError as e:
            yplb = ''
        leibie = leibie + yplb
        try:
            tese = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "特色")]/text()')[0].split('：')[-1]
        except IndexError as e:
            tese = ''
        try:
            texing = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "特性")]/text()')[0].split('：')[-1]
        except IndexError as e:
            texing = ''
        try:
            tedian = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "特点")]/text()')[0].split('：')[-1]
        except IndexError as e:
            tedian = ''
        tese = tese + texing + tedian
        try:
            jiawei = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "价位")]/text()')[0].split('：')[-1]
        except IndexError as e:
            jiawei = ''
        try:
            guige = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "规格")]/text()')[0].split('：')[-1]
        except IndexError as e:
            try:
                guige = tree.xpath(
                    '//*[@id="specifications"]/table/tbody/tr/td[contains(text(),"规格")]/following-sibling::td/text()')[0]
            except IndexError as e:
                guige = ''
        try:
            chicun = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "尺寸")]/text()')[0].split('：')[-1]
        except IndexError as e:
            chicun = ''
        try:
            yuanliao = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "原料")]/text()')[0].split('：')[-1]
        except IndexError as e:
            yuanliao = ''
        try:
            shuliang = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "数量")]/text()')[0].split('：')[-1]
        except IndexError as e:
            shuliang = ''
        try:
            yongtu = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "用途")]/text()')[0].split('：')[-1]
        except IndexError as e:
            yongtu = ''
        try:
            xingzhi = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "性质")]/text()')[0].split('：')[-1]
        except IndexError as e:
            xingzhi = ''
        try:
            chima = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "尺码")]/text()')[0].split('：')[-1]
        except IndexError as e:
            chima = ''
        try:
            qunchang = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "裙长")]/text()')[0].split('：')[-1]
        except IndexError as e:
            qunchang = ''
        try:
            mianliao = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "面料")]/text()')[0].split('：')[-1]
        except IndexError as e:
            mianliao = ''
        try:
            houdu = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "厚度")]/text()')[0].split('：')[-1]
        except IndexError as e:
            houdu = ''
        try:
            lingxiang = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "领型")]/text()')[0].split('：')[-1]
        except IndexError as e:
            lingxiang = ''
        try:
            lxys = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "流行元素")]/text()')[0].split('：')[-1]
        except IndexError as e:
            lxys = ''
        try:
            syjj = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用季节")]/text()')[0].split('：')[-1]
        except IndexError as e:
            syjj = ''
        try:
            sfyd = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "是否有兜")]/text()')[0].split('：')[-1]
        except IndexError as e:
            sfyd = ''
        try:
            sycj = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用场景")]/text()')[0].split('：')[-1]
        except IndexError as e:
            sycj = ''
        try:
            syrq = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用人群")]/text()')[0].split('：')[-1]
        except IndexError as e:
            syrq = ''
        try:
            fzs = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "分子筛")]/text()')[0].split('：')[-1]
        except IndexError as e:
            fzs = ''
        try:
            dmfs = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "调码方式")]/text()')[0].split('：')[-1]
        except IndexError as e:
            dmfs = ''
        try:
            jygn = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "记忆功能")]/text()')[0].split('：')[-1]
        except IndexError as e:
            jygn = ''
        try:
            clbw = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "测量部位")]/text()')[0].split('：')[-1]
        except IndexError as e:
            clbw = ''
        try:
            znbj = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "智能警报")]/text()')[0].split('：')[-1]
        except IndexError as e:
            znbj = ''
        try:
            cdfs = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "充电方式")]/text()')[0].split('：')[-1]
        except IndexError as e:
            cdfs = ''
        try:
            ylfw = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "压力范围")]/text()')[0].split('：')[-1]
        except IndexError as e:
            ylfw = ''
        try:
            gzms = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "工作模式")]/text()')[0].split('：')[-1]
        except IndexError as e:
            gzms = ''
        try:
            ylms = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "压力模式")]/text()')[0].split('：')[-1]
        except IndexError as e:
            ylms = ''
        try:
            zhongliang = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "重量")]/text()')[0].split('：')[-1]
        except IndexError as e:
            zhongliang = ''
        try:
            sybw = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用部位")]/text()')[0].split('：')[-1]
        except IndexError as e:
            sybw = ''
        try:
            buwei = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "部位")]/text()')[0].split('：')[-1]
        except IndexError as e:
            buwei = ''
        sybw = sybw + buwei
        try:
            dyfs = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "电源方式")]/text()')[0].split('：')[-1]
        except IndexError as e:
            dyfs = ''
        try:
            syzt = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用症状")]/text()')[0].split('：')[-1]
        except IndexError as e:
            syzt = ''
        try:
            zhuangtai = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "症状")]/text()')[0].split('：')[-1]
        except IndexError as e:
            zhuangtai = ''
        syzt = syzt + zhuangtai
        try:
            baozhuang = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "包装")]/text()')[0].split('：')[-1]
        except IndexError as e:
            try:
                baozhuang = tree.xpath('//*[@id="specifications"]/table/tbody/tr/td[contains(text(),"包装")]/following-sibling::td/text()')[0]
            except IndexError as e:
                baozhuang = ''
        try:
            lmbs = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "蓝帽标识")]/text()')[0].split('：')[-1]
        except IndexError as e:
            lmbs = ''
        try:
            kuanshi = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "款式：")]/text()')[0].split('：')[-1]
        except IndexError as e:
            kuanshi = ''
        try:
            sfkwc = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "是否可外穿")]/text()')[0].split('：')[-1]
        except IndexError as e:
            sfkwc = ''
        try:
            xingtai = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "形态")]/text()')[0].split('：')[-1]
        except IndexError as e:
            xingtai = ''
        try:
            xingzhuang = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "形状")]/text()')[0].split('：')[-1]
        except IndexError as e:
            xingzhuang = ''
        try:
            syfs = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "使用方式")]/text()')[0].split('：')[-1]
        except IndexError as e:
            syfs = ''
        try:
            fengge = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "风格")]/text()')[0].split('：')[-1]
        except IndexError as e:
            fengge = ''
        try:
            caizhi = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "材质")]/text()')[0].split('：')[-1]
        except IndexError as e:
            caizhi = ''
        try:
            xiuchang = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "袖长")]/text()')[0].split('：')[-1]
        except IndexError as e:
            xiuchang = ''
        try:
            sydx = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "使用对象")]/text()')[0].split('：')[-1]
        except IndexError as e:
            sydx = ''
        try:
            xgrd = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "选购热点")]/text()')[0].split('：')[-1]
        except IndexError as e:
            xgrd = ''
        try:
            sylx = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用类型")]/text()')[0].split('：')[-1]
        except IndexError as e:
            sylx = ''
        try:
            ypjx = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "药品剂型")]/text()')[0].split('：')[-1]
        except IndexError as e:
            ypjx = ''
        try:
            jixing = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "剂型")]/text()')[0].split('：')[-1]
        except IndexError as e:
            jixing = ''
        try:
            cplx = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "产品类型")]/text()')[0].split('：')[-1]
        except IndexError as e:
            cplx = ''
        ypjx = ypjx + jixing + cplx
        try:
            syff = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "使用方法")]/text()')[0].split('：')[-1]
        except IndexError as e:
            syff = ''
        try:
            zycf = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "成份") or contains(text(), "成分")]/text()')[0].split('：')[-1]
        except IndexError as e:
            zycf = ''
        try:
            gongxiao = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "功效")]/text()')[0].split('：')[-1]
        except IndexError as e:
            gongxiao = ''
        try:
            gongneng = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "功能")]/text()')[0].split('：')[-1]
        except IndexError as e:
            gongneng = ''
        try:
            kzlx = tree.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "控制类型")]/text()')[0].split('：')[-1]
        except IndexError as e:
            kzlx = ''
        #商品详情图片
        try:
            spxqtpCssStr = tree.xpath('//div[@id="J-detail-content"]/style/text()')[0]
            pat = r'(//img.*?(jpg|gif|png))'
            re_img = re.compile(pat, re.S)
            imgList = re_img.findall(spxqtpCssStr) #商品详情图片列表
            spxqtpCssbwz = []
            for item in imgList:
                spxqtpCssbwz.append(item[0])
            spxqtpCss = []
            for item in spxqtpCssbwz:
                if 'https:' not in item:
                    item = 'https:' + item
                    spxqtpCss.append(item)
        except IndexError as e:
            spxqtpCss = []
        try:
            spxqtpImgList = tree.xpath('//div[@id="J-detail-content"]//img/@src') #商品详情图片列表
            spxqtpImg = []
            for item in spxqtpImgList:
                if 'https:' not in item:
                    item = 'https:' + item
                    spxqtpImg.append(item)
        except IndexError as e:
            spxqtpImg = []
        spxqtp = []
        spxqtp.extend(spxqtpCss)
        spxqtp.extend(spxqtpImg)
        #商品视频
        try:
            spsp = tree.xpath('//video/@src')[0]
        except IndexError as e:
            spsp = ''
        try:
            ylqxzczbh = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "医疗器械注册证编号或者备案凭证编号")]/../dd/text()')[0]
        except IndexError as e:
            ylqxzczbh = ''
        try:
            ylqxmc = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "医疗器械名称")]/../dd/text()')[0]
        except IndexError as e:
            ylqxmc = ''
        try:
            xinghao = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "型号")]/../dd/text()')[0]
        except IndexError as e:
            xinghao = ''
        try:
            zcrhzbarxx = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "注册人或者备案人信息")]/../dd/text()')[0]
        except IndexError as e:
            zcrhzbarxx = ''
        try:
            scqy = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "生产企业")]/../dd/text()')[0]
        except IndexError as e:
            scqy = ''
        try:
            scxkzhbapzbh = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "生产许可证或者备案凭证编号")]/../dd/text()')[0]
        except IndexError as e:
            scxkzhbapzbh = ''
        try:
            gxyjs = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "高血压警示")]/../dd/text()')[0]
        except IndexError as e:
            gxyjs = ''
        try:
            yybb = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "语音播报")]/../dd/text()')[0]
        except IndexError as e:
            yybb = ''
        try:
            jyfs = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "加压方式")]/../dd/text()')[0]
        except IndexError as e:
            jyfs = ''
        try:
            clsj = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(),"测量时间")]/../dd/text()')[0]
        except IndexError as e:
            clsj = ''
        try:
            jygnc = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "记忆功能（次）")]/../dd/text()')[0]
        except IndexError as e:
            jygnc = ''

        try:
            clfw = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "测量范围")]/../dd/text()')[0]
        except IndexError as e:
            clfw = ''
        try:
            sfzdgb = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "是否自动关闭")]/../dd/text()')[0]
        except IndexError as e:
            sfzdgb = ''
        try:
            clff = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "测量方法")]/../dd/text()')[0]
        except IndexError as e:
            clff = ''
        try:
            clsj = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "测量时间")]/../dd/text()')[0]
        except IndexError as e:
            clsj = ''
        try:
            cljd = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "测量精度")]/../dd/text()')[0]
        except IndexError as e:
            cljd = ''
        try:
            cpcc = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "产品尺寸（cm）")]/../dd/text()')[0]
        except IndexError as e:
            cpcc = ''
        try:
            xsfs = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "显示方式")]/../dd/text()')[0]
        except IndexError as e:
            xsfs = ''
        try:
            jgjzc = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "结构及组成")]/../dd/text()')[0]
        except IndexError as e:
            jgjzc = ''
        try:
            syfw = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "适用范围")]/../dd/text()')[0]
        except IndexError as e:
            syfw = ''
        try:
            tqms = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "通气模式")]/../dd/text()')[0]
        except IndexError as e:
            tqms = ''
        try:
            yqnd = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "氧气浓度")]/../dd/text()')[0]
        except IndexError as e:
            yqnd = ''
        try:
            yqll = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "氧气流量")]/../dd/text()')[0]
        except IndexError as e:
            yqll = ''
        try:
            gonglv = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "功率")]/../dd/text()')[0]
        except IndexError as e:
            gonglv = ''
        try:
            whklsfkt = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "雾化颗粒是否可调")]/../dd/text()')[0]
        except IndexError as e:
            whklsfkt = ''
        try:
            whlsfkt = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "雾化量是否可调")]/../dd/text()')[0]
        except IndexError as e:
            whlsfkt = ''
        try:
            jjz = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "禁忌症")]/../dd/text()')[0]
        except IndexError as e:
            jjz = ''
        try:
            zctj = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "贮藏条件")]/../dd/text()')[0]
        except IndexError as e:
            zctj = ''
        try:
            ysjsm = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "压缩机寿命")]/../dd/text()')[0]
        except IndexError as e:
            ysjsm = ''
        try:
            whkldxfb = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "雾化粒大小分布")]/../dd/text()')[0]
        except IndexError as e:
            whkldxfb = ''
        try:
            rongliang = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "容量")]/../dd/text()')[0]
        except IndexError as e:
            rongliang = ''
        try:
            gdgzms = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "工作模式")]/../dd/text()')[0]
        except IndexError as e:
            gdgzms = '' #更多工作模式
        try:
            zlbcc = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "治疗板尺寸")]/../dd/text()')[0]
        except IndexError as e:
            zlbcc = ''
        try:
            cpjz = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "产品净重（kg）")]/../dd/text()')[0]
        except IndexError as e:
            cpjz = ''
        try:
            zdzz = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "最大载重（kg）")]/../dd/text()')[0]
        except IndexError as e:
            zdzz = ''
        try:
            zuokuan = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "座宽（cm）")]/../dd/text()')[0]
        except IndexError as e:
            zuokuan = ''
        try:
            zdh = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "折叠后长*宽*高（cm）")]/../dd/text()')[0]
        except IndexError as e:
            zdh = ''
        try:
            lcc = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "前/后轮尺寸（cm）")]/../dd/text()')[0]
        except IndexError as e:
            lcc = ''
        try:
            ltlx = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "轮胎类型")]/../dd/text()')[0]
        except IndexError as e:
            ltlx = ''
        try:
            zxzwbj = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "最小转弯半径（cm）")]/../dd/text()')[0]
        except IndexError as e:
            zxzwbj = ''
        try:
            ppds = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "爬坡度数（°）")]/../dd/text()')[0]
        except IndexError as e:
            ppds = ''
        try:
            dclx = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "电池类型")]/../dd/text()')[0]
        except IndexError as e:
            dclx = ''
        try:
            dcrl = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "电池容量（AH）")]/../dd/text()')[0]
        except IndexError as e:
            dcrl = ''
        try:
            llcdsj = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "理论充电时间（H）")]/../dd/text()')[0]
        except IndexError as e:
            llcdsj = ''
        try:
            zdsl = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "最大速率（KM/H）")]/../dd/text()')[0]
        except IndexError as e:
            zdsl = ''
        try:
            edxh = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "额定续航（KM）")]/../dd/text()')[0]
        except IndexError as e:
            edxh = ''
        try:
            ypspm = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "药品商品名")]/../dd/text()')[0]
        except IndexError as e:
            ypspm = ''
        try:
            yptym = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "药品通用名")]/../dd/text()')[0]
        except IndexError as e:
            yptym = ''
        try:
            pzwh = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "批准文号")]/../dd/text()')[0]
        except IndexError as e:
            pzwh = ''
        try:
            cpgg = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "产品规格")]/../dd/text()')[0]
        except IndexError as e:
            cpgg = ''
        try:
            yfyl = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "用法用量")]/../dd/text()')[0]
        except IndexError as e:
            yfyl = ''
        try:
            yxq = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "有效期")]/../dd/text()')[0]
        except IndexError as e:
            yxq = ''
        try:
            syzgnzz = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "适用症/功能主治")]/../dd/text()')[0]
        except IndexError as e:
            syzgnzz = ''
        try:
            bzgg = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "包装规格")]/../dd/text()')[0]
        except IndexError as e:
            bzgg = ''
        try:
            knsfaphgl = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "库内是否按批号管理")]/../dd/text()')[0]
        except IndexError as e:
            knsfaphgl = ''
        try:
            knsfagysgl = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "库内是否按供应商管理")]/../dd/text()')[0]
        except IndexError as e:
            knsfagysgl = ''
        try:
            blfy = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "不良反应")]/../dd/text()')[0]
        except IndexError as e:
            blfy = ''
        try:
            bzq = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "保质期")]/../dd/text()')[0]
        except IndexError as e:
            try:
                bzq = tree.xpath('//*[@id="specifications"]/table/tbody/tr/td[contains(text(),"保质期")]/following-sibling::td/text()')[0]
            except IndexError as e:
                bzq = ''
        try:
            gongyong = tree.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "功用")]/../dd/text()')[0]
        except IndexError as e:
            gongyong = ''
        try:
            synl = tree.xpath('//*[@id="specifications"]/table/tbody/tr/td[contains(text(),"适用年龄")]/following-sibling::td/text()')[0]
        except IndexError as e:
            synl = ''
        return synl, xiuchang, ztlb, pinpai, spmc, spbh, huohao, dianpu, leibie, spmz, spcd, gcjk, dianyuan, fenlei, yplb, tese, jiawei, guige, chicun, yuanliao, shuliang, yongtu, xingzhi, chima, qunchang, mianliao, houdu, lingxiang, lxys, syjj, sfyd, sycj, syrq, fzs, dmfs, jygn, clbw, spsp, spxqtp, znbj, cdfs, ylfw, gzms, ylms, zhongliang, sybw, dyfs, syzt, baozhuang, lmbs, kuanshi, sfkwc, xingtai, xingzhuang, syfs, fengge, caizhi, sydx, xgrd, sylx, ypjx, syff, zycf, gongxiao, gongneng, kzlx, ylqxzczbh, ylqxmc, xinghao, zcrhzbarxx, scqy, scxkzhbapzbh, gxyjs, yybb, jyfs, clsj, jygnc, clfw, sfzdgb, clff, cljd, cpcc, xsfs, jgjzc, syfw, tqms, yqnd, yqll, gonglv, whklsfkt, whlsfkt, jjz, zctj, ysjsm, whkldxfb,rongliang, gdgzms, zlbcc, cpjz, zdzz, zuokuan, zdh, lcc, ltlx, zxzwbj, ppds, dclx, dcrl, llcdsj, zdsl, edxh, ypspm, yptym, pzwh, cpgg, yfyl, yxq, syzgnzz, bzgg, knsfaphgl, knsfagysgl, blfy, bzq, gongyong

    # 启动无头浏览器访问该url,并将html存入htmlQueue
    def handler_request(self, url):
        print('{}启动无头浏览器'.format(self.parseThreadName))
        # 设置谷歌的无头浏览器
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # options.add_argument("–proxy-server=http://120.132.18.138:8888")
        # 创建无头浏览器对象
        path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        browser = webdriver.Chrome(executable_path=path, options=options)
        try:
            # 打开京东商品页
            try:
                browser.get(url)
            except TimeoutException as e:
                print('打开url超时：{}'.format(url))
            print('{}打开了京东页面，url:{}'.format(self.parseThreadName, url))
            print('等待3秒')
            time.sleep(3)
            # 给京东商品页拍照
            browser.save_screenshot('./screenshot/{}_1.png'.format(url))
            # 让browser执行简单的js代码，滚动条滚动到底部，此时会一直发送ajax请求加载更多内容，加载过程需要时间
            for i in range(10):
                js = 'var q=document.documentElement.scrollTop=100000'
                browser.execute_script(js)
                sleepTime = random.random()*20
                print('{}操作无头浏览器，向下滑动{}次，等待{}'.format(self.parseThreadName, i+1, sleepTime))
                time.sleep(sleepTime)
            browser.save_screenshot('./screenshot/{}_2.png'.format(url))
            # 获取网页代码
            html = browser.page_source
            print('{}获取html,等待3秒'.format(self.parseThreadName))
            time.sleep(3)
        finally:
            # 退出浏览器
            browser.quit()
            print('{}退出无头浏览器'.format(self.parseThreadName))
        return html

    #传入商品列表页，遍历每个商品，解析商品列表页的每个商品以及每个商品的内页
    def htmlParse(self, html):
        tree = etree.HTML(html)
        #懒加载data-lazy-img
        #获取一级分类，二级分类，三级分类，四级分类，商品图片，商品价格，商品标题，评论数量，店铺名称，商品图标
        try:
            type_1 = tree.xpath('//div[@id="J_crumbsBar"]/div/div/div/div[1]/a/text()')[0]
        except IndexError as e:
            type_1 = ''
        try:
            type_2 = tree.xpath('//div[@id="J_crumbsBar"]/div/div/div/div[2]//span/text()')[0]
        except IndexError as e:
            type_2 = ''
        try:
            type_3 = tree.xpath('//div[@id="J_crumbsBar"]/div/div/div/div[3]//span/text()')[0]
        except IndexError as e:
            type_3 = ''
        try:
            type_4 = tree.xpath('//div[@id="J_crumbsBar"]/div/div/div/div[4]//em/text()')[0]
        except IndexError as e:
            type_4 = ''
        try:
            type_search = tree.xpath('//div[@id="J_crumbsBar"]/div/div/div[2]/strong/text()')[0].strip('"')
        except IndexError as e:
            type_search = ''
        #找到所有商品的li对象，遍历此对象
        items = tree.xpath('//ul[contains(@class, "gl-warp")]/li')
        for item in items:
            #访问每个商品的详情页
            innerUrl = item.xpath('./div/div[1]/a/@href')[0]
            if 'http' not in innerUrl:
                innerUrl = 'https:' + innerUrl
            html= self.handler_request(innerUrl) #调用采集线程类中的无头浏览器功能
            #调用内页解析函数，解析每个详情页的html，解析子图1、子图2、子图3、子图4、子图5、商品品牌、商品名称、商品编号、商品毛重、商品产地、国产 / 进口、电源、分类、特色、价位、商品视频、商品详情图片
            synl, xiuchang, ztlb, pinpai, spmc, spbh, huohao, dianpu, leibie, spmz, spcd, gcjk, dianyuan, fenlei, yplb, tese, jiawei, guige, chicun, yuanliao, shuliang, yongtu, xingzhi, chima, qunchang, mianliao, houdu, lingxiang, lxys, syjj, sfyd, sycj, syrq, fzs, dmfs, jygn, clbw, spsp, spxqtp, znbj, cdfs, ylfw, gzms, ylms, zhongliang, sybw, dyfs, syzt, baozhuang, lmbs, kuanshi, sfkwc, xingtai, xingzhuang, syfs, fengge, caizhi, sydx, xgrd, sylx, ypjx, syff, zycf, gongxiao, gongneng, kzlx, ylqxzczbh, ylqxmc, xinghao, zcrhzbarxx, scqy, scxkzhbapzbh, gxyjs, yybb, jyfs, clsj, jygnc, clfw, sfzdgb, clff, cljd, cpcc, xsfs, jgjzc, syfw, tqms, yqnd, yqll, gonglv, whklsfkt, whlsfkt, jjz, zctj, ysjsm, whkldxfb, rongliang, gdgzms, zlbcc, cpjz, zdzz, zuokuan, zdh, lcc, ltlx, zxzwbj, ppds, dclx, dcrl, llcdsj, zdsl, edxh, ypspm, yptym, pzwh, cpgg, yfyl, yxq, syzgnzz, bzgg, knsfaphgl, knsfagysgl, blfy, bzq, gongyong = self.innerParse(html)
            #将解析数据整理成字典

            #数据清洗
            #判断商品图片是否包含https，如果没有就为其添加头
            try:
                sptp = item.xpath('./div/div[contains(@class,"p-img")]/a/img/@src')[0]
            except IndexError as e:
                sptp = item.xpath('./div/div[contains(@class,"p-img")]/a/img/@data-lazy-img')[0]
            if 'https:' not in sptp:
                sptp = 'https:' + sptp
            #清洗评论数量
            try:
                plsl = str(float(item.xpath('./div/div[contains(@class,"p-commit")]/strong/a/text()')[0].strip('\n+').split('万')[0])*10000)
            except IndexError as e:
                plsl = ''
            #店铺名称不存在时的异常处理
            try:
                dpmc = item.xpath('./div/div[contains(@class,"p-shop")]/span/a/@title')[0]
            except IndexError as e:
                dpmc = ''
            #商品图标
            sptb = item.xpath('./div/div[contains(@class,"p-icons")]/descendant::i/text()')
            commodityDict = {
                '详情页url':innerUrl,
                '一级分类':type_1,
                '二级分类':type_2,
                '三级分类':type_3,
                '四级分类':type_4,
                '搜索分类':type_search,
                '商品图片':sptp,
                '商品价格':item.xpath('./div/div[contains(@class,"p-price")]/strong/i/text()')[0],
                '商品标题':' '.join(item.xpath('./div/div[contains(@class,"p-name")]/a/descendant::*/text()')).replace('    ', ' ').replace('   ', ' ').replace('  ', ' ').strip('\n '),
                '评论数量':plsl,
                '店铺名称':dpmc,
                '商品图标':'、'.join(sptb),
                '子图列表':'、'.join(ztlb),
                '品牌':pinpai,
                '商品名称':spmc,
                '商品编号':spbh,
                '货号':huohao,
                '店铺':dianpu,
                '商品毛重':spmz,
                '商品产地':spcd,
                '国产进口':gcjk,
                '电源':dianyuan,
                '分类':fenlei,
                '类别':leibie,
                '特色':tese,
                '价位':jiawei,
                '规格':guige,
                '尺寸':chicun,
                '原料':yuanliao,
                '数量':shuliang,
                '用途':yongtu,
                '性质':xingzhi,
                '尺码':chima,
                '裙长':qunchang,
                '面料':mianliao,
                '厚度':houdu,
                '领型':lingxiang,
                '流行元素':lxys,
                '适用季节':syjj,
                '是否有兜':sfyd,
                '适用场景':sycj,
                '适用人群':syrq,
                '分子筛':fzs,
                '调码方式':dmfs,
                '记忆功能':jygn,
                '测量部位':clbw,
                '智能警报':znbj,
                '充电方式':cdfs,
                '压力范围':ylfw,
                '工作模式':gzms,
                '压力模式':ylms,
                '重量':zhongliang,
                '适用部位':sybw,
                '电源方式':dyfs,
                '适用症状':syzt,
                '包装':baozhuang,
                '蓝帽标识':lmbs,
                '款式':kuanshi,
                '袖长':xiuchang,
                '是否可外穿':sfkwc,
                '形态':xingtai,
                '形状':xingzhuang,
                '使用方式':syfs,
                '风格':fengge,
                '材质':caizhi,
                '使用对象':sydx,
                '选购热点':xgrd,
                '适用类型':sylx,
                '药品剂型':ypjx,
                '使用方法':syff,
                '主要成份':zycf,
                '功效':gongxiao,
                '功能':gongneng,
                '控制类型':kzlx,
                '商品详情图片':'、'.join(spxqtp),
                '商品视频': spsp,
                '医疗器械注册证编号或者备案凭证编号':ylqxzczbh,
                '医疗器械名称':ylqxmc,
                '型号':xinghao,
                '注册人或者备案人信息':zcrhzbarxx,
                '生产企业':scqy,
                '生产许可证或者备案凭证编号':scxkzhbapzbh,
                '高血压警示':gxyjs,
                '语音播报':yybb,
                '加压方式':jyfs,
                '测量时间':clsj,
                '记忆功能_次':jygnc,
                '测量范围':clfw,
                '是否自动关闭':sfzdgb,
                '测量方法':clff,
                '测量精度':cljd,
                '产品尺寸_cm':cpcc,
                '显示方式':xsfs,
                '结构及组成':jgjzc,
                '适用范围':syfw,
                '通气模式':tqms,
                '氧气浓度':yqnd,
                '氧气流量':yqll,
                '功率_w':gonglv,
                '雾化颗粒是否可调':whklsfkt,
                '雾化量是否可调':whlsfkt,
                '禁忌症':jjz,
                '贮藏条件':zctj,
                '压缩机寿命':ysjsm,
                '雾化粒大小分布':whkldxfb,
                '容量':rongliang,
                '治疗板尺寸':zlbcc,
                '产品净重_kg':cpjz,
                '最大载重_kg':zdzz,
                '座宽_cm':zuokuan,
                '折叠后长宽高_cm':zdh,
                '前后轮尺寸_cm':lcc,
                '轮胎类型':ltlx,
                '最小转弯半径_cm':zxzwbj,
                '爬坡度数_度':ppds,
                '电池类型':dclx,
                '电池容量_AH':dcrl,
                '理论充电时间_H':llcdsj,
                '最大速率_千瓦时':zdsl,
                '额定续航_KM':edxh,
                '药品商品名':ypspm,
                '药品通用名':yptym,
                '批准文号':pzwh,
                '产品规格':cpgg,
                '用法用量':yfyl,
                '有效期':yxq,
                '适用年龄':synl,
                '适用症功能主治':syzgnzz,
                '包装规格':bzgg,
                '库内是否按批号管理':knsfaphgl,
                '库内是否按供应商管理':knsfagysgl,
                '不良反应':blfy,
                '保质期':bzq,
                '功用':gongyong,
            }
            print(commodityDict)
            commodityList.append(commodityDict)
            print('成功爬取商品：{}'.format(spmc))
            #database:mysql db:yjs table:goods
            mysql = MySql('192.168.0.104', 'root', '135cylpsx4848@', 'yjs')
            mysql.insert('goods', commodityDict)

    #从htmlQueue中取出html，解析出需要的数据，保存为字典，添加到列表中，并返回
    def run(self):
        print('{}开始'.format(self.parseThreadName))
        while True:
            #从htmlQueue中取出html
            try:
                html = self.htmlQueue.get(True, 60)
            except Exception as e:
                print('等待60秒，html队列仍然没有数据，结束{}'.format(self.parseThreadName))
                break
            #创建html的解析函数
            self.htmlParse(html)

#京东爬虫类
class jdSpider():
    urlNumber = 1
    def __init__(self):
        self.urlQueue = Queue()
        self.htmlQueue = Queue()

    #构造jdUrl添加到url队列中
    def putUrlQueue(self, JDUrl, startPage, endPage, step=1):
        for i in range(startPage, endPage, step):
            url = JDUrl.format(i)
            self.urlQueue.put(url)
            print('在url队列中添加了{}条url'.format(self.urlNumber))
            self.urlNumber += 1

    #构成jdUrl，并传入putUrlQueue中，将url添加到url队列中
    def createUrlQueue(self):
        # # 保健器械-健康监测-上臂血压计
        sb_url = 'https://list.jd.com/list.html?cat=9192,9197,12189&ev=1107_71227&page={}&sort=sort_rank_asc&trans=1&JL=3_%E5%88%86%E7%B1%BB_%E4%B8%8A%E8%87%82%E5%BC%8F#J_crumbsBar'
        # self.putUrlQueue(sb_url, 13, 20) #1-5 6-12 13-20 57
        #保健器械-健康监测-手腕血压计
        # sw_url = 'https://list.jd.com/list.html?cat=9192,9197,12189&ev=1107_71226&page={}&sort=sort_rank_asc&trans=1&JL=3_%E5%88%86%E7%B1%BB_%E6%89%8B%E8%85%95%E5%BC%8F#J_crumbsBar'
        # self.putUrlQueue(sw_url, 8, 16) # 1-9 8-16（还未开始） 18
        # #保健器械-健康监测-臂筒血压计
        # bt_url = 'https://list.jd.com/list.html?cat=9192,9197,12189&ev=1107_119532&page={}&sort=sort_rank_asc&trans=1&JL=2_1_0#J_crumbsBar'
        # self.putUrlQueue(bt_url, 2)
        # #保健器械-健康监测-其他血压计
        # qt_url = 'https://list.jd.com/list.html?cat=9192,9197,12189&ev=1107_33710&page={}&sort=sort_rank_asc&trans=1&JL=2_1_0#J_crumbsBar'
        # self.putUrlQueue(bt_url, 9)
        # #保健器械-健康监测-血糖仪
        # xty_url = 'https://list.jd.com/list.html?cat=9192,9197,12187&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=7#J_main'
        # self.putUrlQueue(xty_url, 200)
        # #保健器械-健康监测-体温计
        # twj_url = 'https://list.jd.com/list.html?cat=9192,9197,12588&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=9#J_main'
        # self.putUrlQueue(twj_url, 34)
        # #保健器械-健康监测-心电/血氧仪
        # xdxyy_url = 'https://list.jd.com/list.html?cat=9192,9197,12587&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=10#J_main'
        # self.putUrlQueue(xdxyy_url, 16)
        # #保健器械-呼吸制氧-制氧机
        # zyj_url = 'https://search.jd.com/Search?keyword=%E5%88%B6%E6%B0%A7%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=1&wq=z&page={}&s=159&click=0'
        # self.putUrlQueue(zyj_url, 200, 2)
        # #保健器械-呼吸制氧-呼吸机
        # hxj_url = 'https://search.jd.com/Search?keyword=%E5%91%BC%E5%90%B8%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=huxi&page={}&s=57&click=0'
        # self.putUrlQueue(hxj_url, 86, 2)
        # #保健器械-呼吸制氧-雾化器
        # whq_url = 'https://list.jd.com/list.html?cat=9192,9197,12593&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=7#J_main'
        # self.putUrlQueue(whq_url, 52)
        # #保健器械-呼吸制氧-洗鼻器
        # xbq_url = 'https://search.jd.com/Search?keyword=%E6%B4%97%E9%BC%BB%E5%99%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=x&page={}&s=54&click=0'
        # self.putUrlQueue(xbq_url, 200, 2)
        # #保健器械-呼吸制氧-血氧仪
        # xyy_url = 'https://search.jd.com/Search?keyword=%E6%B4%97%E9%BC%BB%E5%99%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=x&page={}&s=54&click=0'
        # self.putUrlQueue(xyy_url, 96, 2)
        # #保健器械-养生理疗-中频治疗仪
        # zpzly_url = 'https://search.jd.com/Search?keyword=%E4%B8%AD%E9%A2%91%E6%B2%BB%E7%96%97%E4%BB%AA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%B8%AD%E9%A2%91zhi&page={}&s=53&click=0'
        # self.putUrlQueue(zpzly_url, 56, 2)
        # #保健器械-养生理疗-电烤灯
        # dkd_url = ''
        # self.putUrlQueue(dkd_url, 200, 2)
        # #保健器械-养生理疗-紫外线光疗仪
        # zwxgly_url = ''
        # self.putUrlQueue(zwxgly_url, 30, 2)
        # #保健器械-养生理疗-艾灸
        # aj_url = 'https://search.jd.com/Search?keyword=%E8%89%BE%E7%81%B8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=ai&page={}&s=55&click=0'
        # self.putUrlQueue(aj_url, 200, 2)
        # #保健器械-养生理疗-拔罐
        # bg_url = 'https://search.jd.com/Search?keyword=%E6%8B%94%E7%BD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=ba&page={}&s=57&click=0'
        # self.putUrlQueue(bg_url, 200, 2)
        # #保健器械-养生理疗-刮痧板
        # gsb_url = 'https://search.jd.com/Search?keyword=%E5%88%AE%E7%97%A7%E6%9D%BF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=guasha&page={}&s=55&click=0'
        # self.putUrlQueue(gsb_url, 200, 2)
        #
        # #保健器械-康复辅助-手动轮椅
        # sdly_url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E5%8A%A8%E8%BD%AE%E6%A4%85&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=s&page={}&s=56&click=0'
        # self.putUrlQueue(sdly_url, 200, 2)
        # #保健器械-康复辅助-电动轮椅
        # ddly_url = 'https://search.jd.com/Search?keyword=电动轮椅&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=电动lu&page={}&s=58&click=0'
        # self.putUrlQueue(ddly_url, 200, 2)
        # #保健器械-康复辅助-拐杖
        # gz_url = 'https://list.jd.com/list.html?cat=9192,9197,12596&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=8#J_main'
        # self.putUrlQueue(gz_url, 174)
        # #保健器械-康复辅助-护理床
        # hlc_url = 'https://search.jd.com/Search?keyword=护理床&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=hlihc&page={}&s=58&click=0'
        # self.putUrlQueue(hlc_url, 200, 2)
        # #保健器械-康复辅助-爬楼机
        # plj_url = 'https://search.jd.com/Search?keyword=爬楼机&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=pal&page={}&s=59&click=0'
        # self.putUrlQueue(plj_url, 188, 2)
        # #保健器械-康复辅助-助听器
        # ztq_url = 'https://search.jd.com/Search?keyword=助听器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=zhuti&page={}&s=59&click=0'
        # self.putUrlQueue(ztq_url, 200, 2)
        #
        # #中西药品-滋补调养-补肾壮阳
        # bszy_url = 'https://list.jd.com/list.html?cat=9192,12632,12634&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(bszy_url, 209)
        # #中西药品-滋补调养-维矿物质
        # wkwz_url = 'https://list.jd.com/list.html?cat=9192,12632,13240&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(wkwz_url, 194)
        # # 中西药品-滋补调养-风湿骨外
        # fsgw_url = 'https://list.jd.com/list.html?cat=9192,12632,12642&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(fsgw_url, 202)
        # # 中西药品-滋补调养-心脑血管
        # xnxg_url = 'https://list.jd.com/list.html?cat=9192,12632,12646&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(xnxg_url, 26)
        # # 中西药品-滋补调养-安神助眠
        # aszm_url = 'https://list.jd.com/list.html?tid=1006319&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(aszm_url, 22) #22
        # # 中西药品-滋补调养-补气养血
        # bqyx_url = 'https://list.jd.com/list.html?cat=9192,12632,12635&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(bqyx_url, 199)
        #
        # # 中西药品-家庭常备-耳鼻喉用
        # ebhy_url = 'https://list.jd.com/list.html?cat=9192,12632,12637&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ebhy_url, 203)
        # # 中西药品-家庭常备-眼科用药
        # ykyy_url = 'https://list.jd.com/list.html?cat=9192,12632,12638&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ykyy_url, 94)
        # # 中西药品-家庭常备-皮肤用药
        # pfyy_url = 'https://list.jd.com/list.html?cat=9192,12632,12640&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(pfyy_url, 215)
        # # 中西药品-家庭常备-止痛镇痛
        # ztzt_url = 'https://list.jd.com/list.html?cat=9192,12632,12636&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ztzt_url, 139)
        # # 中西药品-家庭常备-肠胃消化
        # cwxh_url = 'https://list.jd.com/list.html?cat=9192,12632,12641&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(cwxh_url, 206)
        # # 中西药品-家庭常备-感冒咳嗽
        # gmks_url = 'https://list.jd.com/list.html?cat=9192,12632,12633&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(gmks_url, 245)
        #
        # # 中西药品-男科用药-脾肾亏损
        # psks_url = 'https://list.jd.com/list.html?cat=9192,12632,12634&ev=3397%5F82294&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(psks_url, 18)
        # # 中西药品-男科用药-生发固发
        # sfgf_url = 'https://list.jd.com/list.html?tid=1001205&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(sfgf_url, 3)
        # # 中西药品-男科用药-尿路感染
        # nlgr_url = 'https://list.jd.com/list.html?cat=9192,12632,12643&ev=3397%5F82262&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(nlgr_url, 3)
        # # 中西药品-男科用药-前列腺增
        # qlxz_url = 'https://list.jd.com/list.html?cat=9192,12632,12634&ev=3397_79362&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(qlxz_url, 6)
        # # 中西药品-男科用药-阳痿不育
        # ywby_url = 'https://list.jd.com/list.html?cat=9192,12632,12634&ev=3397%5F82290&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ywby_url, 26)
        #
        # # 中西药品-妇科用药-妇科炎症
        # fkyz_url = 'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F79370&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(fkyz_url, 56)
        # # 中西药品-妇科用药-更年期
        # gnq_url = 'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F37790&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(gnq_url, 8)
        # 中西药品-妇科用药-孕产期
        # ycq_url = 'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F79374&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ycq_url, 4) #原数为4
        # # 中西药品-妇科用药-阴道炎
        # ydy_url = 'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F82286&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ydy_url, 25)
        # # 中西药品-妇科用药-月经不调
        # yjbt_url = 'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F79371&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(yjbt_url, 69)
        # # 中西药品-妇科用药-避孕用药
        # byyy_url = 'https://list.jd.com/list.html?cat=9192,12632,13241&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(byyy_url, 25)

        # # 计生情趣-避孕套-超薄
        # cb_url = 'https://search.jd.com/Search?keyword=%E8%B6%85%E8%96%84%E9%81%BF%E5%AD%95%E5%A5%97&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%B6%85%E8%96%84%E9%81%BF%E5%AD%95%E5%A5%97&stock=1&page={}&s=59&click=0'
        # self.putUrlQueue(cb_url, 200, 2)
        # # 计生情趣-避孕套-持久
        # cj_url = 'https://search.jd.com/Search?keyword=%E6%8C%81%E4%B9%85%E9%81%BF%E5%AD%95%E5%A5%97&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%8C%81%E4%B9%85%E9%81%BF%E5%AD%95%E5%A5%97&stock=1&page={}&s=60&click=0'
        # self.putUrlQueue(cj_url, 200, 2)
        # # 计生情趣-避孕套-紧型
        # jx_url = 'https://search.jd.com/Search?keyword=%E7%B4%A7%E5%9E%8B%E9%81%BF%E5%AD%95%E5%A5%97&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%B4%A7%E5%9E%8B%E9%81%BF%E5%AD%95%E5%A5%97&stock=1&page={}&s=59&click=0'
        # self.putUrlQueue(jx_url, 48, 2)

        # # 计生情趣-排卵验孕-验孕试纸
        # yysz_url = 'https://search.jd.com/Search?keyword=%E9%AA%8C%E5%AD%95%E8%AF%95%E7%BA%B8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%AA%8C%E5%AD%95%E8%AF%95%E7%BA%B8&page={}&s=57&click=0'
        # self.putUrlQueue(yysz_url, 48, 2)
        # # 计生情趣-排卵验孕-验孕棒
        # yyb_url = 'https://search.jd.com/Search?keyword=%E9%AA%8C%E5%AD%95%E6%A3%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%AA%8C%E5%AD%95%E6%A3%92&page={}&s=58&click=0'
        # self.putUrlQueue(yyb_url, 30, 2)
        # # 计生情趣-排卵验孕-排卵试纸
        # plsz_url = 'https://search.jd.com/Search?keyword=%E6%8E%92%E5%8D%B5%E8%AF%95%E7%BA%B8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%8E%92%E5%8D%B5%E8%AF%95%E7%BA%B8&page={}&s=59&click=0'
        # self.putUrlQueue(plsz_url, 28, 2)
        #
        # # 计生情趣-润滑液-热感
        # rg_url = 'https://search.jd.com/Search?keyword=%E7%83%AD%E6%84%9F%E6%B6%A6%E6%BB%91%E6%B6%B2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%83%AD%E6%84%9F%E6%B6%A6%E6%BB%91%E6%B6%B2&page={}&s=55&click=0'
        # self.putUrlQueue(rg_url, 200, 2)
        # # 计生情趣-润滑液-冰感
        # bg_url = 'https://search.jd.com/Search?keyword=%E5%86%B0%E6%84%9F%E6%B6%A6%E6%BB%91%E6%B6%B2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%B0%E6%84%9F%E6%B6%A6%E6%BB%91%E6%B6%B2&page={}&s=61&click=0'
        # self.putUrlQueue(bg_url, 90, 2)
        # # 计生情趣-润滑液-果香
        # gx_url = 'https://search.jd.com/Search?keyword=%E6%9E%9C%E9%A6%99%E6%B6%A6%E6%BB%91%E6%B6%B2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%B6%A6%E6%BB%91%E6%B6%B2&page={}&s=60&click=0'
        # self.putUrlQueue(gx_url, 16, 2)
        #
        # # 计生情趣-男用延时-喷剂
        # pj_url = 'https://search.jd.com/Search?keyword=%E5%BB%B6%E6%97%B6%E5%96%B7%E5%89%82&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%BB%B6%E6%97%B6&page={}&s=56&click=0'
        # self.putUrlQueue(pj_url, 200, 2)
        # # 计生情趣-男用延时-湿巾
        # sj_url = 'https://search.jd.com/Search?keyword=%E5%BB%B6%E6%97%B6%E6%B9%BF%E5%B7%BE&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%BB%B6%E6%97%B6&page={}&s=61&click=0'
        # self.putUrlQueue(sj_url, 200, 2)
        # # 计生情趣-男用延时-其他
        # nyqt_url = 'https://search.jd.com/Search?keyword=%E5%BB%B6%E6%97%B6&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%BB%B6%E6%97%B6&page={}&s=51&click=0'
        # self.putUrlQueue(nyqt_url, 200, 2)
        #
        # # 计生情趣-飞机杯-震动
        # fjbzd_url = 'https://search.jd.com/Search?keyword=%E9%9C%87%E5%8A%A8%E9%A3%9E%E6%9C%BA%E6%9D%AF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9C%87%E5%8A%A8%E9%A3%9E%E6%9C%BA%E6%9D%AF&page={}&s=61&click=0'
        # self.putUrlQueue(fjbzd_url, 200, 2)
        # # 计生情趣-飞机杯-手动
        # fjbsd_url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E5%8A%A8%E9%A3%9E%E6%9C%BA%E6%9D%AF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E5%8A%A8%E9%A3%9E%E6%9C%BA%E6%9D%AF&page={}&s=61&click=0'
        # self.putUrlQueue(fjbsd_url, 200, 2)
        #
        # # 计生情趣-倒模-阴臀
        # yt_url = 'https://search.jd.com/Search?keyword=%E9%98%B4%E8%87%80%E5%80%92%E6%A8%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%80%92%E6%A8%A1&page={}&s=61&click=0'
        # self.putUrlQueue(yt_url, 200, 2)
        # # 计生情趣-倒模-胸部
        # xb_url = 'https://search.jd.com/Search?keyword=%E8%83%B8%E9%83%A8%E5%80%92%E6%A8%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E9%83%A8&page={}&s=61&click=0'
        # self.putUrlQueue(xb_url, 54, 2)
        # # 计生情趣-倒模-半身
        # bs_url = 'https://search.jd.com/Search?keyword=%E5%8D%8A%E8%BA%AB%E5%80%92%E6%A8%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%8D%8A%E8%BA%AB%E5%80%92%E6%A8%A1&page={}&s=61&click=0'
        # self.putUrlQueue(bs_url, 200, 2)
        #
        # # 计生情趣-仿真娃娃-充气娃娃
        # cqww_url = 'https://search.jd.com/Search?keyword=%E5%85%85%E6%B0%94%E5%A8%83%E5%A8%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%85%85%E6%B0%94%E5%A8%83%E5%A8%83&page={}&s=61&click=0'
        # self.putUrlQueue(cqww_url, 200, 2)
        # # 计生情趣-仿真娃娃-实体娃娃
        # stww_url = 'https://search.jd.com/Search?keyword=%E5%AE%9E%E4%BD%93%E5%A8%83%E5%A8%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%AE%9E%E4%BD%93%E5%A8%83%E5%A8%83&page={}&s=61&click=0'
        # self.putUrlQueue(stww_url, 200, 2)
        # # 计生情趣-仿真娃娃-其他
        # fzwwqt_url = 'https://list.jd.com/list.html?cat=9192,9196,14697&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(fzwwqt_url, 300)
        #
        # # 计生情趣-仿真阳具-震动
        # fzyjzd_url = 'https://search.jd.com/Search?keyword=%E4%BB%BF%E7%9C%9F%E9%98%B3%E5%85%B7%E6%8A%BD%E6%8F%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=3.def.0.T19&wq=%E4%BB%BF%E7%9C%9F%E9%98%B3%E5%85%B7&page={}&s=61&click=0'
        # self.putUrlQueue(fzyjzd_url, 110, 2)
        # # 计生情趣-仿真阳具-手动
        # fzyjsd_url = 'https://search.jd.com/Search?keyword=%E4%BB%BF%E7%9C%9F%E9%98%B3%E5%85%B7&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%BB%BF%E7%9C%9F%E9%98%B3%E5%85%B7&page={}&s=61&click=0'
        # self.putUrlQueue(fzyjsd_url, 100, 2)
        # # 计生情趣-仿真阳具-其他
        # fzyjqt_url = 'https://list.jd.com/list.html?cat=9192,9196,14701&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(fzyjqt_url, 274)
        #
        # # 计生情趣-震动棒-震动棒
        # zdb_url = 'https://list.jd.com/list.html?cat=9192,9196,12610&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(zdb_url, 334)
        # 计生情趣-震动棒-AV棒
        # avb_url = 'https://search.jd.com/Search?keyword=AV%E6%8C%AF%E5%8A%A8%E6%A3%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=AV&page={}&s=61&click=0'
        # self.putUrlQueue(avb_url, 200, 2)
        # # 计生情趣-震动棒-转珠棒
        # zzb_url = 'https://search.jd.com/Search?keyword=%E8%BD%AC%E7%8F%A0%E6%A3%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%BD%AC%E7%8F%A0%E6%A3%92&page={}&s=61&click=0'
        # self.putUrlQueue(zzb_url, 200, 2)
        #
        # # 计生情趣-跳蛋-跳蛋
        # td_url = 'https://list.jd.com/list.html?cat=9192,9196,14700&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(td_url, 258)
        # # 计生情趣-跳蛋-缩阴球
        # syq_url = 'https://search.jd.com/Search?keyword=%E7%BC%A9%E9%98%B4%E7%90%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page={}&s=61&click=0'
        # self.putUrlQueue(syq_url, 200, 2)
        #
        # 计生情趣-情趣内衣-套装
        # tz_url = 'https://search.jd.com/Search?keyword=%E5%A5%97%E8%A3%85%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%A5%97%E8%A3%85%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&page={}&s=61&click=0'
        # self.putUrlQueue(tz_url, 200, 2) #原数为200
        # # 计生情趣-情趣内衣-睡裙
        # sq_url = 'https://search.jd.com/Search?keyword=%E7%9D%A1%E8%A3%99%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%9D%A1%E8%A3%99%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&page={}&s=53&click=0'
        # self.putUrlQueue(sq_url, 200, 2)
        # # 计生情趣-情趣内衣-丁字裤
        # dzk_url = 'https://search.jd.com/Search?keyword=%E4%B8%81%E5%AD%97%E8%A3%A4%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page={}&s=51&click=0'
        # self.putUrlQueue(dzk_url, 200, 2)
        #
        # # 计生情趣-其他情趣用品-锁精环
        # sjh_url = 'https://search.jd.com/Search?keyword=%E9%94%81%E7%B2%BE%E7%8E%AF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%94%81%E7%B2%BE%E7%8E%AF&page={}&s=61&click=0'
        # self.putUrlQueue(sjh_url, 200, 2)
        # # 计生情趣-其他情趣用品-后庭
        # ht_url = 'https://search.jd.com/Search?keyword=%E5%90%8E%E5%BA%AD&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%90%8E%E5%BA%AD&page={}&s=61&click=0'
        # self.putUrlQueue(ht_url, 200, 2)
        # # 计生情趣-其他情趣用品-SM
        # sm_url = 'https://search.jd.com/Search?keyword=%E6%88%90%E4%BA%BA%E7%94%A8%E5%93%81SM&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%88%90%E4%BA%BA%E7%94%A8%E5%93%81SM&page={}&s=61&click=0'
        # self.putUrlQueue(sm_url, 200, 2)
        #
        #
        # # 营养保健-调节免疫-蛋白粉
        # dbf_url = 'https://search.jd.com/Search?keyword=%E8%9B%8B%E7%99%BD%E7%B2%89&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.1&vt=2&page={}&s=58&click=0'
        # self.putUrlQueue(dbf_url, 200, 2)
        # # 营养保健-调节免疫-维生素
        # wss_url = 'https://search.jd.com/Search?keyword=%E7%BB%B4%E7%94%9F%E7%B4%A0&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%BB%B4%E7%94%9F%E7%B4%A0&page={}&s=58&click=0'
        # self.putUrlQueue(wss_url, 200, 2)
        # # 营养保健-调节免疫-螺旋藻
        # lxz_url = 'https://search.jd.com/Search?keyword=%E8%9E%BA%E6%97%8B%E8%97%BB&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%9E%BA%E6%97%8B%E8%97%BB&page=3&s=60&click=0'
        # self.putUrlQueue(lxz_url, 200, 2)
        #
        # # 营养保健-骨骼健康-钙片
        # gp_url = 'https://search.jd.com/Search?keyword=%E9%92%99&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=gai&stock=1&page={}&s=57&click=0'
        # self.putUrlQueue(gp_url, 200, 2) #200
        # # 营养保健-骨骼健康-氨糖
        # at_url = 'https://search.jd.com/Search?keyword=%E6%B0%A8%E7%B3%96&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.1&vt=2&stock=1&page={}&s=59&click=0'
        # self.putUrlQueue(at_url, 200, 2)
        # # 营养保健-骨骼健康-儿童钙
        # etg_url = 'https://search.jd.com/Search?keyword=%E5%84%BF%E7%AB%A5%E9%92%99&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&stock=1&page={}&s=56&click=0'
        # self.putUrlQueue(etg_url, 200, 2)
        #
        # # 营养保健-美体塑身-健身达人
        # jsdr_url = 'https://list.jd.com/list.html?cat=9192,9193,12163&ev=6684%5F97259&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(jsdr_url, 4)
        # # 营养保健-美体塑身-窈窕丽人
        # ytlr_url = 'https://list.jd.com/list.html?cat=9192,9193,12163&ev=6684%5F97260&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ytlr_url, 42)
        # # 营养保健-美体塑身-肠道福音
        # cdfy_url = 'https://list.jd.com/list.html?cat=9192,9193,12163&ev=6684%5F97261&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(cdfy_url, 21)
        #
        # # 营养保健-美容养颜-维生素E
        # wsse_url = 'https://list.jd.com/list.html?cat=9192,9193,9200&ev=4874%5F6121&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(wsse_url, 26)
        # # 营养保健-美容养颜-胶原蛋白
        # jydb_url = 'https://list.jd.com/list.html?cat=9192,9193,9200&ev=4874%5F6118&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(jydb_url, 40)
        # # 营养保健-美容养颜-大豆异黄酮
        # ddyht_url = 'https://list.jd.com/list.html?cat=9192,9193,9200&ev=4874%5F6142&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ddyht_url, 10)
        #
        # # 营养保健-肠胃养护-益生菌
        # ysj_url = 'https://list.jd.com/list.html?cat=9192,9193,9207&ev=4874%5F8136&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ysj_url, 37)
        # # 营养保健-肠胃养护-润肠通便
        # rctb_url = 'https://search.jd.com/search?keyword=%E6%B6%A6%E8%82%A0%E9%80%9A%E4%BE%BF&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&cid2=9193&cid3=9207&page={}&s=106&click=0'
        # self.putUrlQueue(rctb_url, 34, 2)
        # # 营养保健-肠胃养护-养胃
        # yw_url = 'https://search.jd.com/search?keyword=%E5%85%BB%E8%83%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%85%BB%E8%83%83&cid2=9193&cid3=9207&page={}&s=56&click=0'
        # self.putUrlQueue(yw_url, 40, 2)
        #
        # # 营养保健-孕期营养-叶酸
        # ys_url = 'https://list.jd.com/list.html?cat=9192,9194,12171&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=2#J_main'
        # self.putUrlQueue(ys_url, 20)
        # # 营养保健-孕期营养-孕妇钙
        # yfg_url = 'https://search.jd.com/search?keyword=%E5%AD%95%E5%A6%87%E9%92%99&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%AD%95%E5%A6%87%E9%92%99&cid2=9194&page={}&s=61&click=0'
        # self.putUrlQueue(yfg_url, 30, 2)
        # # 营养保健-孕期营养-锌硒宝
        # xxb_url = 'https://search.jd.com/Search?keyword=%E9%94%8C%E7%A1%92%E5%AE%9D&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%94%8C%E7%A1%92%E5%AE%9D&stock=1&page={}&s=53&click=0'
        # self.putUrlQueue(xxb_url, 30, 2)
        #
        # # 营养保健-明目益智-叶黄素
        # yhs_url = 'https://list.jd.com/list.html?cat=9192,9193,9205&ev=4874%5F85734&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(yhs_url, 33)
        # # 营养保健-明目益智-DHA
        # dha_url = 'https://list.jd.com/list.html?cat=9192,9193,9205&ev=4874%5F20494&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(dha_url, 18)
        # # 营养保健-明目益智-蓝莓
        # lm_url = 'https://list.jd.com/list.html?cat=9192,9193,9205&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(lm_url, 84)
        #
        # # 营养保健-缓解疲劳-维生素B
        # wssb_url = 'https://list.jd.com/list.html?cat=9192,9193,12162&ev=4874%5F8264&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(wssb_url, 6)
        # # 营养保健-缓解疲劳-牛磺酸
        # nhs_url = 'https://list.jd.com/list.html?cat=9192,9193,12162&ev=4874%5F85618&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(nhs_url, 5)
        # # 营养保健-缓解疲劳-海狗丸
        # hgw_url = 'https://list.jd.com/list.html?cat=9192,9193,12162&ev=4874%5F85619&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(hgw_url, 4)
        #
        # # 营养保健-清喉利咽-润喉糖
        # rht_url = 'https://search.jd.com/search?keyword=%E6%B6%A6%E5%96%89%E7%B3%96&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%B6%A6%E5%96%89%E7%B3%96&cid2=9193&cid3=12170&stock=1&page={}&s=52&click=0'
        # self.putUrlQueue(rht_url, 54, 2)
        # # 营养保健-清喉利咽-金嗓子
        # jsz_url = 'https://list.jd.com/list.html?cat=9192,9193,12170&ev=exbrand%5F9476&sort=sort_totalsales15_desc&trans=1&JL=2_1_0#J_crumbsBar'
        # self.putUrlQueue(jsz_url, 2)
        # # 营养保健-清喉利咽-龙角散
        # ljs_url = 'https://list.jd.com/list.html?cat=9192,9193,12170&ev=exbrand%5F121636&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ljs_url, 8)
        #
        # # 传统滋补-阿胶-阿胶糕
        # ejg_url = 'https://list.jd.com/list.html?cat=9192,9195,12180&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(ejg_url, 71)
        #
        # # 传统滋补-燕窝-燕盏
        # yz_url = 'https://search.jd.com/Search?keyword=%E7%87%95%E7%9B%8F&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%87%95%E7%9B%8F&page={}&s=58&click=0'
        # self.putUrlQueue(yz_url, 134, 2)
        # # 传统滋补-燕窝-即食燕窝
        # jsyw_url = 'https://search.jd.com/Search?keyword=%E5%8D%B3%E9%A3%9F%E7%87%95%E7%AA%9D&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&wtype=1&page={}&s=58&click=1'
        # self.putUrlQueue(jsyw_url, 12, 2)
        #
        # # 传统滋补-冬虫夏草-3g/条
        # xxdcxc_url = 'https://list.jd.com/list.html?cat=9192,9195,9229&ev=2314_85552&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(xxdcxc_url, 3)
        # # 传统滋补-冬虫夏草-4g/条
        # dxdcxc_url = 'https://list.jd.com/list.html?cat=9192,9195,9229&ev=2314%5F85553&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(dxdcxc_url, 3)
        #
        # # 传统滋补-人参/西洋参-人参
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,9230&ev=1107%5F8396&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(_url, 66)
        # # 传统滋补-人参/西洋参-西洋参
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,9230&ev=1107%5F6136&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(_url, 57)
        # # 传统滋补-人参/西洋参-高丽参
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,9230&ev=1107%5F71115&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(_url, 12)
        # # 传统滋补-人参/西洋参-野山参
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,9230&ev=1107%5F85650&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(_url, 19)
        #
        # # 传统滋补-药食同源-山药
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,12185&ev=1107%5F85672&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(_url, 5)
        # # 传统滋补-药食同源-决明子
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,12185&ev=1107_85675&sort=sort_totalsales15_desc&trans=1&JL=3_%E5%88%86%E7%B1%BB_%E5%86%B3%E6%98%8E%E5%AD%90#J_crumbsBar'
        # self.putUrlQueue(_url, 2)
        # # 传统滋补-药食同源-胖大海
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,12185&ev=1107_82704&sort=sort_totalsales15_desc&trans=1&JL=3_%E5%88%86%E7%B1%BB_%E8%83%96%E5%A4%A7%E6%B5%B7#J_crumbsBar'
        # self.putUrlQueue(_url, 2)
        #
        # # 传统滋补-三七-三七花
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,12613&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(_url, 89)
        # '''
        # # 传统滋补-三七-三七粉
        # _url = ''
        # self.putUrlQueue(_url, )
        # # 传统滋补-三七-三七头
        # _url = ''
        # self.putUrlQueue(_url, )
        # # 传统滋补-三七-盘龙云海
        # _url = ''
        # self.putUrlQueue(_url, )
        # # 传统滋补-三七-贡府堂
        # _url = ''
        # self.putUrlQueue(_url, )
        # '''
        #
        # # 传统滋补-蜂产品-蜂胶
        # _url = 'https://list.jd.com/list.html?cat=9192,9195,12186&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # self.putUrlQueue(_url, 46)
        # '''
        # # 传统滋补-蜂产品-蜂花粉
        # _url = ''
        # self.putUrlQueue(_url, )
        # # 传统滋补-蜂产品-蜂王浆
        # _url = ''
        # self.putUrlQueue(_url, )
        # # 传统滋补-蜂产品-蜂蜜
        # _url = ''
        # self.putUrlQueue(_url, )
        # # 传统滋补-蜂产品-汪氏
        # _url = ''
        # self.putUrlQueue(_url, )
        # # 传统滋补-蜂产品-百花
        # _url = ''
        # self.putUrlQueue(_url, )
        # '''
        # # 隐形眼镜-透明隐形
        # tmyx_url = 'https://search.jd.com/Search?keyword=%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C&page={}&s=55&click=0'
        # self.putUrlQueue(tmyx_url, 200, 2)
        # # 隐形眼镜-彩色隐形
        # csyx_url = 'https://search.jd.com/Search?keyword=%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C%20%E7%BE%8E%E7%9E%B3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C%20%E7%BE%8E%E7%9E%B3&page={}&s=54&click=0'
        # self.putUrlQueue(csyx_url, 200, 2)
        # # 隐形眼镜-护理液
        # hly_url = 'https://search.jd.com/Search?keyword=%E6%8A%A4%E7%90%86%E6%B6%B2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%8A%A4%E7%90%86%E6%B6%B2&page={}&s=56&click=0'
        # self.putUrlQueue(hly_url, 200, 2)
        # # 隐形眼镜-眼镜配件
        # yjpj_url = 'https://search.jd.com/Search?keyword=%E4%BC%B4%E4%BE%A3%E7%9B%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%BC%B4%E4%BE%A3%E7%9B%92&page={}&s=58&click=0'
        # self.putUrlQueue(yjpj_url, 200, 2)
        #
        # #体检卡
        # tjk_url = 'https://search.jd.com/Search?keyword=%E4%BD%93%E6%A3%80%E5%8D%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%BD%93%E6%A3%80%E5%8D%A1&page=3&s=57&click=0'
        # self.putUrlQueue(tjk_url, 150, 2)

    #开始采集线程和解析线程
    def createThread(self):
        # 创建采集线程名字
        crawlThreadsName = ['采集线程1', '采集线程2', '采集线程3', '采集线程4', '采集线程5', '采集线程6', '采集线程7', '采集线程8']
        # 创建8个采集线程存放于下面列表中
        tCrawlThreadingList = []
        for crawlThreadName in crawlThreadsName:  # 遍历线程名称，传递给线程
            tCrawlThreading = CrawlThread(crawlThreadName, self.urlQueue, self.htmlQueue)
            tCrawlThreadingList.append(tCrawlThreading)

        # 创建解析线程名字
        parseThreadsName = ['解析线程1', '解析线程2', '解析线程3', '解析线程4', '解析线程5', '解析线程6', '采集线程7', '采集线程8']
        # 创建8个解析线程存放于下面列表中
        tParseThreadingList = []
        for parseThreadName in parseThreadsName:
            # 实例化解析线程
            tParseThreading = ParseThread(parseThreadName, self.htmlQueue)
            tParseThreadingList.append(tParseThreading)

        # 启动8个采集线程
        for tCrawlThreading in tCrawlThreadingList:  # 遍历8个线程，启动线程
            tCrawlThreading.start()
            time.sleep(5)
        # 启动8个解析线程
        # 等待30秒，让采集线程先运行，避免html队列为空
        time.sleep(30)
        print('采集线程全部结束30秒后开启解析线程')
        time.sleep(3)
        for tParseThreading in tParseThreadingList:
            tParseThreading.start()
            time.sleep(5)

        # 子线程结束主线才程结束
        for tCrawlThreading in tCrawlThreadingList:  # 遍历8个线程，启动线程
            tCrawlThreading.join()
        # 子线程结束主线程才结束
        for tParseThreading in tParseThreadingList:
            tParseThreading.join()

    #爬虫京东执行
    def run(self):
        #创建队列并将dj的url放入url队列中
        self.createUrlQueue()
        #创建采集线程,从urlQueue中取出url并发起请求，将返回的html存放于htmlQueue中
        #创建解析线程，从htmlQueue中取出html，解析出需要的数据，保存为字典，添加到全局列表中
        self.createThread()
        #保存全局列表
        jsonStr = json.dumps(commodityList, ensure_ascii=False)
        with open('jdsj.json', 'w', encoding='utf8') as f:
            f.write(jsonStr)

def main():
    spider = jdSpider()
    spider.run()

if __name__ == '__main__':
    main()