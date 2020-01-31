import socket

def main():
    utp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # utp_socket.bind(('192.168.2.100',8080))
    utp_socket.bind(('127.0.0.1',8081))
    while True:
        data_send = input('输入内容：')
        utp_socket.sendto(data_send.encode('gbk'), ('127.0.0.1', 8080))
        if data_send == 'exct()':
            break
    utp_socket.close()
if __name__ == '__main__':
    main()