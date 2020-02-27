def login():
    return '欢迎来到login'

def index():
    with open('./templates/index.html', 'r', encoding='utf8') as f:  # 注意：启动服务器命令-python3 web服务器.py。那工作路径默认定位到web服务器.py所在路径，即web服务器.py的所在路径下才有templates文件夹
        return f.read()

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    if file_name == '/index.py':
        return index()
    elif file_name == '/login.py':
        return login()
    else:
        return 'Hello World 我爱你中国'