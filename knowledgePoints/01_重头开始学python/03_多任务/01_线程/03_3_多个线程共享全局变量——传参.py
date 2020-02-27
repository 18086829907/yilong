import threading
import time


def mytest1(var):
    var.append(3)


def mytest2(var):
    print(var)    #共享全局变量


def main():
    myList = [1, 2]
    t1 = threading.Thread(target=mytest1, args=(myList,))    #args将传输传递到函数中，注意必须传递元组，方便传递多个参数
    t2 = threading.Thread(target=mytest2, args=(myList,))
    t1.start()
    time.sleep(1) #保证t1先执行
    t2.start()

#总结：
#   mytest1,mytest2是共享全局变量的
#   因为线程往往是配合使用，经常需要同时处理一个数据，如果不共享，就需要来回传递，太麻烦，因此全局变量是共享的


if __name__ == '__main__':
    main()
