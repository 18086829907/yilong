import re
from pymysql import connect

URL_FUNC_DICT = dict()

def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route('/login.html')
def login():
    return '欢迎来到login'

@route('/index.html')
def index():
    with open('./templates/index.html', 'r', encoding='utf8') as f:
        content = f.read()
    conn = connect(host='localhost', port=3306, user='root', password='135cylpsx', database='stock_db', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from info')
    stock_info = cursor.fetchall()
    print(stock_info)
    cursor.close()
    conn.close()
    return re.sub('%\d+','a', content)

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    try:
        return URL_FUNC_DICT[file_name]()
    except Exception as e:
        return '未找到页面：%s' % str(e)
