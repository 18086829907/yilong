from shoppingMall import ShoppingMall
class Shop(object):
    def __init__(self, name, address, area, unitRent, enteringPersonNumber=0, shopingPersonNumber=0, turnoverRate=0, performance=0, profit=0, costCommodity=0, costFixed=0):
        self.name = name
        self.address = address
        self.area = area
        self.unitRent = unitRent
        self.rent = self.area * self.unitRent
        self.enteringPersonNumber = enteringPersonNumber
        self.shopingPersonNumber = shopingPersonNumber
        self.turnoverRate = turnoverRate
        self.performance = performance
        self.profit = profit
        self.costCommodity = costCommodity
        self.costFixed = costFixed


    def renovation(self, costFixed): #装修
        self.costFixed += costFixed

    def practice(self, costFixed): #开业，参数2：店铺实例
        self.renovation(costFixed)

    def getInto(self, person): #进店
        self.enteringPersonNumber += 1 #人流量

    def shopingCommodity(self, commodity): #购买商品
        commodity.reduceStock() #这个商品减少一件库存
        self.performance += commodity.price #增加店铺营业额
        self.costCommodity += commodity.cost #增加店铺商品成本
        self.profit = self.performance - self.costCommodity #店铺利润
        self.shopingPersonNumber += 1
        if self.enteringPersonNumber > 0: #计算成交转化率
            self.turnoverRate = self.shopingPersonNumber / self.enteringPersonNumber
        ShoppingMall.tatalPerformance += commodity.price


    def replenishment(self, commodity): #补货
        self.costCommodity += (commodity.cost * commodity.stock) #店铺货品成本 = 商品成本 * 商品数量

    def reportFrom(self): #报表
        print(self.performance, self.costCommodity, self.costFixed, self.profit, self.enteringPersonNumber, self.shopingPersonNumber, self.turnoverRate) #营业额、商品成本、固定成本、利润、进店人数、消费人数、转化率