def out_func1(raw_func):
    def inner_func(*args, **kwargs):
        print('func1')  # 首先执行此行
        return raw_func(*args, **kwargs)
    return inner_func

def out_func2(raw_func):
    def inner_func(*args, **kwargs):
        print('func2') # 其次执行此行
        return raw_func(*args, **kwargs)
    return inner_func

@out_func1
@out_func2
def myTest():
    print('0')  # 最后执行此行

myTest()


#总结：
#   15行，16行，是先装饰func1，再装饰2，则先执行func1中的inner，再执行func2中的inner，最后执行原函数中的内容
#   即，先装饰谁，就先执行哪个装饰器中的内层函数