class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('TypeErorr:请使用int类型')

if __name__ == '__main__':
    m = Money()
    print(m.money)
    m.money = 100
    print(m.money)