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

def out_func3(raw_func):
    def inner_func(*args, **kwargs):
        print('func3') # 再次执行此行
        return raw_func(*args, **kwargs)
    return inner_func


@out_func1
@out_func2
@out_func3
def myTest():
    print('0')  # 最后执行此行

myTest()
