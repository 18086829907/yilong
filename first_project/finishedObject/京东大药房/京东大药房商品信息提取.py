from bs4 import BeautifulSoup
import os
from myClass import mySpider
import json
import pickle
import time
import random
from myClass.mySql import MySql
mysql = MySql('192.168.0.103', 'root', '135cylpsx4848@', 'asj')


#获取商品信息字典
def getInfoDict(allCommodity, pictureSavePath):
    commodityInfoList = []
    num = 1
    for i in range(len(allCommodity)):
        picture = allCommodity[i].find('img')['src']
        commodityName = allCommodity[i].find('h3').text
        commodityAttr = allCommodity[i].find('p').text
        price = allCommodity[i].find('div', attrs={'class': 'p-price-cur'}).text
        if allCommodity[i].find('div', attrs={'class':'p-price-r'}) != None:
            discount = allCommodity[i].find('div', attrs={'class': 'p-price-r'}).text.split(' ')[1]
            originalPrice = allCommodity[i].find('div', attrs={'class': 'p-price-r'}).text.split(' ')[2]
        else:
            discount = None
            originalPrice = None
        advantage = allCommodity[i].find('div', attrs={'class':'p-desc'}).text
        policy = allCommodity[i].find('i').text
        commodityInfo = {}
        commodityInfo['No.{}'.format(num)] = {'picture': picture,
                                              'commodityName': commodityName,
                                              'commodityAttr': commodityAttr,
                                              'price': price.split('￥')[1],
                                              'discount': discount,
                                              'originalPrice': originalPrice,
                                              'advantage': advantage,
                                              'policy': policy
                                              }
        commodityInfoList.append(commodityInfo)
        # time.sleep(random.randint(10, 30))
        # myCra.seveImage(picture, pictureSavePath.format(num, num))  # 保存图片
        num += 1
    return commodityInfoList

#网页数据提取执行主程序
def getInfoMain():
    # 实例化爬虫
    myCra = mySpider.MyCrawler()
    # 图片保存地址
    pictureSavePath = r'D:\qian_feng_education\first_project\finishedObject\同城帮数据爬取\image\{}page\{}.jpg'
    # json保存地址
    jsonSavePath = r'D:\qian_feng_education\first_project\finishedObject\同城帮数据爬取\json\commodityInformation.json'
    # list保存地址
    listSavePath = r'D:\qian_feng_education\first_project\finishedObject\同城帮数据爬取\list\commodityInformation.txt'
    # 导入所有html并解析
    filePath = r'D:\qian_feng_education\first_project\finishedObject\同城帮数据爬取\htmls'
    fileList = os.listdir(filePath)
    pageInfoList = []
    num = 0
    for i in fileList:
        absPath = os.path.join(filePath, i)
        with open(absPath, 'rb') as f:
            data = f.read().decode('utf-8')
            soup = BeautifulSoup(data, features='lxml')
            allCommodity = soup.find_all('div', attrs={'class': 'p-item'})
        info = getInfoDict(allCommodity, pictureSavePath)
        pageInfo = {}
        pageInfo['{}page'.format(num)] = info
        num += 1
        pageInfoList.append(pageInfo)
        # time.sleep(random.randint(10, 30))
    jsonFile = json.dumps(pageInfoList)
    with open(jsonSavePath, 'w') as f:
        json.dump(jsonFile, f)
    with open(listSavePath, 'wb') as f:
        pickle.dump(pageInfoList, f)
if __name__ == '__main__':
    getInfoMain()