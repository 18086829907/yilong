import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.2', 8080))

while True:
    data = input('对服务器说：')
    client.send(data.encode('utf-8'))
    info = client.recv(1024).decode('utf-8') #阻塞程序进行，等待接收数据
    print('服务器说：', info)