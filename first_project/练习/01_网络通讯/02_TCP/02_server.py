import socket


def main():
    #1、创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #socket.AF_INET：设定ip类型为IPV4；socket.SOCK_STREAM：设定协议为TCP

    #2、绑定本地IP和port
    tcp_server_socket.bind(('127.0.0.1', 8080))

    #3、监听
    tcp_server_socket.listen(128)    #功能：负责等待有新的客户端进行连接    #参数：128：设定最大连接数为128
    print('服务器启动成功......')

    #4、等待连接
    new_forClient_socket, client_address = tcp_server_socket.accept()    #功能：产生新的套接字用来为客户端服务    #返回：是个元组，索引0：新的用来服务客户端的socket对象，索引1：(客户端的ip, port)
    print('已连接的客户端：{}'.format(client_address))

    #5、收信息
    recv_data = new_forClient_socket.recv(1024)    #功能：阻塞程序，等待接收信息
    print('客户端说:{}'.format(recv_data.decode('utf-8')))

    #6、发信息
    data = input('对客户端说：')
    new_forClient_socket.send(data.encode('utf-8'))

    #7、关闭套socket
    tcp_server_socket.close()
    new_forClient_socket.close()


if __name__ == '__main__':
    main()