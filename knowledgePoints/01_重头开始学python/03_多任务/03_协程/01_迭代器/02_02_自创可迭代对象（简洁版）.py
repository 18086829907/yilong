from collections.abc import Iterable
from collections.abc import Iterator
import time

class ClassMate():
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            data = self.names[self.current_num]
            self.current_num += 1
            time.sleep(1)
            return data
        else:
            raise StopIteration

if __name__ == '__main__':
    classMate = ClassMate()
    classMate.add('张三')
    classMate.add('李四')

    # classMate是否为可迭代对象
    #   答：ClassMate中有__iter__方法，classMate是可迭代对象
    # __iter__()方法是否返回迭代器
    #   答：__iter__返回的是self，即ClassMate类，ClassMata中同时存在__iter__方法和__next__方法，因此ClassMata是一个迭代器
    # 所以classMate可以被for循环取值
    for i in classMate:
        print(i)