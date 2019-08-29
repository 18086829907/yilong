class Gun(object):
    def __init__(self, cartridge):
        self.cartridge = cartridge
    def shoot(self):
        if self.cartridge.bullteCount == 0:
            print('没子弹了')
        else:
            self.cartridge.bullteCount -= 1
            print('子弹还剩余%d' % self.cartridge.bullteCount)