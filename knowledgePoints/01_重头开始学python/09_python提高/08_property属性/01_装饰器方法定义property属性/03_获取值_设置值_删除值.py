class Goods:
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8


    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price


    @price.setter
    def price(self, value):
        self.original_price = value


    @price.deleter
    def price(self):
        del self.original_price



if __name__ == '__main__':
    obj = Goods()
    print(obj.price)  # 自动执行 @property 修饰的 price()方法，并获取返回值
    obj.price = 200  # 自动执行 @price.setter 修饰的 price()方法，并将 100 赋值给方法的参数value
    print(obj.price)
    del obj.price  # 自动执行 @price.deleter 修饰的 price()方法，
    print(obj.price)  # AttributeError: 'Goods' object has no attribute 'original_price'
