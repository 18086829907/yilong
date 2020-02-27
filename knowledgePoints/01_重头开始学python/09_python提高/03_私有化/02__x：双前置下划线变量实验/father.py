class Father(object):
    def __init__(self, money):
        self.money = money
        self.__money = 10000
    def play(self):
        print('play')
    def getMoney(self):
        print(self.__money)
    def __openCar(self):
        print('openCar')
    def accOpenCar(self):
        self.__openCar()

if __name__ == '__main__':
    father = Father(100)
    father.getMoney()
    # father.__openCar()
    father.accOpenCar()