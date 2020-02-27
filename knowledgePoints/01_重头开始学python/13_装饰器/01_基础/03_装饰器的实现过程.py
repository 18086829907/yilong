def set_func(func):
    def call_func():
        print('权限验证1')
        print('权限验证2')
        func()
    return call_func

def myTest():
    print('1')

# ret = set_func(myTest)  # 变量名可以是ret
# ret()

# a = set_func(myTest)  # 变量名可以是a
# a()

myTest = set_func(myTest)  # 变量名可以是任意的，也可以是myTest
myTest()  # 这里的myTest是覆盖了myTest()函数名，让他指向set_func()的返回值，即指向了call_func

# 装饰器的好处在于
#   1、不用修改myTest函数的内部代码，
#   2、原来怎么调用myTest就怎么调用，加了装饰器也能这样调用，相当于myTest函数在不知情的情况下，就修改了代码
#