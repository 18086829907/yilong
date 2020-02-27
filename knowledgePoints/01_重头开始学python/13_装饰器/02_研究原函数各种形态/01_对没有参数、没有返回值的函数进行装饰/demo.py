def out_func(raw_func):
    def inner_func():
        print('1')
        raw_func()
        print('2')
    return inner_func

@out_func  # myTest = out_func(myTest)
def myTest():
    print('123')

myTest()