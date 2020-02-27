import threading
import time


a = 0
lock = threading.Lock()


def one(num):
    global a
    for i in range(num):
        lock.acquire()    #lock对象上锁
        a += 1
        lock.release()    #lock对象解锁锁


def two(num):
    global a
    for i in range(num):
        lock.acquire()    #当lock是上锁状态时，lock对象又调用acquire()时，会阻塞，直到lock对象解锁后，再执行上锁和解阻塞
        a += 1
        lock.release()


def main():
    # t1 = threading.Thread(target=one, args=(100,))    #a加100次1
    # t2 = threading.Thread(target=one, args=(100,))    #a加100次1
    # t1.start()
    # t2.start()
    # time.sleep(5)
    # print(a)    #最后a的结果为200，没问题

    t1 = threading.Thread(target=one, args=(1000000,))    #a加1000000次1
    t2 = threading.Thread(target=one, args=(1000000,))    #a加1000000次1
    t1.start()
    t2.start()
    time.sleep(5)
    print(a)    #最后a的结果应该为2000000，但是结果为1464322，上了互斥锁后，就能保证结果正确输出了


#资源竞争出现的问题，原理是什么呢？
#   进程1
#       a+=1
#           读取a的值    0
#           加上1    1
#           将值赋值给a    2
#   进程2
#       a+=1
#           读取a的值    0
#           加上1    1
#           将值赋值给a    2
#   cpu会执行上面两个线程时时，恰巧出现这种情况
#       cup执行
#           进程1的第1句，此时a的值为1，但还未保存，就退出此进程
#       cup执行
#           进程2的第1句，此时a的值为1，但还未保存，就退出此进程
#       cup执行
#           进程1的第2句，此时的a被赋值为1，退出此进程
#       cup执行
#           进程2的第2句，此时的a被复制为1，退出此进程
#   因此执行了2此加1，但只加了1次一，在数量大了的情况下，这种情况出现的概率会越来越大，


if __name__ == '__main__':
    main()