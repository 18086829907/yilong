class Worker(object):
    def __init__(self, materialScience):
        self.materialScience = materialScience
    def bricklaying(self):
        if self.materialScience.brickCount < 0:
            print('没有砖了')
        else:
            self.materialScience.brickCount -= 20
            print('剩余砖%d' % self.materialScience.brickCount)
    def mixCement(self):
        if self.materialScience.cementCount < 0:
            print('没有水泥了')
        else:
            self.materialScience.cementCount -= 1
            print('剩余水泥%d' % self.materialScience.cementCount)