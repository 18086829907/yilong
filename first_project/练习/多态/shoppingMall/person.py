class Person(object):
    def __init__(self, name, height, weight, consumption=0, shoppingDict={}):
        self.name = name
        self.height = height
        self.weight = weight
        self.consumption = consumption
        self.shoppingDict = shoppingDict

    def buy(self, shop, commodity):
        shop.shopingCommodity(commodity) #店铺销售一件指定商品
        self.shoppingDict[commodity.name] = commodity.price
        self.consumption += commodity.price

    def shoppingInformation(self):
        print(self.shoppingDict)