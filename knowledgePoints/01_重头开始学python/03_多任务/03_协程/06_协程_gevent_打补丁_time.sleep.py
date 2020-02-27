from gevent import monkey
import gevent
import time


#有耗时操作时需要
monkey.patch_all()    # 将程序中所有的耗时操作的代码，都替换为gevent模块中的耗时代码，即time.sleep() 替换成gevent.sleep()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


if __name__ == '__main__':
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)

    g1.join()
    g2.join()
    g3.join()