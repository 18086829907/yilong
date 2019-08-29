import socket
#创建
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定IP和端口
server.bind(('192.168.1.10', 8080)) #本机ip：cmd -> ipconfig -> ipv4地址
#监听
server.listen(5)
print('服务器启动成功......')
#等待连接
clientSocket, clientAddress = server.accept()
print('{}--{} 链接成功'.format(str(clientSocket), clientAddress))
#循环等待接收客户端发送来的数据
while True:
    data = clientSocket.recv(1024) #接收数据1k数据 recv能阻塞程序，等待接收数据
    print('客户端说:{}'.format(data.decode('utf-8')))
    data = input('对客户端说：')
    clientSocket.send(data.encode('utf-8'))

