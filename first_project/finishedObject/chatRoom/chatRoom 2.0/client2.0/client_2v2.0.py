import tkinter
import socket
import threading
import re

ck = None

def connectServer():
    global ck
    # 获取ip、port、user值
    ipStr = eIp.get()
    portStr = ePort.get()
    userStr = eUser.get()
    # 链接服务器
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((ipStr, int(portStr)))
    printStr = '服务器{}链接成功\n'.format(ipStr)
    # 添加界面窗口显示内容
    textLogin.insert(tkinter.END, printStr)
    lbUsers.insert(tkinter.END, (userStr + '(自己)'))
    # 发送用户名信息
    clientSocket.send(userStr.encode('utf-8'))
    # 定义全局变量
    ck = clientSocket
    # 等待服务器返回信息
    while True:
        #更新listBox信息
        strListAllUserName = clientSocket.recv(1024).decode('utf-8') #等待接收allUserName
        if '说' not in strListAllUserName:
            lbUsers.delete(0, lbUsers.size())
            userList = re.findall('\w+', strListAllUserName)
            for i in userList:
                if i == eUser.get():
                    lbUsers.insert(tkinter.ACTIVE, (i + '(自己)'))
                else:
                    lbUsers.insert(tkinter.END, i)
        else:
            textChat.insert(tkinter.END, strListAllUserName)


def connectServerThreading():
    t = threading.Thread(target=connectServer)
    t.start()

def getFriendUserName(event):
    global friendUserName
    friendUserName = lbUsers.get(lbUsers.curselection())

def sendMail():
    sendStr = friendUserName + ',' + eUser.get() + '说:' + eSend.get() + '\n'
    ck.send(sendStr.encode('utf-8'))

def sendMailThreading():
    t = threading.Thread(target=sendMail())
    t.start()

if __name__ == '__main__':
    #创建tk主窗口
    win = tkinter.Tk()
    win.title('客户端')
    win.geometry('800x400+400+200')
    #创建登录frame
    frmUserSign = tkinter.Frame(win)
    frmUserSign.pack(side=tkinter.LEFT, fill=tkinter.Y)
    #创建用户名frame
    frmUser = tkinter.Frame(frmUserSign)
    frmUser.pack(side=tkinter.LEFT, fill=tkinter.Y)
    #创建用户名列表
    elb = tkinter.StringVar()
    lbUsers = tkinter.Listbox(frmUser, selectmode=tkinter.BROWSE, listvariable=elb)
    lbUsers.pack(side=tkinter.LEFT, fill=tkinter.Y)
    lbUsers.bind('<Double-Button-1>', getFriendUserName)

    #创建登录frame
    frmSign = tkinter.Frame(frmUserSign)
    frmSign.pack(side=tkinter.RIGHT, fill=tkinter.Y)


    frmIpPortUser = tkinter.Frame(frmSign)
    frmIpPortUser.pack(side=tkinter.TOP, fill=tkinter.X)

    labelIp = tkinter.Label(frmIpPortUser, text='ip')
    labelIp.grid(row=0, column=0)

    eIp = tkinter.Variable()
    entryIp = tkinter.Entry(frmIpPortUser, textvariable=eIp)
    entryIp.grid(row=0, column=1)

    labelPort = tkinter.Label(frmIpPortUser, text='port')
    labelPort.grid(row=1, column=0)

    ePort = tkinter.Variable()
    entryPort = tkinter.Entry(frmIpPortUser, textvariable=ePort)
    entryPort.grid(row=1, column=1)

    labelUser = tkinter.Label(frmIpPortUser, text='user')
    labelUser.grid(row=2, column=0)

    eUser = tkinter.Variable()
    entryUser = tkinter.Entry(frmIpPortUser, textvariable=eUser)
    entryUser.grid(row=2, column=1)

    buttonLogin = tkinter.Button(frmIpPortUser, text='登陆', command=connectServerThreading)
    buttonLogin.grid(row=3, column=0)

    textLogin = tkinter.Text(frmIpPortUser, width=20, height=1)
    textLogin.grid(row=3, column=1)

    frmLogin = tkinter.Frame(frmSign)
    frmLogin.pack()

    frmChatRoom = tkinter.Frame(win)
    frmChatRoom.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    frmChat = tkinter.Frame(frmChatRoom)
    frmChat.pack(side=tkinter.TOP, fill=tkinter.X)

    textChat = tkinter.Text(frmChat, width=50, height=20)
    textChat.pack()

    frmSend = tkinter.Frame(frmChatRoom)
    frmSend.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    eSend = tkinter.Variable()
    entrySend = tkinter.Entry(frmSend, textvariable=eSend)
    entrySend.pack(side=tkinter.TOP, fill=tkinter.X)

    buttonSend = tkinter.Button(frmSend, text='发送', command=sendMailThreading)
    buttonSend.pack(side=tkinter.BOTTOM)

    win.mainloop()