import socket
import tkinter
import threading

ck = None
def getMail():
    while True:
        mail = ck.recv(1024).decode('utf-8')
        textLinkDialog .insert(tkinter.END, mail)

def connectServer():
    global ck
    ipStr = eIp.get()
    portStr = ePort.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr, int(portStr)))
    printStr = '服务器{}链接成功\n'.format(ipStr)
    textLinkDialog .insert(tkinter.END, printStr)
    userName = eUser.get()
    client.send(userName.encode('utf-8'))
    ck = client
    #等待接收数据
    t = threading.Thread(target=getMail)
    t.start()

def sendMail():
    #点击发送按钮启动此函数代码
    friendUserName = efriendUserName.get()
    sendStr = eSend.get()
    userName = eUser.get()
    sendStr = friendUserName + ',' + userName + '说:' + sendStr + '\n' #发送给朋友的信息内容
    ck.send(sendStr.encode('utf-8'))

if __name__ == '__main__':
    #主窗口
    win = tkinter.Tk()
    win.title('乖萌宝贝客户端')
    win.geometry('250x200+400+200')
    #用户名标签
    labelUser = tkinter.Label(win, text='userName')
    labelUser.grid(row=0, column=0)
    #用户名输入窗口
    eUser = tkinter.Variable()
    entryUser = tkinter.Entry(win, textvariable=eUser)
    entryUser.grid(row=0, column=1)
    #ip标签
    labelIp = tkinter.Label(win, text='Ip')
    labelIp.grid(row=1, column=0)
    #ip输入窗口
    eIp = tkinter.Variable()
    entryIp = tkinter.Entry(win, textvariable=eIp)
    entryIp.grid(row=1, column=1)
    #端口标签
    labelPort = tkinter.Label(win, text='Port')
    labelPort.grid(row=2, column=0)
    #端口输入窗口
    ePort = tkinter.Variable()
    entryPort = tkinter.Entry(win, textvariable=ePort)
    entryPort.grid(row=2, column=1)
    #链接按钮
    buttonLink = tkinter.Button(win, text='连接', command=connectServer)
    buttonLink.grid(row=3, column=0)
    #链接文本
    textLinkDialog  = tkinter.Text(win, height=5, width=20)
    textLinkDialog .grid(row=3, column=1)
    #朋友用户名标签
    labelFriendUserName = tkinter.Label(win, text='friendUserName')
    labelFriendUserName.grid(row=4, column=0)
    #朋友用户名输入窗口
    efriendUserName = tkinter.Variable()
    entryFriendUserName = tkinter.Entry(win, textvariable=efriendUserName)
    entryFriendUserName.grid(row=4, column=1)
    #发送按钮
    buttonSend = tkinter.Button(win, text='发送', command=sendMail)
    buttonSend.grid(row=5, column=0)
    #发送输入窗口
    eSend = tkinter.Variable()
    entrySend = tkinter.Entry(win, textvariable=eSend)
    entrySend.grid(row=5, column=1)

    win.mainloop()