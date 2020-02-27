import socket
import re
import os
import multiprocessing


def sendData(filename, new_serverForClient_socket, new_fromClient_addr):
    if filename == '/':
        filename = '/index.html'
    filePath = os.path.join('.', filename.split(r'/')[-1])
    with open(filePath, 'rb') as f:
        response_body_data = f.read().decode('utf8')
    response_header_data = 'HTTP/1.1 200 ok\r\n'
    if filename == '/404.html':
        response_header_data = 'HTTP/1.1 404 NOT FOUND\r\n'
    response_header_data += '\r\n'    # 头部和体部之间必须要多一个空行，浏览器才有办法分辨头和体部(\r\n的目的是为了让windows的浏览器识别换行，linux和mac只需要\n即可)
    response = response_header_data + response_body_data
    new_serverForClient_socket.send(response.encode('utf8'))
    print('已断开服务器的地址：', new_fromClient_addr)
    new_serverForClient_socket.close()


def receive_and_process_data(new_serverForClient_socket, new_fromClient_addr):
    '''
    接收数据
    :param new_serverForClient_socket:
    :param new_fromClient_addr:
    :return:
    '''
    print('已连接服务器的地址：', new_fromClient_addr)
    header_data = new_serverForClient_socket.recv(1024).decode('utf8')
    if header_data:
        obj_filename = re.match(r'[^/]+(/[^ ]*)', header_data.split('\n')[0])
        if obj_filename:    #预防正则错误
            filename = obj_filename.group(1)
            try:
                sendData(filename, new_serverForClient_socket, new_fromClient_addr)
            except Exception:    #捕捉文件是否正确打开，如果异常，则返回404
                sendData('/404.html', new_serverForClient_socket, new_fromClient_addr)


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #让服务器绑定的端口可以重复使用，避免服务器先调close时，等待2分钟不释放资源时，不能在用8080这个端口启动服务器
    tcp_server_socket.bind(('127.0.0.1', 8080))
    tcp_server_socket.listen(128)
    print('服务器已启动。。。')
    while True:
        new_serverForClient_socket, new_fromClient_addr = tcp_server_socket.accept()
        # receive_and_process_data(new_serverForClient_socket, new_fromClient_addr)
        p = multiprocessing.Process(target=receive_and_process_data, args=(new_serverForClient_socket, new_fromClient_addr))
        p.start()
        new_serverForClient_socket.close()
        # 为什么要在主进程中，先关闭套接字呢？
        # 因为当创建子进程时，套接字对象会被复制一份，
        # 这两个套接字对象都会指向系统底层真正的套接字文件。
        # 如果只关闭子进程中的套接字对象是无法真的关闭套接字文件的。
        # 因为主进程中的套接字对象还指向该套接字文件。
        # 如果没有真的关闭套接字文件，系统是不会给浏览器发送关闭信息的。
        # 如果浏览器没有收到关闭信息，浏览器会一直等待服务器发送数据，即一直打圈等待

if __name__ == '__main__':
    main()