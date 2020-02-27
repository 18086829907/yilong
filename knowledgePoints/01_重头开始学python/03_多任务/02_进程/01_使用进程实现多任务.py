import multiprocessing
import time


def myTest1(a):
    for i in range(5):
        print(a)
        time.sleep(2)


def myTest2(a):
    for i in range(5):
        print(a)
        time.sleep(2)


def main():
    p1 = multiprocessing.Process(target=myTest1, args=('1',))
    p2 = multiprocessing.Process(target=myTest2, args=('2',))
    p1.start()
    p2.start()


#总结
#   启动的进程可以通过 # ps aux命令查询得到，验证：通过kill pid 杀死开启的进程
#   进程是代码+占用的电脑资源，当start()时，操作系统会将当前所有代码复制到新的空间里面，即创建出新的子进程
#       注意：start()创建子进程，主进程仍然在运行，如果主进程又调用了start()，则再创建一个新的子进程
#       因此进程能实现多任务，但比线程耗费的资源要大得多
#   进程和线程
#       相似点：创建与启动，只是换了模块和类
#       不同点：进程与进程之间不共享数据，只能通过队列（内存对象）来通讯
#   深度理解：代码不修改，代码不会被复制，只是多个进程共享，而不同的进程会使用各自的数据，因此会被复制到新子进程空间的，只有数据
#       但是，如果通过某些手段，子进程中需要修改代码，此时代码就会被复制，这就叫做写时拷贝（修改的时候拷贝）

if __name__ == '__main__':
    main()

