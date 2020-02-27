# web框架支持主从的思路
#   让所有的增删改数据库的操作，连接到主服务器中的mysql中进行
#   让所有的查询操作，连接到从服务器的mysql中进行

import urllib.parse
import re
from pymysql import connect

URL_FUNC_DICT = dict()


import logging
logging.basicConfig(
    filename='./log.txt',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(levelname)s - %(message)s'
)



def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route(r'/form\.html\?(.*)')
def save_form(ret, post):
    info = ret.group(1).split('&')
    info_dict = dict()
    for key,value in [i.split('=')  for i in info]:
        info_dict[key] = urllib.parse.unquote(value)

    # 1、连接数据库
    # 2、准备sql语句
    # 3、提交到数据库

    return '已经保存数据：{}'.format(str(info_dict))

@route(r'/form.html')
def show_form(ret, post):
    #1、打开模板
    with open('./templates/form.html', 'r', encoding='utf8') as f:
        content = f.read()

    if post:
        info_dict = dict()
        post = post.split('&')
        for key, value in [i.split('=') for i in post]:
            info_dict[key] = urllib.parse.unquote(value)
        return '已经保存数据：{}'.format(str(info_dict))

    return content


@route(r'/update/(\d+)/(.*)\.html')
def save_update_page(ret, post):
    # 1、获取股票代码和备注信息
    stock_code = ret.group(1)
    note_info = ret.group(2)

    # note_info解码
    note_info = urllib.parse.unquote(note_info)

    # 2、根据股票代码修改focus中对应的note_into
    conn = connect(host='localhost', port=3306, user='root', password='135cylpsx', database='stock_db', charset='utf8')
    cursor = conn.cursor()
    sql = """update focus set note_info=%s where info_id=(select id from info where code=%s);"""
    cursor.execute(sql, [note_info, stock_code])
    conn.commit()
    cursor.close()
    conn.close()

    return '修改成功'

@route(r'/update/(\d+)\.html')
def show_update_page(ret, post):
    # 1、获取股票代码
    stock_code = ret.group(1)

    '''显示修改的页面'''
    # 2、打开模板
    with open('./templates/update.html', 'r', encoding='utf8') as f:
        content = f.read()

    # 3、根据股票代码查询相关的备注信息
    conn = connect(host='192.168.2.105', port=3306, user='slave', password='slave', database='stock_db', charset='utf8')
    cursor = conn.cursor()
    sql = """select f.note_info from focus as f inner join info as i on f.info_id=i.id where i.code=%s;"""
    cursor.execute(sql, [stock_code])
    note_info = cursor.fetchone()[0]  # 获取这支股票对应的备注信息
    cursor.close()
    conn.close()

    if not note_info:
        note_info = 'None'

    content = re.sub(r'\{%content%\}', note_info, content)
    content = re.sub(r'\{%code%\}', stock_code, content)
    return content

@route(r'/del/(\d+)\.html')
def del_focus(ret, post):
    # 1、获取股票代码
    stock_code = ret.group(1)

    # 2、连接数据库
    conn = connect(host='localhost', port=3306, user='root', password='135cylpsx', database='stock_db', charset='utf8')
    cursor = conn.cursor()

    # 3、判断一下info中是否有此股票信息
    sql = """select * from info where code=%s;"""
    cursor.execute(sql, [stock_code])  # 防止sql注入，用列表中的值去填充sql语句中的%s
    if not cursor.fetchone():  # 如果没有这只股票，就认为是非法请求
        cursor.close()
        conn.close()
        return '没有这只股票，大哥，我们是创业公司，请手下留情...'

    # 4、判断是否关注过
    sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.hights,f.note_info from info as i inner join focus as f on i.id = f.info_id where i.code=%s;"""
    cursor.execute(sql, [stock_code])
    if not cursor.fetchone():  # 如果没有值，说明是非法请求
        cursor.close()
        conn.close()
        return '还未关注此股票，不能进行删除此关注'

    # 5、取消关注
    sql = """delete from focus where info_id = (select id from info where code=%s);"""  # 使用insert into value来插入一条从数据库中查出来的数据，不要加value
    cursor.execute(sql, [stock_code])
    conn.commit()

    # 6、关闭连接和游标
    cursor.close()
    conn.close()
    return '取消关注成功'

@route(r'/add/(\d+)\.html')
def add_focus(ret, post):
    # 1、获取股票代码
    stock_code = ret.group(1)

    # 2、连接数据库
    conn = connect(host='localhost', port=3306, user='root', password='135cylpsx', database='stock_db', charset='utf8')
    cursor = conn.cursor()

    # 3、判断一下是否有这个股票代码
    sql = """select * from info where code=%s;"""
    cursor.execute(sql, [stock_code])  # 防止sql注入，用列表中的值去填充sql语句中的%s
    if not cursor.fetchone():  # 如果没有这只股票，就认为是非法请求
        cursor.close()
        conn.close()
        return '没有这只股票，大哥，我们是创业公司，请手下留情...'

    # 4、如果有，判断是否关注过
    sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.hights,f.note_info from info as i inner join focus as f on i.id = f.info_id where i.code=%s;"""
    cursor.execute(sql,[stock_code])
    if cursor.fetchone():  # 如果查出来了，说明已经关注过
        return '已经关注过了，请勿重复关注'

    # 5、添加关注
    sql = """insert into focus(info_id) select id from info where code=%s;"""  # 使用insert into value来插入一条从数据库中查出来的数据，不要加value
    cursor.execute(sql, [stock_code])
    conn.commit()

    # 6、关闭连接和游标
    cursor.close()
    conn.close()
    return '关注成功'

@route('/center.html')
def center(ret, post):
    # 1、打开模板
    with open('./templates/center.html', 'r', encoding='utf8') as f:
        content = f.read()

    # 2、连接数据库
    conn = connect(host='192.168.2.105', port=3306, user='slave', password='slave', database='stock_db', charset='utf8')
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
                <a type='button' class='btn btn-default btn-xs' href='/update/%s.html'><span class='glyphicon glyphicon-star' aria-hidden='true'></span>修改</a>
            </td>
            <td>
                <a href='/del/%s.html' target='_blank'><input type='button' value='删除' id='toDel' name='toDel'></a>
            </td>
        </tr>
    '''

    # 4、插入数据
    html = ''''''
    for line_info in stock_info:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[0],line_info[0])  # 查出来的数据是一个元组，元组的顺序是根据sql语句来决定的，因此在select时一定要参照web前段需要的数据排序进行查询数据

    # 5、插入数据模板
    return re.sub(r'\{%content%\}', html, content)

@route('/index.html')
def index(ret, post):
    #1、打开模板
    with open('./templates/index.html', 'r', encoding='utf8') as f:
        content = f.read()

    #2、连接数据库
    conn = connect(host='192.168.2.105', port=3306, user='slave', password='slave', database='stock_db', charset='utf8')
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
                <a href='/add/%s.html' target='_blank'><input type='button' value='关注' id='toAdd' name='toAdd'></a>
            </td>
        </tr>
    '''

    #4、插入数据
    html = ''''''
    for line_info in stock_info:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[7],line_info[1])

    #5、插入数据模板
    return re.sub(r'\{%content%\}', html, content)

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    try:
        data_post = environ['post']
    except Exception as e:
        data_post = None
    logging.debug('浏览器访问的文件名：%s' % file_name)
    try:
        for url, func in URL_FUNC_DICT.items():
            logging.debug('遍历字典中的key：%s' % url)
            ret = re.match(url, file_name)  # /add/\d+\.html正则能从file_name中匹配到值，则执行对应的函数引用
            if ret:
                return func(ret, data_post) #
        else:  # 等待for循环中所有的if判断完之后，如果所有条件都不符合if，则执行else
            return '请求的url(%s)没有对应的函数...' % file_name
    except Exception as e:
        return '未找到页面：%s' % str(e)
