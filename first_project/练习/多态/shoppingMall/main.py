'''
客户
类名：Person
属性：name, height, weight, money, consumption(消费)
方法：buy()

商城
类名：ShoppingMall
属性：name, chenckInNum, shopNumber, chenckInRate
方法：checkIn() getIntoTatal()

店铺
类名：Shop
属性：name, address, area, rent, flow, enteringPersonNum, turnoverRate成交率
方法：getInto()

商品 ok
类名：Commodity
属性：name, price, stock
方法：replenishment()

衣服 ok
类名：Clothes(Commodity)
属性：
方法：

裤子 ok
类名：Trousers(Commodity)
属性：
方法：

成本
类名：Cost
属性：cost
方法：
'''
from shoppingMall import ShoppingMall
from shop import Shop
from clothes import Clothes
from trousers import Trousers
from person import Person

def shopPractice(shoppingMallName, shopName, shopAddress, area, rent):
    shoppingMall = ShoppingMall(shoppingMallName) #实例化商城
    print('%s招商开始' % shoppingMallName)
    shop = Shop(shopName, shopAddress, area, rent) #实例化店铺
    shoppingMall.checkIn(shop) #店铺入住商城
    print('店铺：%s已入住，地址：%s' % (shop.name, shop.address))
    shop.practice(1000000) #店铺开业
    print('店铺：%s已装修完毕' % shop.name)
    clothes = Clothes('T恤', 1000, 10, 200, 'tx001') #实例化商品：name, price, stock, cost, id
    trousers = Trousers('短裤', 500, 10, 100, 'dk001') #实例化商品：name, price, stock, cost, id
    shop.replenishment(clothes)  # 店铺铺货
    shop.replenishment(trousers)  # 店铺铺货
    print('店铺：%s已经铺货，营业正式开始' % shop.name)
    return (shop, clothes, trousers)

def Consumer():
    person = Person('justin', 170, 70) #实例化客户 name, height, weight
    shop_Practice = shopPractice('奥特莱斯', '恩宁', '一区一楼15号', 50, 400)
    shop = shop_Practice[0]
    shop.getInto(person) #客户进入店铺
    print('客户：%s已进入店铺：%s' % (person.name, shop.name))
    person.buy(shop, shop_Practice[1]) #客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[1])  # 客户在这家店买了一件衣服
    person.buy(shop, shop_Practice[2]) #客户在这家店买了一条裤子

def main():
    Consumer()

if __name__ == '__main__':
    main()
    print(ShoppingMall.tatalPerformance)