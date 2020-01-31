import socket

def main():
    utp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    utp_socket.bind(('127.0.0.1',8082))
    while True:
        data = utp_socket.recvfrom(1024)
        print('内容：'+data[0].decode('gbk'))
        print('发送者的ip'+data[1][0],'发送者的端口'+str(data[1][1]))
if __name__ == '__main__':
    main()