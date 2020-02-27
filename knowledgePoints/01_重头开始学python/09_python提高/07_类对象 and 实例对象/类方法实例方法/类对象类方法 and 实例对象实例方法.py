class Daught(object):
    father = 'cyl'

    def __init__(self, name):
        self.name = name


    def ord_func(self):
        '''定义实例方法至少需要一个形参self'''
        print('实例方法')
        print(self.name)



    @classmethod  # 定义类方法的装饰器
    def class_func(cls):
        '''定义类方法，至少有一个cls参数'''
        print('类方法')
        print(cls.father)  # 能访问就能修改


    @staticmethod  # 静态方法，可以理解为定义在类中的普通的函数，普通函数不需要传self或cls，在类中调用静态函数，可以直接用self.static_func()来调用
    def static_func():
        '''定义静态方法，无默认参数'''
        print('静态方法')


if __name__ == '__main__':
    f = Daught('中国')
    # 调用实例方法
    # 调用实例方法，默认传入的是实例对象的引用，self，即self指向的是实例对象，可以用self来调用实例属性
    f.ord_func()

    # 调用类方法
    # 调用类方法，默认传入的是类对象的引用，cls，即cls指向的是类对象，可以用cls来调用类属性
    Daught.class_func()  # 类目调用类方法

    #调用静态方法
    f.static_func()  # 实例对象调用静态方法
    Daught.static_func()  # 类对象调用静态方法


# 实例方法、类方法、静态方法的相同
#   所有的方法都定义在类对象中
#       即表示类对象的方法都是公用的

# 实例方法、类方法、静态方法的不同
#   传入参数不同
#       调用实例方法时，python解释器会在实例函数中自动传入一个实例对象self的引用
#       调用类方法时，python解释器会在实例函数中自动传入一个类对象cls的引用
#       调用静态方法时，python解释器不会传入任何引用
#   调用者不同
#       类对象只能调用类方法、静态方法
#       实例对象可以调用类方法（通过__class__）、实例方法、静态方法