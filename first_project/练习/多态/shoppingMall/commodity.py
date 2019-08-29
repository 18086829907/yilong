class Commodity(object):
    def __init__(self, name, price, stock, cost, id):
        self.name = name
        self.price = price
        self.stock = stock
        self.cost = cost
        self.id = id

    def reduceStock(self): #减少库存
        if self.stock < 0:
            print('%s已售完')
        else:
            self.stock -= 1
            print('%s商品还剩%d' % (self.name, self.stock))


    def loadingGoods(self, commodity): #上货
        self.stock = commodity.stock

