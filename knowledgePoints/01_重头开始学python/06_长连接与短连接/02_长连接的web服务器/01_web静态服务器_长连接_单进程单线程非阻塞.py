import socket
import re
import os


def service_client(new_socket, request):
    # 1、正则提取需要的访问的资源路径并拼接为本地路径
    obj = re.match(r'[^/]+/([^ ]*)', request.splitlines()[0])
    fileName = ''  # 定义全局变量
    if obj:
        fileName = obj.group(1)
        if fileName == '/':
            fileName = 'index.html'
    # 2、打开资源读取资源
    filePath = os.path.join('./', fileName)
    try:
        with open(filePath, 'rb') as f:
            response_body = f.read()
    except Exception as e:
        with open('./404.html', 'rb') as f:
            response_body = f.read()
            response_headers = 'HTTP/1.1 404 NOT FOUND\r\n'
            response_headers += 'Content-Length:{}\r\n'.format(len(response_body))
            response_headers += '\r\n'
            Rsponse = response_headers.encode('utf8') + response_body
            new_socket.send(Rsponse)
    else:
        # 3、将头和体拼接成Response
        response_headers = 'HTTP/1.1 200 ok\r\n'
        response_headers += 'Content-Length:{}\r\n'.format(len(response_body))  # Content-Length记录body的字符长度，起到告知浏览器发送的数据已经发送完毕的作用
        response_headers += '\r\n'
        Rsponse = response_headers.encode('utf8') + response_body
        # 4、发送会客户端
        new_socket.send(Rsponse)


def main():
    # 1、创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、非阻塞
    tcp_socket.setblocking(False)
    # 3、绑定
    tcp_socket.bind(('',8080))
    # 4、监听
    tcp_socket.listen(128)
    # 5、被动
    socket_list = list()
    while True:
        try:
            new_socket, new_addr = tcp_socket.accept()
            # 1、非阻塞
            new_socket.setblocking(False)
            # 2、添加到列表
            socket_list.append(new_socket)
        except Exception as e:
            pass

        for new_socket in socket_list:
            try:
                recv_data = new_socket.recv(1024).decode('utf8')
            except Exception as e:
                pass
            else:
                if recv_data:
                    service_client(new_socket, recv_data)
                else:
                    new_socket.close()
                    socket_list.remove(new_socket)

if __name__ == '__main__':
    main()
