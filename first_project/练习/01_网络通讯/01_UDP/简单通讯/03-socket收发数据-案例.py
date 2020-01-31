import socket


def main():

    utp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    utp_socket.bind(('',8080))
    while True:
        utp_socket.sendto('123123'.encode('gbk'), ('192.168.1.1',8080))
        utp_socket.recvfrom(1024)
        ctrlProgram = input('是否退出')
        if ctrlProgram == 'exit' :
            break
    utp_socket.close()


if __name__ == '__main__':
    main()