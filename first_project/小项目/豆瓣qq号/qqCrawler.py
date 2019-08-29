from myClass.mySpider import MyCrawler
from myClass.regularExpression import RegularExpression
from myClass.rwfile import RwFile

def qqCrawler(url, toPath):
    myCrawler = MyCrawler()
    htmlBytes = myCrawler.getHtmlBytes(url)
    #toPath1 = r'D:\qian_feng_education\first_project\myClass\豆瓣qq号\file1.html'
    #toPath2 = r'D:\qian_feng_education\first_project\myClass\豆瓣qq号\file2.txt'
    #writeFileBytes2Bytes(htmlBytes, toPath1)
    #writeFileBytes2String(htmlBytes, toPath2)
    #爬取QQ号
    htmlStr = str(htmlBytes)
    regular = RegularExpression()
    re_QQ = regular.getQQ(htmlStr)
    qqList = list(set(re_QQ))
    rwFile = RwFile()
    rwFile.listToTxt(toPath, qqList)
    print('成功爬取一页qq号')
    #爬取网址
    re_Url = regular.getUrl(htmlStr)
    urlList = list(set(re_Url))
    return urlList

if __name__=='__main__':
    url = 'https://www.douban.com/group/topic/17359302/?start=0'
    toPath = r'D:\qian_feng_education\first_project\data\QQ号\qqList.txt'
    myCrawler = MyCrawler()
    myCrawler.center(url, toPath, qqCrawler)