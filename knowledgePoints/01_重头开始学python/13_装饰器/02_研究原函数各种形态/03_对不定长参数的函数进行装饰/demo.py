def out_func(raw_func):
    def inner_func(*args, **kwargs):  # 有参数，没参数，参数有多个，参数有关键词参数，不管哪种，直接不定长参数，解决问题
        print('-'*5)
        # raw_func(args, kwargs)  # 这样不行，因为args是一个元组，kwargs是一个字典
        raw_func(*args, **kwargs)
        print('-'*5)
    return inner_func

@out_func  # myTest = out_func(myTest)
def myTest(num, *args, **kwargs):
    print('%d' % num)
    print(args)
    print(kwargs)

myTest(100)  # 实质：inner_func(100)
myTest(100, 200)  # 实质：inner_func((100, 200)
myTest(100, 200, 300, kk=400)  # 实质：inner_func(100, 200, 300, kk=400)