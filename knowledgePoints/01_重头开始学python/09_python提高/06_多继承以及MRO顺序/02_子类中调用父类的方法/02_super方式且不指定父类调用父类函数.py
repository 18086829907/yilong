class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')



class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')



class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):  # 重写父类方法
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)  # 子类中调用父类方法
        print('Son2的init结束被调用')



class Grandson(Son1,Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        super().__init__(name, age, gender)  # super()方法，返回的父类对象 = [Grandson.__mro__[Grandson.__mro__.index(i) + 1] for i in Grandson.__mro__ if i == "<class '__main__.Grandson'>"][0]
        print('Grandson的init开始被调用')


if __name__ == '__main__':
    print(Grandson.__mro__)  # 每个类都有一个属性__mro__，这个属性中的值是一个元组，元组中的值是类的实例对象，这些实例对象的排序是通过python解释器中默认的一个叫C3的算法计算得到的，C3算法是一种能保证调用父类只调用一次的算法
    # 这个元组中值的顺序的作用，是用来判断super()应该返回哪个父类对象，判断依据是，在子类中调用super()，首先会在元组中找到当前子类名的位置，返回的父类对象，就在这个子类的后面

    gs = Grandson('grandson', 12, '男')
    # print(gs.__dict__)
    print('姓名：', gs.name)
    print('年龄：', gs.age)
    print('性别：', gs.gender)
