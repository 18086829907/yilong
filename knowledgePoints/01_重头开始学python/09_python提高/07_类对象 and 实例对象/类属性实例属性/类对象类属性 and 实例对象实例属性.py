#创建一个类，类也是一个对象，叫类对象
class Province(object):  # python3：写与不写object没有区别，python2：写object就是新四类，不写object就是经典类
    #类属性
    country = '中国'

    def __init__(self, name):
        #实例属性
        self.name = name

if __name__ == '__main__':
    # 类目可以直接访问
    print(Province.country)
    # 实例属性名需要创建实例来访问
    obj = Province('四川')
    print(obj.name)
    print(obj.__class__)  # 每个实例对象都有一个__class__属性，来指向创造它的类对象
    print(obj.__class__.country)  # 每个实例对象都有一个__class__属性，来指向创造它的类对象


    # 增加类属性变量
    Province.population = 1400000000
    obj.__class__.population = 1400000000
    # 增加实例属性变量
    obj.money = 1000000


    # 修改类属性变量的值
    Province.population = 1500000000
    obj.__class__.population = 1500000000
    # 修改实例属性变量的值
    obj.money = 100


#Province('四川')实际执行流程
#   调用__new__方法，在内存中开辟一个空的空间
#   调用__init__方法，初始化空的内存空间中，并且让__init__的第一个参数指向这个内存空间，再在这个空间中，存入name的值
#   self.name = name，是在初始化后的内存空间中创建一个name变量，这个变量指向name值

# 总结
#   类对象只有一个
#   实例对象可以是n个
#   每个实例对象共有的属性可以放在类对象中，即类属性
#   每个实例对象各自拥有自己的实例属性
#   如果属性是独有的，则放在实例属性中，如果是共有的放在类属性中
#       比如，我有两女儿，他们的名字不一样，年龄不一样，这些放到实例属性中，他们的父亲一定是我，则放在类属性中