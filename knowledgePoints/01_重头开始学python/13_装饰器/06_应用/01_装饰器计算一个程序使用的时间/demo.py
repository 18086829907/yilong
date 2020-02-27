import time

def out_func_computing_time(func):
    def inner_func():
        t1 = time.time()
        func()
        t2 = time.time()
        print('myTest所用时间：{}'.format(t2-t1))
    return inner_func

@out_func_computing_time  # myTest = out_func_computing_time(myTest)
def myTest():
    time.sleep(1)

myTest()