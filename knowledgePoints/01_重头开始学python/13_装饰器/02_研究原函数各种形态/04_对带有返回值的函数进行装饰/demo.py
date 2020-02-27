def out_func(raw_func):
    def inner_func(num):
        num += 1
        return raw_func(num)  # 闭包内层函数 需要返回 原函数的返回值
    return inner_func

@out_func  # myTest = out_func(myTest)
def myTest(num):
    return num

a =  myTest(1)
print(a)