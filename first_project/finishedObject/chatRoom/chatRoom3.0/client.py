from myClass.myClient import MyClient
from myClass.myTkinter import MyTkinter
from myClass.myRedis import MyRedis
myClient=None
myRedis = MyRedis('135cylpsx4848@')
import time
import socket
def connectServer():
    global myClient
    entryInfo1 = eIp.get()
    entryInfo2 = ePort.get()
    mytk.insertText('服务器{}\n连接成功...\n'.format(entryInfo1))
    myClient = MyClient(entryInfo1, int(entryInfo2))
    myClient.connectThreading()

def register():
    userName = eUN.get()
    passWord = ePW.get()
    myClient.sendRegister(userName, passWord)
    time.sleep(0.1)
    mail = myRedis.get('result')
    mytk.insertText(mail)

def signIn():
    global myRedis
    userName = eUN.get()
    passWord = ePW.get()
    myClient.sendSignIn(userName, passWord)
    time.sleep(0.1)
    mail = myRedis.get('result')
    mytk.insertText(mail)

if __name__=='__main__':
    mytk = MyTkinter('client', '500x400+200+200')
    frame1 = mytk.frame(mytk.win, 'pack', side=mytk.left, fill=mytk.y)
    frame2 = mytk.frame(mytk.win, 'pack', side=mytk.right, fill=mytk.y)
    frame3 = mytk.frame(frame1, 'pack', side=mytk.top)
    frame4 = mytk.frame(frame1, 'pack', side=mytk.bottom)
    mytk.lable(frame3, 'ip', 'grid', row=0, column=0)
    eIp = mytk.entry(frame3, 'grid', row=0, column=1)
    eIp.set(socket.gethostbyname(socket.gethostname()))
    mytk.lable(frame3, 'port', 'grid', row=1, column=0)
    ePort = mytk.entry(frame3, 'grid', row=1, column=1)
    ePort.set(8080)
    mytk.button(frame3, '连接', 'grid', row=2, column=0, command=connectServer)
    mytk.lable(frame4, 'userName', 'grid', row=0, column=0)
    eUN = mytk.entry(frame4, 'grid', row=0, column=1)
    mytk.lable(frame4, 'passWord', 'grid', row=1, column=0)
    ePW = mytk.entry(frame4, 'grid', row=1, column=1)
    mytk.button(frame4, '登录', 'grid', row=2, column=0, command=signIn)
    mytk.button(frame4, '注册', 'grid', row=2, column=1, command=register)
    mytk.text(frame2, 40, 50, 'pack', side=mytk.top, fill=mytk.y)
    mytk.mainloop()


