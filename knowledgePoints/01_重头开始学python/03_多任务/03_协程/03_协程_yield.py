import time


def task1():
    while True:
        print('--1--')
        time.sleep(0.5)
        yield    #在函数的循环内任意位置添加yield


def task2():
    while True:
        print('--2--')
        time.sleep(0.5)
        yield    #yield将函数变成了生成器模板


def main():
    t1 = task1()    #创建生成器对象
    t2 = task2()

    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()