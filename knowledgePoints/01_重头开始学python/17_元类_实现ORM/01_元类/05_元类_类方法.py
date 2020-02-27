@staticmethod
def func():
    print('这是静态方法')

A = type('A', (), {'func':func})

help(A)