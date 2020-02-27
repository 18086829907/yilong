import socket
import re
import os
import multiprocessing


def service_client(new_socket):
    '''为这个客户端返回数据'''
    # 1、接收浏览器发过来的请求，即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024).decode('utf8')
    request_lines = request.splitlines()
    file_name = ''
    res = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if res:
        file_name = res.group(1)
        if file_name == '/':
            file_name = '/index.html'

    # 2、返回http格式的数据，给浏览器
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

    new_socket.close()

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #让服务器绑定的端口可以重复使用，避免服务器先调close时，等待2分钟不释放资源时，不能在用8080这个端口启动服务器
    tcp_server_socket.bind(('127.0.0.1', 8080))
    tcp_server_socket.listen(128)
    while True:
        new_socket, new_addr = tcp_server_socket.accept()
        p = multiprocessing.Process(target=service_client, args=(new_socket,))
        p.start()
        new_socket.close()


if __name__ == '__main__':
    main()