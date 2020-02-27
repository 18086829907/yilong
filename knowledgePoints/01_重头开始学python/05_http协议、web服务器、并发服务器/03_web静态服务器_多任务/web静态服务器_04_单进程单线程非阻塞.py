import socket
import time

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setblocking(False)    #将tcp_socket设置为非阻塞套接字
    tcp_socket.bind(('',8080))
    tcp_socket.listen(128)


    new_socket_list = list()
    while True:
        try:
            new_socket, new_addr = tcp_socket.accept()
            new_socket.setblocking(False)    #将new_socket设为非阻塞套接字
        except Exception as e:
            print('\r没有客户端连接', end='')
        else:
            new_socket_list.append(new_socket)

        for new_socket in new_socket_list:
            try:
                recv_data = new_socket.recv(1024).decode('utf8')
            except Exception as e:
                print('\r客户端还未发送数据', end='')
            else:
                if recv_data:
                    # 客户端发回数据
                    print(recv_data)    #这样就用单进程单线程非阻塞实现了能服务多个客户端的静态服务器
                else:
                    # 客户端调用close()，导致recv返回
                    new_socket.close()
                    new_socket_list.remove(new_socket)


if __name__ == '__main__':
    main()