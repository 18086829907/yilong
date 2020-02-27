#小故事理解带参数的装饰器
#   我与爷爷过安检
#       安检看爷爷80岁，说老大爷，请直接过去
#       安检看见我，仔细对我进行了安全监测，才允许我通过

def level_func(level):
    def out_func(raw_func):
        def inner_func(*args,**kwargs):
            if level == 1:
                print('直接通过')
            if level == 2:
                print('最高级别检测')
            raw_func(*args,**kwargs)
        return inner_func
    return out_func

@level_func(1)
def myTest1():
    print('爷爷')
    return 'ok'

@level_func(2)
def myTest2():
    print('我')
    return 'ok'

myTest1()
myTest2()

#总结：
#   带参数装饰器分为两步执行
#       1、先调用装饰器名指向的函数，参数当做实参，传递到函数中
#       2、函数内最后会根据条件返回真正的装饰器（闭包）
#       3、再用真正的装饰器装饰原函数，即myTest1 = out_func(myTest1)