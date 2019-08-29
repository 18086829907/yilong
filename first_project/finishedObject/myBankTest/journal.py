import pickle
import os
class Journal(object):
    def __init__(self, nowTime, journal=''):
        self.creatTime = nowTime #创建卡的时间
        self.changeMoneyOperationjournal = '开户时间：{}\n'.format(self.creatTime) + journal
