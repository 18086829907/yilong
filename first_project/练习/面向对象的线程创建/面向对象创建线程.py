import threading
import time
class singThread(threading.Thread):
    def __init__(self, name, a):
        super().__init__() #super()调用父类，.__init__()执行父类中的构造方法
        self.name = name
        self.a = a

    def run(self):
        print('线程名字是{},接收的参数是{}'.format(self.name, self.a))
        for i in range(5):
            print('我在唱歌')
            time.sleep(1)

class danceThread(threading.Thread):
    def __init__(self, name, a):
        super().__init__() #super()调用父类，.__init__()执行父类中的构造方法
        self.name = name
        self.a = a

    def run(self):
        print('线程名字是{},接收的参数是{}'.format(self.name, self.a))
        for i in range(5):
            print('我在跳舞')
            time.sleep(1)

def main():
    #创建线程
    tSing = singThread('sing', 5)
    tDance = danceThread('dance', 6)
    #线程启动
    tSing.start() #启动后，会自动执行run方法，本质是重写了threading.Thread中的run方法，也就是说方法名必须叫run
    tDance.start()
    #主进程等待子进程结束再结束
    tSing.join()
    tDance.join()

if __name__ == '__main__':
    main()