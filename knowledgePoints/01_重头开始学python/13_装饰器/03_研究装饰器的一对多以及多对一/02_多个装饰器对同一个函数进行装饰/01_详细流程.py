def out_func1(raw_func):
    print('开始装饰func1')
    def inner_func():
        print('func1')
        raw_func()
    return inner_func

def out_func2(raw_func):
    print('开始装饰func2')
    def inner_func():
        print('func2')
        raw_func()
    return inner_func

@out_func1  # myTest = out_func1(myTest)
@out_func2  # myTest = out_func2(myTest)
def myTest():
    print('0')

myTest()


#总结：
#   执行15行，判断下面代码是否是函数，如果不是，则暂停执行myTest = out_func1(myTest)
#   执行16行，判断下面代码是否是函数，如果是，则开始执行myTest = out_func2(原函数)
#       print('开始装饰func2')
#       myTest指向闭包2中的内层函数
#       闭包2中中的内层函数中的变量指向原函数
#   执行15行，判断下面代码是否是函数，是函数（此时的函数是闭包2中的内层函数）,则执行myTest = out_func1(闭包2中的内层函数)
#       print('开始装饰func1')
#       当执行到5行时，实质执行的是闭包2中的内层函数
#       print('func2')
#       当执行到12行时，实质执行的是原函数

