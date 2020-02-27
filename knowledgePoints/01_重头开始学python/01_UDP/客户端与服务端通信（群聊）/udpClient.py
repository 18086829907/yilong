import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('', 8080))

while True:
    data = input('对服务端说：')
    client.sendto(data.encode('utf-8'), ('192.168.1.10', 8080)) #参数1：说什么，参数2：给谁说
