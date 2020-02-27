def set_func(func):
    def call_func():
        print('权限验证1')
        print('权限验证2')
        func()
    return call_func

@set_func  # @set_func 等价于  myTest = set_func(myTest)
def myTest():
    print('1')


# myTest = set_func(myTest)
myTest()

# 特点：装饰器只能在原函数前或后进行修改，不能修改原函数内部的代码
# 装饰器就是对原函数加功能
# 核心点：装饰器将原函数名传到闭包中，保存到外层函数的局部变量中，当闭包内层函数去调用这个原函数引用时，就执行原函数代码，只要在调用这个引用之前或之后添加功能，就能为原函数添加功能而不修改原函数
