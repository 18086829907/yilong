class Person(object):
    def __init__(self, gun):
        self.gun = gun
    def fire(self):
        self.gun.shoot()
    def fillBullte(self, bullteCount):
        self.gun.cartridge.bullteCount = bullteCount #per.gun是Gun的实例化对象，可以调用属性cartridge，per.gun.cartridge又是Cartridge的实例化对象，因此可以调用其bullteCount的属性
