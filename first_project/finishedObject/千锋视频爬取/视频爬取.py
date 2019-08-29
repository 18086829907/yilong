from myClass import mySpider
myCra = mySpider.MyCrawler()
htmlBytes = myCra.getHtmlBytes('http://video.mobiletrain.org/course/index/courseId/485?pinzhuanbdtg=biaoti')
path1 = r'D:\qian_feng_education\first_project\finishedObject\千锋视频爬取\数据库开发入门到精通.html'
myCra.writeFileHtmlBytes2Html(htmlBytes, path1)
