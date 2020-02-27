class Car:
    def __init__(self, colour):
        self.colour = colour

    def open(self):
        print('开{}车'.format(self.colour))

car1 = Car('blue')
print(car1.__class__)  # 实例对象的__class__属性标记着实例的类 <class '__main__.Car'>
print(car1.__dict__)  # 实例对象的__dict__属性记录着实例的属性值{'colour': 'blue'}，因此可以用car1.colour取值

car1 = Car('red')
print(car1.__class__)
print(car1.__dict__)
