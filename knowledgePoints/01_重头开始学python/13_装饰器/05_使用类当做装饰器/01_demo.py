class A(object):
    def __init__(self, raw_func):
        self.raw_func = raw_func

    def __call__(self):
        print('lala')
        self.raw_func()


@A  # myTest = A(myTest)
def myTest():
    print('haha')

myTest()