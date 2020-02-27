x = 300
def test1():
    x = 200  # 这里是定义外层函数的局部变量x，而不是全局变量x
    def test2():
        nonlocal x  # 在内层函数中修改外层函数的局部变量，需要加nonlocal，如果需要修改全局变量x，则添加global
        print('%d'%x)
        x = 100
        print('%d'%x)
    return test2