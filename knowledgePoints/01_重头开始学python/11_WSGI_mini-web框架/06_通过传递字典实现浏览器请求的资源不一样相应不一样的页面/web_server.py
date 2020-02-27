import socket
import re
import multiprocessing
import time
import mini_frame

class WSGIServer():
    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #让服务器绑定的端口可以重复使用，避免服务器先调close时，等待2分钟不释放资源时，不能在用8080这个端口启动服务器
        self.tcp_server_socket.bind(('127.0.0.1', 8080))
        self.tcp_server_socket.listen(128)
    

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
                f = open('./html' + file_name, 'rb')
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
            body = mini_frame.application(env,self.set_headers)  # 调用逻辑的模块函数

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
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()

if __name__ == '__main__':
    main()