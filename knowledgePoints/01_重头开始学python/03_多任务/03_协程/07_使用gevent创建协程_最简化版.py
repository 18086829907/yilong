from gevent import monkey
import gevent
import time


#有耗时操作时需要
monkey.patch_all()


def function(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


if __name__ == '__main__':

    gevent.joinall([    #等待列表中所有的协程执行完，在结束主函数
        gevent.spawn(function, 5),    #这里创建一个对象g1对象，并且执行了g1.join()
        gevent.spawn(function, 5),
        gevent.spawn(function, 5)
    ])


#总结：gevent.joinall中启动几个协程，就启动几个协程
#   monkey.patch_all()能把time.sleep(),替换为gevent.sleep()
#   用协程，能将代码中所有的暂停的时间都利用上，大大提高效率