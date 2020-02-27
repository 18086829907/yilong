import socket


def main():

    #1、创建socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #{gn=实例化套接字，cs={1=ipv4,2=tcp}，fh=实例化对象}

    #2、连接服务器
    serverAddr = ('127.0.0.1', 8080)
    tcp_client_socket.connect(serverAddr)

    while True:
        #3、发信息
        send_data = input('给服务器说：')
        tcp_client_socket.send(send_data.encode('utf8'))

        #4、收信息
        recv_data = tcp_client_socket.recv(1024)
        print('服务端说：{}'.format(recv_data.decode('utf8')))

    #5、关闭socket
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
