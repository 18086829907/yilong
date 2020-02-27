class UpperAttrMetaClass(type):
    # __new__ 是在 __init__ 之前被调用的特殊方法
    # __new__ 是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望自定义它，所以改写了__new__
    # 如果你还有传参需求，也可以再定义__init__，在__init__中做点事情
    # 还有一些高级用法会涉及到改写__call__方法，这里我们用不到
    def __new__(cls, class_name, class_parents, class_attr):
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith('__'):
                new_attr[name.upper()] = value
        return type(class_name, class_parents, new_attr)

class Foo(object, metaclass=UpperAttrMetaClass):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)
