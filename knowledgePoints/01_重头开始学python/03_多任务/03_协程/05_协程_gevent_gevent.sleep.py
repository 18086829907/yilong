#为什么要用gevent
#   因为它遇到time.sleep()就切换任务
#       即，一个任务在休眠时，就切换下个任务进行执行
#           充分利用了其他任务的休眠时间，真实现了多任务
#注意：延时不能同time.sleep()，而是用gevent.sleep()


import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


if __name__ == '__main__':
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)

    g1.join()
    g2.join()
    g3.join()

#流程
#   1、创建gevent对象，绑定函数名，传递参数
#   2、g1.join(),阻塞等待g1绑定的函数执行完，才继续往下执行
#   3、gevent对象发现阻塞，自动执行g1绑定的函数
#   4、在g1绑定的函数中发现gevent.sleep，gevent自动启动g2绑定的函数
#   5、在g2绑定的函数中发现gevent.sleep，gevent自动启动g3绑定的行数
#   6、在g3绑定的函数中发现gevent.sleep，gevent自动切回g1绑定的函数，继续执行
#   7、就这样g1、g2、g3绑定的函数都执行完后，所有的join解堵塞。主程序结束