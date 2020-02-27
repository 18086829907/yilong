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

    money = property(getMoney, setMoney)


if __name__ == '__main__':
    m = Money()
    print(m.money)  # 看起来就像是真的方调属性
    m.money = 100  # 看起来就想真的给属性赋值
    print(m.money)