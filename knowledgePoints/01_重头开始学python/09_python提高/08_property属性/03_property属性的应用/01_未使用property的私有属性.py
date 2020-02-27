class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('TypeErorr:请使用int类型')

if __name__ == '__main__':
    m = Money()
    print(m.__money)  #

# 一般定义私有属性时，会配套设置两个函数来获取私有属性值和修改它的值
# 对不同用户权限开通或不开通这两个函数的使用权限
# 在其他语言中都会给私有属性配套get方法和set方法，python中也能写，但是python不推荐
# 因为我要获取这个值时，需要查看源码，获取这个值的方法名是什么，才能调用
# 因此需要用porperty升级