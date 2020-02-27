'''
URL_FUNC_DICT = {
    './index.py' = index,
    './login.py' = login
}
'''

URL_FUNC_DICT = dict()

def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func  # URL_FUNC_DICT['./index.py'] = index
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func  # 织里会将闭包内部函数返回给原函数之前用的的变量名，如果手动调那个变量，才会执行call_func()，如果不调怎不会执行call_func()
    return set_func

@route('/login.py')  # 1、执行route('./login.py')，2、返回的set_func来装饰login函数，即login = set_func(login)。注意：此时call_func函数中就能使用装饰器传参以及原函数引用来生成字典了
def login():
    return '欢迎来到login'

@route('/index.py')
def index():
    with open('./templates/index.html', 'r', encoding='utf8') as f:
        return f.read()

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    try:
        return URL_FUNC_DICT[file_name]()  # 去执行字典中取出的对应file_name的函数名，最后返回函数的返回值给服务器，服务器最后返回给浏览器
    except Exception as e:
        return '未找到页面：%s' % str(e)  # 将异常范围到web_server,它再将异常返回给浏览器

#总结：
#   用装饰器，装完一个函数，URL_FUNC_DICT字典中就多一对键值对，key是装饰器传参，value是被装饰函数的引用
#   用带参装饰器可以生成{'带参':被装饰函数引用}

#执行流程
#   8行：定义一个空字典
#   18行：执行route('./login.py'),此时url='./login.py',16行返回闭包set_func
#   18行：执行login = set_func(login),此时func=原函数的引用
#   12行：给字典赋值：URL_FUNC_DICT = {'./login.py':login原函数的引用}
#   22行：按照上面的流程，走一遍，同样能给URL_FUNC_DICT中添加一对键值对
#   当web_server调用application时
#   27行：执行application(environ,start_response)
#   28行：start_response是web_server中的函数引用，将状态码和响应头传入web_server中的函数，并保存起来，拼接成响应头
#   29行：web_server传入了一个字典，字典中包含了浏览器需要访问文件的路径，取出路径赋值给变量
#   31行：以需要访问文件路径作为key，从字典中取出对应的函数引用，执行这个函数，最后返回这个函数的返回值
#       此时web_server就收到了响应头和响应体，将它们拼接后返回给浏览器。浏览器就能看到页面了

#路由
#   针对不同需求，能指挥调用不同函数的功能叫做路由
#   在代码31行体现，return URL_FUNC_DICT[file_name]()，来了一个file_name就指挥调用对应file_name的函数引用