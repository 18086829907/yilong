#模拟流量器访问服务器
#   1、打开网络调试助手，tcp:server，ip:127.0.0.1，port:8080
#   2、打开谷歌浏览器，地址栏输入127.0.0.1:8080/a/index.html
#   3、网络助手会收到浏览器发送过来的http协议的第一部分
#          浏览器--->服务器发送的请求格式
#             GET /a/index.html HTTP/1.1    #表示浏览器请求服务器中的哪个资源，注意GET 后面的地址=浏览器地址栏输入的端口号后面的内容
#             Host: 127.0.0.1:8080    #表示服务器的地址
#             Connection: keep-alive    #连接方式：长连接
#             Upgrade-Insecure-Requests: 1
#             User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36    #浏览器的版本号
#             Sec-Fetch-User: ?1
#             Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3    #允许服务器发送过来的数据格式
#             Sec-Fetch-Site: none
#             Sec-Fetch-Mode: navigate
#             Accept-Encoding: gzip, deflate, br    #允许服务器发送过来的数据的压缩格式
#             Accept-Language: zh-CN,zh;q=0.9    #允许服务器发送过来的数据语言：支持中文
#   4、网络助手回送数据
#       服务器---->浏览器回送的数据格式
#           查询格式的方法
#               打开浏览器，F12打开调试器，点击Network，点击清屏按钮，按F5刷新，Network就会记录访问百度首页的所有数据交互记录
#               点击第一个任务的Headers
#                   General    #描述
#                         Request URL: https://www.baidu.com/
#                         Request Method: GET
#                         Status Code: 200 OK
#                         Remote Address: 39.156.66.14:443
#                         Referrer Policy: no-referrer-when-downgrade
#                   Response Headers    #可以点击view source，显示http协议格式    #应答
#                         HTTP/1.1 200 OK    #http协议版本    #200 ok表示浏览器请求的页面存在
#                         Bdpagetype: 2
#                         Bdqid: 0xe94f0413007c93a5
#                         Cache-Control: private    #缓存拥有方式：私有
#                         Connection: keep-alive    #链接方式：长连接
#                         Content-Encoding: gzip    #压缩格式
#                         Content-Type: text/html;charset=utf-8    #内容格式：html格式，数据编码：utf8
#                         Date: Wed, 05 Feb 2020 18:13:52 GMT    #服务器当前时间
#                         Expires: Wed, 05 Feb 2020 18:13:52 GMT
#                         Server: BWS/1.1    #服务器名称：百度服务器（一般Apach or Negix）
#                         Set-Cookie: BDSVRTM=297; path=/    #设置cookie值，流程：浏览器访问服务器，服务器会检测请求头中是否有cookie，如果有它会拿来使用（追踪用户），如果没有它会在响应头中的set-Cookie中设置cookie值，浏览器读到set-cookie后，会自动将cookie值保存到缓存中。下一次访问该网站，就会在请求头中携带cookie
#                         Set-Cookie: BD_HOME=1; path=/
#                         Set-Cookie: H_PS_PSSID=1463_21121_26350; path=/; domain=.baidu.com
#                         Strict-Transport-Security: max-age=172800
#                         Traceid: 1580926432058431156216811660413656404901
#                         X-Ua-Compatible: IE=Edge,chrome=1
#                         Transfer-Encoding: chunked
#   5、用网络调试助手，模拟真实服务器，将响应头+html源码发送给浏览器
#       HTTP/1.1 200 OK    #http协议版本    #200 ok表示浏览器请求的页面存在
#                       这个空格很重要，它是header和body的分割行，是为了使浏览器清楚哪部分信息输入header，哪部分输入body，header是告诉浏览器怎么设置，body是浏览器真正展示的内容
#       <h1>太帅了</h1>