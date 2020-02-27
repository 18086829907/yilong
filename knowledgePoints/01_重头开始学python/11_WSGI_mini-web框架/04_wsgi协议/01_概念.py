# wsgi协议是规定nginx和web框架之间数据通讯的规范

# 规定一：web框架中必须定义一下函数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return 'Hello World'

#说明
#   application函数名是固定的
#   environ是形参，叫啥名都可以，它是用来接收服务器传过来的字典数据
#   start_response是形参，叫啥名都可以，它是用来接收服务器传过来的函数引用
#       start_response()，调用这个函数，目的是将header传给服务器
#   return的内容就是body
#   最终服务器就接收到了header和body，服务器将header和body组装成response，通过tcp传给浏览器
#   浏览器就能看到请求的页面了