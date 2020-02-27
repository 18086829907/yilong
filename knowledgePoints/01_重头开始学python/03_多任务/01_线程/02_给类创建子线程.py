import threading
import time


class MyThread(threading.Thread):    #必须继承threading.Thread类
    def run(self):    #必须定义run方法
        for i in range(3):
            time.sleep(1)
            msg = "i'm" + self.name + '@' + str(i)
            print(msg)
        self.test()    #在启动类子线程时，调用test函数

    def test(self):    #注意：当t.start()时，只会自动调用run(),test函数不会被调用，除非在run()中调用self.test()
        print('1')


if __name__ == '__main__':
    t = MyThread()    #等价于t1 = threading.Thread(target=funtionName)
    t.start()    #启动类子线程，调用的是继承自threading.Thread中的start方法。调用后会自动调用run方法