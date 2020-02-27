def out_func(raw_func):
    def inner_func(a):
        print('1')
        raw_func(a)
        print('2')
    return inner_func

@out_func  # myTest = out_func(myTest)  原函数名变量 = 闭包外函数(原函数名引用)
def myTest(num):
    print('%d' % num)
myTest(0)

# 总结：被装饰的函数如果有参数，有几个参数，闭包内部函数一定要有几个形参，并且要传给其内部的原函数的引用