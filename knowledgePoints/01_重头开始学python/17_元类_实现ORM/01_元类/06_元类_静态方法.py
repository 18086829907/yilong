@classmethod
def func(cls):
    print('这是类方法')

A = type('A', (), {'func':func})

help(A)