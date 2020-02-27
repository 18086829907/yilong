class Parent(object):
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')



class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        Parent.__init__(self, name)
        print('Son1的init结束被调用')



class Son2(Parent):
    def __init__(self, name, gender):  # 重写父类方法
        print('Son2的init开始被调用')
        self.gender = gender
        Parent.__init__(self, name)  # 子类中调用父类方法
        print('Son2的init结束被调用')



class Grandson(Son1,Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print('Grandson的init开始被调用')


if __name__ == '__main__':
    gs = Grandson('grandson', 12, '男')
    print('姓名：', gs.name)
    print('年龄：', gs.age)
    print('性别：', gs.gender)


# 从打印结果来看Parent，被调用了很多次
# 用父类名的方式调用父类函数的问题
#   当父类很多时，通过父类名调用爷爷类，爷爷类中的属性就会在无形之间被创建多次
#   由于一个进程中定义变量的个数是有上限的1024
#   因此需要衡量父类的个数，酌情使用父类名调用父类行数这种方式

