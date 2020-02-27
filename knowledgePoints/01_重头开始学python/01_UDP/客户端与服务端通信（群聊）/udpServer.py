import socket
udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(('192.168.1.10', 8080))#有时候端口被占用会导致无法启动服务器，换一个端口即可
print('服务器启动成功......')
while True:
    data, addr = udpServer.recvfrom(1024)#从哪里接收的信息(1k)
    print('客户端说：%s' % data.decode('utf-8'))
