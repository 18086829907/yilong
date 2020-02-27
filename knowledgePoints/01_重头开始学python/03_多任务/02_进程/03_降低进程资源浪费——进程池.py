#进程池Pool：
#   初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，
#   如果池还没有满，那么就会创建一个新的进程用来执行该请求，
#   但如果进程数已达到最大进程数，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务
#进程池节约资源的原因：
#   是在进程池中先创建n个子进程，子进程在循环执行新的请求，自始至终没有重新创建和销毁进程，降低了这两个步骤的资源浪费

#multiprocessing.Process() 与 multiprocessing.Pool()的取舍
#   当任务数<10个时，采用Process手动创建进程
#   当任务数>10个时，采用Pool进程池来完成

import multiprocessing
import os, time, random


def myWork(i):    #注意：函数必须保证没有异常，如果在子进程中执行，出现异常它不会报错
    t_start = time.time()
    print('{}号开始执行，进程号为：{}'.format(i,os.getpid()))
    time.sleep(random.random()*2)    #random.random()随机生成0~1的浮点数
    t_end = time.time()
    print('{}号进程结束,耗时{}'.format(i, t_end - t_start))


def main():
    po = multiprocessing.Pool(3)    #创建进程池对象，池中最多运行3个子进程，注意创建对象时，不启动子进程，当需要用到多个进程时，自动创建
    for i in range(10):
        po.apply_async(myWork, (i,))    #.apply_async:指定要添加到进程池的函数名及传递进去的参数，过程描述：所有任务会一次性全部添加到进程池的缓存区，任务会自动分配到进程池中的子进程中去执行。但一旦有任务被添加到缓存区，就会被分配到子进程中去运行

    print('---start---')
    po.close()
    po.join()    #等待po中的所有子进程执行完成，必须放在close语句之后，如果不添加join语句，主进程结束，不管进程池中的任务是否执行完，整个程序都会结束
    print('---end---')


if __name__ == '__main__':
    main()