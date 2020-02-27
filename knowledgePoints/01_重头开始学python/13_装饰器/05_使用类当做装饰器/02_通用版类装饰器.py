class A(object):
    def __init__(self, raw_func):
        self.raw_func = raw_func

    def __call__(self, *args, **kwargs):
        print('lala')
        return self.raw_func(*args, **kwargs)


@A  # myTest = A(myTest)
def myTest():
    print('haha')

myTest()