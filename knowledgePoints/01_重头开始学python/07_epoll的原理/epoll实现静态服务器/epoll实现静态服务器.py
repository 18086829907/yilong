import socket
import re
import os
import select


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
            response_headers = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
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
    # 5、创建epoll对象
    epl = select.epoll()  # epoll对象指向特殊内存空间
    # 6、将监听套接字对应的fd注册到epoll中
    epl.register(tcp_socket.fileno(), select.EPOLLIN)  # .fileno，可以得到tcp_socket在系统中的实际文件  # select.EPOLLIN参数表示检测tcp_socket文件有数据写入的事件名

    fd_event_dict = dict()
    while True:
        fd_event_list = epl.poll()  # 默认会阻塞，直到os检测数据到来，通过事件通知方式，告知程序，此时解阻塞，返回一个列表
        #fd_event_list内是元组：[(fd, event),('套接字对应的文件描述符', '这个文件描述符可以触发的事件——可以调用recv接收、可以调用send发送等')]
        for fd, event in fd_event_list:
            if fd == tcp_socket.fileno():
                new_socket, new_addr = tcp_socket.accept()
                fd_event_dict[new_socket.fileno()] = new_socket  # 将文件描述符和socket对象保存到字典
                epl.register(new_socket.fileno(), select.EPOLLIN)
            elif event == select.EPOLLIN:  # 判断已经连接的客户端是否有数据发送过来
                new_socket = fd_event_dict[fd]
                recv_data = new_socket.recv(1024).decode('utf8')
                if recv_data:
                    service_client(new_socket, recv_data)
                else:
                    new_socket.close()  # 关闭套接字
                    epl.unregister(fd)  # 将该套接字的文件描述符从epl中注销
                    del fd_event_dict[fd]  # 删除字典中的fd和套接字


if __name__ == '__main__':
    main()
