'''
class Cat(object):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + '吃')
'''

from 练习.多态.feedingAnimals.animal import Animal
class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)