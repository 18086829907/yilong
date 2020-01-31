#【书写】
#习惯：函数与函数之间，隔两个空行

#【ip、端口】
#   概念
#       ip用于识别数据传输的目标电脑
#       端口用于识别数据传输的目标软件
#   描述
#       ip精准传输数据
#           本机 - 路由 - 交换机 - 路由1-（电脑1，电脑2（10.3.5.4））、路由2-（电脑3，电脑4）、路由3-（电脑5，电脑6）
#           数据包【10.3.5.4】
#                         ？选择路由1、路由2、路由3？，ip地址指路
#                                  ？选择电脑1，电脑2？，ip地址指路
#                                                 ？选择qq、微信？，端口指路
#       ip+端口精准传输数
#           电脑1（10.1.3.4）
#               qq（100）
#                   发送数据包：【10.3.5.4:100，数据】
#                       注意：包头信息包括，对方电脑的ip地址，以及对方电脑qq软件的100号端口
#           电脑2（10.3.5.4）
#               qq（100）
#                   通过分析数据包头的ip地址和端口，才能准确的将信息接收到qq软件，而不是微信
#               微信（101）
#   知名端口（已经被占用）
#       范围：0-1023
#   动态端口（自己可以随意占用）
#       范围：1024-65535


#【udp】使用socket，实现udp通讯
#创建socket
#   导入模块：import socket
#       类：socket.socket()
#           功能：创建socket对象，即初始化socket类对象
#           语法：socket.socket(AddressFamily, Type)
#           参数
#               参数1(确定使用IPV4还是IPV6)
#                   socket.AF_INET    #IPV4
#               参数2：(确定创建TCP还是UDP)
#                   socket.SOCK_DGRAM    #UDP
#           返回：socket对象
#           实例：UDP_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#       实例化对象调用函数
#           s.sendto()
#               功能：给指定ip和端口的电脑发送信息
#               语法：s.sendto(bytes, (ip_str,端口_int))
#               参数
#                   参数1（bytes）
#                       说明
#                           要发送的内容
#                           内容的编码为bytes
#                           string转bytes："字符串".encode('gbk')
#                   参数2（(ip_str,端口_int)）
#                       说明：一个元组，0：对方电脑的ip字符串，1：端口号，类型为int
#               实例:s.sendto('我饿了'.encode('gbk'), ('192.168.70.1', 8080))
#           s.bind()
#               功能：给s实例化对象绑定固定的ip和端口，绑定固定ip和端口后才能接收信息
#               语法：s.bind((ip_str,端口_int))
#               参数：一个元组，0：本机的ip字符串，1：端口号，类型为int
#               实例：s.bind(('192.168.70.134',8080))
#               注意：ip为空字符串时，默认绑定本机ip，即s.bind(('',8080))
#           s.recvfrom()
#               功能：接收信息
#               语法：s.recvfrom(data_max)
#               参数：接收数据的最大值，超过指定大小的数据不接收，数据类型为int
#               实例：data = s.recvfrom(1024)
#               返回
#                   一个元组
#                   0：bytes类型的数据内容，需要decode('gbk')，可以保存在变量中进行打印
#                   1：（对方ip,对方端口号）
#           s.close()
#               功能：socket实例调用close函数，可以关闭socket实例
#udp流程总结
#   发送数据流程
#       创建socket对象（实例化）
#       发送数据
#       关闭socket对象
#   接收数据流程
#       创建socket对象
#       绑定本机ip及端口
#       接收数据
#       关闭socket对象
#注意问题
#   如果给windows系统发信息，需要用gbk编码
#   除windows之外的系统之间通讯，用utf8编码
#   收发的信息，需要统一编码和解码——'gbk'or'utf8'
#   两台电脑的ip不能相同，一台电脑中不同的程序端口不能相同
#   一个socket对象能同时收发信息


#【tcp】使用socket，实现tcp通讯
#tcp、udp区别
#   udp想象为写信，信件有可能丢失，丢失后，发信方不知道收信方没有收到信
#   tcp想象为打电话，数据更安全更稳定。
#       可靠传输机制
#           采用发送应答机制
#               a发送数据到b，b收到数据后会告诉a已经收到数据，完成这次数据发送
#           超时重传
#               如果a在一定时间内没有收到b发送的签收消息，则会重新发送数据
#           错误校验
#               根据清单，检测数据包内容，如果有错，则要求a重发
#           流量控制和阻塞管理
#               流量控制用来避免主机发送得过快而使接收方来不及完全收下
#       tcp通讯三步骤
#           创建连接：tcp首先会创建通讯双方的连接，并且阻塞其他人员进入这个连接（您拨打的电话正在通话中...）
#           收发数据：
#           终止连接
#   总结
#       使用场景中，如果允许一部分数据丢失，就用udp（市面上几乎不用）
#       如果必须保证百分百数据不丢失，就用tcp

#tcp流程
#   客户端
#       创建socket
#       连接服务器
#       发送、接收信息
#       关闭套接字
#   服务端
#       创建socket                               #买个手机
#       bind绑定本地ip和port                         #插上手机卡
#       listen使socket变为可以被动链接（监听）   #设计手机为正常响铃状态
#       accept等待客户端的连接                   #静静等待别人给你打电话
#       recv/send收发信息
#客户端sokect模块
#   详见：C:\Users\justin\DataGit\yilong\first_project\练习\01_网络通讯\02_TCP\01_client.py
#服务端socket模块
#   tcp_server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   实例化对象调用的函数
#       tcp_server_socket.bind(('本地ip',port))    #{gn=绑定ip和port，cs=元组，fh=无}
#       tcp_server_socket.listen(128)    #{gn=}
#        = tcp_server_socket.accept()