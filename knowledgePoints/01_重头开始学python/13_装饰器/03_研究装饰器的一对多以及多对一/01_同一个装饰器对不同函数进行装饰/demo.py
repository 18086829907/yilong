def out_func(raw_func):
    def inner_func():
        print('-'*10)
        raw_func()
        print('-'*10)
    return inner_func

@out_func  # myTest1 = out_func(myTest1)
def myTest1():
    print('111')

@out_func  # myTest2 = out_func(myTest2)
def myTest2():
    print('222')

myTest1()
myTest2()

# 执行流程
#   一、执行第8行，myTest1 = out_func(myTest1)
#       调用闭包外层函数，将原函数1的引用传输，并保存在外层函数的局部变量中，方便闭包内层函数调用
#       原函数名1指向了闭包内层函数
#   二、执行第12行，myTest2 = out_func(myTest2)
#       调用闭包外层函数，将原函数2的引用传输，并保存在外层函数的局部变量中，方便闭包内层函数调用
#       原函数名2指向了闭包内层函数
#   三、执行16行，实质是执行闭包内层函数，当执行到4行时，实质是闭包内层函数的形参传给原函数1，并且执行原函数1
#   四、执行17行，实质是执行闭包内层函数，当执行到4行时，实质是闭包内层函数的形参传给原函数2，并且执行原函数2

#总结：
#   用同一个装饰器可以装饰多个函数
#   遇到@符号的装饰器就开始装饰，而不用等到调用这个函数时进行装饰
#   @装饰器 等价于 执行 原函数名 = 装饰器名(原函数名)