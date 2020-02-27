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

@route('/center.html')
def center():
    # 1、打开模板
    with open('./templates/center.html', 'r', encoding='utf8') as f:
        content = f.read()

    # 2、连接数据库
    conn = connect(host='localhost', port=3306, user='root', password='135cylpsx', database='stock_db', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select i.code,i.short,i.chg,i.turnover,i.price,i.hights,f.note_info from info as i inner join focus as f on i.id = f.info_id;')
    stock_info = cursor.fetchall()
    cursor.close()
    conn.close()

    # 3、创建数据模板
    tr_template = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type='button' class='btn btn-default btn-xs' href='/update/300268.html'><span class='glyphicon glyphicon-star' aria-hidden='true'></span>修改</a>
            </td>
            <td>
                <input type='button' value='删除' id='toDel' name='toDel' systemidvaule='300268'>
            </td>
        </tr>
    '''

    # 4、插入数据
    html = ''''''
    for line_info in stock_info:
        html += tr_template % line_info  # 查出来的数据是一个元组，元组的顺序是根据sql语句来决定的，因此在select时一定要参照web前段需要的数据排序进行查询数据

    # 5、插入数据模板
    return re.sub(r'\{%content%\}', html, content)

@route('/index.html')
def index():
    #1、打开模板
    with open('./templates/index.html', 'r', encoding='utf8') as f:
        content = f.read()

    #2、连接数据库
    conn = connect(host='localhost', port=3306, user='root', password='135cylpsx', database='stock_db', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from info')
    stock_info = cursor.fetchall()
    cursor.close()
    conn.close()

    #3、创建数据模板
    tr_template = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type='button' value='添加' id='toAdd' name='toAdd' systemidvaule='000007'>
            </td>
        </tr>
    '''

    #4、插入数据
    html = ''''''
    for line_info in stock_info:
        html += tr_template % line_info

    #5、插入数据模板
    return re.sub(r'\{%content%\}', html, content)

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    try:
        return URL_FUNC_DICT[file_name]()
    except Exception as e:
        return '未找到页面：%s' % str(e)
