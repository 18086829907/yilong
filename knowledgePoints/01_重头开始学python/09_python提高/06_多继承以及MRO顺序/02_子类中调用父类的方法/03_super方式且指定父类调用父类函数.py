class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')



class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('Son1的init开始被调用')
        self.age = age
        super(Son1, self).__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')



class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):  # 重写父类方法
        print('Son2的init开始被调用')
        self.gender = gender
        super(Son2, self).__init__(name, *args, **kwargs)  # 子类中调用父类方法
        print('Son2的init结束被调用')



class Grandson(Son1,Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        super(Grandson, self).__init__(name, age, gender)  # super()方法，返回的父类对象 = [Grandson.__mro__[Grandson.__mro__.index(i) + 1] for i in Grandson.__mro__ if i == "<class '__main__.Grandson'>"][0]
        print('Grandson的init开始被调用')



if __name__ == '__main__':
    #super() 参数1：可以指定当前类名，参数2：当前类对象slef
    #说明
    #   参数1是将当前类名替换为指定的类名(参数1)，再根据__mro__去寻找参数1的父级类名，最后返回该指定类名的父类名对象
    #   由此super()方法可以自由设定返回的父类对象
    #   super()的参数1一般都用自己当前的类目作为参数1，与不写参数1的效果是一样，但区别就在于，如果需要指定super()返回的父类对象，这里就可以对其进行设置
    print(Grandson.__mro__)
    gs = Grandson('grandson', 12, '男')
    # print(gs.__dict__)
    print('姓名：', gs.name)
    print('年龄：', gs.age)
    print('性别：', gs.gender)
