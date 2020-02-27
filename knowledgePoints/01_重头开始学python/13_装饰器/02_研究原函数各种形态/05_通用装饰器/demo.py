def out_func(raw_func):
    def inner_func(*args, **kwargs):
        print('-'*10)
        return raw_func(*args, **kwargs)
    return inner_func

@out_func  # myTest = out_func(myTest)
def myTest1():  #不带参数的
    print('1')

@out_func  # myTest = out_func(myTest)
def myTest2(num):  #带参数的
    print(num)

@out_func  # myTest = out_func(myTest)
def myTest3(num):  #带返回值的
    return num

@out_func  # myTest = out_func(myTest)
def myTest4(num1, num2):  #返回多值的
    return num1, num2

myTest1()
myTest2(10)
print(myTest3(100))
print(myTest4(1000,2000))
