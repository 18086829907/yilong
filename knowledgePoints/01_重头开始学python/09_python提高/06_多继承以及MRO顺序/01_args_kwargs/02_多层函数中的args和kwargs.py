def fun1(a, b, *args, **kwargs):
    print(args)
    print(kwargs)

def fun2(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    print('----------')
    fun1(a, b, args, kwargs)  # 相当于fun1(1,2,(3,4),{'num'=1234})
    print('----------')
    fun1(a, b, *args, kwargs)  # 相当于fun1(1,2,3,4,{'num'=1234})
    print('----------')
    fun1(a, b, *args, **kwargs)  # 相当于fun1(1,2,3,4,name=1234)


fun2(1,2,3,4,num=1234)