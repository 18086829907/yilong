class Foo:
    def get_bar(self):
        print('getter...')
        return 'laowang'

    def set_bar(self, value):
        '''必须有两个参数'''
        print('setter...')
        return 'set_value' + value

    def del_bar(self):
        print('deletert...')
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, 'description...')  # 创建一个类属性，指向的是property类的实例对象

if __name__ == '__main__':
    obj = Foo()

    print(obj.BAR)  # 自动调用第一个参数中定义的方法，即get_bar()    # 调用类属性

    obj.BAR = 'alex'  # 自动调用第二个参数中定义的方法，即set_bar()

    desc = Foo.BAR.__doc__  # 自动调取第四个参数中定义的方法，即'description...'
    print(desc)

    del obj.BAR  # 自动调用第三个参数中定义的方法，即del_bar()