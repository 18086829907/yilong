# 搜索框
#   tcp  # 搜索tcp协议的数据包
#   udp  # 搜索udp协议的数据包
#   ip.dst == 10.143.445.23  # 搜索目地ip为10.143.445.23的数据包
#   ip.src == 192.168.1.1  # 搜索原ip为192.168.1.1的数据包
#   ip.src == 192.168.1.1 and udp  # 搜索原ip为192.168.1.1的数据包，并且是udp协议的数据包
#   udp.port == 8080  # 搜索udp协议端口为8080的数据包
#   tcp.port == 8080  # 搜索udp协议端口为8080的数据包
# 包列表栏
#   No.: 包的编号
#   Time: 捕获到包的时间
#   Source: 原ip
#   Destination: 目标ip
#   Protocol: 协议
#   Length: 数据长度
#   Info: 信息描述
# 包详情
#   udp协议的详情
#       Frame 24272: 该包的所有数据总计
#       Etherenet II: 链路层数据,mac地址
#       Internet Protocol Version: 网络层数据,ip
#       User Datagram Protocol: 传输层数据,port
#       Data: 应用层数据,具体传输的内容
# 包数据
#   十六进制
#   尽可能的翻译
# 总结：
#   当工作中，做的是网络程序，如果遇到发送一个包，结果目的端口死活收不到数据。
#   此时，你可以用wirshark抓包，程序是否将数据发出，如果发出则是网络问题，如果未发出是程序问题
