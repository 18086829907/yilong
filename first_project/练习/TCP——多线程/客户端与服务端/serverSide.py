import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.2', 8080)) #本机ip：cmd -> ipconfig -> ipv4地址
server.listen(5)
print('服务器开启成功，等待客户端的链接')

def run(clientSocket, clientAddress):
    data = clientSocket.recv(1024)
    print('客户端{}说:{}'.format(clientAddress, data.decode('utf-8')))
    clientSocket.send('网页主页HTML'.encode('utf-8'))


while True:
    clientSocket, clientAddress = server.accept()
    print('{}--{} 链接成功'.format(str(clientSocket), clientAddress))
    t1 = threading.Thread(target=run, args=(clientSocket, clientAddress))
    t1.start()



