class Parent(object):
    x = 1  # 类属性
    def __init__(self):
        self.name = 1



class Child1(Parent):
    pass



class Child2(Parent):
    pass



print(Parent.x, Child1.x, Child2.x)
Child1.x = 2  #多肽，这里重写了x
print(Parent.x, Child1.x, Child2.x)  # 调用子类时，如果重写了变量，则调用重写变量的值，如果没有重写变量，就调用父类的值
Parent.x = 3  #这里修改了父类的值
print(Parent.x, Child1.x, Child2.x)  # Child1.x之前就重写了，在调用时，调用自己重写的属性，chilrd2.x没有被重写，仍然是调用父类的变量
