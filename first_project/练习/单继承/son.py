from 练习.多继承.father import Father
class Son(Father):
    def __init__(self, name, money):
        super(Son, self).__init__(name, money)