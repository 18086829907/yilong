def func(self):  # 实例方法需要将类对象传入
    print('这是实例方法')

A = type('A', (), {'func':func})

# help(A)
a = A()
a.func()