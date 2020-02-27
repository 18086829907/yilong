import threading
import time


num = 100


def mytest1():
    global num
    num += 1    #修改全局变量的值


def mytest2():
    print(num)    #共享全局变量


def main():
    t1 = threading.Thread(target=mytest1)
    t2 = threading.Thread(target=mytest2)
    t1.start()
    time.sleep(1) #保证t1先执行
    t2.start()


if __name__ == '__main__':
    main()