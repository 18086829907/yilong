from commodity import Commodity
class Trousers(Commodity):
    def __init__(self, name, price, stock, cost, id):
        Commodity.__init__(self, name, price, stock, cost, id)
