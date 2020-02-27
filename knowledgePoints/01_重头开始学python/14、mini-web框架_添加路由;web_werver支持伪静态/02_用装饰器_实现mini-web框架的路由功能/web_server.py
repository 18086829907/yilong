import sys
import socket
import re
import multiprocessing

#python3 demp.py 7890 mini_frame:application

class WSGIServer():
    def __init__(self, port, app, static_path):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #让服务器绑定的端口可以重复使用，避免服务器先调close时，等待2分钟不释放资源时，不能在用8080这个端口启动服务器
        self.tcp_server_socket.bind(('192.168.2.103', port))
        self.tcp_server_socket.listen(128)
        self.application = app
        self.static_path = static_path

    def service_client(self, new_socket):
        '''为这个客户端返回数据'''
        # 1、接收浏览器发过来的请求，即http请求
        # GET / HTTP/1.1
        request = new_socket.recv(1024).decode('utf8')
        request_lines = request.splitlines()
        file_name = ''
        res = ''
        try:
            res = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
        except Exception as e:
            pass
        if res:
            file_name = res.group(1)
            if file_name == '/':
                file_name = '/index.html'

        # 2、返回http格式的数据，给浏览器
        if not file_name.endswith('.py'):  # 请求的文件名如果不是以.py结尾，则表示请求的是静态资源（html,css,js,png,jpg）
            try:
                f = open(self.static_path + file_name, 'rb')
            except:
                response = 'HTTP/1.1 404 NOT FOUND\r\n'
                response += '\r\n'
                response += '-----file not found-----'
                new_socket.send(response.encode('utf8'))
            else:
                html_content = f.read()
                f.close()
                response = 'HTTP/1.1 200 OK\r\n'
                response += '\r\n'

                new_socket.send(response.encode('utf8'))
                new_socket.send(html_content)
        else:  #如果是以.py，则执行动态请求
            env = dict()
            env['PATH_INFO'] = file_name
            body = self.application(env,self.set_headers)  # 调用逻辑的模块函数

            header = 'HTTP/1.1 %s\r\n' % self.status
            for temp in self.headers:
                header += '%s:%s\r\n' % (temp[0], temp[1])
            header += '\r\n'

            response = header + body
            new_socket.send(response.encode('utf8'))
        new_socket.close()

    def set_headers(self, status, headers):
        self.status = status
        self.headers = [('server', 'mini_web v1.0')]
        self.headers += headers

    def run_forever(self):
        while True:
            new_socket, new_addr = self.tcp_server_socket.accept()
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()

def main():
    if len(sys.argv) == 3:  # sys.argv是一个列表，里面存储了指向程序时，所传的参数，比如python3 web_server.py 8080。sys.argv == [web_server.py, 8080]
        try:
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]
        except Exception as e:
            print('端口错误！')
            return
    else:
        print('请按以下方式执行server')
        print('python web_server.py 8080 mini_frame:application')
        return

    res = re.match(r'([^:]+):(.*)', frame_app_name)
    if res:
        frame_name = res.group(1)  # mini_frame
        app_name = res.group(2)  # application
    else:
        print('请按以下方式执行server')
        print('python web_server.py 8080 mini_frame:application')
        return

    with open('./web_server.conf', 'r') as f:
        conf_info = eval(f.read())  # eval剥离字符串的最外层的'号，
    # confi_info此时为字典，数据为
    # {
    #     'static_path': './static',
    #     'dynamic_path': './dynamic'
    # }


    # 加载包路径
    # 加载模块
    # 加载模块函数
    sys.path.append(conf_info['dynamic_path'])  # 将当前工作目录中的dynamic文件包加载到模块搜索路径（sys.path），即导入模块时会到dynamic包中去寻找模块
    frame = __import__(frame_name)  # __import__可以导入指向模块名字符串的变量名，它的返回值就是要导入的模块的对象
    app = getattr(frame, app_name)  # getattr()，从mini_frame模块中获得application函数，并用app变量指向这个函数，即app指向模块mini_frame（框架）中的application函数



    wsgi_server = WSGIServer(port, app, conf_info['static_path'])
    wsgi_server.run_forever()

if __name__ == '__main__':
    main()