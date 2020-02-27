#for i in obj:
#   pass
#能否用for取值判断流程
#   1、判断obj是否为可迭代对象
#       isinstance(obj)
#           要想使isinstance返回True，只需要在自定义类中添加一个def __iter__(self):方法
#   2、在第一步成立的情况下
#       自动调用内置函数iter(obj)
#           内置函数iter会自动调用obj对象的__iter__()方法，即obj.__iter__()
#   3、__iter__()的返回值必须是一个迭代器对象
#       迭代器对象满足条件是，其类一定有 def __iter__():方法 和 def __next__():方法
#       返回迭代器对象时，会自动调用其__next__()方法，返回迭代器对象的__next__()方法的返回值
#           这个值就会给到for i in obj中的i，即__next__返回什么，i就是什么值
#
from collections import Iterable    #可迭代对象
from collections import Iterator    #迭代器

class ClassMate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):    #满足了第一步：只要有这个方法
        return MyIterator(self)    #满足第二步：返回的是可迭代对象

class MyIterator(object):
    def __init__(self, ClassMataObj):
        self.ClassMataobj = ClassMataObj
        self.current_num = 0

    def __iter__(self):    #满足第三步：只要有__iter__和__next__就是能实例化一个可迭代对象
        pass

    def __next__(self):
        if self.current_num < len(self.ClassMataobj.names):    #判断当前值是否小于列表的长度，小于才去用作下标取值
            res = self.ClassMataobj.names[self.current_num]
            self.current_num += 1
            return res    #这里返回一个数据，for就将值给i
        else:
            raise StopIteration    #自定义一个异常，否则for会一直调用__next__()取值


if __name__ == '__main__':
    classMate = ClassMate()
    classMate.add('张三')
    classMate.add('李四')
    classMate.add('王五')


    print('判断classMate是否为可迭代对象', isinstance(classMate, Iterable))
    classMate_iterator = iter(classMate)
    print('判断classMate_iterator是否为迭代器', isinstance(classMate_iterator, Iterator))


    #迭代器可以用next()取值
    print(next(classMate_iterator))    #内置函数next()，可以调用迭代器对象中的__next__()方法，next()的返回值就是__nexe__()方法的返回值


    #总结：classMate是一个可迭代对象，__iter__()方法返回的是一个迭代器，就能够用for循环取值
    for i in classMate:
        print(i)