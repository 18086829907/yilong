class ShoppingMall(object):
    tatalPerformance = 0 # 总销售额
    def __init__(self, name, shopName='', checkInShopNumber=0,  checkInRate=0, checkInTatalNumber=100): #, tatalPerformance=0
        self.name = name #商城名字
        self.shopName = shopName #店铺名字
        self.checkInShopNumber = checkInShopNumber #入住店铺数量
        self.checkInRate = checkInRate #入住率

        self.checkInTatalNumber = checkInTatalNumber #店铺总数量

    def checkIn(self, shop):
        self.checkInShopNumber += 1 #入住店铺数量
        self.shopName = shop.name #店铺名称
        self.checkInRate = self.checkInShopNumber / self.checkInTatalNumber #入住率

    def reportFrom(self):
        print(self.checkInShopNumber, self.checkInRate, ShoppingMall.tatalPerformance) #入住商铺数量，入住率
