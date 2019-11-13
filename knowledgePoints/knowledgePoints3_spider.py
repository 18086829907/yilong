#【day】百度爬虫
#爬虫分类
#   通用爬虫
#   聚焦爬虫
#通用爬虫如何爬取新网站?
#   方式
#       主动提交
#       设置友情链接
#       百度会和DNS服务商合作，抓取新网站
#检索排名
#   竞价排名
#   根据pagerank值
#       访问量
#       点击量
#不希望通用爬虫爬取
#   robots.txt
#       Allow 规定能爬取url
#       Disalow 规定不能爬取的url
#       示例
#           www.taobao.com/robots.txt
#                 User-agent:  Baiduspider
#                 Allow:  /article
#                 Allow:  /oshtml
#                 Allow:  /ershou
#                 Allow: /$
#                 Disallow:  /product/
#                 Disallow:  /
#
#                 User-Agent:  Googlebot
#                 Allow:  /article
#                 Allow:  /oshtml
#                 Allow:  /product
#                 Allow:  /spu
#                 Allow:  /dianpu
#                 Allow:  /oversea
#                 Allow:  /list
#                 Allow:  /ershou
#                 Allow: /$
#                 Disallow:  /
#
#                 User-agent:  Bingbot
#                 Allow:  /article
#                 Allow:  /oshtml
#                 Allow:  /product
#                 Allow:  /spu
#                 Allow:  /dianpu
#                 Allow:  /oversea
#                 Allow:  /list
#                 Allow:  /ershou
#                 Allow: /$
#                 Disallow:  /
#
#                 User-Agent:  360Spider
#                 Allow:  /article
#                 Allow:  /oshtml
#                 Allow:  /ershou
#                 Disallow:  /
#
#                 User-Agent:  Yisouspider
#                 Allow:  /article
#                 Allow:  /oshtml
#                 Allow:  /ershou
#                 Disallow:  /
#
#                 User-Agent:  Sogouspider
#                 Allow:  /article
#                 Allow:  /oshtml
#                 Allow:  /product
#                 Allow:  /ershou
#                 Disallow:  /
#
#                 User-Agent:  Yahoo!  Slurp
#                 Allow:  /product
#                 Allow:  /spu
#                 Allow:  /dianpu
#                 Allow:  /oversea
#                 Allow:  /list
#                 Allow:  /ershou
#                 Allow: /$
#                 Disallow:  /
#
#                 User-Agent:  *
#                 Disallow:  /
#聚焦爬虫
#   根据特定需求，抓取指定的数据
#   思路
#       代替浏览器使用
#           网页的特点
#               网页都有自己唯一的url
#               网页内容都是html结构的
#               使用的都是http、https协议
#           爬取步骤
#               给一个url
#               写程序，模拟浏览器访问url
#               解析内容，提取数据
#           100%爬取原则
#               从根url一步一步走到需要爬取的数据位置，就一定能爬取
#环境
#   windows环境
#   python3.6 64位
#   pycharm
#课程内容
#   使用的库
#       访问浏览器
#           urllib
#           request
#           bs4
#       解析网页内容
#           正则表达式
#           bs4
#           xpath
#           jsonpath练习
#       获取动态加载数据
#           selenium练习 + phantomjs
#           selenium练习 + chromeheadless
#       高性能框架
#           scrapy框架
#       scrapy-redis组件
#           redis
#           分布式爬虫
#       涉及到爬虫-反爬虫-反反爬虫
#           UA
#           代理
#           验证码
#           动态页面
#http协议
#   什么是http协议
#       双方规定通信（说话、传输）的形式
#   http与https的区别
#       https://www.cnblogs.com/wqhwe/p/5407468.html
#           1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用。
# 　       　2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议。
# 　       　3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。
#        　　4、http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。
#       密码学
#           对称加解密
#               加密密钥 == 解密密钥
#           非对称加解密
#               加密密钥 != 解密密钥
#           密钥
#               每一次会话会生成一个证书，证书中就包括公钥和私钥，他们两是一对
#                   公钥
#                       服务器响应请求时，使用公钥加密传输数据
#                   私钥
#                       客户端接收请求时，使用私钥解密传输数据
#   http协议详解
#       电子书
#           图解http协议
#       博客
#           https://www.cnblogs.com/10158wsj/p/6762848.html
#       请求头
#        　　accept:浏览器通过这个头告诉服务器，它所支持的数据类型
#        　　Accept-Charset: 浏览器通过这个头告诉服务器，它支持哪种字符集
#        　　Accept-Encoding：浏览器通过这个头告诉服务器，支持的压缩格式
#        　　Accept-Language：浏览器通过这个头告诉服务器，它的语言环境
#        　　Host：浏览器通过这个头告诉服务器，想访问哪台主机
#        　　If-Modified-Since: 浏览器通过这个头告诉服务器，缓存数据的时间
#        　　Referer：浏览器通过这个头告诉服务器，客户机是哪个页面来的，即上一个页面的url  防盗链
#        　　Connection：浏览器通过这个头告诉服务器，请求完后是断开链接还是何持链接
#           x-Requested-With: XMLHttpRequest 代表ajax方式进行访问
#       响应内容
#           状态行
#           消息头
#             　　HTTP响应中的常用响应头(消息头)
#             　　Location: 服务器通过这个头，来告诉浏览器跳到哪里
#             　　Server：服务器通过这个头，告诉浏览器服务器的型号
#             　　Content-Encoding：服务器通过这个头，告诉浏览器，数据的压缩格式
#             　　Content-Length: 服务器通过这个头，告诉浏览器回送数据的长度
#             　　Content-Language: 服务器通过这个头，告诉浏览器语言环境
#             　　Content-Type：服务器通过这个头，告诉浏览器回送数据的类型
#             　　Refresh：服务器通过这个头，告诉浏览器定时刷新
#             　　Content-Disposition: 服务器通过这个头，告诉浏览器以下载方式打数据
#             　　Transfer-Encoding：服务器通过这个头，告诉浏览器数据是以分块方式回送的
#             　　Expires: -1  控制浏览器不要缓存
#             　　Cache-Control: no-cache
#             　　Pragma: no-cache
#           空白
#           实体内容
#抓包
#   谷歌
#       网页中按F12
#           Network
#               ALL
#                   request1
#                       Header
#                           General
#                           ResponseHeader
#                           RequestHeader
#                               Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
#                               Accept-Encoding: gzip, deflate, br
#                               Accept-Language: zh-CN,zh;q=0.9
#                               Cache-Control: max-age=0
#                               Connection: keep-alive
#                               Cookie: BAIDUID=0BD6A8EB50BB9073779F057D56426E59:FG=1; BIDUPSID=0BD6A8EB50BB9073779F057D56426E59; PSTM=1554281453; BD_UPN=12314753; ispeed=1; ispeed_lsm=1; BDUSS=ZiY1EzM2hQWDN4bDFtME1kfmFBOENUMTRld1VxcDd3UWFmbnpPQUxVOGd2Q05kSVFBQUFBJCQAAAAAAAAAAAEAAACK0jWGwfrBvNPqMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAv~FwgL~xcSE; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=e75542ed08036a5ec59bfe78a3d1b19bd453c352_1561733645_js; H_PS_645EC=f55da4uhmvkD86v%2F1des1mHug8CZnxoLI5QseNDpw97ee3dawjP2bl890UmtmeSfbL5s; COOKIE_SESSION=39406_0_8_2_10_8_0_1_8_3_0_0_42380_0_109_0_1561777275_0_1561777166%7C9%2358404_5_1561734058%7C2; BD_HOME=1; H_PS_PSSID=1435_21082_29135_29238_28519_29099_29131_28839_29221_26350; sug=3; sugstore=1; ORIGIN=0; bdime=0
#                               Host: www.baidu.com
#                               Upgrade-Insecure-Requests: 1
#                               User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
#                           Query String Parameters：get请求的数据
#                           Form Data：post请求数据
#                       Preview
#                       Reasponse：响应内容
#                   request2
#                   request3
#                   ...
#               XHR:ajax请求
#               JS
#               CSS
#               img
#               Media
#               Font
#               Doc
#               WS
#               Manifest
#               Other
#   fiddler
#       使用：https://www.cnblogs.com/woaixuexi9999/p/9247705.html
#            按照流程进行配置
#       inspectors
#           request
#               raw：请求头部的详细信息
#               webforms：请求所带参数，get数据和post数据
#           response
#               首先点击Decode进行解码
#               raw：响应的所有信息（包括请求头）
#               webview：css
#               json：接口返回的内容
#       quickExec
#           左下角黑色框
#               可输入指令快捷操作request
#               指令
#                   clear 清除所有request
#                   select json 快速选择json格式的request
#                   select image 快速选择图片
#                   select html
#                   ?内容 搜索包含内容
#                   敲enter执行
#urllib库
#   概念：模拟浏览器发送请求的库，等价python2的urllib
#   导入方式：import urllib.request
#       方法
#           .urlopen(url)
#               功能：获得rqsponse对象
#               注意：该函数访问的url必须是完整url，url不带参数时结尾必须是/，比如http://www.baidu.com/
#               示例
#                   url = 'http://www.baidu.com'
#                   response = urllib.request.urlopen(url)
#               返回值：response对象
#                   方法
#                       read()
#                           功能：读取response对象中的html代码
#                           注意：返回值是二进制
#                               .encode() 字符串转二进制
#                                   参数：默认utf-8,可写'gbk'
#                               .decode() 二进制转字符串
#                                   参数：默认utf-8,可写'gbk'
#                                   说明：如果网页源代码规定的是gbk格式，.decode('gbk')
#                                        网页右键查看源代码 <meta charset="gbk" />
#                               读取后保存到文件
#                                   path = r'd:/baidu.html'
#                                   字符串格式保存
#                                       with open(path, 'w', encode='utf-8') as fp:
#                                           fp.write(response.read().decode('gbk'))
#                                   二进制格式保存
#                                       with open(path, 'wb') as fp:
#                                           fp.write(response.read())
#                       geturl()
#                           功能：获取请求url
#                       getheaders()
#                           功能：获得响应头信息
#                           返回值
#                               格式：[('key','value')] #列表元组转字典
#                               转换为字典
#                                   示例:header = dict(response.getheaders())
#                               字典获取指定头信息
#                                   示例：Content-Type = header['Content-Type']
#                       getcode()
#                           功能：获取状态码
#                       readlines()
#                           功能：按行读取，返回列表，元素都是字节类型，一个列表元素是response.read()一行的内容
#                           返回值：['htmlCode一行','htmlCode一行','htmlCode一行']
#           .urlretrieve()
#               功能：下载图片
#               下载图片方式
#                   一、访问图片url，保存图片到本地
#                       示例
#                           image_url='https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2850821783,1061449836&fm=26&gp=0.jpg'
#                           response = urllib.request.urlopen(image_url)
#                           with open('qing.jpg', 'wb') as fp:
#                               fp.write(response.read())
#                   二、urlretrieve方法
#                       原型：urllib.request.urlretrieve(url,filename=None)
#                       参数：url访问的图片地址，filename保存到本地，图片文件的名字
#                       示例
#                           urllib.request.urlretrieve(image_url, r'D:/qing.jpg') 绝对路径
#                           urllib.request.urlretrieve(image_url, 'qing.jpg') 相对路径，保存到同级文件
#                           urllib.request.urlretrieve(image_url, '/fileName/qing.jpg') 相对路径，保存到同级文件目录下
#urllib.parse
#   概念：等价python2的urllib2
#   导入方式：import urllib.parse
#   方法
#       quote()
#           功能：url中的$、空格、中文进行编码
#           示例
#               url = 'https://www.baidu.com/index.html?name=陈艺龙&pwd=123456'
#               result = urllib.parse.quote(url)
#               print(ret) -> 'https%3A//www.baidu.com/index.html%3Fname%3D%E9%99%88%E8%89%BA%E9%BE%99%26pwd%3D123456'
#           说明：url格式规定只能由字母、数字、下划线、特殊符组成，如果出现$、空格、中文的url，通过urlopen(url)访问浏览器是会报错的，因此需要对其进行编码
#           提示：遇到编码的url，可以通过http://tool.chinaz.com/Tools/urlencode.aspx在线解码
#       unquote()
#           功能：url中的$、空格、中文进行解码
#           示例：
#               url = 'https%3A//www.baidu.com/index.html%3Fname%3D%E9%99%88%E8%89%BA%E9%BE%99%26pwd%3D123456'
#               result = urllib.parse.unquote(url)
#               print(result) -> https://www.baidu.com/index.html?name=陈艺龙&pwd=123456
#       urlencode(dict)
#           功能：处理字典格式数据，{'a':'b', 'c':'d'} -- urlencode() --> 'a=b&c=d'
#           注意：完整url不带参数时最后结尾必须是/，比如http://www.baidu.com/
#           实现原理
#               url = 'http://www.baidu.com/index.html'
#               name = '陈艺龙'
#               gender = '男'
#               dic = {'name': name,'gender': gender}
#               lis = []
#               for k,v in zip(dic.keys(),dic.values()):
#                   lis.append(k + '=' + str(v))
#               query_string = '&'.join(lis)
#               url = url + '?' + query_string
#               result = urllib.parse.quote(url)
#               print(result) -> 'http%3A//www.baidu.com/index.html%3Fname%3D%E9%99%88%E8%89%BA%E9%BE%99%26gender%3D%E7%94%B7'
#           示例
#               url = 'http://www.baidu.com/index.html'
#               name = '陈艺龙'
#               gender = '男'
#               dic = {'name': name, 'gender': gender}
#               query_string = urllib.parse.urlencode(dic)
#               url = url + '?' + query_string
#               print(url) -> http://www.baidu.com/index.html?name=%E9%99%88%E8%89%BA%E9%BE%99&gender=%E7%94%B7
#urllib.parse和urllib.request的应用
#    get方式抓取页面
#        需求：输入一个值得到一个关于这个值的url,并且访问这个url，获取响应的html，保存到本地
#             from myClass.myCrawler import MyCrawler
#             urlCope = 'https://www.baidu.com/s?wd=%E9%99%88&rsv_spt=1&rsv_iqid=0xb0f99ab9001d0526&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=57028281_hao_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_t=c3185SKQWFvBSCJj5sXeRzWpb175%2Fl6wrKBl9KYr3BCiuHZ%2B3V2roSGxKXaQXp2oQ83k%2FioC&rsv_sug2=0&inputT=1977&rsv_sug4=1977&rsv_sug=1'
#             myCrawler = MyCrawler()
#             myCrawler.getCrawler(urlCope)
#        构建请求头部信息(反反爬第一步)
#            思路
#                用正常浏览器访问目标网站，观察fiddler结果的requestHeader
#                伪造头的UA必须跟真实头的UA字段一模一样
#                百度搜索UA大全
#                构建Request对象配置伪造头的UA，让服务器认为你是浏览器在上网
#            Request对象
#                导入方式：import urllib.request
#                实例化请求对象：request = urllib.request.Request(url, headers)
#                目的：用真AU构建真实请求头
#                示例
#                    url = 'http://www.baidu.com/'
#                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60 Opera/8.0 (Windows NT 5.1; U; en)'}
#                    request = urllib.request.Request(url=url, headers=headers) #构建请求对象
#                    response = urllib.reqeust.urlopen(request)
#                    print(response.read().decode())
#    post方式抓取页面
#        浏览器发送post请求并捕获
#            谷歌浏览器抓包-百度翻译的输入文字返回的译文ajsx请求
#                打开百度翻译
#                点击F12
#                点击Network
#                点击XHR
#                输入baby
#                找到需求对应的请求
#                    查看Type=xhr的请求
#                    查看请求.Headers.General.Request_Method = POST
#                    查看请求.Headers.Request_Headers.X-Requested-With = XMLHttpRequest
#                    查看求亲.Headers.Form_Data = kw:baby
#                查看对应请求的Response中的json是否是需要的json
#                    三击json
#                    复制json
#                    在线解析json
#                       https://www.json.cn/
#                       粘贴json
#            fiddler抓包-百度翻译的输入文字返回的译文ajsx请求
#               打开fiddler
#               打开百度翻译
#               输入baby
#               切换到fiddler界面点击F12关闭实时抓包
#                    找到需求对应的请求
#                        #字段的图标 = 一本书加一个右箭头 //代表post请求
#                        URL = /sug
#                        三者选其一
#                            请求.Inspectors.TextView = 'kw=baby'
#                            请求.Inspectors.WebForms.Body = {'Name':'kw','Value':'baby'}
#                            请求.Inspectors.Raw = {'X-Requested-With':'XMLHttpRequest','kw':'baby'}
#                    查看对应请求的Response中的json是否是需要的json
#                        decodeResponse
#                            点击请求.Inspectors.response框上面的Response body is encoded.click to decode.
#                        请求.Inspectors.response.JSON
#        python模拟浏览器给百度的sug接口发送post请求获得部分json数据
#             from myClass.myCrawler import MyCrawler
#             myCrawler = MyCrawler()
#             post_url = 'https://fanyi.baidu.com/sug/'
#             myCrawler.postCrawler(post_url)
#        python模拟浏览器给百度的v2transapi接口发送post请求获得完整json数据
#            在爬出这个接口时会遇到反爬虫
#                 反反爬虫
#                   思路
#                       当你的爬虫遇到错误时
#                           有没有成功模拟浏览器
#                               头部信息是否完全模拟
#                                   fiddler抓包，观察头部信息
#                                       发现头部信息包含sign
#                                           不能直接复制sign的值来进行伪造头
#                                               因为sign是通过js代码计算得到的可变值，你每次访问时sign值不同
#                                                   分析js代码，解析出sign的算法，再自己编写js文件模拟算法
#                                                       捕获百度翻译的js文件
#                                                           进入百度翻译
#                                                           谷歌F12
#                                                           NetWork
#                                                           js
#                                                           F5
#                                                               观察js请求名，需要解析的js代码就存在于这些捕获的js响应中
#                                                                   index_c8a141d.js
#                                                                       Response
#                                                                           复制js代码
#                                                                           粘贴到js在线格式化网站中https://www.html.cn/tool/js_beautify/
#                                                                               点击美化按钮
#                                                                               读懂代码找到生成sign的算法代码（理论可行，实际很难）
#                   示例
#                       import urllib.request
#                       import urllib.parse
#                       import execjs
#                       #定义百度翻译v2transapi接口
#                       post_url = 'https://fanyi.baidu.com/v2transapi' #在fiddler中请求窗口，URL列，复制对应接口的url
#                       # 输入需要翻译的单词
#                       quert = input('请输入您想查询的单词：')
#                       # 打开百度翻译v2transapi接口的js文件
#                       with open('baidusign.js') as f:
#                           jsCode = f.read()
#                       # 将查询的单词传入js代码并用python调用js代码中的e函数，传输参数e函数的参数quert，获得返回值sign
#                       # 注意：如果fiddler中抓取到的POST请求中有sign，即WebForm中有sign
#                       #      需要用谷歌F12去捕获ajax响应的js文件，并分析js代码，找到类似baidusign.js的代码
#                       sign = execjs.compile(jsCode).call('e', quert)
#                       #伪造post参数,参数获取的方式：fiddler.v2transapi接口.Inspectors.Request.WebForms
#                       data_form = {
#                           'from': 'en',
#                           'query': quert,
#                           'sign': sign,
#                           'simple_means_flag': 3,
#                           'to': 'zh',
#                           'token': '2062ab7729a8cb504cbc1913b24a5173',
#                           'transtype': 'realtime',
#                       }
#                       #预处理post参数
#                       data_form = urllib.parse.urlencode(data_form).encode()
#                       #伪造头部信息，头部信息获取方式：fiddler.v2transapi接口.Inspectors.Request.Raw,注意不要复制第一排，即POST http://...
#                       headers = {
#                           'Host': 'fanyi.baidu.com',
#                           'Connection': 'keep-alive',
#                           # 'Content-Length': '121', //此条也要注释掉，这个是返回的内容长度，服务器会自动算返回文本的长度
#                           'Accept': '*/*',
#                           'Origin': 'https://fanyi.baidu.com',
#                           'X-Requested-With': 'XMLHttpRequest',
#                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#                           'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
#                           # 'Accept-Encoding': 'gzip, deflate, br',
#                           'Accept-Language': 'zh-CN,zh;q=0.9',
#                           'Cookie': 'BAIDUID=0BD6A8EB50BB9073779F057D56426E59:FG=1; BIDUPSID=0BD6A8EB50BB9073779F057D56426E59; PSTM=1554281453; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=ZiY1EzM2hQWDN4bDFtME1kfmFBOENUMTRld1VxcDd3UWFmbnpPQUxVOGd2Q05kSVFBQUFBJCQAAAAAAAAAAAEAAACK0jWGwfrBvNPqMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAv~FwgL~xcSE; CHINA_PINYIN_SWITCH=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1561847780,1561849112,1561873096,1561882295; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1561883366; yjs_js_security_passport=7909d1a932a5b58e24257dd1b0a3ec14f5d6e9d4_1561883368_js',
#                       }
#                       request = urllib.request.Request(url=post_url, headers=headers)
#                       response = urllib.request.urlopen(request, data_form)
#                       print(response.read().decode())
#                       注意
#                           response.read()出来的数据为b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\xc5}...'时，需要解压缩，但是我不会解压缩，直接的处理方式：告诉服务器不要给我压缩文件，即在头中注释掉'Accept-Encoding': 'gzip, deflate, br'
#                           未压缩的response.read()格式为b'{"trans_result":{"data":[{"dst":"\\u82f9\\u679c"...'
#                               它无法直接用www.json.cn解析，因为它未解码
#                                   response.read().decode()
#                                       注意：如果解码出现报UnicodeDecodeError,说明解码的数据是压缩数据，不能对其直接解码，解决办法为在伪造头中注释掉'Accept-Encoding': 'gzip, deflate, br'
#    爬取ajax发送get请求返回的数据
#        python模拟浏览器给豆瓣电影的https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=20&limit=20接口发送get请求获得json数据，get请求是由ajsx触发
#            打开fiddler
#            用浏览器打开豆瓣电影排行榜
#            在ajax请求之前对fiddler进行清屏
#            滑动滚轮触发ajax请求
#            切换到fiddler
#            关闭实时截获F12
#            fiddler捕获到json图标的接口
#            查看接口url
#                url = json请求.Inspectors.Raw.Get
#                    即 url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=20&limit=20'
#            说明：ajax发出的get请求，本质就是访问上面url接口获得数据，也就是说向以上接口发送get请求就能获得json数据
#            分析接口的start和limit参数
#                在浏览器中发送start=0，limit=5的get请求
#                再发送start=1，limit=5的get请求
#                观察数据
#                    如果第一次的第2条数据等于第二次的第1条数据
#                         说明start是下标
#                    如果第一次的所有数据和第二次的所有数据都不相同
#                         说明start是页码
#                观察可得豆瓣的start参数表示的是数据下标
#            示例
#                import urllib.request
#                import urllib.parse
#                # primary_url  = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=20&limit=20'
#                baseUrl = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&'
#                start = int(input('请输入查询页数：'))
#                limit = 20
#                #构建get参数
#                get_dict = {
#                   'start': (start-1)*limit,
#                   'limit': limit,
#                }
#                #预处理get参数
#                get_data = urllib.parse.urlencode(get_dict)
#                #拼接url
#                url = baseUrl + get_data
#                #构造请求头
#                headers = {
#                    'Host': 'movie.douban.com',
#                    'Connection': 'keep-alive',
#                    'Accept': '*/*',
#                    'X-Requested-With': 'XMLHttpRequest',
#                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#                    'Referer': 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=',
#                    # 'Accept-Encoding': 'gzip, deflate, br',
#                    'Accept-Language': 'zh-CN,zh;q=0.9',
#                    'Cookie': 'll="118318"; bid=lGZHTVxI3Kk; __yadk_uid=SwxKvolbnlDiP4P9wTwPXuHUHyNDv5wh; _vwo_uuid_v2=D2ABD48A24891394589D59580F0C222D0|98a72e7f2f24384bc74f7dba9e03b41e; douban-fav-remind=1; gr_user_id=8cf2d862-2df8-4865-97a9-e29101a129fb; __gads=ID=8bcd3fa417042e57:T=1560298416:S=ALNI_MaHLnq4S9THwmQk64R088Xr7Xdyfg; viewed="1007914"; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1561900563%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utmc=30149280; __utma=223695111.149382321.1556423894.1560298376.1561900563.6; __utmb=223695111.0.10.1561900563; __utmc=223695111; __utmz=223695111.1561900563.6.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.266525776.1556423889.1561900563.1561900563.15; __utmz=30149280.1561900563.15.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1561900563; _pk_id.100001.4cf6=e73dcbb5be348d5c.1556423894.6.1561900592.1560298430.',
#                }
#                #构造请求体
#                request = urllib.request.Request(url, headers=headers)
#                #发送请求
#                response = urllib.request.urlopen(request)
#                print(response.read().decode())
#    爬取ajax发送post请求返回的数据
#        import urllib.request
#        import urllib.parse
#        post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
#        #伪造头部信息
#        headers = {
#        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
#        }
#        #构造post数据
#        city = input('请输入您需要查询的城市：')
#        pageIndex = input('请输入要查询的页数：')
#        pageSize = input('请输入要查询数据的个数：')
#        post_data = {
#            'cname': city,
#            'pid': '',
#            'pageIndex': pageIndex,
#            'pageSize':	pageSize
#        }
#        #预处理post数据
#        data_from = urllib.parse.urlencode(post_data).encode()
#        #构造请求体
#        request = urllib.request.Request(url=post_url, headers=headers) #如果出现unknown url，则是该处没有用关键字参数
#        #发送请求
#        response = urllib.request.urlopen(request, data=data_from)
#        #读取响应值
#        print(response.read().decode())
#   复杂的get请求
#       爬取百度贴吧中的信息
#           分析网页思路或步骤
#               随便进入一个吧
#               观察其url,确定可用参数
#                   http://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search&red_tag=a2698151386
#                       red_tag参数
#                           通过逐个删除参数来测试参数是否有效，有效则不能正常进入页面
#                               发现red_tag=a2698151386不管怎么删除都无法删除
#                               暂时搁置
#                           点击下一页，观察url
#                               http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
#                               发现red_tag参数被pn=50替换了
#                               再点击下一页pn的值变成了100
#                               我们尝试将pn的值修改为0，发现它又回到了刚才的第一页
#                               说明pn参数是控制页码的参数
#                                   第一页 pn=0
#                                   第二页 pn=50
#                                   第三页 pn=100
#                                   第n页  pn=(n-1)*50
#                       kw参数
#                           不难发现这是代表在哪个吧
#           确定基础url
#               去掉有效可变参数
#                   url = 'http://tieba.baidu.com/f?ie=utf-8'
#           需求：输入吧名，输入起始页面，输入结束页码，在当前文件夹中创建一个以吧名为名字的文件夹，里面是每一页的html内容，文件名为吧名_page.html
#               import urllib.request
#               import urllib.parse
#               import os
#               import time
#               import random
#               wk = input('请输入吧名：')
#               start_pn = int(input('请输入起始页码：'))
#               end_pn = int(input('请输入结束页码：'))
#               #判断该贴吧的文件目录是否存在，不存在则创建文件目录，注意在文件目录存在并且其中也存在html文件时，不需要考虑删除在写入，因为html写入的格式是wb，文件名相同时，会覆盖之前的文件内容
#               if not os.path.exists(wk):
#                   os.mkdir(wk)
#               #创建文件夹
#               dirPath= os.path.join(os.getcwd(), wk)
#               for page in range(start_pn, end_pn+1):
#                   print('第{}页下载开始...'.format(page))
#                   url = 'http://tieba.baidu.com/f?ie=utf-8'
#                   # get数据
#                   get_data = {
#                       'wk': wk,
#                       'pn': (page - 1) * 50,
#                   }
#                   # 预处理数据
#                   requery_string = urllib.parse.urlencode(get_data)
#                   url += requery_string #循环中使用+= 一定要注意区别是否需要累加，如果不需要累加，一定要把基本数据拿到循环内部来定义
#                   # 构造头
#                   headers = {
#                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
#                   }
#                   # 构造请求体
#                   request = urllib.request.Request(url=url, headers=headers)
#                   # 发送请求
#                   response = urllib.request.urlopen(request)
#                   #保存响应值
#                   absPath = os.path.join(dirPath, '{}_{}.html'.format(wk, page))
#                   with open(absPath, 'wb') as f:
#                       f.write(response.read())
#                   time.sleep(random.randint(10,30))
#                   print('第{}页下载结束...'.format(page))
#异常处理URLError、HTTPError
#    异常本质：urllib.error类里面的URLError类和HTTPError类
#    处理异常
#       抛出异常
#       捕获异常
#       记录日志
#       结构
#           try-except
#   异常类型
#       URLError
#           抛出异常情况
#               没有连接网络
#               服务器链接失败
#               找不到指定服务器
#           代码模拟URLEroor,并处理异常
#               url = 'https://www.maodan.com/'
#               import urllib.request
#               import urllib.parse
#               import urllib.error
#               try:
#                   respons = urllib.request.urlopen(url)
#                   print(respons.read())
#               except urllib.error.URLError as f:
#                   print('该url不存在')
#       HTTPError
#           是URLError的子类
#           抛出异常情况
#               正确的域名，即服务器能正确连接，但url参数部分有稍微一点点错误式
#           示例
#               urlCorrect = 'https://blog.csdn.net/m0_37622530/article/details/81257015'
#               urlError   = 'https://blog.csdn.net/m0_37622530/article/details/812570'
#               import urllib.request
#               import urllib.error
#               #URLError
#               try:
#                   respons = urllib.request.urlopen(urlError)
#                   print(respons.read())
#               except urllib.error.URLError as e:
#                   print('URLError可以捕获HTTPError{}', format(e.code))
#               #HTTPError
#               # try:
#               #     respons = urllib.request.urlopen(urlError)
#               #     print(respons.read())
#               # except urllib.error.HTTPError as e:
#               #     print('HTTPError的状态码为:{}'.format(e.code))
#           注意：如果两个异常都需要捕获，则HTTPError优先捕获
#               try:
#                   respons = urllib.request.urlopen(urlError)
#                   print(respons.read())
#               except urllib.error.HTTPError as e1:
#                   print(e1)
#               except urllib.error.URLError as e2:
#                   print(e2)
#Handler处理器、自定义Opener
#   回顾
#       urlopen(url)
#           功能：给一个url发送请求，返回响应
#           局限性：不能定制头部
#           解决办法：结合urllib.request.Request类，定制请求头，创建请求对象，再用请求头发送请求获取响应
#           任然有局限性：无法使用代理
#   基本用法
#       通过Handler、Opener发送请求
#           示例
#               import urllib.request
#               import urllib.parse
#               url = 'http://www.baidu.com/'
#               headers = {
#                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
#               }
#               #创建Handler
#               handler = urllib.request.HTTPHandler()
#               #通过Handler创建一个Opener
#               #   opener就是一个对象，使用其open方法发送请求
#               opener = urllib.request.build_opener(handler)
#               #构建请求对象
#               request = urllib.request.Request(url=url, headers=headers)
#               #发送请求
#               response = opener.open(request) #后续都用opener.open方法发送请求
#               print(response.read())
#   高级功能
#       使用代理
#           作用：当我们使用爬虫去爬取一个网站时，被反爬虫屏蔽掉了ip，该ip则无法访问该网页，此时只有使用代理ip来访问该网站
#           概念：
#               生活中的代理，微商、代考、代练、代驾、代购、代孕
#               程序中的代理
#                   正向代理
#                       说明：代理客户端获取数据
#                       访问流程：客户端将请求发送给代理服务器，代理服务器在发送给目标服务器，目标服务器将响应发送给代理服务器，最后代理服务器将响应内容发送给客户端，其中的代理服务器有很多，目标服务器就不知道封哪个服务器了
#                       本地ip查询：百度ip --> 本机IP: 171.221.149.132四川省成都市 电信
#                       更改ip
#                           代理知识
#                               HTTP代理按匿名度可分为
#                                   透明代理
#                                       使用透明代理，对方服务器可以知道你使用了代理，并且也知道你的真实IP
#                                           透明代理访问对方服务器所带的HTTP头信息如下：
#                                               REMOTE_ADDR = 代理服务器IP
#                                               HTTP_VIA = 代理服务器IP
#                                               HTTP_X_FORWARDED_FOR = 你的真实IP
#                                   匿名代理
#                                       使用匿名代理，对方服务器可以知道你使用了代理，但不知道你的真实IP。
#                                           匿名代理访问对方服务器所带的HTTP头信息如下：
#                                               REMOTE_ADDR = 代理服务器IP
#                                               HTTP_VIA = 代理服务器IP
#                                               HTTP_X_FORWARDED_FOR = 代理服务器IP
#                                   高度匿名代理
#                                       使用高匿名代理，对方服务器不知道你使用了代理，更不知道你的真实IP。
#                                           高匿名代理访问对方服务器所带的HTTP头信息如下：
#                                               REMOTE_ADDR = 代理服务器IP
#                                               HTTP_VIA 不显示
#                                               HTTP_X_FORWARDED_FOR 不显示
#                           配置正向代理
#                               浏览器配置
#                                   获取免费代理
#                                       https://www.kuaidaili.com/
#                                           免费代理
#                                               响应速度最快
#                                                   ip：60.13.42.83
#                                                   port：9999
#                                   点击浏览器的自定义控制按钮(右边3个点)
#                                       设置
#                                           高级
#                                               打开代理设置
#                                                   局域网设置
#                                                       勾选为lan...
#                                                       粘贴复制ip和port
#                                                       确定确定
#                                   百度搜索ip，查看是否配置成功
#                                       如果网页无法打开则说明该ip不能使用
#                                           测试其他ip和port,直到测试出可用ip
#                                               ip:60.10.22.229
#                                               port:63141
#                                       如果没有一个可用或不想手工测试
#                                           爬取https://www.xicidaili.com/?tdsourcetag=s_pctim_aiomsg中的ip
#                                               执行finishedObject/西祠代理ip爬取/xiciCrawler.py
#                                                   得到一个装满ip和端口号的txt文件
#                                                       打开花刺软件
#                                                           取消ie代理
#                                                           将txt文件导入花刺软件
#                                                           验证全部
#                                                               清理
#                                                               选择剩余ip
#                                                                   设置ie代理
#                                                                       百度ip测试是否配置成功
#                               代码配置代理(代码配置正向代理)
#                                   import urllib.request
#                                   import urllib.parse
#                                   #创建具有代理的handler
#                                   handler = urllib.request.ProxyHandler({'http':'59.32.37.49:8010'})
#                                   #通过handler创建opener
#                                   opener = urllib.request.build_opener(handler)
#                                   #构造请求体
#                                   url = 'https://www.baidu.com/s?wd=ip'
#                                   headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
#                                   request = urllib.request.Request(url=url, headers=headers)
#                                   #opner访问请求体
#                                   response = opener.open(request)
#                                   #保存结果
#                                   path = 'ip.html'
#                                   with open(path, 'wb') as f:
#                                       f.write(response.read())
#                   反向代理
#                       说明：代理服务端提供数据
#                       访问流程：成都客户端 -- 发送请求 --> 反向代理（成都子服务器,数据以镜像的方式存储了总服务的数据，） <-- 数据同步 -- 北京总服务器，目的使所有地区上网的速度都很快
#       使用cookie(获取cookie，抓取cookie)
#           本质：cookie是一个字典
#           概念：cookie是记录你的浏览器状态的，比如你第一次登录时，服务器会给你发一个cookie，本地就保存一下这个cookie，下次登录时本地在把这个cookie发送给服务器，服务器就知道你是谁，也就是说身份标识都在cookie里
#           模拟登录
#               概念：模拟浏览器访问登录后的页面
#               登录的本质：向目标接口发送post请求，发送请求后目标网站会返回cookie，对其网站进行其他get访问时，请求中都携带cookie，目标网站就会认为你是某某用户在登录使用，并返回给你响应的数据
#               方式一：伪造cookie模拟登录
#                   cookie获取方式
#                       fiddler抓包
#                           注意：不需要抓点击登录时的包，只需要抓取登录后页面的操作请求的包，因为此时带有身份标识的cookie已经保存在本地，每次向服务器发送请求时都会带cookie中的身份标识
#                           将抓取到的请求头部信息复制粘贴到代码中就能模拟登录了
#                   示例
#                       import urllib.request
#                       import urllib.parse
#                       #请求体
#                       url = 'http://www.renren.com/971351636/profile'
#                       headers = {
#                       'Host': 'www.renren.com',
#                       'Connection': 'keep-alive',
#                       'Upgrade-Insecure-Requests': '1',
#                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#                       'Referer': 'http://www.renren.com/971351636/newsfeed/photo',
#                       #'Accept-Encoding': 'gzip, deflate',
#                       'Accept-Language': 'zh-CN,zh;q=0.9',
#                       'Cookie': 'anonymid=jxl276snx7rdrl; depovince=GW; jebecookies=b4e8c892-2396-4a19-8750-5773f4dd167a|||||; _r01_=1; JSESSIONID=abcLAq0oDYMDL-Yl6bWUw; ick_login=0bffc864-5fda-468f-ac42-790698007bc3; _de=2E757325973CAD40D28173EB34A8CC93; p=d66f6ed6bcb03cc243a97796364c51976; first_login_flag=1; ln_uact=18086829907; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=382521937cc6a612bf91dbde1b1d33046; societyguester=382521937cc6a612bf91dbde1b1d33046; id=971351636; xnsid=4ff6bce0; ver=7.0; loginfrom=null; jebe_key=22738ca2-ea84-4c1c-a594-4a186dcf246f%7Cd68038a7330c1c27a93e726b5b24a666%7C1562026527492%7C1%7C1562026527277; jebe_key=22738ca2-ea84-4c1c-a594-4a186dcf246f%7Cd68038a7330c1c27a93e726b5b24a666%7C1562026527492%7C1%7C1562026527281; wp_fold=0',
#                       }
#                       request = urllib.request.Request(url=url, headers=headers)
#                       #发送请求
#                       handler = urllib.request.HTTPHandler()
#                       opner = urllib.request.build_opener(handler)
#                       response = opner.open(request)
#                       #保存文件
#                       with open('renrenwang.html', 'wb') as f:
#                           f.write(response.read())
#
#               方式二：post请求模拟登录
#                   fiddler捕获点击登录时的包
#                       复制post请求网址
#                           post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201962959544 '
#                               如果发送请求失败，就需要观察一下post_url中的参数
#                       伪造post请求数据，复制WebForm.Body
#                           email	18086829907
#                           icode
#                           origURL	http://www.renren.com/home
#                           domain	renren.com
#                           key_id	1
#                           captcha_type	web_login
#                           password	38fb7f0a5fc64dc43d0331aa9dc5198f4bce1a3a06af7f7faf778ba82a140c79
#                           rkey	322ee4e2dbf2c0737bfe67342f01f9bb
#                           f	http%3A%2F%2Fwww.renren.com%2F971351636%2Fnewsfeed%2Fphoto
#                   示例
#                       import urllib.request
#                       import urllib.parse
#                       import http.cookiejar
#                       #创建CookieJar对象
#                       cj = http.cookiejar.CookieJar()
#                       #通过cj创建一个handler
#                       handler = urllib.request.HTTPCookieProcessor(cj)
#                       #通过handler创建opener
#                       opener = urllib.request.build_opener(handler)
#                       #需要发送请求的地方都用opener.open的方法，因为这里面带着cookie
#                       #——————————————————————————————————请求登录界面————————————————————————————————————
#                       #请求体
#                       post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201962959544 '
#                       post_data = {
#                           'email':	'18086829907',
#                           'icode':'',
#                           'origURL':	'http://www.renren.com/home',
#                           'domain':	'renren.com',
#                           'key_id':	'1',
#                           'captcha_type':	'web_login',
#                           'password':	'38fb7f0a5fc64dc43d0331aa9dc5198f4bce1a3a06af7f7faf778ba82a140c79', #破译密码也是去js中解析代码，搞懂算法
#                           'rkey':	'322ee4e2dbf2c0737bfe67342f01f9bb',
#                           'f':	'http%3A%2F%2Fwww.renren.com%2F971351636%2Fnewsfeed%2Fphoto',
#                       }
#                       post_data = urllib.parse.urlencode(post_data).encode()
#                       headers = {
#                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#                       }
#                       post_request = urllib.request.Request(url=post_url, headers=headers)
#                       #发送请求
#                       post_response = opener.open(post_request, data=post_data)
#                       #——————————————————————————————请求登录后页面中的页面————————————————————————————————
#                       #print(response.read()) #b'{"code":true,"homeUrl":"http://www.renren.com/home"}'
#                       #code=true，表示登录成功，再去访问登录后网址中的网页，即http://www.renren.com/971351636/profile
#                       #真实模拟浏览器，当发送完post请求的时候，将cookie保存到代码中
#                       #请求体
#                       get_url = 'http://www.renren.com/971351636/profile'
#                       get_request = urllib.request.Request(url=get_url, headers=headers)
#                       #opener发送请求
#                       get_response = opener.open(get_request)
#                       with open('renrenwang.html', 'wb') as f:
#                           f.write(get_response.read())
#网页内容提取，网页解析
#   正则表达式解析
#       概念：用来匹配一类具有相同规则的字符串
#       主要用于
#           正则匹配
#           正则替换
#       规则
#           单字符
#               . : 匹配除换行以外的所有字符
#               []: [aoe],[a-z],[\u4e00-\u9fa5] 匹配集合中任意一个字母或中文（正则匹配中文）
#               \d: 数字 [0-9]
#               \D: 非数字
#               \w: 数字、字母、下划线、中文
#               \W: 非\w
#               \s: 所有的空白字符
#               \S: 非空白字符
#
#           数量修饰
#               *: 任意多次 >=0
#               +: 至少1此 >=1
#               ?: 可有可无 =0 or =1
#               {m}: 固定n次
#               {m,}: 至少m次
#               {m,n}: m到n次
#           边界
#              \b:
#              \B:
#               ^: 以某某开头
#               $: 以某某结尾
#           分组
#               ()
#                   视为一个整体
#                       ab{3}:abbb, (ab){3}:ababab
#                   子模式
#                       (...)/1
#                       (...)/2
#               示例
#                   import re
#                   Str = '<p><div><spon>猪八戒</spon></div></p>'
#                   pat = r'<(\w+)><(\w+)>\w+</\2></\1>'
#                   re_mobile = re.compile(pat)
#                   data = re_mobile.search(Str)
#                   print(data.group(0))
#           贪婪模式
#               概念：尽可能多得匹配
#               取消贪婪
#                   .*？
#                       示例
#                           import re
#                           Str = '<div>猪八戒</div><div></div>'
#                           pat = r'<div>.*?</div>'
#                           re_mobile = re.compile(pat)
#                           data = re_mobile.findall(Str)
#                           print(data)
#                   .+？
#           re
#               re.compile(par, re.I): 忽略大小写
#               re.compile(par, re.M): 多行匹配
#                   示例
#                       import re
#                       Str = '''
#                       my name is justin
#                       i love my wife
#                       i love my daughters
#                       '''
#                       pat = r'^i love'
#                       re_mobile = re.compile(pat, re.M)
#                       data = re_mobile.findall(Str)
#                       print(data)
#               re.compile(par, re.S): 单行匹配
#                   单行模式能让.匹配换行
#                   示例
#                       Str = '''
#                       <div>
#                       北国风光，
#                       千里冰封，
#                       万里雪飘。
#                       望长城内外，
#                       惟余莽莽；
#                       大河上下，
#                       顿失滔滔。
#                       山舞银蛇，
#                       原驰蜡象，
#                       欲与天公试比高。
#                       须晴日，
#                       看红装素裹，
#                       分外妖娆。
#                       江山如此多娇，
#                       引无数英雄竞折腰。
#                       惜秦皇汉武，
#                       略输文采；
#                       唐宗宋祖，
#                       稍逊风骚。
#                       一代天骄，
#                       成吉思汗，
#                       只识弯弓射大雕。
#                       俱往矣，
#                       数风流人物，
#                       还看今朝。
#                       </div>
#                       '''
#                       pat = r'<div>(.*)</div>'
#                       pattern = re.compile(pat, re.S)
#                       data = pattern.findall(Str)
#                       print(data)
#               方法
#                   正则匹配
#                       match 开头位置找
#                       search 任意位置找
#                       findall 匹配所有，返回列表
#                   正则替换
#                       re.sub(pattern，repl，string)
#                           功能：替换
#                           参数
#                               pattern：正则表达式
#                               repl
#                                   替换的内容
#                                   函数
#                               string：原字符串
#                           返回值：替换后的字符串
#                           示例一
#                               import re
#                               Str = 'i love you, you love me, ye'
#                               subStr = 'hate'
#                               result = re.sub(r'love', subStr, Str)
#                               print(result)
#                           示例二(正则函数替换)
#                               需求，匹配到数字字符串，数字字符串+10后，替换原文本
#                                   import re
#                                   Str = 'i love 160'
#                                   def subStr(a):
#                                       ret = str(int(a.group(0)) + 10)
#                                       return ret
#                                   result = re.sub(r'\d+', subStr, Str)
#                                   print(result)
#       实战一
#           正则提取图片下载
#               需求：糗事百科的糗图爬取
#                   import urllib.request
#                   import urllib.parse
#                   import re
#                   import os
#                   import time
#
#                   def handler_request(url, page):
#                       url = url + str(page) + '/'
#                       headers = {
#                           'Host': 'www.qiushibaike.com',
#                           'Connection': 'keep-alive',
#                           'Upgrade-Insecure-Requests': '1',
#                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#                           # 'Accept-Encoding': 'gzip, deflate, br',
#                           'Accept-Language': 'zh-CN,zh;q=0.9',
#                           'Cookie': '_ga=GA1.2.1859399017.1556469673; _qqq_uuid_="2|1:0|10:1562045710|10:_qqq_uuid_|56:YThmNzAxYjdlM2QyM2IxN2QxNDY5NTlhYWViMjYyY2ViMzlhYjI2Mg==|1ac500ef6d6b8091a8fd15272d0a1160d99ce14135163829ebc13e922e4b084c"; _gid=GA1.2.1959390664.1562045710; _xsrf=2|4e038820|33b1b9f7fd0de31d055be13f8384d0a1|1562052790; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1562045710,1562052791; _gat=1; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1562052980',
#                       }
#                       request = urllib.request.Request(url=url, headers=headers)
#                       return request
#
#                   def download_image(content):
#                       pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', re.S)
#                       lt = pattern.findall(content)
#                       # 遍历列表，下载图片
#                       for image_src in lt:
#                           # 先处理image_src
#                           image_src = 'https:' + image_src
#                           # 发送请求，下载图片
#                           # 创建文件件
#                           dirname = 'qiutu'
#                           if not os.path.exists(dirname):
#                               os.mkdir(dirname)
#                           # 图片的名字叫啥
#                           filename = image_src.split('/')[-1]
#                           filepath = dirname + '/' + filename
#                           print('%s图片正在下载...' % filename)
#                           urllib.request.urlretrieve(image_src, filepath)
#                           print('%s图片下载结束...' % filename)
#                           time.sleep(1)
#
#                   def main():
#                       url = 'https://www.qiushibaike.com/pic/page/'
#                       start_page = int(input('请输入起始页码：'))
#                       end_page = int(input('请输入结束页码：'))
#                       for page in range(start_page, end_page+1):
#                           print('第%s页开始下载...' % page)
#                           # 生成请求对象
#                           request = handler_request(url, page)
#                           # 发送请求对象，获取响应内容
#                           content = urllib.request.urlopen(request).read().decode()
#                           # 解析下载内容，提取所有的图片链接，下载图片
#                           download_image(content)
#                           print('第%s页开始下载结束' % page)
#                           time.sleep(2)
#
#                   if __name__ == '__main__':
#                       main()
#       实战二
#           爬取循环翻页的标题以及标题内页的内容
#               需求
#                   爬取指定页面的标题和内容
#                   保存到html文件中，标题用h1,内容用p标签
#                   案例网站：http://www.yikexun.cn/lizhi/qianming/list_50_{}.html
#           示例
#               import urllib.request
#               import re
#               import time
#               import random
#
#               def http_image(src):
#                   url_img = src.group(1) + 'http://www.yikexun.cn/' + src.group(2) + src.group(3)
#                   return url_img
#
#               def get_text(url):
#                   #创建内容请求体
#                   request = handler_request(url)
#                   #发送请求
#                   response = urllib.request.urlopen(request).read().decode()
#                   #解析内容
#                   #提取内容
#                   pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
#                   content = pattern.findall(response)[0]
#                   #替换全部图片内容为完整url
#                   content = re.sub(r'(<img.*?src=")(.*?)(".*?>)', http_image, content)
#                   return content
#
#               def parse_content(content):
#                   pat = r'<h3><a href="(/lizhi/qianming/\d+\.html)"><b>(.*?)</b></a></h3>'
#                   pattern = re.compile(pat)
#                   #返回的标题是一个列表，列表中的元素都是元组，元素中第一个元素就是正则中第一个小括号匹配到的内容，元素中的二个元素就是正则中第二个小括号匹配到的内容
#                   lis = pattern.findall(content)
#                   #遍历列表
#                   for href_title in lis:
#                       #获取内容的链接
#                       a_href = 'http://www.yikexun.cn' + href_title[0]
#                       #获取标题
#                       title = href_title[1]
#                       #向a_href发送请求，获取响应内容
#                       content = get_text(a_href)
#                       #写入到html文件中
#                       string = '<h1>{}</h1>{}'.format(title, content)
#                       with open('lizhi.html', 'a') as f:
#                           f.write(string)
#                       # time.sleep(random.randint(10, 30))
#
#               def handler_request(url):
#                   headers = {
#                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#                   }
#                   request = urllib.request.Request(url=url, headers=headers)
#                   return request
#
#               def main():
#                   url = 'http://www.yikexun.cn/lizhi/qianming/list_50_{}.html'
#                   start_page = int(input('请输入起始页码：'))
#                   end_page = int(input('请输入结束页码：'))
#                   for page in range(start_page, end_page+1):
#                       #根据url和page去生成指定的request
#                       url = url.format(page)
#                       request = handler_request(url)
#                       #发送请求
#                       content = urllib.request.urlopen(request).read().decode()
#                       #解析内容
#                       parse_content(content)
#                       # time.sleep(random.randint(10,30))
#
#              if __name__=='__main__':
#                   main()
#   bs4解析网页
#       全称：BeautifulSoup
#       安装
#           pip源设置为国内源 切换pip源 pip切换源
#               windows
#                   在文件资源管理器的地址栏中输入%appdata%回车
#                       新建pip文件夹
#                           新建文件pip.ini
#                               用sublime打开
#                                   [global]
#                                   timeout = 6000
#                                   index_url = https://mirrors.aliyun.com/pypi/simple/
#                                   trusted-host = mirrors.aliyun.com
#               linux
#                   cd ~
#                   mkdir ~/.pip
#                   vi ~/.pip/pip.conf
#                   编辑内容，和windows一模一样
#           pip install bs4
#           pip install lxml
#       简单使用
#           说明：可以用选择器来匹配内容
#           导入方式：from bs4 import BeautifulSoup
#           BeautifulSoup类
#               本地html文件实例化对象
#                   soup = BeautifulSoup(open('本地文件'), 'lxml') #open不写打开方式，默认为r模式，即只读模式
#               网络html文件实例化对象
#                   soup = BeautifuSoup('字符串类型/字节类型', 'lxml')
#               soup属性
#                   原型：soup.标签名
#                   示例：soup.a
#                   返回值：第一个对应标签的bs4标签字典对象
#                       获取标签字典对象中的属性值
#                           原型：soup.标签名['属性值']
#                           示例：soup.a['href']
#                       属性
#                           attrs
#                               原型：soup.标签名.attrs
#                               示例：soup.a.attrs
#                               返回值：指定标签中所有属性，以字典数据格式返回
#                           text
#                               原型：soup.标签名.text
#                               示例：soup.a.text
#                               返回值：a标签中的文本内容
#                           string
#                               原型：soup.标签名.string
#                               示例：soup.a.string
#                               返回值：a标签中的文本内容
#                               注意：当标签的文本内容中有标签嵌套，则返回None，无法获取当前标签的文本内容，
#                       方法
#                           get_text()
#                               功能：获取标签中的文本内容
#                               原型：soup.标签名.get_text()
#                               示例：soup.a.get_text()
#                               返回值：标签中的文本内容
#                           find()
#                               功能、参数、用法同soup对象的find()方法
#                               示例：soup.div.find('p')
#                           find_all()
#                               功能、参数、用法同soup对象的find_all()方法
#                               示例
#                                   div = soup.find('div', class='tang')
#                                   div.find_all('a')
#                           select()
#                               功能、参数、用法同soup对象的select方法
#                               示例
#                                   div = soup.find('div', class='tang')
#                                   div.select('.du')
#                   用法：根据标签名匹配第一个对应标签的bs4标签对象
#               soup方法
#                   find()
#                       功能：查询指定标签并且设置限制条件
#                       返回值：第一个的指定标签字典对象
#                       原型：soup.find(’标签名‘, 限制条件)
#                       参数
#                           限制条件
#                               本质：关键字参数
#                               原型：属性名=属性值
#                               示例
#                                   title = ‘123’
#                                   id=’id‘
#                                   class_=’feng‘
#                                       注意:当使用class作为限制条件时，不能直接用class=‘feng’,因为class是python中的关键字，class_='feng'才能正常使用
#                                   alt=‘qu’
#                       示例：soup.find('a', title='qin')
#                       需求：当class='du'标记了两个a，我需要匹配到的二个(提取指定div下的标签对象)
#                           div = soup.find('div', class='tang')
#                           div.find('a', class='du')
#                   find_all()
#                       功能：匹配所有的指定标签
#                       原型：soup.find_all(name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)
#                       参数
#                           name：
#                               格式：
#                                   标签名字符串
#                                       返回值：返回一个列表，其中的元素是标签名字符串所指定的所有标签对象
#                                       示例：soup.find_all('a') --> [<a...>,<a...>,...]
#                                   标签名列表
#                                       返回值：返回一个列表，其中的元素是列表元素所指定的所有的标签对象
#                                       示例：soup.find_all(['a','b']) --> [<a...>,...,<b...>,...]
#                           attrs
#                               功能：使用标签的属性来匹配标签对象
#                               示例：soup.find_all(attrs={'class':'p_item'}) --> [找到所有class=p_item的标签对象]
#                           limit
#                               功能：指定提取标签对象的条数,从开始计算，即前面几条
#                               示例：soup.find_all('a', limit=2) --> [<a...><a/>,<a...></a>]
#                   select()
#                       功能：根据选择器，匹配指定的标签对象
#                       常用选择器
#                           标签选择器 a{}
#                           id选择器 #idName
#                           class选择器 .className
#                           属性选择器 a[attr]/a[attr='value']
#                           通配符选择器 *
#                           交集选择器 p[attr='value1']p[attr='value2']
#                           并集选择器 .className, #idName, a
#                           弟弟选择器 #idName+a
#                           子代选择器 #idName>a
#                           后代选择器 #idName a
#                           伪类选择器 div a:first-child
#                       返回值：返回列表，其中的元素是通过选择器匹配到的所有标签对象
#                       示例
#                           soup.select('#a + li > a')
#                           soup.select(.tang a)[2]
#                       注意
#                           选择器之间的符号必须用空格分割，比如 .className > a / #idName + a
#                           后代选择器的空格符号可以是一个或二个或三个
#                           选择器匹配一个标签对象时，也是返回的列表，需要[0],获得标签对象
#                           当你需要选择其中一个标签元素时，可以用下标索引
#       测试
#           from bs4 import BeautifulSoup
#           #生成对象
#           with open('bs4Test.html', 'r', encoding='utf8') as f:
#               html = f.read()
#           soup = BeautifulSoup(html, 'lxml')
#           # print(soup.a)
#           # print(soup.a['href'])
#           # print(soup.a['target'])
#           # print(soup.a['title'])
#           # print(soup.a.attrs)
#           # print(soup.div.find('p'))
#           # print(soup.div.text)
#           # print(soup.div.string)
#           # print(soup.div.get_text())
#           # print(soup.find('a', title='qin'))
#           # print(soup.find('a', alt='qin'))
#           # div = soup.find('div', class_='tang')
#           # print(div.find('a', class_='du'))
#           # print(soup.find('a', id='feng'))
#           # print(soup.find_all(['a','b']))
#           # print(soup.find_all('a', limit=2))
#           # print(soup.select('.tang  a'))
#           # print(soup.select('#feng')[0].text)
#       实战：智联招聘爬虫
#           import urllib.request
#           import urllib.parse
#           from bs4 import BeautifulSoup
#           import json
#           import time
#           class ZhiLianSpider():
#               #类属性，url不变部分,类属性的访问方式：1、self.类属性名 2、类名.类属性名
#               url = 'https://sou.zhaopin.com/?p={}&jl={}&sf=0&st=0&kw={}&kt=0'
#               def __init__(self, jl, kw, start_page, end_page):
#                   #将参数都保存为自己的成员属性
#                   self.jl = jl
#                   self.kw = kw
#                   self.start_page = start_page
#                   self.end_page = end_page
#                   self.headers = {
#                       'Host': 'sou.zhaopin.com',
#                       'Connection': 'keep-alive',
#                       'Cache-Control': 'max-age=0',
#                       'Upgrade-Insecure-Requests': '1',
#                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#                       # 'Accept-Encoding': 'gzip, deflate, br',
#                       # 'Accept-Language': 'zh-CN,zh;q=0.9',
#                       'Cookie': 'urlfrom=121113803; urlfrom2=121113803; adfbid=0; adfbid2=0; x-zp-client-id=611bd170-7446-44da-9490-40b81d4cb975; registerGroup=capi; sts_deviceid=16bb48fc4a6367-0f27b2fe7bba56-6353160-1749600-16bb48fc4a7732; sts_sg=1; sts_sid=16bb48fc4ab82d-0804aba847f4db-6353160-1749600-16bb48fc4ac528; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAsaVz9VI00000r2_AdC00000JqvHVm.THLyktAJdIjA80K85HRLnjc3nW6kgv99UdqsusK15yD3m1TLrjfYnj0snH-9mhn0IHYsfbfvfH97fWRsfbc4njT1P1T4wW0dPYfdPWfzPbRdrfK95gTqFhdWpyfqn1cznWmzPH63PBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1YYnH6srf%26tpl%3Dtpl_11535_18778_14772%26l%3D1511763170%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3222625886_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D241%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3D57028281_hao_pg%26inputT%3D3533; sajssdk_2015_cross_new_user=1; at=aa59c172498d4a588a402fdf6a1da677; rt=d3dacd4fb1ad4590805169ef61771927; ZP_OLD_FLAG=false; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1562102702; dywea=95841923.4323406215926274600.1562103011.1562103011.1562103011.1; dywec=95841923; dywez=95841923.1562103011.1.1.dywecsr=i.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/resume/new; __utma=269921210.1700397125.1562103011.1562103011.1562103011.1; __utmc=269921210; __utmz=269921210.1562103011.1.1.utmcsr=i.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/resume/new; jobRiskWarning=true; acw_tc=2760823b15621030399942441efbd69db813a17a745dead5482e3112052e14; sou_experiment=unexperiment; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221025306053%22%2C%22%24device_id%22%3A%2216bb48fc4fb1b0-0100b636dfa8f1-6353160-1749600-16bb48fc4fc17a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%2216bb48fc4fb1b0-0100b636dfa8f1-6353160-1749600-16bb48fc4fc17a%22%7D; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1562106652; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; ZL_REPORT_GLOBAL={%22/resume/new%22:{%22actionid%22:%22abbbcdcf-7442-4fa4-afa8-c81526c9ca71%22%2C%22funczone%22:%22addrsm_ok_rcm%22}%2C%22sou%22:{%22actionid%22:%224cf50a9e-72aa-4f93-bcdc-b9786f374007-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%22f58c80b0-d844-4a1a-ac77-b30ec94eaa1d-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_evtseq=196',
#                   }
#                   #定义一个空列表，用来存放所有的工作信息
#                   self.items = []
#                #根据page拼接指定的url，然后生成请求对象
#                def handler_request(self, page):
#                    url_now = self.url.format(page, self.jl, self.kw)
#                    #构建请求对象，发送请求
#                    request = urllib.request.Request(url=url_now, headers=self.headers)
#                    return request
#                #解析内容
#                def parse_response(self, response):
#                    #生成soup对象
#                    soup = BeautifulSoup(response, 'lxml')
#                    #思路：先找到所有的岗位外层div，因为一个外层div就是一个岗位，然后通过div对象的select方法获取每一条岗位的对应信息
#                    position_divList = soup.select('#listContent > .contentpile__content__wrapper > .contentpile__content__wrapper__item > a')
#                    contentList = []
#                    for a_first in position_divList:
#                        # 职位url
#                        position_href = a_first['href']
#                        # 职位名称
#                        position = a_first.select('.contentpile__content__wrapper__item__info__box__jobname__title')[0].text
#                        # 公司url
#                        company_herf = a_first.select('a')[0]['href']
#                        # 公司名称
#                        company = a_first.select('a')[0].text
#                        # 月薪
#                        mSalary = a_first.select('p')[0].text
#                        # 工作地址
#                        address = a_first.select('.contentpile__content__wrapper__item__info__box__job__demand__item')[0].text
#                        # 工作年限
#                        wLife = a_first.select('.contentpile__content__wrapper__item__info__box__job__demand__item')[
#                            1].text.replace(' ', '').replace('\n', '')
#                        # 学历
#                        education = a_first.select('.contentpile__content__wrapper__item__info__box__job__demand__item')[2].text
#                        # 公司体制
#                        system = a_first.select('.contentpile__content__wrapper__item__info__box__job__comdec__item')[0].text
#                        # 员工人数
#                        staffNumber = a_first.select('.contentpile__content__wrapper__item__info__box__job__comdec__item')[1].text
#                        # 岗位标签
#                        label = a_first.select('.contentpile__content__wrapper__item__info__box__welfare')[0].text.replace(' ', '')
#                        # 整合数据到字典
#                        dic = {'position_href': position_href, 'position': position, 'company_herf': company_herf,
#                               'company': company, 'mSalary': mSalary, 'address': address, 'wLife': wLife, 'education': education,
#                               'system': system, 'staffNumber': staffNumber, 'labe': label}
#                        self.items.append(dic) #将每条工作岗位信息，即每个字典存放到列表中
#                   return contentList
#                #爬取程序
#                def run(self):
#                    #循环爬取每一页数据
#                    for page in range(self.start_page, self.end_page+1):
#                        print('开始爬取第%s页'%page)
#                        #根据页码生成一个请求对象
#                        request = self.handler_request(page)
#                        #发送请求
#                        response = urllib.request.urlopen(request).read().decode()
#                        #解析内容
#                        self.parse_response(response)
#                        print('结束爬取第{}页'.format(page))
#                        time.sleep(2)
#                    #将列表数据保存到文件中
#                    string = json.dumps(self.items, ensure_ascii=False) #ensure_ascii表示将列表字典转换成json时，禁用ascII编码
#                    with open('zhilian.txt', 'w', encoding='utf8') as f:
#                        f.write(string)
#            def main():
#                jl = input('请输入工作地点编号：')
#                kw = input('请输入关键字：')
#                start_page = int(input('请输入起始页码：'))
#                end_page = int(input('请输入结束页码：'))
#                #创建对象，启动爬取程序
#                spider = ZhiLianSpider(jl, kw, start_page, end_page)
#                spider.run()
#            if __name__ == '__main__':
#                main()
#   xpath
#       概念
#           xml
#               概念
#                   xml是用来传输数据和存储数据的
#                   xml的格式和html类似
#                       跟节点-子节点-文本
#                   区别在于html的标签时预设定的，而xml的标签是自定义的
#           xpath
#               概念
#                   xpath是在xml中查询xml数据的语言
#                   我们学习的xpath是第三方封装的用于查询html节点的库
#                   它是一种路径表达式
#       安装：pip install lxml
#       常用的路径表达式
#           /  从跟节点开始查找
#           // 不考虑位置的查找
#           ./ 从当前节点往下查找
#           @  选取属性
#           .. 上一级
#           示例
#               /bookstore/book 选取根节点bookstore下面所有直接子节点book
#               //book 选取所有book
#               bookstore//book 查找bookstore下面所有的book
#               /bookstore/book[1] 查找bookstore下面的第一个book
#               /bookstore/book[last()] bookstore里面的最后一个book
#               /bookstore/book[position()<3] bookstore里面前2个book
#               //title[@lang] 查找所有的包含lang属性的title，
#               //title[@lang=’eng‘] 查找所有的包含lang属性='eng'的title
#               * 查找所有节点
#       在chrome安装 谷歌访问助手
#           下载谷歌访问助手解压得到.crx文件
#           将.crx文件拖动到谷歌浏览器
#       在chrome安装 Xpath helper插件
#           打开谷歌浏览器
#               点击三个点
#                   更多工具
#                       扩展程序
#                           打开谷歌访问助手
#                               点击谷歌助手
#                                   点击Chrome商店
#                                       搜索xpath
#                                           将xpath helper添加至Chrome
#                                               安装好后重启浏览器即可使用
#       插件使用
#           点击XPath Helper
#               query
#                   路径表达式
#               results
#                   返回结果
#           快捷键
#               打开或关闭ctrl+shift+x
#       常见定位方式
#           属性定位
#               //input[@id="kw"] --> input#kw
#               //input[@class="btn self-btn bg s_btn"] --> input.btn self-btn bg s_btn
#           层级定位
#               //div[@id="u"]/a[@class="toindex"] --> div#u>a.toindex
#           索引定位
#               //div[@id="head_wrapper"]/div[2]/a[1] --> div#head_wrapper>div:nth-child{2}>a:nth-child{1}
#               注意索引从1开始
#           逻辑运算
#               //input[@type="hidden" and @name="rsv_spt"]
#           模糊匹配
#               contains
#                   //input[contains(@class,"s_")] 模糊匹配class为包含s_的所有input标签
#                   //input[contains(text(),"爱")] 模糊匹配文本中包含“爱”的所有input标签
#               starts-with
#                   //input[starts-with(@class,"s_")] 模糊匹配class为s_开头的所有input标签
#                   //input[starts-with(text(), "彭")] 模糊匹配文本中以彭开头的所有input标签
#           取文本
#               //div[@id="u_sp"]/a[5]/text()
#               //div[@id="u_sp"]//text() --> 找到div#u_sp下的所有文本内容,不包含div本身的文本内容
#           取属性
#               //div[@id="u_sp"]/a[5]/@href
#           灵活运用双斜杠
#               //div[@id="head"]//a[@class="toindex"]
#               //div[@id="u_sp"]//text() --> 找到div#u_sp下的所有文本内容
#       代码中使用xpath
#           导入方式：from lxml import etree
#           原理：将html文档变成一个对象，然后调用对象的方法去查找指定的节点
#           本地文件
#               tree = etree.parse(文件名)
#               注意
#                   如果出现lxml.etree.XMLSyntaxError,就用以下方式打开
#                       from lxml import etree
#                       parser = etree.HTMLParser(encoding="utf-8")
#                       tree = etree.parse("123.html", parser=parser)
#               说明：tree是一个实例化对象，同soup对象相同
#                   实例化对象的方法
#                       原型：xpath('xpath代码')
#                       功能：定位标签
#                       返回值：列表，元素是标签对象
#                       示例：result = tree.xpath('//div[@id="you"]')
#                           标签对象的属性
#                               text
#                                   存储：标签对象的文本内容
#                                   取值：标签对象.text
#                                   示例：print(result.text)
#                           标签对象的xpath方法
#                               xpath()
#                                   text = result.xpath('//a[@class="i"]/text()')
#                                   href = result.xpath('//a[@class="i"]/@href')
#                               text
#               示例
#                   from lxml import etree
#                   #生成etree对象
#                   tree = etree.parse('text.html')
#                   result1 = tree.xpath('//div[@class="tang"]/ul/li[@class="love"]/text()')[0]
#                   result2 = tree.xpath('//li[@class="love"]/@name')[0]
#                   result3 = tree.xpath('//div[@class="tang"]/ul/li[last()]/a/@href')[0]
#                   result4 = tree.xpath('//div[@class="tang"]/ul/li[@class="love" and @name="456"]/text()')[0]
#                   result5 = tree.xpath('//div[@class="tang"]/ol/li[contains(@class, "sd")]/text()')
#                   result6 = tree.xpath('//li[contains(text(), "陈")]/text()')
#                   result7 = tree.xpath('//li[starts-with(@class, "ba")]/text()')[0]
#                   result8 = tree.xpath('//li[starts-with(text(), "彭")]/text()')
#                   #将获得的内容列表组合成一个字符串
#                   result9 = ','.join(tree.xpath('//div[@class="song"]//text()')).replace('\n','').replace(' ','').replace(',,',',')
#                   print(result9)
#                   #先获取一个div，再在这个div中去获取标签对象,注意//前一定要加.先选区域再选局部
#                   divElements = tree.xpath('//div[@id="you"]')
#                   text = divElements.xpath('.//a[@class="i"]/text()')
#           xpath与tbody
#               谷歌浏览器在遇到没有添加tbody的表时会自动添加tbody
#               其实原码中并没有tbody
#               因此用xpath写规则时一定要注意tbody是否真实存在，不存在则直接向下匹配就行，即在规则中直接跳过tbody
#           网络文件
#               tree = etree.HTML(网页字符串)
#   实战
#       站长素材
#            import urllib.request
#            import urllib.parse
#            from lxml import etree
#            import json
#            import time
#            import os
#
#            class zzscSipder():
#                url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian_{}.html'
#                def __init__(self, start_page, end_page):
#                    self.start_page = start_page
#                    self.end_page = end_page
#                    self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
#                    self.contentList = []
#
#                def download_image(self, image_src):
#                    dirPath = 'xingan'
#                    if not os.path.exists(dirPath):
#                        os.mkdir(dirPath)
#                    fileName = os.path.basename(image_src)
#                    filePath = os.path.join(dirPath, fileName)
#                    urllib.request.urlretrieve(image_src, filePath)
#
#
#                def XPath(self, response):
#                    htmlelement = etree.HTML(response)
#                    pictureList = htmlelement.xpath('//div[@id="container"]/div/div/a/img/@src2')
#                    #遍历列表，依次下载图片
#                    for image_src in pictureList:
#                        self.download_image(image_src)
#                        time.sleep(1)
#
#
#                def handler_request(self, page):
#                    #伪造url
#                    #设置不同的url
#                    if page != 1:
#                        url_new = self.url.format(page)
#                    else:
#                        url_new = 'http://sc.chinaz.com/tupian/xingganmeinvtupian.html'
#                    #伪造请求头
#                    headers = self.headers
#                    #构造请求体
#                    response = urllib.request.Request(url=url_new, headers=headers)
#                    return response
#
#                def run(self):
#                    #构造请求体,根据输入的页面伪造url
#                    for page in range(self.start_page, self.end_page + 1):
#                        #构造请求体
#                        request = self.handler_request(page)
#                        #发送请求，获取响应
#                        response = urllib.request.urlopen(request).read().decode()
#                        #解析内容
#                        self.XPath(response)
#                        time.sleep(2)
#                    #保存数据
#                    string = json.dumps(self.contentList, ensure_ascii=False)
#                    with open('xgmv.txt', 'w', encoding='utf8') as f:
#                        f.write(string)
#            def main():
#                #根据用户输入的开始页和结束页爬取对应页面内容
#                start_page = int(input('请输入开始页码：'))
#                end_page = int(input('请输入结束页码：'))
#                #构造一个爬虫对象是
#                zzsc = zzscSipder(start_page, end_page)
#                zzsc.run()
#
#            if __name__=='__main__':
#                main()
#       总结：在爬取站长之家的素材时，遇到了前段的懒加载技术
#           懒加载概念
#               主要解决用户登录网站时一次性加载图片过多，导致用户体验差的问题
#               懒加载能让用户用到图片时再加载图片
#           实现方式
#               img标签的图片路径名只有是src时才能请求图片
#                   <img src="图片路径">
#               图片网站中的img标签全部写的是非src属性名
#                   <img _src="图片路径">
#                   <img data_src="图片路径">
#               通过js滚轮滑动事件，判断图片是否进入可视区
#                   进入就用js修改img属性为src
#           查看到底是什么，替换了src进行懒加载的
#               可以查看网页源代码，观察img标签
#json数据解析
#   python处理json
#       导入：import json
#       示例变量：lt = [{'a':'b'},{'c':'d'}，{'e':'f'}]
#       方法
#           json.dumps()
#               功能：将字典列表转化成json格式的字符串
#           json.loads()
#               功能：将json格式转化为字典列表
#           json.dump()
#               功能：将字典列表转化为json格式字符串并且写入到文件中
#               示例：json.dump(lt, open('json.txt', 'w', encoding='utf8'))
#           json.load()
#               功能：从文件中读取json格式字符串转化为字典列表
#               示例：obj = json.load(open(‘json.txt’, 'r', encoding='utf8'))
#   前段处理json
#       将json格式字符串转化为js对象
#       JSON.parse('json格式字符串')
#       eval('('+json格式字符串+')')
#   jsonpath练习
#       用途：用于解析json数据
#       安装：pip install jsonpath练习
#       学习：https://blog.csdn.net/luxideyao/article/details/77802389
#       导入：import jsonpath练习
#       方法：jsonpath练习.jsonpath练习()
#       原型：jsonpath练习.jsonpath练习(obj, expr)
#       参数
#           obj：python对象——列表或字典，即[{},{}]or{'':{'':[{},{}]}}
#               注意：在读取json文件时，可以用json.load()进行加载，因为加载过来的数据是python对象
#           expr：jsonpath的路径表达式
#       返回值：列表，列表中的元素以找到的节点为key的value
#       常用路径表达式
#           $：根元素查询
#           .：下一级查询
#          ..：任意位置查询
#          []：列表操作符号
#         ?()：选择器
#           @：当前元素
#       示例
#           json文件
#             { "store": {
#                 "book": [
#                   { "category": "参考",
#                     "author": "Nigel Rees",
#                     "title": "Sayings of the Century",
#                     "price": 8.95
#                   },
#                   { "category": "文学",
#                     "author": "Evelyn Waugh",
#                     "title": "Sword of Honour",
#                     "price": 12.99
#                   },
#                   { "category": "言情",
#                     "author": "Herman Melville",
#                     "title": "Moby Dick",
#                     "isbn": "0-553-21311-3",
#                     "price": 8.99
#                   },
#                   { "category": "fiction",
#                     "author": "J. R. R. Tolkien",
#                     "title": "The Lord of the Rings",
#                     "isbn": "0-395-19395-8",
#                     "price": 22.99
#                   }
#                 ],
#                 "bicycle": {
#                   "color": "红色",
#                   "price": 19.95
#                 }
#               }
#             }
#           解析此json
#               import jsonpath练习
#               import json
#               obj = json.load(open('book.json', 'r', encoding='utf8'))
#
#               从根部开始，store下面的book所有的字典值中的autor的字典值
#               [*]代表查询列表中所有元素，book下面是一个列表，列表中存放了每本书的数据，因此[0]表示第一本数的数据，以此类推
#               result = jsonpath.jsonpath(obj, '$.store.book[*].author')
#               print(result)
#
#               从根部开始，所有位置查询作者
#               返回列表，列表元素为所有author的字典值
#               result = jsonpath.jsonpath(obj, '$..author')
#               print(result)
#
#               查询store下面所有节点，即book和bicycle，,[[{},{}...],{}]
#               返回列表，列表中有两个元素，第一个元素是book的字典值，第二个元素是bicyle的字典值
#               result = jsonpath.jsonpath(obj, '$.store.*')
#               print(result)
#
#               查询store下面所有的price
#               返回列表，列表中有price为键的字典值值，
#               result = jsonpath.jsonpath(obj, '$.store..price')
#               print(result) --> [8.95, 12.99, 8.99, 22.99, 19.95]
#
#               从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行索引（索引从0开始）
#               返回列表，列表元素为book的第三个字典值，
#               result = jsonpath.jsonpath(obj, '$..book[2]')
#               print(result)
#
#               从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行匹配操作，即[]也是一个列表，列表元素的数值对应book的值
#               返回列表，列表元素为book的第0个、第1个、第2个、第3个字典值，
#               result = jsonpath.jsonpath(obj, '$..book[0,1,2,3]')
#               print(result)
#
#               从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行切片操作
#               返回列表，列表元素为book的前3个字典值，
#               result = jsonpath.jsonpath(obj, '$..book[:3]')
#               print(result)
#
#               从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行索引操作，索引值为当前列表的长度-1的值
#               返回列表，列表元素为book的最后一个字典值，
#               result = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
#               print(result)
#
#               从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行切片操作，索引值为当前列表中包含isbn的值
#               返回列表，列表元素为book的包含了isbn的字典值，
#               result = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
#               print(result)
#
#               从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行匹配操作，索引值为当前列表中价格小于10元的值
#               返回列表，列表元素为book的价格小于10元的字典值，
#               result = jsonpath.jsonpath(obj, '$..book[?(@.price<10)]')
#               print(result)
#
#               从根部开始，查询所有位置的所有的字典值
#               返回列表，第一个列表元素为第一层的字典值，即store的字典值；第二个元素为第二层第一个的字典值，即book的字典值；第三个元素为第二层第二个的字典值；第四个是第三层的第一个字典值
#               result = jsonpath.jsonpath(obj, '$..*')
#               print(result)
#   实战：智联招聘
#       网站分析
#           获取登录后网页信息
#               人工登录网站
#                   进入需要采集信息页面，即岗位信息页面
#                       分析网站的url结构，分析数据加载方式
#                           数据是通过ajax动态加载，动态加载的数据一般都是json格式
#                               打开fiddler
#                                   刷新网页
#                                       观察fiddler，可以查看到动态加载过来的json数据
#                                           分析头部信息，可以知道只要向指定url发送get请求就能响应json数据
#                                               再次抓取翻页后的json数据包
#                                                   对比观察不同页的url的变化情况，确定翻页参数
#                                                       分析url中可手动输入的有用变化参数
#                                                           分析后可以得出结论
#                                                               start 开始数据条数
#                                                               cityId 城市编号
#                                                               wk 关键字
#                                                           可以开始写代码了
#         import urllib.request
#         import urllib.parse
#         import json
#         import jsonpath练习
#         import pandas as pd
#         import time
#         import random
#
#         GjobName = []
#         GjobCity = []
#         GupdateDate = []
#         Gsalary = []
#         Gdistance = []
#         GeduLevel = []
#         GjobType = []
#         GfeedbackRation = []
#         GemplType = []
#         GpositionURL = []
#         Gwelfare = []
#         GtimeState = []
#         Gcompany = []
#         GcompanyType = []
#         GcompanySize = []
#         GcompanyUrl = []
#         GcompanyLogo = []
#         GbusinessArea = []
#
#         def saveDataFrame(cityId, wk):
#             # 创建pandas
#             dataFrame = pd.DataFrame({
#                 '岗位名称': GjobName,
#                 '工作城市': GjobCity,
#                 '更新时间': GupdateDate,
#                 '薪资待遇': Gsalary,
#                 '工作地点': Gdistance,
#                 '学历要求': GeduLevel,
#                 '岗位类型': GjobType,
#                 '响应速度': GfeedbackRation,
#                 '雇员类型': GemplType,
#                 '岗位详情': GpositionURL,
#                 '雇员福利': Gwelfare,
#                 '岗位状态': GtimeState,
#                 '公司名字': Gcompany,
#                 '公司体制': GcompanyType,
#                 '在职员工': GcompanySize,
#                 '公司详情': GcompanyUrl,
#                 '公司logo': GcompanyLogo,
#                 '商圈范围': GbusinessArea,
#             })
#             dataFrame.to_excel('城市编号{}的{}岗位.xlsx'.format(cityId, wk), encoding='utf8')
#             return dataFrame
#
#         class zlSpider():
#             def __init__(self, url, page, cityId, wk):
#                 self.url = url
#                 self.page = 90*page
#                 self.cityId = cityId
#                 self.wk = wk
#                 self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
#
#             def jsonPath(self, obj):
#                 #解析json数据
#                 jobName = jsonpath练习.jsonpath练习(obj, '$..results[*].jobName')
#                 jobCity = jsonpath练习.jsonpath练习(obj, '$..results[*].city.display')
#                 updateDate = jsonpath练习.jsonpath练习(obj, '$..results[*].updateDate')
#                 salary = jsonpath练习.jsonpath练习(obj, '$..results[*].salary')
#                 distance = jsonpath练习.jsonpath练习(obj, '$..results[*].distance')
#                 eduLevel = jsonpath练习.jsonpath练习(obj, '$..results[*].eduLevel.name')
#                 jobType = jsonpath练习.jsonpath练习(obj, '$..results[*].jobType.items[*].name')
#                 feedbackRation = jsonpath练习.jsonpath练习(obj, '$..results[*].feedbackRation')
#                 emplType = jsonpath练习.jsonpath练习(obj, '$..results[*].emplType')
#                 positionURL = jsonpath练习.jsonpath练习(obj, '$..results[*].positionURL')
#                 welfare = jsonpath练习.jsonpath练习(obj, '$..results[*].welfare')
#                 timeState = jsonpath练习.jsonpath练习(obj, '$..results[*].timeState')
#                 company = jsonpath练习.jsonpath练习(obj, '$..results[*].company.name')
#                 companyType = jsonpath练习.jsonpath练习(obj, '$..results[*].company.type.name')
#                 companySize = jsonpath练习.jsonpath练习(obj, '$..results[*].company.size.name')
#                 companyUrl = jsonpath练习.jsonpath练习(obj, '$..results[*].company.url')
#                 companyLogo = jsonpath练习.jsonpath练习(obj, '$..results[*].companyLogo')
#                 businessArea = jsonpath练习.jsonpath练习(obj, '$..results[*].businessArea')
#                 #添加到全局变量中
#                 GjobName.extend(jobName)
#                 GjobCity.extend(jobCity)
#                 GupdateDate.extend(updateDate)
#                 Gsalary.extend(salary)
#                 Gdistance.extend(distance)
#                 GeduLevel.extend(eduLevel)
#                 GjobType.extend(jobType)
#                 GfeedbackRation.extend(feedbackRation)
#                 GemplType.extend(emplType)
#                 GpositionURL.extend(positionURL)
#                 Gwelfare.extend(welfare)
#                 GtimeState.extend(timeState)
#                 Gcompany.extend(company)
#                 GcompanyType.extend(companyType)
#                 GcompanySize.extend(companySize)
#                 GcompanyUrl.extend(companyUrl)
#                 GcompanyLogo.extend(companyLogo)
#                 GbusinessArea.extend(businessArea)
#
#             def handler_request(self):
#                 url_new = self.url.format(self.page, self.cityId, self.wk)
#                 request = urllib.request.Request(url=url_new, headers=self.headers)
#                 return request
#
#             def run(self):
#                 request = self.handler_request()
#                 json_txt = urllib.request.urlopen(request).read().decode()
#                 #解析json
#                 obj = json.loads(json_txt)
#                 #将遍历的所有数据保存到全局变量中
#                 self.jsonPath(obj)
#
#         def main():
#             url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId={}&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&=0&at=fb56e0ff848b454d96b3aed7969c99af&rt=eaafa995cb03407293c812875876150a&_v=0.69207691&userCode=1025306053&x-zp-page-request-id=154a76fd6db2456384fdb8a8bc55b640-1562203709996-356095&x-zp-client-id=611bd170-7446-44da-9490-40b81d4cb975'
#             start_page = int(input('开始页：'))
#             end_page = int(input('结束页：'))
#             cityId = int(input('城市编号：'))
#             wk = input('搜索关键字：')
#             #遍历所有页，得到dataFrame，可以调用dataFrame()函数返回总的dataFrame数据
#             for page in range(start_page, end_page+1):
#                 spider = zlSpider(url, page, cityId, wk)
#                 spider.run()
#                 time.sleep(random.random()*10)
#             saveDataFrame(cityId, wk)
#
#         if __name__ == '__main__':
#             main()



#Selenium
#   概念：python的第三方库，对外接口可以操作你的浏览器，让浏览器完成自动化的操作
#   安装：pip install selenium练习
#   使用selenium
#       导入：from selenium import webdriver
#           webdriver类
#               方法
#                   原型：webdriver.Chrome(executable_path=path)
#                   功能：创建一个谷歌浏览器的示例对象
#                   参数：executable_path 谷歌浏览器的驱动路径 r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#                   返回值：谷歌驱动的实例化对象
#                   示例
#                       path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#                       browser = webdriver.Chrome(executable_path=path) #创建对象就会自动打开浏览器
#                           驱动对象的属性
#                               browser.page_source
#                               功能：获取当前网页的html源代码
#                               用法：可以将网页源代码赋值给一个变量，变量可以保存
#                               示例
#                                   html = browser.page_source
#                                   with open('doubandiany.html', 'w', encoding='utf8') as f:
#                                       f.write(html)
#                           驱动对象的方法
#                               get()
#                                   原型：browser.get(url)
#                                   功能：打开指定网页
#                                   返回值：None
#                               back()
#                                   原型：browser.back()
#                                   功能：退回
#                                   返回值：None
#                               forward()
#                                   原型：browser.forward()
#                                   功能：前进
#                                   返回值：None
#                               查询节点的方法
#                                   find_element_by_id('idName')
#                                       功能：根据id找节点
#                                       返回值：节点对象
#                                       示例：my_input = browser.find_element_by_id('kw')
#                                           节点对象方法
#                                               send_keys()
#                                                   原型：send_keys('content')
#                                                   功能：向节点标签中输入内容
#                                                   示例：my_input.send_keys('美女')
#                                               click()
#                                                   原型：click
#                                                   功能：点击节点标签
#                                                   示例：browser.find_element_by_id('button').click()
#                                   find_elements_by_name('name')
#                                       功能：根据name找节点
#                                   find_elements_by_xpth('xpth')
#                                       功能：根据xpath找节点
#                                   find_elements_by_tag_name('tagName')
#                                       功能：根据标签名找节点
#                                   find_elements_by_class_name('className')
#                                       功能：根据类名找节点
#                                       返回值：返回列表，列表中是多个节点对象
#                                   find_elements_by_css_selector('selector')
#                                       功能：根据选择器找节点
#                                   find_elements_by_link_text('text')
#                                       功能：根据链接内容找节点
#                                       返回值：列表，列表元素是a标签为text的节点对象
#                                       示例
#                                           a = browser.find_elemets_by_link_text('设置')
#                                           a.click()
#                               switch_to_alert()
#                                   功能：捕获弹窗对象
#                                   示例：browser.switch_to_alert()
#                                   返回值：弹窗对象
#                                       弹窗对象方法
#                                           accept()
#                                               功能：确定
#                                               示例：browser.switch_to_alert().accept()
#                                           dismiss()
#                                               功能：取消
#                                               示例：browser.switch_to_alert().dismiss()
#                               save_screenshot(path)
#                                   功能：给浏览器界面截图
#                                   参数：path 截图保存路径
#                                   示例：browser.save_screenshot('meinv.png')
#                               execute_script(js)
#                                   功能：让驱动对象执行js代码
#                                   参数：原生js代码
#                                   示例
#                                       js = 'var q=document.documentElement.scrollTop=100000' #模拟滚动条滚到底部
#                                       browser.execute_script(js)
#       操作谷歌浏览器
#           安装谷歌浏览器驱动
#               下载驱动
#                   http://chromedriver.storage.googleapis.com/index.html
#                   下载驱动时注意对应谷歌浏览的版本号
#               将驱动解压到谷歌浏览器的根目录下
#               将其路径设置到环境变量中
#           有头版本
#               from selenium import webdriver
#               import time
#               #创建一个模拟浏览器对象
#               path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#               browser = webdriver.Chrome(executable_path=path) #创建对象就会自动打开浏览器
#           无头版本
#               from selenium.webdriver.chrome.options import Options
#               from selenium import webdriver
#
#               #设置谷歌的无头浏览器
#               options = Options()
#               options.add_argument('--headless') #添加属性无头
#               options.add_argument('--disable-gpu') #添加属性gpu不加载
#
#               #创建无头浏览器对象
#               path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#               browser = webdriver.Chrome(executable_path=path, options=options)

#复杂登录
#   小技巧
#       快速清洗post请求数据，正则快速替换
#           在登录过程中总会伴随抓包post数据
#               在fiddler中的request的Raw中最后一排就是&格式的post请求数据
#                   粘贴到pycharm中，可以用正则替换快速将&格式的post数据转化为字典格式数据
#                       username=cd028cylpsx&password=135cylpsx&_token=eSqhJNCz0B2Is8AeaNXGKxcWMDabM2tT2JtNyiyR&_t=1562234602689
#                       ctrl + r
#                       勾选 Regex
#                       搜索框写入 (.*?)=(.*?)&      谷歌抓包(.*?): (.*?)\n      fildder抓包 (\w+)\s(.*?)\n
#                       替换框写入 '$1':'$2',\n             '$1':'$2',\n                   '$1':'$2',\n
#                       点ReplaceAll
#                       数据就变成了
#                           'username':'cd028cylpsx',
#                           'password':'135cylpsx',
#                           '_token':'eSqhJNCz0B2Is8AeaNXGKxcWMDabM2tT2JtNyiyR',
#                           _t=1562234602689
#   formhash
#       概念：
#           表单令牌，每次登陆的哈希值都不一样，防止重复登陆或防止爬虫
#           登陆的本质：给接口发送post请求，将post数据提交上去
#           提交post数据时，有formhash值就必须要用代码动态获取哈希值同post数据一起提交才能登陆
#       前端formhash实现原理
#           <form>
#               <input type="hidden" name="formhash" value="a7a50903">
#           </form>
#           提价表单时会默认提交name=formhash，value=哈希值的post数据
#       说明
#           如果有formhash或者其他需要再网页中动态获取的参数，登陆过程就变了
#               没有需要动态获取参数的网页模拟登录过程为：直接抓包找到post地址，发送pose请求即可登录成功
#               有需要动态获取参数的网页模拟登录过程为：先发送get请求到登录页面，然后通过xpath或bs4获取需要的表单令牌，然后发送post请求开始登录，登录后再发get到需要获取数据的页面获取数据


#requests
#   安装：pip install requests
#   官方文档：http://cn.python-requests.org/zh_CN/latest/
#   用来做什么：等同于urllib，即模拟浏览器发送请求
#   本质：是urllib的一层封装
#   requests的使用
#       导入：import requests
#       request类的方法
#           get(url, headers, params, proxies)
#               功能：发送get请求
#               参数
#                   url 目标网址
#                   headers 伪造headers
#                   params get参数，数据格式要求是字典数据
#                   proxies 添加代理，代理的格式为{'http':'http://115.200.211.49:8118'}, 一定要注意http协议还是https协议
#               返回值：响应对象，即response对象
#               示例
#                   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
#                   get_data = {'kw':'陈'}
#                   res = requests.get(url='http://www.baidu.com', headers=headers, params=get_data)
#                       response对象属性
#                           res.encoding
#                               值：当前文档的编码格式
#                               查看值 print(res.encoding) --> 'utf8'
#                               设置值 res.encoding = 'utf8'
#                           res.text
#                               值：字符串格式的html文档
#                               查看值：print(res.text)
#                               保存值
#                                   with open('1.html', 'w') as f:
#                                       f.write(res.text)
#                           res.content
#                               值：字节格式的html文档
#                               查看值：print(res.content)
#                               保存值
#                                   with open('1.html', 'wb') as f:
#                                       f.write(res.content)
#                           res.status_code
#                               值：状态码
#                               查看值：print(res.status_code)
#                           res.headers
#                               值：响应头部，字典格式
#                               查看值：print(res.headers)
#                           res.url
#                               值：请求url
#                               查看值：print(res.url)
#                       response对象方法
#                           res.json()
#                               功能：返回json数据
#       post(url, headers, data)
#           功能：模拟浏览器给目标网址发送post请求
#           参数：data是字典格式的formdata
#           返回值：响应对象
#           响应对象：属性 encoding text content status_code headers url 方法 json()
#           示例
#               import requests
#               url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=48654C3FB7894B0C8B61C29E875AD977&IID=translator.5038.17'
#               headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
#               formdata = {'fromLang':'auto-detect','text':'who am i？','to':'zh-Hans',}
#               res = requests.post(url=url, data=formdata, headers=headers)
#               res.encoding = 'utf8'
#               print(res.text)
#       ajax的get请求
#           主要是抓包分析出ajax的请求url，发送get请求的方式同上
#       ajax的post请求
#           主要是抓包分析出ajax的请求url，发送post请求的方式同上
#       代理
#           注意：一定要注意代理的http类型，http类型向网站发送http协议，https类型向网站发送https协议
#               示例
#                   import requests
#                   proxies = {'http':'http://115.200.211.49:8118'}
#                   headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
#                   url = 'http://www.baidu.com/s?wd=ip'
#                   res = requests.get(url=url, headers=headers, proxies=proxies)
#                   res.encoding = 'utf8'
#                   with open('baiduIp.html', 'w', encoding='utf8') as f:
#                       f.write(res.text)
#       cookie
#           说明：requests在处理会话问题时，首先应当实例化一个Session对象
#           示例：s = request.Session()
#               s对象方法
#                   post()
#                       功能、参数、返回值同requests.post()
#                       区别：s.post()请求网站后，s对象的属性中就保存了服务器给你发送过来的cookie,以及cookie中的session
#                       示例
#                           import requests
#                           headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
#                           formdata = {'email':'18086829907','password':'5a76a6568554a113c432e2128a2b6ec918002245fd9c74f791dc8d45ac0368cf',}
#                           post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201965628423'
#                           s = requests.Session()
#                           s.post(url=post_url, data=formdata, headers=headers)
#                   get()
#                       功能、参数、返回值同requests.get()
#                       区别：s如果发送过post请求模拟登录，s中将会保存cookie，s.get()就会携带此cookie
#                       示例
#                           get_url = 'http://www.renren.com/971351636/profile'
#                           res = s.get(url=get_url, headers=headers)
#                           res.encoding='utf8'
#                           with open('人人网用户界面.html', 'w', encoding='utf8') as f:
#                               f.write(res.text)
#   实战 chinaunix复杂登录
#       思路
#           先get，再post，最后get
#               import requests
#               from bs4 import BeautifulSoup
#               import time
#               #伪造头
#               headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
#               #get请求登录页面
#               get1_url = 'http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2F'
#               s = requests.Session()
#               get1_res = s.get(url=get1_url, headers=headers)
#               #保存为本地html方便测试bs4
#               # with open('get1.html', 'w', encoding='gbk') as f:
#               #     f.write(get1_res.text)
#               #解析登录页面获取token值
#               soup = BeautifulSoup(get1_res.text, 'lxml')
#               _token = soup.select('input[name="_token"]')[0]['value']
#               #from表单中_t值的分析思路 破解post请求参数 破解post参数 破解post位置参数
#               #是否存在与html中
#               #   否：肯定是通过ajax动态加载js代码生成的
#               #       抓包分析js代码
#               #           在js中搜索_t
#               #               发现 'ajax':function(e){ e.data["_t"] = (new Date).getTime()}
#               #                   确定_t是13位时间戳
#               #                       在python中用time.time()创造一个13位时间戳来伪造_t值
#               date = str(time.time()).split('.')
#               new_date = date[0]+date[-1][:3]
#               _t = new_date
#               #post请求登录
#               post_url = 'http://account.chinaunix.net/login/login'
#               post_data = {
#                   'username':'18086829907',
#                   'password':'135cylpsx',
#                   '_token': _token,
#                   '_t': new_date,
#               }
#               post_res = s.post(url=post_url, headers=headers, data=post_data)
#               #访问登录后的页面
#               get2_url = 'http://bbs.chinaunix.net/home.php?mod=space&uid=69937883&do=profile'
#               get2_res = s.get(url=get2_url, headers=headers)
#               #保存登录后的界面
#               with open('get2.html', 'w', encoding='gbk') as f:
#                   f.write(get2_res.text)
#   实战8684公交成线路爬取
#         import requests
#         from lxml import etree
#         import json
#         import time
#         import random
#
#         s = requests.Session()
#
#         class busSpider():
#             def __init__(self, city):
#                 self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
#                 self.baseUrl = 'https://{}.8684.cn'.format(city)
#                 self.detailsPageList = []
#                 self.city = city
#
#             #导航栏
#             def navigetionHandler(self):
#                 '''
#                 功能：爬取主导航栏并返回所有指向副导航栏的a链接href属性，以列表的方式返回
#                 '''
#                 #发送get请求
#                 r = s.get(self.baseUrl, headers=self.headers)
#                 #解析内容，获取导航链接
#                 tree = etree.HTML(r.text)
#                 #查找以数字开头的链接
#                 naviList_href_number = tree.xpath('//div[@class="bus_kt_r1"]/a/@href')
#                 #查找以字母开头的链接
#                 naviList_href_letter = tree.xpath('//div[@class="bus_kt_r2"]/a/@href')
#                 #将需要爬取的所有链接返回
#                 return naviList_href_number + naviList_href_letter
#
#             #副导航栏
#             def subNavigetionHandler(self, naviList):
#                 '''
#                  功能：遍历访问所有a链接显示所有副导航栏中指向详情页的a链接href属性,以列表的方式返回
#                 '''
#                 subNaviList = []
#                 for item in naviList:
#                     url = self.baseUrl + item
#                     r = s.get(url=url, headers = self.headers)
#                     tree = etree.HTML(r.text)
#                     subNaviList += tree.xpath('//div[@id="con_site_1"]/a/@href')
#                     time.sleep(random.random()*10)
#                 return subNaviList
#
#             #详情页
#             def detailsPageHandler(self, subNaviList):
#                 '''
#                 遍历访问所有的副导航栏链接，获取详情页信息列表，列表元素为每个详情页信息的字典
#                 '''
#                 n = 1
#                 for item in subNaviList:
#                     url = self.baseUrl + item
#                     r = s.get(url=url, headers = self.headers)
#                     tree = etree.HTML(r.text)
#                     # xpath的测试
#                     # with open('innerTest.html', 'w', encoding='utf8') as f:
#                     #     f.write(r.text)
#                     print('开始爬取{}'.format(tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0]))
#                     print(url)
#                     try:
#                         downwardRoute_totalStationNumber = tree.xpath('//span[@class="bus_line_no"]/text()')[1]
#                         downwardRoute = tree.xpath('//div[@class="bus_site_layer"]')[1].xpath('./div/a/text()')
#                     except IndexError:
#                         downwardRoute_totalStationNumber = ''
#                         downwardRoute = []
#                     detailsPageDict = {
#                         '公交车号': tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0],
#                         '运行时间': tree.xpath('//p[@class="bus_i_t4"][1]/text()')[0].split('：', 1)[-1],
#                         '票价信息': tree.xpath('//p[@class="bus_i_t4"][2]/text()')[0].split('：', 1)[-1],
#                         '公交公司': tree.xpath('//p[@class="bus_i_t4"][3]/a/text()')[0].split('：', 1)[-1],
#                         '最后更新': tree.xpath('//p[@class="bus_i_t4"][4]/text()')[0].split('：', 1)[-1],
#                         '上行总站数': tree.xpath('//span[@class="bus_line_no"]/text()')[0],
#                         '上行站台': tree.xpath('//div[@class="bus_site_layer"]')[0].xpath('./div/a/text()'),
#                         '下行总站数': downwardRoute_totalStationNumber,
#                         '下行站台':downwardRoute,
#                     }
#                     self.detailsPageList.append(detailsPageDict)
#                     print('爬取第{}条数据'.format(n))
#                     time.sleep(random.random()*10)
#                     n += 1
#
#             #爬虫执行
#             def run(self):
#                 #爬取主导航栏并返回所有指向副导航栏的a链接href属性，以列表的方式返回
#                 naviList = self.navigetionHandler()
#                 #遍历访问所有a链接显示所有副导航栏中指向详情页的a链接href属性,以列表的方式返回
#                 subNaviList = self.subNavigetionHandler(naviList)
#                 #遍历访问所有的副导航栏链接，获取详情页信息列表，列表元素为每个详情页信息的字典
#                 self.detailsPageHandler(subNaviList)
#                 #将字典转化为json并保存文件
#                 jsonData = json.dumps(self.detailsPageList, ensure_ascii=False)
#                 with open('{}_busInfo.json'.format(self.city), 'w', encoding='utf8') as f:
#                     f.write(jsonData)
#
#         def main():
#             city = input('输入城市拼音：')
#             spider = busSpider(city)
#             spider.run()
#
#         if __name__ == '__main__':
#             main()


#验证码
#    图片验证码
#        破解方式
#            手动输入
#                适用：验证码不多
#                思路：将验证码图片保存到本地，在代码中用input暂缓程序，打开本地图片，手动输入验证码
#                优点：人工识别，识别率高
#                缺点：效率低
#                实战示例：古诗文网验证码破解并登录
#                     import requests
#                     from lxml import etree
#
#                     class poetrySpider():
#                         s = requests.Session()
#                         def __init__(self, loginUrl, clickLoginUrl):
#                             self.loginUrl = loginUrl
#                             self.clickLoginUrl = clickLoginUrl
#                             self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
#                             self.innerGetUrl = 'https://so.gushiwen.org/user/collect.aspx?type=s&id=342290&sort=t'
#
#                         #完成登录后访问收藏夹内容
#                         def collection(self):
#                             # self.s.get(self.innerGetUrl)
#                             pass
#
#                         def manualInput(self):
#                             #get登录界面
#                             r1 = self.s.get(url=self.loginUrl, headers=self.headers)
#                             #获取需要的post参数
#                             tree = etree.HTML(r1.text)
#                             __VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
#                             __VIEWSTATEGENERATOR = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
#                             picture = 'https://so.gushiwen.org' + tree.xpath('//img[@id="imgCode"]/@src')[0]
#                             r2 = self.s.get(url=picture, headsers=self.headers)
#                             with open('picture.jpg', 'wb') as f:
#                                 f.write(r2.content)
#                             code = input('请输入验证码：')
#                             #post参数
#                             post_data = {
#                                 '__VIEWSTATE': __VIEWSTATE,
#                                 '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
#                                 'from': '',
#                                 'email': '18086829907',
#                                 'pwd': '135cylpsx',
#                                 'code': code,
#                                 'denglu': '登录',
#                             }
#                             r3 = self.s.post(self.clickLoginUrl, data=post_data, headers=self.headers)
#                             print(r3.text)
#                             #完成登录后访问收藏夹内容
#                             self.collection()
#
#                         def run(self):
#                             #手动下载图片验证登录
#                             self.manualInput()
#
#                     def main():
#                         #登录界面的url
#                         loginUrl = 'https://so.gushiwen.org/user/login.aspx?'
#                         #点击登录后，post请求的url
#                         clickLoginUrl = 'https://so.gushiwen.org/user/login.aspx'
#                         spider = poetrySpider(loginUrl, clickLoginUrl)
#                         spider.run()
#
#                     if __name__ == '__main__':
#                         main()
#            光学验证
#               tesseract
#                   概念：光学识别软件
#                   安装：https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows
#                   注意：安装时，一定要勾选数字、简体中文、英语、日语的数据包
#                   验证安装：cmd输入tesseract
#                   功能：学习验证码，识别验证码
#                   优点：免费
#                   缺点：识别率低，但可以通过机器学习让其增加效率
#                   验证码学习准备：新建一个存放验证码的图片文件夹，里面准备多张目标网站的验证码图片
#               python调用tesseract
#                   库的安装
#                       pip install pytesseract
#                       pip install pillow            #python图片库
#                   打开图片数据
#                       import pytesseract
#                       from PIL import Image
#                       img = Image.open('code1.jpg')
#                   图片数据预处理
#                       灰度处理
#                           img = img.convert('L')
#                           img.show()
#                       二值化处理
#                           threshold = 140
#                           table = []
#                           for i in range(256):
#                               if i < threshold:
#                                   table.append(0)
#                               else:
#                                   table.append(1)
#                           out = img.point(table, '1')
#                           out.show()
#                           img = img.convert('RGB')
#                   模型训练(暂未成功)
##                      概念：根据大量图片来训练自定义语言。生成训练文件的语言库文件，然后放入指定位置即可
#                       步骤
#                           合成tif文件
#                               选取样本文件，比如选择30张jpg文件，当然越多越好，使用jtessBoxEditor合成tif文件，命名为mylang.myfont.exp0.tif
#                                   安装
#                                       jtessBoxEditor
#                                           下载地址：https://blog.csdn.net/weixin_44499757/article/details/86511520
#                                       jdk-8u211-windows-x64.exe
#                                           下载地址：https://www.7down.com/soft/334699.html
#                           根据mylang.myfont.exp0.tif生成box文件（命令行），box文件记录的是字符在每个图片中的位置信息
#                               tesseract mylang.myfont.exp0.tif mylang.myfont.exp0 -l eng -psm 5 batch.nochop makebox
#                               注意：mylang.myfont.exp0.tif要放在Tesseract-OCR目录下
#                           用jtesseract来修改box文件，即用jtessBoxEditor打开对应的tif文件mylang.myfont.exp0.tif，矫正识别出的字符，如果识别错误的话，改正，并且看下X、Y、W、H是否需要修改
#                           生成font文件，这里的font为自定义的myfont，与前面一致命令：（命令行）
#                               echo myfont 0 0 0 0 > font_properties
#                           生成训练文件（命令行）
#                               tesseract mylang.myfont.exp0.tif mylang.myfont.exp0 -l end -psm 7 nobatch box.train
#                           生成字符集文件（命令行）
#                               unicharset_extractor mylang.myfont.exp0.box
#                           生成shape文件（命令行）
#                               shapeclustering -F font_properties -Uunicharset -O mylang.unicharset mylang.myfont.exp0.tr
#                           生成聚焦字符特征文件（命令行）
#                               mftraining -F font_properties -U unicharset -O mylang.unicharset mylang.myfont.exp0.tr
#                           生成字符正常化特征文件（命令行）
#                               cntraining mylang.myfont.exp0.tr
#                           更名（命令行）
#                               rename normproto myfont.normproto
#                               rename inttemp myfont.inttemp
#                               rename pffmtable myfont.pffmtable
#                               rename unicharset myfont.unicharset
#                               rename shapetable myfont.shapetable
#                           合并训练文件（命令行）
#                               combine_tessdata myfont
#                           测试将最终得到的myfont.traineddata放到tesseract安装目录的tessdata目录下
#                               tesseract xx.jpg result -1 myfont -psm 5
#                   学习验证码图片
#                       print(pytesseract.image_to_string(img))
#            打码平台
#               功能：识别验证码
#               优势：识别率高，因为都是人工识别
#               缺点：收费，100元1000000分，纯数字验证码10分/个
#               推荐平台：云打码http://www.yundama.com/
#               注册
#                   用户注册
#                       用户名：18086829907
#                       密码：135cylpsx
#                   开发者注册
#                       用户名：18086829907
#                       密码：135cylpsx
#                       支付宝账号：chenyilong112233@163.com
#               下载aip示例
#                   登录开发者账户
#                       点击根据开发语言下载DEMO
#                           点击PythonHTTP示例下载
#               添加新软件
#                   登录开发者账户
#                       我的软件
#                           添加新软件
#                               软件名称：justin
#                               软件代码：8242
#                               通讯密钥：e8b42a12331d497dc73935155d334cc2
#               api示例
#                     import http.client, mimetypes, urllib, json, time, requests
#
#
#                     ######################################################################
#
#                     class YDMHttp:
#                         apiurl = 'http://api.yundama.com/api.php'
#                         username = ''
#                         password = ''
#                         appid = ''
#                         appkey = ''
#
#                         def __init__(self, username, password, appid, appkey):
#                             self.username = username
#                             self.password = password
#                             self.appid = str(appid)
#                             self.appkey = appkey
#
#                         def request(self, fields, files=[]):
#                             response = self.post_url(self.apiurl, fields, files)
#                             response = json.loads(response)
#                             return response
#
#                         def balance(self):
#                             data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid,
#                                     'appkey': self.appkey}
#                             response = self.request(data)
#                             if (response):
#                                 if (response['ret'] and response['ret'] < 0):
#                                     return response['ret']
#                                 else:
#                                     return response['balance']
#                             else:
#                                 return -9001
#
#                         def login(self):
#                             data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid,
#                                     'appkey': self.appkey}
#                             response = self.request(data)
#                             if (response):
#                                 if (response['ret'] and response['ret'] < 0):
#                                     return response['ret']
#                                 else:
#                                     return response['uid']
#                             else:
#                                 return -9001
#
#                         def upload(self, filename, codetype, timeout):
#                             data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid,
#                                     'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
#                             file = {'file': filename}
#                             response = self.request(data, file)
#                             if (response):
#                                 if (response['ret'] and response['ret'] < 0):
#                                     return response['ret']
#                                 else:
#                                     return response['cid']
#                             else:
#                                 return -9001
#
#                         def result(self, cid):
#                             data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid,
#                                     'appkey': self.appkey, 'cid': str(cid)}
#                             response = self.request(data)
#                             return response and response['text'] or ''
#
#                         def decode(self, filename, codetype, timeout):
#                             cid = self.upload(filename, codetype, timeout)
#                             if (cid > 0):
#                                 for i in range(0, timeout):
#                                     result = self.result(cid)
#                                     if (result != ''):
#                                         return cid, result
#                                     else:
#                                         time.sleep(1)
#                                 return -3003, ''
#                             else:
#                                 return cid, ''
#
#                         def report(self, cid):
#                             data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid,
#                                     'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
#                             response = self.request(data)
#                             if (response):
#                                 return response['ret']
#                             else:
#                                 return -9001
#
#                         def post_url(self, url, fields, files=[]):
#                             for key in files:
#                                 files[key] = open(files[key], 'rb');
#                             res = requests.post(url, files=files, data=fields)
#                             return res.text
#
#
#                     ######################################################################
#
#                     # 用户名
#                     username = 'username'
#
#                     # 密码
#                     password = 'password'
#
#                     # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
#                     appid = 1
#
#                     # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
#                     appkey = '22cc5376925e9387a23cf797cb9ba745'
#
#                     # 图片文件
#                     filename = 'getimage.jpg'
#
#                     # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
#                     codetype = 1004
#
#                     # 超时时间，秒
#                     timeout = 60
#
#                     # 检查
#                     if (username == 'username'):
#                         print('请设置好相关参数再测试')
#                     else:
#                         # 初始化
#                         yundama = YDMHttp(username, password, appid, appkey)
#
#                         # 登陆云打码
#                         uid = yundama.login();
#                         print('uid: %s' % uid)
#
#                         # 查询余额
#                         balance = yundama.balance();
#                         print('balance: %s' % balance)
#
#                         # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
#                         cid, result = yundama.decode(filename, codetype, timeout);
#                         print('cid: %s, result: %s' % (cid, result))
#
#                     ######################################################################


#视频下载
#    示例网站：http://www.365yg.com/
#    视频连接：http://v9-tt.bytecdn.cn/d31248e6a252fbcc63c1a8178442b01d/5d2460d0/video/m/220279b8c6a2eb6486a95aa2fbf00b2525e1162b986b0000bd7234fac08f/?rc=anhxdW45czhtbjMzNjczM0ApQHRAbzczNDs3MzgzMzY1NDMzNDVvQGg2dilAZzN3KUBmM3UpZHNyZ3lrdXJneXJseHdmOzpAXzAvZ3MtaTJhXy0tXi0vc3MtbyNvIzU2Mi0yMi4uMTYzNjQ2LTojbyM6YS1vIzpgLXAjOmB2aVxiZitgXmJmK15xbDojMy5e
#    实战365阳光视屏网站的视屏爬取
#         import requests
#         from lxml import etree
#         from selenium.webdriver.chrome.options import Options
#         from selenium import webdriver
#         import time
#         import random
#
#         class YgSpider():
#             s = requests.Session()
#             def __init__(self):
#                 self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
#
#             def handler_selenium(self, url, pages):
#                 print('启动无头浏览器')
#                 # 设置谷歌的无头浏览器
#                 options = Options()
#                 options.add_argument('--headless')
#                 options.add_argument('--disable-gpu')
#                 # 创建无头浏览器对象
#                 path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#                 browser = webdriver.Chrome(executable_path=path, options=options)
#                 # 打开365yg视频网站二级页面
#                 browser.get(url)
#                 time.sleep(2)
#                 #滚动条滚动到底部,50次
#                 for page in range(pages):
#                     js = 'var q=document.documentElement.scrollTop=100000' #模拟滚动条滚到底部
#                     browser.execute_script(js)
#                     browser.save_screenshot('./image/{}.png'.format(page))
#                     time.sleep(random.random() * 5)
#                 # 获得网页html
#                 html = browser.page_source
#                 # 关闭无头浏览器
#                 browser.quit()  # 退出浏览器
#                 print('关闭无头浏览器')
#                 return html
#
#             def handler_fristPage(self, page):
#                 '''
#                 功能：使用无头浏览器访问一级页面，获取所有二级页面url列表
#                 :return: 完整的二级页面url
#                 '''
#                 #365yg视频网站一级页面
#                 url = 'http://www.365yg.com/'
#                 #启动无头浏览器，获取一级页面的html，滑动滚轮到底部page次
#                 html = self.handler_selenium(url, page)
#                 #解析源代码
#                 tree = etree.HTML(html)
#                 secondPageUrlList = tree.xpath('//div[@class="title-box"]/a/@href')
#                 secondPageCompleteUrlList = []
#                 for item in secondPageUrlList:
#                     completeUrl = 'http://www.365yg.com' + item
#                     secondPageCompleteUrlList.append(completeUrl)
#                 return secondPageCompleteUrlList
#
#             def handler_secondPage(self, secondPageCompleteUrlList):
#                 '''
#                 功能：使用无头浏览器遍历访问每一个二级页面，并获取视频地址，并向视频地址发送get请求，保存视频到本地
#                 :param secondPageCompleteUrlList: 完成的二级页面url
#                 :return: 无
#                 '''
#                 n = 1
#                 for secondUrl in secondPageCompleteUrlList:
#                     #启动无头浏览器访问二级页面，并返回html
#                     html = self.handler_selenium(secondUrl, 1)
#                     #解析网站内页
#                     tree = etree.HTML(html)
#                     videoUrl = tree.xpath('//video/@src')[0]
#                     title = tree.xpath('//h1/text()')[0]
#                     r = requests.get(url=videoUrl, headers=self.headers)
#                     with open('./video/{}.mp4'.format(title), 'wb') as f:
#                         f.write(r.content)
#                     print('开始爬取视频{}：{}'.format(n, title))
#                     n += 1
#                     time.sleep(random.random()*10)
#
#             def run(self):
#                 #使用无头浏览器访问一级页面，获取所有二级页面url列表,参数表示滑动5次滚轮，触发ajax加载更多二级页面链接
#                 secondPageCompleteUrlList = self.handler_fristPage(5)
#                 #使用无头浏览器遍历访问每一个二级页面，并获取视频地址，并向视频地址发送get请求，保存视频到本地
#                 self.handler_secondPage(secondPageCompleteUrlList)
#
#         def main():
#             spider = YgSpider()
#             spider.run()
#
#         if __name__ == '__main__':
#             main()

#线程回顾
#    线程创建
#       面对过程
#           import threading
#           t = threading.Thread(target=funciont, name='线程名', args=(参数1,))
#           name = threading.current_Thread().name
#           t.start()
#           t.join()
#       面对对象
#           定义一个类，继承自threading.Thread,重写一个run方法，需要线程名字、传递参数，则重写__init__方法，但注意需要手动调用父类的__init__方法
#                 import threading
#                 import time
#                 class singThread(threading.Thread):
#                     def __init__(self, name, a):
#                         super().__init__()  # super()调用父类，.__init__()执行父类中的构造方法
#                         self.name = name
#                         self.a = a
#
#                     def run(self):
#                         print('线程名字是{},接收的参数是{}'.format(self.name, self.a))
#                         for i in range(5):
#                             print('我在唱歌')
#                             time.sleep(1)
#
#                 class danceThread(threading.Thread):
#                     def __init__(self, name, a):
#                         super().__init__()  # super()调用父类，.__init__()执行父类中的构造方法
#                         self.name = name
#                         self.a = a
#
#                     def run(self):
#                         print('线程名字是{},接收的参数是{}'.format(self.name, self.a))
#                         for i in range(5):
#                             print('我在跳舞')
#                             time.sleep(1)
#
#                 def main():
#                     # 创建线程
#                     tSing = singThread('sing', 5)
#                     tDance = danceThread('dance', 6)
#                     # 线程启动
#                     tSing.start()  # 启动后，会自动执行run方法，本质是重写了threading.Thread中的run方法，也就是说方法名必须叫run
#                     tDance.start()
#                     # 主进程等待子进程结束再结束
#                     tSing.join()
#                     tDance.join()
#
#                 if __name__ == '__main__':
#                     main()
#   线程同步
#       线程之间共享全局变量，很容易造成数据紊乱，这时候要使用线程锁，子线程在等待上一个子线程解锁时，是通过抢的方式，谁先抢到，谁先上锁，谁先使用
#       创建锁
#           suo = threading.lock()
#       上锁
#           sou.acquire()
#       释放锁
#           sou.release()
#   队列(queue)
#       用于
#           下载线程（生产者）
#           解析线程（消费者）
#       使用
#           创建
#               from queue import Queue
#               q = Queue(5)
#           加入值
#               q.put('xxx') #如果队列满了，会程序阻塞，等待队列腾出空位，再加入
#               q.put('xxx', False) #如果队列满了，不等待加入，而是直接报队列已满的错误
#               q.put('xxx', True, 3) #如果队列满了，等待3秒，3秒后还没空位，再报错
#           提取值
#               print(q.get()) #如果队列空了，会程序阻塞，等待队列有新数据，再取值
#               print(q.get(False)) #如果队列空了，不等待取值，而是直接报队列空的错误
#               print(q.get(True, 3)) #如果队列空了，等待3秒，3秒后还没数据，再报错
#           判断
#               q.empty() #判断队列是否为空
#               q.full() #判断队列是否已满
#               q.qsize() #判断队列长度
#多线程爬虫
#   分析
#       需要几类线程，一类里面启动几个线程
#           采集类线程（3）
#           解析类线程（3）
#       数据交互
#           内容队列
#               下载线程，从内容队列put数据
#               解析线程，从内容队列get数据
#           url队列
#               下载线程，从url队列get数据
#           写数据
#               解析数据写到文件中，线程要加锁


#【day】亚马逊服务器
#登录网址：https://console.aws.amazon.com/console/home?nc2=h_ct&region=us-east-1&src=header-signin#
#电邮：417217170@qq.com
#密码：135cylpsx4848@
#AWS名称：justin

#【day】黑马代理池维护


#【day】ADSL拨号
#云立方
#   登录网址：https://www.yunlifang.cn/login.asp
#   账号：justin
#   密码：135cylpsx4848@
#   购买三台动态ip云主机
#       官网地址：https://www.yunlifang.cn/dynamicvps.asp
#       购买后各种验证
#       最后到控制面板给云主机安装linux系统
#   本地xshell链接两台云主机
#       一号主机：
#           名称：justinvps1
#           主机：221.10.101.108
#           端口：21601
#       二号主机：
#           名称：justinvps2
#           主机：221.10.101.108
#           端口：21151
#       三号主机：
#           名称：justinvps3
#           主机：
#           端口
#           用于创建ip的api接口
#       点击连接后，再点击保存
#       输入
#           用户名：root
#           密码：135cylpsx
#       可用adsl命令
#           拨号上网：$ adsl-start
#           关闭adsl：adsl-stop
#   在两台云主机的linux下搭建HTTP代理服务
#       链接网络
#           $ adsl-start
#       安装
#           $ yum install -y epel-release
#           $ yum update -y
#           $ yum install -y tinyproxy
#       配置
#           @ $ vi /etc/tinyproxy/tinyproxy.conf
#               @ 将Allow 127.0.0.1注释掉
#       启动
#           $ systemctl enable tinyproxy.service
#           $ systemctl restart tinyproxy.service
#       测试
#           $ curl -x IP:PORT www.baidu.com
#           IP为ifconfig后，ppp0的inet，PORT为默认端口8888 （注意，此代码是在另外一台云主机上执行，意思是将云主机的设置对应代理后访问百度网站）
#       防火墙
#           $ iptables -I INPUT -p tcp --dport 8888 -j ACCEPT
#           $ systemctl stop firewalld.service    #关闭防火墙，执行了上部，可以不用执行此步骤
#       安装python3
#           $ sudo yum groupinstall -y development tools
#           $ sudo yum install -y epel-release python36-devel libxslt-devel libxml2-devel openssl-devel
#           $ sudo yum install -y python36 python36-setuptools
#           $ sudo easy_install-3.6 pip
#       安装库
#           $ pip install requests
#           $ pip install tornado
#           $ pip install redis
#       clone项目
#           $ git clone https://github.com/Germey/ADSLProxy.git
#       安装redis
#           $ sudo yum install epel-release
#           $ sudo yum update
#           $ sudo yum -y install redis
#           $ sudo systemctl start redis
#           $ vi /etc/redis.conf    #vi搜索技巧：在命令输入状态下的搜索命令——\需搜索字符串,示例\requirepass
#               注释 bind 127.0.0.1
#               将protected-mode yes 改为 protected-mode no
#               修改密码 requirepass 135cylpsx4848@
#               点击esc
#               $ :wq
#           $ sudo systemctl restart redis    #重启、启动reids-server
#       允许外部访问6379端口
#           $ yum install iptables-services
#           $ iptables -I INPUT 1 -p tcp -m state --state NEW -m tcp --dport 6379 -j ACCEPT
#　　　      $ service iptables save
#           $ systemctl enable iptables.service
#       配置云拨号主机
#           @ $ ifconfig    #查看局域网ip
#           @ $ vi /root/ADSLProxy/adslproxy/config.py
#               拨号间隔
#                   ADSL_CYCLE = 100
#               拨号出错重试间隔
#                   ADSL_ERROR_CYCLE = 5
#               ADSL命令
#                   ADSL_BASH = 'adsl-stop;adsl-start'
#               代理运行端口
#                   PROXY_PORT = 8888
#               客户端唯一标识
#                   CLIENT_NAME = 'adsl2'
#               拨号网卡
#                   ADSL_IFNAME = 'ppp0'
#               Redis数据库IP
#                   REDIS_HOST = '192.168.1.24'    #拨号主机的redis_host设置为接口主机的ifconfig-eth0-innet
#               Redis数据库密码, 如无则填None
#                   REDIS_PASSWORD = '135cylpsx4848@'
#               Redis数据库端口
#                   REDIS_PORT = 6379
#               代理池键名
#                   PROXY_KEY = 'adsl'
#               测试URL
#                   TEST_URL = 'https://www.mzitu.com/tag/youhuo/'
#               测试超时时间
#                   TEST_TIMEOUT = 20
#               API端口
#                   API_PORT = 8000
#       @ 启动adsl拨号
#           修改测试函数的get请求参数
#               $ vi /root/ADSLProxy/adslproxy/sender.py
#                   将：response = requests.get(TEST_URL, proxies={'http': 'http://' + proxy, 'https': 'https://' + proxy}, timeout=TEST_TIMEOUT)
#                       目标网站时http修改为
#                           response = requests.get(TEST_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',} ,proxies={'http': 'http://' + proxy}, timeout=TEST_TIMEOUT)
#                       目标网站时https修改为
#                           response = requests.get(TEST_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',} ,proxies={'https': 'https://' + proxy}, timeout=TEST_TIMEOUT)
#           $ cd /root/ADSLProxy
#           $ python3 run.py    #测试无误后可以ctrl+c
#           $ (python3 run.py > /dev/null &)    #守护运行
#       @ 开启接口服务（第三台服务器上运行）
#           $ cd /root/ADSLProxy
#           $ ifconfig
#           $ python3 api.py
#           $ (python3 api.py > /dev/null &)    #守护运行
#       爬虫程序通过访问api获取代理
#

#定时器
#   夜间停止爬取定时器
#       import time
#       import random
#       randomtime = random.randint(1, 59)
#       if time.strftime('%H:%M:%S', time.localtime()) == '9:{}:{}'.format(randomtime, randomtime):
#           time.sleep(39600)


#【day】Scrapy
#安装
#   pip install Scrapy
#scrapy类
#   作为类
#       scrapy
#           方法
#               scrapy.Request()
#                   功能：模拟浏览器发送GET请求
#                   原型：scrapy.Request(url[, callback, method='GET', headers, body, cookies, meta, dont_filter=True])
#                       说明：定义回调函数def function(response)
#                   参数
#                       url：发送请求的网址
#                       callback：定义回调函数，响应体返回后交给function
#                       header：默认读取配置文件中的header
#                       cookies：默认读取配置文件中的cookies
#                       meta：接收数据格式为字典，字典的key任意取名，value可以是当前解析函数中的变量，发送请求的同时，会携带这个字典一起发送，响应返回时会携带这个字典传送到下一个解析函数中，下一个解析函数如果需要用到这个字典里面的值，就需要使用response.meta将这个字典取出，同时用对应key取出需要的value值，即上一个解析函数的变量传送到下一个解析函数中
#                       dont_filter：让scrapy的去重不会考虑当前url,scrapy默认有url去重的功能，对需要重复请求的url有重要用途。False是要去重，True是不去重。当要爬取的url会实时变化数据时，需要将此参数设为True
#                       errback：在发生错误的时候执行此函数
#                   示例
#                       def parse(self, response):
#                           a = '我要转到下一个解析函数中'
#                           meta = {'a':a}
#                           scrapy.Request(ps://www.baidu.com/', callback=innerParse, meta=meta)
#                       def innerParse(self, response):
#                           print(response.meta['a']) --> '我要转到下一个解析函数中'
#               scrapy.FormRequest()
#                   本质：FormRequest是一个类
#                   功能：模拟浏览器发送POST请求
#                   原型：scrapy.FormRequest(url, formdata=dict, callback[, headers, cookies, dont_filter=False])
#                   参数
#                       formadata：post请求的数据，是一个字典格式
#                       callback：定义一个处理响应的函数，不管成功与否都交给这个函数
#                   示例
#                       import scrapy
#                       import re
#                       class GithubSpider(scrapy.Spider):
#                           name = 'github'
#                           allowed_domains = ['github']
#                           start_urls = ['https://github.com/login/']    #开始url是登录界面
#                           def start_requets(self, response):
#                               #构造post请求的formdata
#                               post_data = {
#                                   'login': "18086829907",
#                                   'password': "135cylpsx",
#                                   'authenticity_token': response.xpath(r'//*[@id="login"]/form/input[2]/@value').extract_first(),
#                                   'utf8': response.xpath(r'//*[@id="login"]/form/input[1]/@value').extract_first(),
#                                   'commit': response.xpath(r'//*[@id="login"]/form/div[3]/input[4]/@value').extract_first(),
#                                   'webauthn-support': response.xpath(r'//*[@id="login"]/form/div[3]/input[3]/@value').extract_first(),
#                               }
#                               #携带post数据向接口地址发送post请求
#                               yield scrapy.FormRequest('https://github.com/session', formdata=post_data, callback=self.after_login, dont_filter=True)
#                           #处理返回数据
#                           def after_login(self, response):
#                               print(re.findall('justin', response.text))    #验证是否有用户名，有多个即成功登录
#               scrapy.FormRequest.from_response(cls, response, formname=None, formid=None, formnumber=0, formdata=None,clickdata=None, dont_click=False, formxpath=None, formcss=None, **kwargs)
#                   本质：是FormRequest类的方法
#                   功能
#                       当网页代码中<form anction='/session'>,即action属性有请求url时可以用这个简单方法
#                       自动在响应中寻找from表单的action指定的url地址，即post数据提交的url，对这个地址发送post请求
#                       区别在于只需要账号和密码这两个参数即可登录
#                   参数：formxpath,当有多个form表单时，可以用xpath来定位from表单
#                   示例
#                       import scrapy
#                       import re
#                       class Github2Spider(scrapy.Spider):
#                           name = 'github2'
#                           allowed_domains = ['github.com']
#                           start_urls = ['https://www.github.com/login/']
#                           def parse(self, response):
#                               yield scrapy.FormRequest.from_response(
#                                   response, #自动从response中寻找from表单
#                                   formdata={'login': '18086829907',    #<input name='login'...>, 用户名，即字典第一个key = input标签中name的值
#                                             'password': '135cylpsx'},    ##<input name='password'...>, 密码，即字典第二个key = input标签的name值
#                                   callback=self.after_login,
#                                   formxpath='//*[@id="login"]/form',    #xpath定位form表单，如果有两个及以上时使用
#                                   dont_filter=False,    #不过滤这条请求
#                               )
#                           #处理返回数据
#                           def after_login(self, response):
#                               print(re.findall('justin', response.text))    #验证是否有用户名，有多个即成功登录
#
#           类中类
#               概念：scrapy中的类
#                   Spider类
#                       方法
#                           start_requests()
#                               功能：返回请求体给引擎，引擎会将请求体对象传给调度器，简单理解就是返回请求体对象给调度器
#                               说明：此方法一般会在爬虫文件中读取start_url,将start_url通过scrpy.Request()方法包装为请求体对象后，用yield返回给调度器
#                               注意：此方法在爬虫文件中进行重写，重写后可以遍历自造url（可以是接口url，获取json）
#                               示例
#                                   # 目标url：http://images.so.com/
#                                   # 自造其ajax接口，接口分析是通过抓包获得的
#                                   data = {'ch': 'photography', 'listtype': 'new'}
#                                   base_url = 'https://image.so.com/zj?'
#                                   for page in range(1, self.settings.get('MAX_PAGE') + 1):
#                                       data['sn'] = page * 30
#                                       params = urlencode(data)
#                                       url = base_url + params
#                                       yield Request(url, self.parse)
#                   cmdline类
#                       方法：execute()
#                           功能：模拟终端执行scrapy命令
#                           原型：scrapy.cmdline.execute(['command1','command2','command3'])
#                           技巧：scrapy.cmdline.execute('command1 command2 command3'.split())
#                           参数
#                               command
#                                   是scrapy的任何一套命令列表
#                           示例
#                               新建一个run.py
#                               from scrapy import cmdline
#                               cmdline.execute('scrapy crawl jdspider'.split())  -->  名为jdspider的爬虫开始执行
#   作为命令
#   $ scrapy
#
#       bench
#           功能：测试
#           示例：scrapy bench
#       fetch
#           功能：爬取网页，返回网页源代码
#           格式：scrapy fetch 目标url
#           示例：scrapy fetch 'http://www.baidu.com/'
#       genspider
#           功能：创建爬虫文件
#           格式：scrapy genspider 爬虫名 url范围域
#           参数
#               爬虫名不能是项目名，用于区分多个爬虫文件
#               url范围域规定了爬取的url开头部分格式，如果爬取到的url不是该开头，则不爬取
#           示例：scrapy genspider baiduCrawl 'https://www.baidu.com/'
#           说明
#               该命令在哪个目录执行，就在哪个目录创建.py文件，我们需要在在爬虫工程目录下的spider目录中创建爬虫文件，即/root/jdSpider/jdSpider/spiders
#               执行了此命令，scrapy类会又多几个方法check、crawl、edit、list、parse、list
#       genspider -t crawl
#           功能：创建爬虫文件，爬虫文件中的类继承自CrawlSpider
#           说明：运用此命令生成的爬虫文件中多了rules=(url规则)
#           适用：在目标网站中观察到翻页以及详情内页的url都是按照一定规律变化的url则可以使用此命令
#           优势：可以按照规则自动生成需要的url发起请求
#           原型：genspider -t crawl 爬虫名 url区域限制
#           示例
#               genspider -t crawl cbrc www.cbrc.gov.cn
#                   -*- 一下为爬虫文件 -*-
#                   import scrapy    #自动生成
#                   from scrapy.linkextractors import LinkExtractor    #自动生成
#                   from scrapy.spiders import CrawlSpider, Rule    #自动生成
#                   from ajxxgk.items import AjxxgkItem    #手动生成
#                   class QssSpider(CrawlSpider):     #自动生成
#                       name = 'qss'    #自动生成
#                       allowed_domains = ['ajxxgk']    #自动生成
#                       start_urls = ['http://www.ajxxgk.jcy.gov.cn/html/zjxflws/']    #手动修改生成
#                       rules = (
#                           #Rule：是一个类，Rule()在做实例化，得到的一条实例就是一条url规则
#                           #LinkExtractor：链接提取器，提取url地址
#                           #allow：定义正则表达式
#                           #callback：提取出来的url地址的response会交个callback处理
#                           Rule(LinkExtractor(allow=r'/html/20190723/2/\d+\.html'), callback='parse_item', follow=False),
#                           Rule(LinkExtractor(allow=r'/html/zjxflws/\d+\.html'), follow=True),
#                       )
#                       #parse函数其实还是存在的，当我们用正则提取出url后，url会传到父类的parse函数中，发送请求
#                       #因此这里不能用parse命名函数，否则会重写父类方法
#                       def parse_item(self, response):
#                           item = AjxxgkItem()
#                           item['content'] = response.text
#                           yield item
#           过程：爬虫首先对start_urls发出get请求，返回的响应中就包含了内页的url和翻页的url，此时就会用allow规定的正则表达式去匹配这些url，同时会自动补全这些url，
#                接着会通过parse函数包装成请求体传入调度器，调度器进行去重入队列出队列，下载器通过异步处理对这些url并发get请求，
#                如果该LinkExtractor的allow的follow为True，这些返回回来的响应又会通过allow来匹配url，循环刚才的操作，
#                如果为False，则不会重复提取url。此时如果指定了callback，就会将这些响应传入callback所指定的函数并调用该函数解析响应
#
#           补充
#               LinkExtractor更多参数
#                   allow：满足括号中“正则表达式”的url会被提取，如果为空，则全部提取
#                   deny：满足括号中“正则表达式”的url一定不提取，优先级高于allow
#                   allow_domains：满足alow_domains，即满足域名限制的url会被提取
#                   deny_domains：满足alow_domains，即满足域名限制的url不会被提取
#                   restrict_xpaths：使用xpath表达式，和allow共同工作用过滤链接，即xpath满足范围内的url地址会被提取
#               spiders.Rule常见参数
#                   link_extractor：是一个Link Extractor对象，用于定义需要提取的链接
#                   callback：从link_extractor中每获取到链接时，参数锁指定的值作为回调函数
#                   follow：是一个布尔值，指定了根据该规则从response提取的链接是否需要跟进，如果callback为None,follow默认设置为True,否则默认为Fasle
#                   process_links：指定该爬虫文件中哪个的函数将会被调用，调用触发条件是从link_extractor中获取到链接列表时，该方法主要用来过滤url
#                   process_request：指定该爬虫文件中哪个的函数将会被调用，调用触发条件是该规则提取到每个request时，用过来过滤request
#
#       check
#           功能：查看新建爬虫爬取状态
#           格式：scrapy check 爬虫名    #爬虫文件名为$ vi /root/baiduSpider/baiduSpider/spiders/baiduCrawl.py中name变量的值
#           示例：scrapy check baiduCrawl  #一个项目中有多个爬虫，全部以name值来区分
#       crawl
#           功能：运行一个爬虫程序
#           格式：scrapy crawl 爬虫名
#           示例：$ scrapy crawl baiduCrawl
#           说明：该命令可以在任何位置使用，如果管道文件有将数据保存本地的代码，保存文件的目录就是该命令运行的当前目录
#       list
#           功能：查看当前爬虫项目中有哪些爬虫名
#           格式：scrapy list
#           示例：scrapy list
#       runspider
#           功能：执行一个爬虫文件
#           格式：scrapy runspider 文件全路径
#           示例：scrapy runspider /home/zlSpider.py
#       settings
#           功能：配置文件
#       shell
#           功能：爬取网页，返回源代码等各种信息，进入python编译环境
#           格式：scrapy shell 目标网站
#           示例：scrapy shell 'http://www.baidu.com'
#                In [1]: print(response.body) #打印html,编码格式
#                In [2]: print(response.text) #打印html,解码格式-中文能读
#                In [3]: print(response.xpath('//a[contains(text(),"关于百度")]/text()')) #返回的是Selector对象
#                In [4]: exit()
#       startproject
#           功能：创建一个爬虫项目
#           格式：scrapy startproject 项目名称
#           示例：$ scrapy startproject jdSpider
#                生成文件
#                   jdSpider
#                       jdSpider
#                           settings.py    说明：配置文件，他会被scrapy.Spider.settings读取成字典格式，其他类继承自scrapy.Spider时，可以调用其类属性setting来读取配置文件变量
#                               必须粘贴的
#                                   付费代理
#                                       from myClass.proxyZset.save_Get_UA_Proxy import RedisClient    #导入调度器
#                                       red = RedisClient()    #实例化调度器
#                                       USER_AGENT = red.get_userAgentList()    #获取UA列表
#                                       PROXY = red.get_proxyList_redis()    #获取代理列表
#                                   mongodb相关设置
#                                       方法一
#                                           MONGO_URI = 'localhost'    #mongodb的本地服务连接
#                                           MONGO_DB = 'images360'    #mongodb的数据库
#                                           PORT = 27017    #mongodb的端口
#                                       方法二
#                                           MONGO_URI = 'mongodb://admin:135cylpsx4848\@@192.168.0.102:27017'
#                                   mysql相关设置
#                                       MYSQL_HOST = 'localhost'    #mysql的链接地址
#                                       MYSQL_DATABASE = 'scrapytest'    #mysql的数据库名字
#                                       MYSQL_USER = 'root'    #mysql的用户名
#                                       MYSQL_PASSWORD = '135cylpsx4848@'    #mysql的密码
#                                   redis相关设置
#                                       方法一
#                                           REDIS_HOST = '192.168.0.102'
#                                           REDIS_PORT = 6379
#                                           REDIS_PASSWORD = 'foobared'
#                                       方法二
#                                           REDIS_URL = 'redis://:135cylpsx4848\@@192.168.0.102:6379'
#                                   splash相关设置
#                                       SPLASH_URL = 'http://localhost:8050'    #splash服务地址
#                                       DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'    #去重类
#                                       HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'    #Cache的存储类
#                                   代理池的api接口
#                                       PROXY_URL = 'http://175.155.234.178:8000/random'
#                                   分布式爬虫
#                                       SCHEDULER = 'scrapy_redis.scheduler.Scheduler'    #配置分布式爬虫共享redis的调度器
#                                       DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'    #配置共享redis的去重类
#                                   自动超时关闭爬虫
#                                       CLOSESPIDER_TIMEOUT = 36000
#                               可选粘贴的
#                                   MAX_PAGE = 1    #设定最大翻页数
#                                   LOG_LEVEL = 'WARNING'    #定义显示日志文件的最高级别。即：开启后启动爬虫时，终端不会打印比WARNGIN级别低的日志,日志级别还有debug、info。配置文件中配置了什么等级，在爬虫文件中，logging就应该调用相对应的方法
#                                   LOG_FILE = './log.log'    #定义日志保存的位置，此时终端就不会输出信息了，而是直接将信息保存在本地
#                                   COOKIES_DEBUG = True    #开关cookies的调试，能在终端看到cookies在各个页面之间的传递过程
#                                   IMAGES_STORE = './images'    #将图片保存到本地的文件位置
#                               必须开启和修改的
#                                   ROBOTSTEX_OBEY = False    #是否遵循网站的robots协定，当然是False
#                                   DOWNLOAD_DELAY = 5    #下载时等待3秒，默认不等待
#                                   COOKIES_ENABLED = True    #是否启用cookies， 默认是开启的，请求第一个url时会返回cookies，下一个url请求会携带这个cookies
#                                   DEFAULT_REQUEST_HEADERS = {...}    #默认的请求包头
#                                   #爬虫中间件（splash）
#                                       SPIDER_MIDDLEWARES = {
#                                           'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
#                                       }
#                                   #下载的中间键（splash）
#                                       DOWNLOADER_MIDDLEWARES = {
#
#                                           'jdCrawl.middlewares.randomUserAgentDownloaderMiddleware': 98,    #随机useragent
#                                           'jdCrawl.middlewares.ProxyMiddleware': 99,    #随机代理
#                                           'scrapy_splash.SplashCookiesMiddleware':723,
#                                           'scrapy_splash.SplashMiddleware':725,
#                                           'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':810,
#                                       }
#                                   #管道文件
#                                       ITEM_PIPELINES = {...}     #管道文件可以配置多个用来处理不同的任务，比如一个管道文件将数据保存到本地，一个管道文件将数据保存到数据库
#                                   COOKIES_DEBUG = True    #能看到cookies的转送过程
#                               可以修改的
#                                   CONCURRENT_REQUESTS=320    #当前最大请求并发数，默认为16
#                                   CONCURRENT_REQUESTS_PER_DOMAIN = 16    #每个域名的最大并发数
#                                   CONCURRENT_REQUESTS_PER_IP = 16    #每个ip的最大请求并发数
#                               不需要修改
#                                   BOT_NAME = 'jdSpider'    #爬虫项目名称
#                                   SPINDER_MODULES = ['jdSpider.spiders']    #创建爬虫文件的目录位置
#                                   NEWSPIDER_MODULE = 'jdSpider.spiders'    #新创建的爬虫文件也会放在./jdSpider/spiders
#                                   TELNETCONSOLE_ENABLED = False    #插件
#                                   SPIDER_MIDDLEWARES = {'jsSpider.middlewares.JDspiderSpiderMiddleware': 543}    #爬虫中间件,说明：字典中可存在多个中间件，但它有优先级的区别，键的值越小优先级越高
#                                   Enable and configure the AutoThrottle extension    #自动限速，根据对方网站的情况，限制爬虫的速度，以免抓崩
#                                   Enable and configure HTTP caching    #开启本地缓存
#                           spiders    #爬虫文件的存放目录
#                               自动创建爬虫文件一——$ scrapy genspider jdSpider 'https://www.jd.com' 创建一件文件及内容
#                                   jdCrawl.py
#                                       非动态加载
#                                           import scrapy
#                                           from jdSpider.items import JdspiderItem
#                                           class JdcrawlSpider(scrapy.Spider):
#                                               name = 'jdCrawl'    #爬虫名
#                                               allowed_domains = ['https://www.jd.com/']    #爬取的url不能超过这个域,当遇到超出范围的url时会报debug错误 Filtered offsite request to '报错网址'
#
#                                               ————————  访问正常url+循环翻页  ————————
#                                               start_urls = ['http://www.jd.com/']    #爬虫会在这个列表中获取url,并放入调度器，调度器会将这些url，入队列去重出队列，交给可以下载器，下载器在internet去下载每个url，每个url都会调用parse方法处理返回值
#                                               def parse(self, response):    #处理返回值的方法
#                                                   #分组
#                                                   alist = response.xpath('//div[@id="123"]')
#                                                   for a in alist:
#                                                       item = JdspiderItem()
#                                                       item['name'] = a.xpath('./h1/text()').extract()  #extract()功能：将SelectorList对象转化成list或将Selector对象转换为str; extract_first()功能：将SelectorList对象转化成list并且从list中索引第一个元素
#                                                       yield item
#                                                   next_url = response.xpath('//button[contains(text(), "下一页")]/@href')
#                                                   if not next_url:
#                                                       return
#                                                   else:
#                                                       base_url = 'https://www.jd.com/list/'
#                                                       yield scrapy.Request(base_url+next_url, callback=self.parse)
#                                               ————————  访问接口url，返回json数据  ————————
#                                                       def start_requests(self):
#                                                           urlBaes = 'https://image.so.com/zjl?ch=photography&sn={}&listtype=new&temp=1'
#                                                           for page in range(1, self.settings.get('MAX_PAGE') + 1):
#                                                               url = urlBaes.format(page * 30)
#                                                               yield Request(url, self.parse)
#                                                       def parse(self, response):
#                                                           result = json.loads(response.text)
#                                                           for image in jsonpath(result, '$.list[*]'):
#                                                               item = ImageItem()
#                                                               item['id'] = jsonpath(image, '$.id')[0]
#                                                               item['url'] = jsonpath(image, '$.imgurl')[0]
#                                                               item['title'] = jsonpath(image, '$.title')[0]
#                                                               yield item
#                                       动态加载
#                                           import scrapy
#                                           from bossCrawl.items import BosscrawlItem
#                                           import time
#                                           import random
#                                           from scrapy_splash import SplashRequest
#
#                                           lua = """
#                                           function main(splash, args)
#                                               splash.images_enabled = false
#                                               assert(splash:go(args.url))
#                                               assert(splash:wait(args.wait))
#                                               splash.scroll_position={y=10000}
#                                               assert(splash:wait(args.wait))
#                                               splash.scroll_position={y=10000}
#                                               assert(splash:wait(args.wait))
#                                               splash.scroll_position={y=10000}
#                                               assert(splash:wait(args.wait))
#                                               return splash:html()
#                                           end
#                                           """
#
#                                           class BossspiderSpider(scrapy.Spider):
#                                               name = 'bossSpider'
#                                               allowed_domains = ['www.zhipin.com']
#                                               start_urls = ['https://www.zhipin.com/c100010000/?query=%E7%88%AC%E8%99%AB&page=1&ka=page-1']
#
#                                               def start_requests(self):
#                                                   yield SplashRequest(self.start_urls[0], callback=self.parse, endpoint='execute', args={'lua_source':lua, 'wait':5}, dont_filter=True)
#
#                                               def parse(self, response):
#                                                   print('111')
#                                                   for i in response.xpath('//div[@class="job-list"]/ul/li'):
#                                                       print('222')
#                                                       item = BosscrawlItem()
#                                                       item['source'] = 'Boss直聘'
#                                                       item['jobName'] = i.xpath('.//div[@class="job-title"]/text()').extract_frist()
#                                                       item['price'] = i.xpath('.//span[@class="red"]/text()').extract_frist()
#                                                       item['companyName'] = i.xpath('//div[@class="company-text"]/h3/a/text()').extract_frist()
#                                                       item['address'] = i.xpath('//div[@class="info-primary"]/p/text()').extract_frist()
#                                                       innerUrl = 'https://www.zhipin.com' + i.xpath('//div[@class="info-primary"]/h3/a/@href').extract_first()
#                                                       yield scrapy.Request(innerUrl, meta={'item':item.cope()}, callback=self.innerParse, dont_filter=True)
#                                                   next_url = response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract_first()
#                                                   print(next_url)
#                                                   if next_url:
#                                                       yield SplashRequest('https://www.zhipin.com' + next_url, callback=self.parse, endpoint='execute', args={'lua_source': lua, 'wait': 5}, dont_filter=True)
#                                                   else:
#                                                       return

#                                               def innerParse(self, response):
#                                                   item = response.meta['item']
#                                                   item['content'] = response.xpath('//div[@class="job-sec"]/div[@class="text"]/text()').extract()
#                                                   print(item)
#                                                   yield item
#                                                   randomtime = random.randint(1, 59)
#                                                   if time.strftime('%H:%M:%S', time.localtime()) == '9:{}:{}'.format(randomtime, randomtime):
#                                                       time.sleep(39600)
#                               自动创建爬虫文件er——$ scrapy genspider -t ybjhxzcf www.cbrc.gov.cn 创建一件文件及内容
#                                   ybjhxzcf.py
#                                       class YbjhxzcfSpider(CrawlSpider):
#                                             start_urls = ['http://www.cbrc.gov.cn/cn/list/9103/910305/ybjfjcf/1.html']    #第一次发送文件
#                                             #url规则定义
#                                             rules = (
#                                                 #Rule：是一个类，Rule()在做实例化，得到的一条实例就是一条url规则
#                                                 #LinkExtractor：链接提取器，提取url地址
#                                                 #allow：定义正则表达式
#                                                 #callback：提取出来的url地址的response会交个callback处理
#                                                 Rule(LinkExtractor(allow=r'/cn/doc/9103/910305/ybjfjcf/\w*?\.html'), callback='parse_item', follow=False),
#                                                 Rule(LinkExtractor(allow=r'\d+\.html'), callback='parse_item', follow=True),
#                                             )
#                                             PS:#parse函数其实还是存在的，当我们用正则提取出url后，url会传到父类的parse函数中，发送请求
#                                             #因此这里不能用parse命名函数，否则会重写父类方法
#                                             def parse_item(self, response):
#                                                 item = CbrcItem()
#                                                 item['companyName'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/table/tbody/tr[3]/td[3]/p/span[1]/text()').extract_first()
#                                                 return item
#                           items.py    说明：用于声明解析字段名
#                               import scrapy
#                               class JdspiderItem(scrapy.Item):
#                                   name = scrapy.Field()    #声明了一个name字段，字段中的名字要与爬虫文件中itme实例对象的键相同
#                           middlewares.py    说明：中间键，高级用法，使用时只需要在配置文件中打开即可
#                               #爬虫中间件
#                               class SpiderMiddleware(object):
#                               #下载中间件
#                               class DownloaderMiddleware(object):
#                                   #处理请求函数
#                                   def process_request(self, request, spider):
#                                       功能：处理请求体对象,主要用于随机切换代理、随机切换user_agent
#                                       触发：当每个request通过下载中间时，该方法被调用
#                                       参数：request是当前爬虫的请求对象，spider是爬虫文件对象
#                                       注意：此方法定义时，一定不能return或yield
#                                       示例：
#                                           #随机切换UA
#                                           from myClass.headers import Headers
#                                           agent = Headers()
#                                           class randomUserAgentDownloaderMiddleware(object):
#                                               @classmethod
#                                               def from_crawler(cls, crawler):
#                                                   # This method is used by Scrapy to create your spiders.
#                                                   s = cls()
#                                                   crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#                                                   return s
#
#                                               def process_request(self, request, spider):
#                                                   userAgent = agent.allHeaders()
#                                                   request.headers['User_Agent'] = userAgent
#                                                   return None
#
#                                               def process_response(self, request, response, spider):
#                                                   # Called with the response returned from the downloader.
#
#                                                   # Must either;
#                                                   # - return a Response object
#                                                   # - return a Request object
#                                                   # - or raise IgnoreRequest
#                                                   return response
##
#                                               def spider_opened(self, spider):
#                                                   spider.logger.info('Spider opened: %s' % spider.name)
#                                           request.headers['User_Agent'] = userAgent  # 在请求头中添加User_Agent
#                                           #随机切换代理
#                                               #付费代理
#                                                   proxy = random.choice(spider.settings.get('PROXY'))  # 将配置文件的UA列表取出，并从其中随机取出一个代理，注意代理的类型，https的网站切换https的代理，http的网站切换http的代理，代理类型选用高匿名类型
#                                                   request.meta['proxy'] = 'https://' + proxy  # 在请求头中添加代理
#                                               #adsl代理
#                                                   scrapy.Request请求
#                                                       from myClass.proxyADSL.proxyADSL import proxyADSL    #在文件顶部导入
#                                                       proxy_ADSL = proxyADSL('175.155.249.13')  # 放在下载中间件类的开始部位，将其设置为类属性,一定要在服务器上开启8000监听，参数为：云服务器ifconfig.ppp0.inet.ip
#                                                       proxy = slef.proxy_ADSL.get_proxyADSL()
#                                                       request.meta['proxy'] = 'https://' + proxy
#                                                   SplashRequest请求
#                                                         class ProxyMiddleware():
#                                                             def __init__(self, proxy_url):
#                                                                 self.logger = logging.getLogger(__name__)
#                                                                 self.proxy_url = proxy_url
#                                                             def get_random_proxy(self):
#                                                                 try:
#                                                                     response=requests.get(self.proxy_url)
#                                                                     if response.status_code == 200:
#                                                                         proxy = response.text
#                                                                         return proxy
#                                                                 except requests.ConnectionError:
#                                                                     return False
#                                                             def process_request(self, request, spider):
#                                                                 if request.meta.get('retry_times'):
#                                                                     proxy = self.get_random_proxy()
#                                                                     if proxy:
#                                                                         uri = 'https://{}'.format(proxy)
#                                                                         request.meta['splash']['args']['proxy'] = uri
#                                                             @classmethod
#                                                             def from_crawler(cls, crawler):
#                                                                 settings = crawler.settings
#                                                                 return cls(proxy_url=settings.get('PROXY_URL'))
#                                   #处理响应函数
#                                   def process_response(slef, request, response, spider):
#                                       功能：处理响应体对象
#                                       触发：当下载器完成http请求，传递响应给引擎的时候调用
#                                       参数：response是当前爬虫的响应对象
#                                       注意：必须return
#                                           return respons 给引擎，引擎会交给爬虫文件
#                                           return request 给硬气，引擎会交给调度器，重新发起请求
#                                       检验userAgent是否设置成功：
#                                       如果procces_requets中的ua值和这里的响应体中的请求头中的us相同，则切换成功
#                                       print(response.request) #响应体中也存放了请求头
#                           pipelines.py    说明：管道文件处理items数据
#                               import json
#                               import re
#                               from pymongo import MongoClient
#                               import pymongo
#                               from scrapy import Request    #下载图片到本地需要的包
#                               from scrapy.exceptions import DropItem    #下载图片到本地需要的包
#                               from scrapy.pipelines.images import ImagesPipeline    #下载图片到本地需要的包
#                               #json格式保存1:[{},{}]
#                                   from scrapy.exporters import JsonItemExporter
#                                   class ItcastPipeline(object):
#                                       def __init__(self):
#                                           self.n = 0
#                                           self.f = open('name.json', 'wb')
#                                           self.exporter = JsonItemExporter(self.f, ensure_ascii=Fasle, encoding='utf8')
#                                           self.exporter.start_exporting()
#                                       def open_spider(self, spider):
#                                           print('爬虫开始')
#                                       def process_item(self, item, spider): #每次有item数据时，即在爬虫文件中的for循环中爬取到一个数据就调用一次
#                                           self.exporter.export_item(item)
#                                           print('已经爬取第{}条数据'.format(self.n += 1))
#                                           return item
#                                       def close_spider(self, spider): #爬虫结束时自动调用这个方法，本质为引擎在循环索取爬虫文件的生成器数据，当生成器中的数据为空时，捕捉到错误做为判断依据，停止循环并调用close_spider方法
#                                           self.f.close()
#                               #json格式保存2:{},{}
#                                   from scrapy.exporters import JsonLinesItemExporter
#                                   class ItcastPipeline(object):
#                                       def __init__(self):
#                                           self.n = 0
#                                           self.f = open('name.json', 'wb')
#                                           self.exporter = JsonLinesItemExporter(self.f, ensure_ascii=Fasle, encoding='utf8')
#                                       def open_spider(self, spider):
#                                           print('爬虫开始')
#                                       def process_item(self, item, spider): #每次有item数据时，即在爬虫文件中的for循环中爬取到一个数据就调用一次
#                                           self.exporter.export_item(item)
#                                           print('已经爬取第{}条数据'.format(self.n += 1))
#                                           return item
#                                       def close_spider(self, spider): #爬虫结束时自动调用这个方法，本质为引擎在循环索取爬虫文件的生成器数据，当生成器中的数据为空时，捕捉到错误做为判断依据，停止循环并调用close_spider方法
#                                           self.f.close()
#                               #mongodb
#                                   class MongoPipeline(object):
#                                       def __init__(self, mongo_uri, mongo_db):
#                                           self.mongo_uri = mongo_uri
#                                           self.mongo_db = mongo_db
#                                       @classmethod
#                                       def from_crawler(cls, crawler):
#                                           return cls(
#                                               mongo_uri=crawler.settings.get('MONGO_URI'),
#                                               mongo_db=crawler.settings.get('MONGO_DB')
#                                           )
#                                       def open_spider(self, spider):
#                                           self.client = pymongo.MongoClient(self.mongo_uri)
#                                           self.db = self.client[self.mongo_db]
#                                       def process_item(self, item, spider):
#                                           name = item.collection
#                                           self.db[name].insert(dict(item))
#                                           return item
#                                       def close_spider(self, spider):
#                                           self.client.close()
#                               #mysql
#                                   from mySql import MySql
#                                   class MysqlPipeline():
#                                       def open_spider(self, spider):
#                                           self.mySql = MySql(spider.settings['MYSQL_HOST'], spider.settings['MYSQL_USER'], spider.settings['MYSQL_PASSWORD'], spider.settings['MYSQL_DATABASE'])
#                                           self.mySql.connect()
#                                       def process_item(self, item, spider):
#                                           item['content'] = self.process_content(item['content'])
#                                           self.mySql.insert('images', dict(item))
#                                           return item
#                                       #如果字段需要清洗可以用一下方法，清洗完毕之后返回到process_item函数中
#                                       def process_content(self, content):
#                                           content = [re.sub(r'\xa0|\s', '', i) for i in content]
#                                           content = [i for i in content if len(i) > 0]
#                                           return content
#                                       def close_spider(self, spider):
#                                           # self.mySql.close()    #因为insert会自动关闭mysql所以不用再关闭
#                                           pass

#                               #图片保存到本地
#                                   class ImagePipeline(ImagesPipeline):
#                                       def file_path(self, request, response=None, info=None):
#                                           url = request.url
#                                           file_name = url.split('/')[-1]
#                                           return file_name
#                                       def item_completed(self, results, item, info):
#                                           image_paths = [x['path'] for ok, x in results if ok]
#                                           if not image_paths:
#                                               raise DropItem('Image Downloaded Failed')
#                                           return item
#                                       def get_media_requests(self, item, info):
#                                           yield Request(item['url'])
#                               #txt
#
#       version
#           功能：打印版本号
#       view
#           功能：用浏览器的方式查看爬取过程
#
#   scrapy模拟登录
#       本质：携带正确的cookies请求网站就能返回正确的结果
#       理论基础：strat_url是首次登录界面的url，将这个url包装成requeste对象的函数是start_requests()
#               因此，如果需要模拟登录网站，我们在自己的爬虫文件中重写start_requests()方法来设置这个url的请求体
#               重写start_requests方法，携带登录后个人主页页面的cookies，发起get请求，获取个人主页页面信息
#       非携带token的cookies
#           示例网站：人人网
#           代码和注释见练习-scrapyTest-renren
#       携带token的cookies
#           在登录页刷新是产生token（js生成后展示在网页代码中、js生成后不展示在网页代码中）
#               示例网站：github
#               示例url：https://www.github.com/login
#               步骤
#                   网页分析
#                       谷歌打开https://www.github.com/login
#                       打开抓包工具F12
#                       在Network中勾选Preserve log(刷新不覆盖之前的包)
#                       刷新
#                       第一次输入一个错误密码点击登录
#                           此时就会出现一个会话包，即session，其中包括了formdata，fromdata中就包含了动态生成的token
#                       第二次输入一个错误密码点击登录
#                           此时又会出现一个session，此时又动态生成了一个token
#                       发送post的url地址就在session的头中
#                       对比这两个会话的的fromdata中的token确实不一样
#                       点击三个点中的search，搜索authenticity_token
#                           就能在所有文件中搜索到出现authenticity_token的文件
#                               搜索到2个js文件和一个网页文件
#                                   如果出现网页文件说明authenticity_token展示在了网页代码中
#                                       每次到源代码中获取authenticity_token的值就行了
#                                       点击这个网页文件，即可查看authenticity_token在网页代码中的位置，被表黄的那条代码中就会有authenticity_token
#                                       再次到Elements中，搜索authenticity_token确定是否真的存在
#                                           所搜到后，这里的authenticity_token值与Network中session中fromdata中的authenticity_token的值进行对比
#                                               这两处的值不相同，没关系，因为在Network的值是本次请求的token，网页中的token则是下一次要登录的token
#                                               获取网页中的token即可
#                                               获取其他formdata元素
#                                                   在网页代码中直接搜索，观察其他参数是否也直接展示在了网页代码中
#                                                       commit、utf8、login、webauthn-support确实也在网页代码的input标签中
#                                                           取input标签的value值即可
#                                   如果只有js文件，说明authenticity_token没有展示在网页代码中
#                                       需要读懂js，了解其生成规则，在通过python代码模拟规则生成同样的token
#                   构造post请求的formdata
#           登录进去后产生token
#   复杂登录
#       https://kyfw.12306.cn/otn/login/init
#   实战
#       项目：银保监分局本级行政处罚
#       url：http://www.cbrc.gov.cn/cn/list/9103/910305/ybjfjcf/1.html
#       坑：521加速乐，
#       解决思路：
#           第一次请求：返回521状态码和一段js代码。js会生成一段cookie并重新请求访问。
#           第二次请求：带着第一次得到的cookie去请求然后正确返回状态码200

#【day】docker
#概念
#   docker是后台虚拟机，类似vmware
#   采用网页方式登录虚拟机
#安装
#   linux安装:见kn4
#   windows安装：
#使用
#   linux使用：见kn4
#   windows使用
#       cmd使用：可以使用docker命令
#       网页客户端使用：https://labs.play-with-docker.com/


#【day】lua语言
#基本语法
'''
--    #注释
#声明变量
print('hellow lua')
num = 100    #申明变量——动态定义变量类型
print(num)
local num = 100    #local关键词——定义局部变量

#定义函数
function sayHello()
    print('hello lua')
end
sayHello() --> hello lua

#定义有参函数
function max(a, b)
    if a>b then
        return a
    else
        return b
    end
end
print(max(2,3))

#if循环
for var = 1 , 100 do
    print(var)
end

#定义表，类似字典
config = {}    #定义空表
config = {'a':'A','b':'1','c':1}    #定义有值的表
表写入值
config.words = 'hello'    #写入值——{'words':'hello'}
config.num = 100    #写入值——{'words':'hello', 'num':100}
config['name'] = 'zhangsan'    #写入值——{'words':'hello', 'num':100,'name':'zhangsan'}
表取出值
print(config.words)    #表中取值
print(config['name'])    #表中取值

遍历表
for key, var in pairs(config) do
    print(key, var)
end
---->  words    hello
       num      100
       name     zhangsan

数组
array = {123,'abc'}
for key, var in pairs(array) do
    print(key, var)
end
---->1 123
     2 abc
注意：索引从1开始

给数组遍历插入值
arr = {}
for var=1, 5 do
    table.insert(arr, 1, var)    #给arr插入值
end
for key, var in pairs(arr) do
    print(key, var)
end
----->1   5
      2   4
      3   3
      4   2
      5   1
#数组长度
print(table.maxn(arr))

:的使用
a:b()
说明 a对象调用b方法
'''


#【day】splash
#概念：splash是支持异步js加载的服务
#启动服务
#   命令：docker run -d -p 8050:8050 scrapinghub/splash    #-d为在后台执行此服务，此时可以关闭该cmd
#   说明：此命令适用于linux、windows的cmd、windows的网页客户端
#链接服务器
#   浏览器中访问localhost:8050
#       链接后就可以进行lua语言脚本的测试
#       检测方式见图灵p263
#lua脚本
'''
    function main(splash, args)    #main方法名不可改变
      assert(splash:go(args.url))    #assert()检验，参数中报错则返回0；splash:go(),调用splash中的类方法go()；args.url：从args参数中取出url，等价于splash.args.url
      assert(splash:wait(0.5))    #wait()类方法等价于time.sleep(1)
      local title=splash:evaljs('document.title')    #local关键字，其后定义的变量为局部变量；evaljs()类方法，功能是执行参数中的js代码；document.title是js代码
      return {
        html = splash:html(),    #返回网页源代码
        png = splash:png(),    #返回截图，是二进制数据
        har = splash:har(),    #返回HAR信息，即网页加载过程信息
      }
    end    #函数结束
'''

lua = """
function main(splash, args)
    splash.images_enabled = false    
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    splash.scroll_position={y=10000}
    assert(splash:wait(args.wait))
    splash.scroll_position={y=10000}
    assert(splash:wait(args.wait))
    splash.scroll_position={y=10000}
    assert(splash:wait(args.wait))
    return splash:html()
end
"""

#splash类
#   属性
#       args
#           说明：args返回的是字典可以用.方法来获取字典中具体的值
#           取值：splash.args.url
#           设值：splash.args.url = 'http://www.baidu.com'
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   print('splash.args.url')
#               end
#               '''
#       resource_timeout
#           说明：设值加载超时时间，超过规定时间还未获得响应则抛出异常
#           设值：splash.resource_timeout = 0.1
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash.resource_timeout = 0.1
#               end
#               '''
#       images_enabled
#           说明：网页是否加载图片
#           注意：JavaScript对图片节点有操作，不要禁止加载，比如对图片有移动动画
#           设值：splash.images_enabled = False
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash.images_enabled = False    #禁止加载图片
#               end
#               '''
#       plugins_enabled
#           说明：控制是否加载插件（如：flash插件），默认是不加载插件
#           设值：splash.plugins_enabled = True
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash.plugins_enabled = True   #加载插件
#               end
#               '''
#       scroll_position
#           说明：控制页面滚轮上下或左右滚动
#           设值
#               splash.scroll_position={x=400}
#               splash.scroll_position={y=400}
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash.scroll_position={x=400}    #横向滚轮，滑动到x=400位置
#                   splash.scroll_position={y=400}    #纵向滚轮，滑动到y=400位置
#               end
#               '''
#   方法
#       go()
#           功能：模拟浏览器发送get或post请求
#           原型：go{url, baseurl=nil, headers=nil, http_method='GET', body=nil, formadata=nil}
#           注意：go方法如果只有url，则用括号即可，类似python传参函数调用，但是如果要设置多个值，需要将小括号换成花括号
#           参数
#               url：请求的url地址
#               baseurl：资源加载相对路径
#               headers：请求头
#               http_method：请求类型，GET/POST
#               body：post请求的表单数据，Content-type为application/json
#               formdata：post请求的表单数据，Content-type为application/x-www-form-urlencoded
#           返回值：状态ok(如果访问网页出错，ok则为None)，网页源码
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   local ok, resonance= splash:go{'http://httpbin.org/post', http_method='POST', body='name=Germey'}
#                   if ok then
#                       return splash:html()
#                   end
#               end
#               '''
#       wait()
#           功能：控制页面等待时间
#           原型：wait{time, cancel_on_redirect=false, cancel_on_error=true}
#           注意：单参数用(),多参数用{}
#           参数
#               tiem：等待时间
#               cancel_on_redirect：如果发送重定向，就停止等待时间，返回重定向后的结果
#               cancel_on_error：如果发生加载错误，就停止等待
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://www.taobao.com')
#                   splash:wait(2)
#               end
#               '''
#       jsfunc()
#           功能：执行js代码
#           原型：jsfunc([[function(){}]])
#           注意：js代码需要用双中括号[[]]包裹
#           参数：js代码
#           返回值：js代码中返回的值，如果js中没有返回值，则jsfunc()无返回值
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   local get_div_count = splash:jsfunc([[function(){
#                       var body = document.body;
#                       var divs = body.getElementsByTagName('div');
#                       return divs.length;
#                   }]])
#                   splash:go('https://www.baidu.com')
#                   return ('There are %s DIVs'):format(get_div_count())
#               end
#               '''
#       evaljs()
#           功能：执行js代码,获取js代码的值
#           原型：evaljs(js)
#           说明：js可以有很多条'document.title;document.body'
#           参数：js代码的字符串
#           返回值：最后一条js代码的值，
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://www.baidu.com')
#                   local title= splash:evaljs('document.title')
#                   return {title=title}
#               end
#               '''
#       runjs()
#           功能：声明js的动作或方法，以备调用
#           原型：runjs('foo = function(){}')
#           注意：foo为lua语言的全局变量
#           参数：要赋值的全局变量以及要执行的js方法赋值
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://www.baidu.com')
#                   splash:runjs('foo = function(){return "bar"}')
#                   local result = splash:evaljs('foo()')
#                   return result
#               end
#               '''
#       autoload()
#           功能：定义打开页面就加载指定js代码或js库的方法
#           原型：autoload{source_or_url, source=nil, rul=nil}
#           参数
#               souce_or_ulr:js代码或js库的链接(比如，jquery库的链接地址)
#               source:js代码
#               url：js库链接地址
#           注意
#               此方法只负责加载不负责执行，需要和evaljs()或runjs()方法联合使用
#               如果传入的参数是js代码需要用[[]]包裹，见示例1
#               如果传入的参数是js库的链接地址要用''包裹，见示例2
#           返回值：无
#           示例1
#               scrapt = '''
#               function main(splash, args)
#                   splash:autoload([[function get_document_title(){
#                       return document.title;
#                   }]])
#                   splash:go('https://www.baidu.com')
#                   return splash:evaljs('get_document_title()')
#               end
#               '''
#           示例2
#               scrapt = '''
#               function main(splash, args)
#                   assert(splash:autoload('https://code.jquery.com/jquery-2.1.3.min.js'))    #加载jquery，jquery地址，jquery网络地址
#                   assert(splash:go('https://www.taobao.com'))
#                   local version = splash:evaljs('$.fn.jquery')
#                   return 'JQuery version: '..version
#               end
#               '''
#       call_later()
#           功能：延迟执行lua代码
#           原型：call_later(fuction()end, laterTime)
#           参数
#               fuction()end：定义lua语言的方法
#               laterTime：延迟执行的时间
#           返回值：无
#           示例1
#               scrapt = '''
#               function main(splash, args)
#                   local snapshots = {}
#                   local timer = splash:call_later(function()
#                       snapshots['a'] = splash:png()
#                       splash:wait(1)
#                       snapshots['b'] = splash:png()
#                   end, 0.2)
#                   splash:go('https://www.taobao.com')
#                   splash:wait(3)
#                   return snapshots
#               end
#               '''
#       set_content()
#           功能：设置页面内容
#           原型：set_content('dom')
#           参数：dom元素
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   assert(splash:set_content('<html><body><h1>Hello</h1></body></html>'))
#                   return splash:png()
#               end
#               '''
#       html()
#           功能：获取网页源代码
#           原型：html()
#           返回值：网页源代码
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://httpbin.org/get')
#                   return splash:html()
#               end
#               '''
#       png()
#           功能：获取网页截图
#           原型：html()
#           返回值：网页png格式的截图
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://www.taobao.com')
#                   return splash:png()
#               end
#               '''
#       jpeg()
#           功能：获取网页截图
#           原型：html()
#           返回值：网页jpeg格式的截图
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://www.taobao.com')
#                   return splash:jpeg()
#               end
#               '''
#       har()
#           功能：获取页面加载过程的描述
#           原型：har()
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://www.taobao.com')
#                   return splash:har()
#               end
#               '''
#       url()
#           功能：获取当前访问的url
#           原型：har()
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://www.taobao.com')
#                   return splash:url()
#               end
#               '''
#       get_cookies()
#           功能：获取当前页面的cookies
#           原型：get_cookies()
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https://www.taobao.com')
#                   return splash:get_cookies()
#               end
#               '''
#       add_cookies()
#           功能：获取当前页面的cookies
#           原型：add_cookies{'sesionid','237465ghgfsd','/',domain='http://example.com'}
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:add_cookies{'sesionid','237465ghgfsd','/',domain='http://example.com'}
#                   splash:go('http://example.com/')
#                   return splash:html()
#               end
#               '''
#       clear_cookies()
#           功能：清除当前页面的cookies
#           原型：clear_cookies()
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:add_cookies{'sesionid','237465ghgfsd','/',domain='http://example.com'}
#                   splash:go('http://example.com/')
#                   return splash:html()
#               end
#               '''
#       get_viewport_size()
#           功能：获取当前页面的大小,即宽高
#           原型：get_viewport_size()
#           返回值：数组
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('http://example.com/')
#                   return splash:get_viewport_size()
#               end
#               '''
#       set_viewport_size()
#           功能：获取当前页面的大小,即宽高
#           原型：get_viewport_size(width, height)
#           返回值：数组
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:set_viewport_size(400,700)
#                   splash:go('http://example.com/')
#                   return splash:png()
#               end
#               '''
#       set_viewport_full()
#           功能：设置浏览器全屏显示
#           原型：set_viewport_full()
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:set_viewport_full()
#                   splash:go('http://example.com/')
#                   return splash:png()
#               end
#               '''
#       set_user_agent()
#           功能：设置浏览器的userAgent
#           原型：set_user_agent('Micalsoft...')
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:set_user_agent('Micalsoft...')
#                   splash:go('http://example.com/')
#                   return splash:html()
#               end
#               '''
#       set_custom_headers()
#           功能：设置请求头
#           原型：set_custom_headers({['User_Agent']='Micalsoft...', ['Site']='Splash'})
#           返回值：无
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:set_custom_headers({['User_Agent']='Micalsoft...', ['Site']='Splash'})
#                   splash:go('http://example.com/')
#                   return splash:html()
#               end
#               '''
#       select()
#           功能：使用css选择器选中符合条件的第一个节点
#           原型：select('selector')
#           参数：css选择器
#           返回值：dom元素对象
#           注意：不管找到多个dom元素对象，只返回第一个
#           示例
#               scrapt = '''
#               function main(splash, args)
#                   splash:go('https:www.baidu.com')
#                   input = splash:select('#kw')
#                   input:send_text('Splash')
#                   splash:wait(3)
#                   return splash:png()
#               end
#               '''
#       select_all()
#           功能：使用css选择器选中符合条件的第一个节点
#           原型：select_all('selector')
#           参数：css选择器
#           返回值：dom元素对象所组成的数组
#           示例
#               scrapt = '''
#                   function main(splash, args)
#                     local treat=require('treat')
#                     assert(splash:go("http://quotes.toscrape.com/"))
#                     assert(splash:wait(0.5))
#                     local texts=splash:select_all('.quote .text')
#                     local results={}
#                     for index,text in ipairs(texts) do
#                         results[index]=text.node.innerHTML
#                     end
#                     return treat.as_array(results)
#                   end
#               '''
#       mouse_click()
#           功能：模拟鼠标点击
#           原型：mouse_click()
#           参数：xy
#           返回值：无
#           说明：可以直接传入xy的值，直接点击
#           示例
#               scrapt = '''
#                   function main(splash, args)
#                       splash:go("https://www.baidu.com/")
#                       input=splash:select("#kw")
#                       input:send_text('Splash')
#                       submit=splash:select('#su')
#                       submit:mouse_click()
#                       splash:wait(3)
#                       return splash:png()
#                   end
#               '''
#   python对Splash接口的访问
#       接口地址格式：Splash运行地址+接口名称+?+参数
#       所有接口
#           reder.html
#               原型：http://192.168.0.104:8050/render.html?url=目标网址
#               功能：获取指定网页渲染后的网页源代码
#               返回：网址的源代码
#               参数：url：目标网址
#               示例
#                   import requests
#                   url='http://192.168.0.104:8050/render.html?url=https://www.baidu.com'
#                   response=requests.get(url)
#                   print(response.text)
#           reder.png
#               原型：http://192.168.0.104:8050/render.png?url=目标网址&wait=5&width=int&height=int
#               功能：获取指定网页渲染后网页截图
#               返回：数据为png格式的二进制数据
#               参数
#                   url：目标网址
#                   wait：等待页面加载时间
#                   width：截图宽度
#                   height：截图高度
#               示例
#                   import requests
#                   url='http://192.168.99.100:8050/render.png?url=https://www.jd.com&wait=5&wait=1000&height=700'
#                   response=requests.get(url)
#                   with open('taobao.png','wb') as f:
#                       f.write(response.content)
#           reder.jpeg
#               原型：http://192.168.0.104:8050/render.jpeg?url=目标网址&wait=5&width=int&height=int
#               功能：获取指定网页渲染后网页截图
#               返回：数据为jpeg格式的二进制数据
#               参数
#                   url：目标网址
#                   wait：等待页面加载时间
#                   width：截图宽度
#                   height：截图高度
#               示例
#                   import requests
#                   url='http://192.168.99.100:8050/render.jpeg?url=https://www.jd.com&wait=5&wait=1000&height=700'
#                   response=requests.get(url)
#                   with open('taobao.jpeg','wb') as f:
#                       f.write(response.content)
#           reder.har
#               原型：http://192.168.0.104:8050/render.har?url=目标网址&wait=5
#               功能：获取指定网页加载渲染的整个过程
#               返回：数据为JSON格式
#               参数
#                   url：目标网址
#                   wait：等待页面加载时间
#               示例
#                   import requests
#                   url='http://192.168.99.100:8050/render.har?url=https://www.jd.com&wait=5&wait=1000&height=700'
#                   response=requests.get(url)
#                   with open('jd.json','wb') as f:
#                       f.write(response.content)
#           reder.json
#               原型：http://192.168.0.104:8050/render.json?url=目标接口网址
#               功能：获取指定接口的json数据
#               返回：数据为JSON格式
#               参数
#                   url：目标接口网址
#               示例
#                   import requests
#                   url='http://192.168.99.100:8050/render.har?url=https://movie.douban.com/j/chart/top_list?type=6'
#                   response=requests.get(url)
#                   with open('move.json','wb') as f:
#                       f.write(response.content)
#           reder.execute
#               原型：http://192.168.0.104:8050/render.execute?lua_source=lua脚本
#               功能：加载自定义的lua脚本与浏览器交互
#               返回：lua中定义的返回值
#               参数
#                   lua_source：lua脚本
#               示例
#                   import requests
#                   from urllib.parse import quote
#                   lua = """
#                   function main(splash, args)
#                     splash:go('http://www.baidu.com')
#                     return splash:html()
#                   end
#                   """
#                   url = 'http://192.168.0.104:8050/execute?lua_source=' + quote(lua)
#                   response = requests.get(url)
#                   print(response.text)


#【day】Nginx
#前导概念
#    服务器
#       概念：提供某种或多种服务(功能)的计算机
#       硬件：性能更好的电脑主机
#       软件：实现各种服务支持特定的协议的软件（http https协议）
#    集群
#       概念
#           多台服务器组成的响应大并发、高数据量访问的架构体系
#           也叫分布式服务器架构
#       web服务软件
#           提供http https 协议的服务器，网站网页访问的功能
#       web服务器架构
#           LAMP
#               linux + apache + mysql + php
#               组件介绍
#                   linux：操作系统
#                   apache：老牌服务器软件、功能多并且稳定、支持多种配置
#                   mysql：数据库
#                   php：服务器高级脚本语言
#           LNMP
#               linux + nginx + mysql + php
#               组件介绍
#                   nginx：并发量高，安装简单小巧，一般用于——web服务器、代理服务器、邮箱服务器、搭建lnmp环境
#           拓展
#               服务器软件
#                   apache
#                   nginx
#                       俄罗斯人、
#                       tengine是nginx的一个国内版本，由阿里巴巴开发，具有更多高级功能、性能强大、运行稳定等特点
#                   lls：微软触屏、asp脚本使用、可以通过fast-cgi(网络接口服务)的方式使用php
#                   lighttpd：德国开发软件、小巧、提供web服务器支持
#               数据库
#                   关系型数据库RDBMS
#                       mysql
#                       oracle 大型商业数据库
#                       sqlserver 微软数据库
#                       DB2 IBM
#                       sqllite3 手机端使用
#                       postgresql 加州伯克利大学 学院派
#                   非关系型数据库
#                       memcached
#                       mongodb
#                       redis
#               负载均衡
#                   概念
#                       一台服务器的负载（流量压力）过大，会导致服务器宕机
#                       为避免这种情况出现，使用一台负载均衡服务器来控制分发，让多台服务器负载均衡
#                       负载均衡服务器
#                           概念
#                               硬件级别为F5，性能好，价格高
#                               软件级使用nginx中的upstream功能分发
#               资源服务器
#                   概念
#                       存储静态资源，如css、js、图片、视频
#                       一般此服务器会有硬盘（ssd固态硬盘）读写快速，带宽更大——一般大型公司的带宽为10兆
#
#               正向代理服务器
#                   概念
#                       a需要访问c，但a不能直接访问c，而a能访问b，b又能访问c，最终a告诉b帮忙访问一下c
#                       因此b就是a的代理服务器
#               反向代理
#                   概念：见本文件782行代码
#                   搭建：nginx搭建反向代理
#               高可用
#                   概念
#                       高可用服务器，用来监控负载均衡服务器，如果一旦负载均衡器宕机，会阶梯负载均衡服务器的工作，继续进行网络的分发工作
#                       可以认为是负载均衡器的备用服务器
#                   搭建
#                       软件
#                           heartbit
#                           keeplive
#               缓存软件
#                   memcached
#                   redis
#               cdn内容分发
#                   用户请求一个网站内容，网站一般会有非常多代理服务器，cdn会分析代理服务器的响应时间、网络流量、各个节点的链接情况、负载情况、离该用户的距离。让该用户能访问到最佳情况的服务器，从而解决网络拥堵，提高响应速度
#
#Nginx服务器
#   概念
#       ginx是一个高性能的HTTP和反向代理服务器
#   特点
#       热部署：nginx在修改配置文件之后，不需要重启
#   安装



#【scrapy】进阶
