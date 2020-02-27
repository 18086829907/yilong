# __doc__
class Foo:
    '''描述类信息：这就是描述类信息'''
    def func(self):
        pass
    '''没有这里哦'''
print(Foo.__doc__)


# __module__ and __class__
from testClass import Person
obj = Person()
print(obj.__module__)  # 输出 testClass，即：输出模块
print(obj.__class__)  # 输出 test.Person，即：输出类


# __init__ and __new__
class Foo:
    def __init__(self):
        pass
f = Foo()  # 自动调用__new__和__init__


# __del__
class Foo:
    def __del__(self):
        pass
a = 5
del a  # 删除一个对象时，python解释器自动调__del__删除对象并释放内存空间


# __call__
class Foo:
    def __init__(self):
        pass

    def __call__(self):  # 实例对象直接调用，前提是类中必须有__call__函数
        print('call')
f = Foo()  # 执行__init__
f()  # 实例对象直接调用，是执行__call__函数


#__dict__
class Province(object):
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')
print(Province.__dict__)  # 获取类属性和方法
obj1 = Province('山东', 1000)
print(obj1.__dict__)  # 获取obj1的实例属性
obj2 = Province('山西', 10)
print(obj2.__dict__)  # 获取obj2的实例属性


# __str__
class Foo:
    def __str__(self):
        return 'laowang'
obj = Foo()
print(obj)  # 获取obj的描述时，自动调用__str__函数
a = '123{}'.format(obj)  # 获取obj的描述时，会自动调用__str__


#__getitem__ and __setitem__ and __delitem__
class Foo:
    def __init__(self):
        self.dic = {'k1':'i love you'}
    def __getitem__(self, key):
        return self.dic[key]
    def __setitem__(self, key, value):
        self.dic[key] = value
    def __delitem__(self, key):
        del self.dic[key]
        print("已删除：dic['{}']".format(key))
if __name__ == '__main__':
    obj = Foo()
    print(obj['k1'])  # 自动触发执行 __getitem__
    obj['k2'] = 'laowang'  # 自动触发执行 __setitem__
    print(obj['k2'])
    del obj['k1']  # 自动触发执行 __delitem__


class Foo:
    def __getitem__(self, index):
        if isinstance(index, slice):
            print('1')
            print('start:{},stop:{},step:{}'.format(index.start, index.stop, index.step))
    def __setitem__(self, index, value):
        if isinstance(index, slice):
            print('2')
            print('start:{},stop:{},step:{},value:{}'.format(index.start, index.stop, index.step, value))
    def __delitem__(self, index):
        if isinstance(index, slice):
            print('3')
            print('start:{},stop:{},step:{}'.format(index.start, index.stop, index.step))
if __name__ == '__main__':
    obj = Foo()
    obj[1:3:1]  # 自动触发执行 __getitem__  # 列表倒序obj[-1:1:-1]
    obj[0:3:1] = [11,22,33]  # 自动触发执行 __setitem__
    del obj[0:3:1]  # 自动触发执行 __delitem__


