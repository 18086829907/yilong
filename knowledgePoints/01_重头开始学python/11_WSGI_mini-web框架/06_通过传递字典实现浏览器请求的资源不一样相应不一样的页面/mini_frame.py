
def login():
    return '欢迎来到login'

def index():
    return '欢迎来到index'

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    if file_name == '/index.py':
        return index()
    elif file_name == '/login.py':
        return login()
    else:
        return 'Hello World 我爱你中国'