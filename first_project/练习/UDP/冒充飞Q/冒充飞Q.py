import socket
import time
'''
#给指定ip发送信息
content = input('发送的内容：')
myStr = '1_1bt4_10#32499#002481627512#0#0#0:1289671407:a:b:288:{}'.format(content)
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.connect(('192.168.1.10', 2425))

while True:
    udp.send(myStr.encode('utf-8'))
    time.sleep(1)
'''

#给同网段的所有人发送信息
content = input('发送的内容：')
for i in range(256):
    myStr = '1_1bt4_10#32499#002481627512#0#0#0:1289671407:a:b:288:{}'.format(content)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = '192.168.1.%d' % i
    print(ip)
    udp.connect((ip, 2425))#飞Q的端口是固定的2425
    udp.send(myStr.encode('utf-8'))
    time.sleep(1)