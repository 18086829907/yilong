def set_func(func):
    def call_func():
        print('权限验证1')
        print('权限验证2')
        func()
    return call_func

@set_func
def myTest_1():
    print('1')
myTest_1()