from myClass.myServer import MyServer
from myClass.myTkinter import MyTkinter
from myClass.regularExpression import RegularExpression
import socket

def startServer():
    re = RegularExpression()
    entryInfo1 = mytk.getEntry(eIp)
    entryInfo2 = mytk.getEntry(ePort)
    if re.checkIp(entryInfo1):
        server = MyServer(entryInfo1, int(entryInfo2), 5) #ip, port, listen
        server.connectThreadting()
        mytk.insertText('服务器{}\n启动成功...\n'.format(entryInfo1))
    else:
        print('place input True ip')

if __name__=='__main__':
    mytk = MyTkinter('server', '300x300+200+200')
    frame1 = mytk.frame(mytk.win, 'pack', side=mytk.top)
    frame2 = mytk.frame(mytk.win, 'pack', side=mytk.bottom)
    mytk.lable(frame1, 'ip', 'grid', row=0, column=0)
    eIp = mytk.entry(frame1, 'grid', row=0, column=1)
    eIp.set(socket.gethostbyname(socket.gethostname()))
    mytk.lable(frame1, 'port', 'grid', row=1, column=0)
    ePort = mytk.entry(frame1, 'grid', row=1, column=1)
    ePort.set(8080)
    mytk.text(frame2, 25, 10, 'pack', side=mytk.top)
    mytk.button(frame2, '启动', 'pack', side=mytk.bottom, command=startServer)
    mytk.mainloop()