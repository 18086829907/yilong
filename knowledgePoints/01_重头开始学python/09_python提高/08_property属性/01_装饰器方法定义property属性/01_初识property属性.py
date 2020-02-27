class Goods:
    def func(self):
        pass


    @property  # 定义一个property属性，被装饰的普通函数名变成一个属性名
    def size(self):  # property属性，只能传入一个形参self(实例对象的引用)，不能再传入第二个参数
        return 100  # 一般都会返回一个值，这个值会被foo_obj.size返回给一个变量

if __name__ == '__main__':
    foo_obj = Goods()
    foo_obj.func()
    size_value = foo_obj.size  #调用size属性，size()会自动执行，
    print(size_value)

#property的好处在于，其实是调用函数，但是用调用属性的方式，即可获取函数的返回值
#大大提高了可读性，因为这里其实只是获取一个值，如果是调用函数，下意识的会去看函数中的代码过程，但是用了调用属性的方式，就明白这里是获取一个属性值
