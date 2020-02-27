import threading
import time


def sing():
    for i in range(10):
        print('正在唱歌')
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞')
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()    # 子线程1开始
    t2.start()    # 子线程2开始

    while True:
        length = len(threading.enumerate())    #.enumerate()，列举当前正在执行的线程，返回的是列表
        print('当前运行的线程数为{}'.format(length))
        if length<=1:
            break

        time.sleep(0.5)

if __name__ == '__main__':
    main()