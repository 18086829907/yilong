def login():
    return '欢迎来到login'

def index():
    with open('./templates/index.html', 'r', encoding='utf8') as f:  # 注意：启动服务器命令-python3 web服务器.py。那工作路径默认定位到web服务器.py所在路径，即web服务器.py的所在路径下才有templates文件夹
        return f.read()

#自己手动组装字典
URL_FUNC_DICT = {
    '/index.py':index,
    '/login.py':login
}

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    return URL_FUNC_DICT[file_name]()  # 去执行字典中取出的对应file_name的函数名，最后返回函数的返回值给服务器，服务器最后返回给浏览器
