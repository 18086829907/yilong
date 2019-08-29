import tkinter
import threading
import socket

#192.168.1.4
users = {}
def signalRun(clientSocket, clientAddress):
    userName = clientSocket.recv(1024).decode('utf-8')
    users[userName] = clientSocket #保存客户端发送过来的用户名和该客户端的客户端对象
    while True:
        mail = clientSocket.recv(2014) #阻塞程序等待接收消息
        mailStr = mail.decode('utf-8') #dataStr = justin : you are very good!
        mailList = mailStr.split(',')
        users[mailList[0]].send(mailList[1].encode('utf-8')) #users[mailList[0]] = suers[friendUserName] = friendUserClient

def startServer():
    ipStr = eIp.get()
    portStr = ePort.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    server.listen(10)
    printStr = '服务器{ipStr}启动成功\n'
    text.insert(tkinter.END, printStr)
    while True:
        clientSocket, clientAddress = server.accept() #会有多个用户连接服务器，因此需要用多线程启动多个服务器对象
        t = threading.Thread(target=signalRun, args=(clientSocket, clientAddress))
        t.start()

def start():
    serverStarting = threading.Thread(target=startServer)
    serverStarting.start()


if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('乖萌宝贝服务端')
    win.geometry('250x100+450+400')
    #ip标签
    labelIp = tkinter.Label(win, text='ip')
    labelIp.grid(row=0, column=0)
    #ip输入窗口
    eIp = tkinter.Variable()
    entryIp = tkinter.Entry(win, textvariable=eIp)
    entryIp.grid(row=0, column=1)
    #端口标签
    labelPort = tkinter.Label(win, text='port')
    labelPort.grid(row=1, column=0)
    #端口输入窗口
    ePort = tkinter.Variable()
    entryPort = tkinter.Entry(win, textvariable=ePort)
    entryPort.grid(row=1, column=1)
    #启动按钮
    buttonStart = tkinter.Button(win, text='启动', command=start)
    buttonStart.grid(row=2, column=0)
    #文本显示窗口
    text = tkinter.Text(win, width=20, height=1) #注：height显示的行数
    text.grid(row=2, column=1)
    win.mainloop()