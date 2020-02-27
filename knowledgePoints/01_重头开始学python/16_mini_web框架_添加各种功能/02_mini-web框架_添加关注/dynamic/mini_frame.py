# 添加关注的逻辑
#   数据库中有两个表，一个info，存储所有的股票信息，一个focus，focus.note_info存储的是对一只股票的备注信息，focus.info_id存储的是一只股票的id，它是外键，实质保存的是info表的主键
#   用户的center界面中显示的是，focus.info_id和info.id相同时的交集
#       只要有交集就显示到center界面中，即表示该用户关注过这支股票
#   关注的本质，就是将一只股票的code对应的id保存到focus.info_id中，将来一取focus.info_id和info.id相同的交集时，就能查出这支股票的信息，即表示已经关注了此股票
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

@route(r'/add/(\d+)\.html')
def add_focus(ret):
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

    # 4、判断是否关注过
    sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.hights,f.note_info from info as i inner join focus as f on i.id = f.info_id where i.code=%s;"""
    cursor.execute(sql,[stock_code])
    if cursor.fetchone():  # 如果查出来了，说明已经关注过
        cursor.close()
        conn.close()
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
def center(ret):
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
def index(ret):
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
                <a href='/add/%s.html' target='_blank'><input type='button' value='添加' id='toAdd' name='toAdd'></a>
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
    print(file_name)
    try:
        for url, func in URL_FUNC_DICT.items():
            print(url)
            ret = re.match(url, file_name)  # /add/\d+\.html正则能从file_name中匹配到值，则执行对应的函数引用
            if ret:
                return func(ret)
        else:  # 等待for循环中所有的if判断完之后，如果所有条件都不符合if，则执行else
            return '请求的url(%s)没有对应的函数...' % file_name
    except Exception as e:
        return '未找到页面：%s' % str(e)
