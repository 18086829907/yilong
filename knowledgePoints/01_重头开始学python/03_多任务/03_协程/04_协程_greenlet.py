from greenlet import greenlet
import time


def task1():
    while True:
        print('--1--')
        gr2.switch()    #3、遇到switch方法，程序暂停，并切换到gr2绑定的函数
        time.sleep(0.5)


def task2():
    while True:
        print('--2--')
        gr1.switch()    #4、遇到switch，暂停程序，切换到task1
        time.sleep(0.5)


if __name__ == '__main__':
    gr1 = greenlet(task1)    #1、greenlet类实例化一个对象，并将这个对象与一个函数名绑定
    gr2 = greenlet(task2)    #gr2是全局变量，可以在函数中直接调用

    gr1.switch()    #2、对象的switch方法，能运行绑定的函数
