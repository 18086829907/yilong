# 元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要使用到元类，
# 那么你就不需要使用它了。那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类
#   --Python界的领袖 Tim Peters

def upper_attr(class_name, class_parents, class_attr):
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith('__'):
            new_attr[name.upper()] = value
    return type(class_name, class_parents, new_attr)

class Foo(object, metaclass=upper_attr):  # 执行到class立即使用默认的type('Foo', (object,), {'bar':'bip'})开始创建类，如果有metaclass，则执行upper_attr('Foo', (object,), {'bar':'bip'})函数，并用返回的type来创建类
    bar = 'bip'

print(hasattr(Foo, 'bar'))  # hasattr(),功能：用于判断类中是否包含指定的属性(变量名)
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)  # 当实例对象调用类属性时，公司要求所有的类属性都必须是大写，此时可以使用元类，让程序自动将类属性名从小写改为大写


#总结：
#    元类可以同装饰器一样使用，在创建类之前给类加功能，即在不修改类原代码的前提下，用元类来装饰类
#    特别适用于，已经写好了非常多类时，需要修改其属性名时，使用元类，事半功倍