from card import Card
from user import User
from journal import Journal
import random
from myClass.mobilePhon import MobilePhone
import os
import pickle
import datetime

class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers

    #开户
    def createUser(self):
        #目标：往用户列表中存键值对（键：卡号，值：用户对象）
        name = input('请输入您的姓名：')
        idCard = input('请输入您的身份证号码：')
        phone = input('请输入您的电话号码：')
        prestoreMoney = float(input('请输入您的预存款金额：'))
        if prestoreMoney < 0:
            print('预存款输入有误！！开户失败')
            return -1 #return有结束函数的功能
        onePassword = input('请设置密码：')
        #验证密码
        if not self.chackPassword(onePassword): #这里是在调用实例化对象的方法，在自己函数内部需要加self
            print('密码验证错误，开户失败！')
            return 0
        #所有需要的信息采集完毕
        #生成卡号
        cardId = self.randomCardId()
        #创建卡对象
        card = Card(cardId, onePassword, prestoreMoney)
        #创建日志对象
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        journal = Journal(nowTime)
        #创建用户对象
        user = User(name, idCard, phone, card, journal) #创建用户对象（名字， 身份证号， 电话，卡的对象）
        #将用户存到字典中
        self.allUsers[cardId] = user
        self.writeAllUers()
        print('****开户成功****')
        print('您的卡号为：%s\n您的名字：%s\n' % (cardId, name))

    #查询
    def searchUserInfo(self):
        #验证卡号、是否锁卡、密码
        user = self.verification()
        if user == 0:
            return 0
        print('姓名：', user.name)
        #隐藏身份证中间值
        idCard = user.idCard
        str_ = ''
        sum_ = 0
        for i in idCard:
            if sum_ < 6:
                str_ += i
            elif sum_ >= 7 and sum_ < 14:
                str_ += '*'
            elif sum_ >= 14:
                str_ += i
            sum_ += 1
        print('身份证号：', str_)
        print('电话：', user.phone)
        print('余额：', user.card.cardMoney)
        print('取钱记录：\n' + user.journal.changeMoneyOperationjournal)

    #取钱
    def getMoney(self):
        user = self.verification()
        if user == 0:
            return 0
        #取款
        sum_ = 0
        while True:
            sum_ += 1
            if sum_ >= 3:
                while True:
                    option = input('是否退出：(是/否)')
                    if option == '是':
                        return 0
                    elif option == '否':
                        break
                    else:
                        print('请输入‘是’或‘否’')
                        continue
            money = int(input('请输入取款金额：'))
            if money > user.card.cardMoney:
                print('余额不足')
                continue
            if money <= user.card.cardMoney:
                break
        user.card.cardMoney -= money
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user.journal.changeMoneyOperationjournal += '{} 取钱金额：{}\n'.format(nowTime, money)

        self.writeAllUers()
        print('****取款成功****\n余额为：%d' % user.card.cardMoney)

    #存钱
    def saveMoney(self):
        user = self.verification()
        if user == 0:
            return 0
        # 存款
        money = int(input('请输入存款金额：'))
        user.card.cardMoney += money
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user.journal.changeMoneyOperationjournal += '{} 存钱金额：{}\n'.format(nowTime, money)
        self.writeAllUers()
        print('存款成功')

    #转账
    def transferMoney(self):
        user1 = self.verification()
        print('对方卡号')
        if user1 == 0:
            return 0
        function = 'transferMoney'
        user2 = self.verification(function)
        print('****请核对****')
        if user2 == 0:
            return 0
        getMoneyName = user2.name
        getMoneyName = '*' + getMoneyName[1:]
        print('收款人姓名：%s' % getMoneyName)
        option = input('是否转账：')
        if option == '是':
            sum_ = 0
            while True:
                sum_ += 1
                if sum_ > 3:
                    while True:
                        option = input('是否退出')
                        if option == '是':
                            return 0
                        elif option == '否':
                            break
                        else:
                            print('请输入‘是’或‘否’')
                            continue
                transferMoney_ = float(input('请输入转账金额：'))
                if transferMoney_ <= user1.card.cardMoney:
                    user1.card.cardMoney -= transferMoney_
                    user2.card.cardMoney += transferMoney_
                    break
                else:
                    print('余额不足，转款失败')
                    continue
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user1.journal.changeMoneyOperationjournal += '{} 转账金额：{} 对方卡号：{}\n'.format(nowTime, transferMoney_, user1.idCard)
            user2.journal.changeMoneyOperationjournal += '{} 转入金额：{} 对方卡号：{}\n'.format(nowTime, transferMoney_, user2.idCard)
            self.writeAllUers()

    #修改密码
    def changePassword(self):
        user = self.verification()
        if user == 0:
            return 0
        newPassWd = input('请输入新密码')
        if not self.chackPassword(newPassWd, 'changePassword'):
            print('新密码验证失败,改密失败')
            return 0
        user.card.cardPassword = newPassWd
        self.writeAllUers()

    #锁卡
    def lockUser(self):
        # 验证卡号、锁卡、密码
        user = self.verification()
        if user == 0:
            return 0
        #验证身份证
        if self.verificationIdCard(user) == 0:
            return 0
        #锁卡
        user.card.cardLock = True
        self.writeAllUers()
        print('锁定成功')

    #解锁
    def unlockUser(self):
        function = 'unlockUser'
        #验证卡号、锁卡、密码
        user = self.verification(function)
        if user == 0:
            return 0
        #验证身份证
        if self.verificationIdCard(user) == 0:
            return 0
        #解锁
        user.card.cardLock = False
        self.writeAllUers()
        print('解锁成功')

    #补卡
    def newCard(self):
        user = self.verification()
        if user != 0:
            if self.verificationIdCard(user) == 0:
                return 0
            runNumber = self.randomCardId()
            self.allUsers[runNumber] = self.allUsers.pop(user.card.cardId)
            user.card.cardId = runNumber
            self.writeAllUers()
            print('补卡成功，卡号为：%s' % user.card.cardId)

    #销户
    def killUser(self):
        user = self.verification()
        if user != 0:
            if self.verificationIdCard(user) == 0:
                return 0
            self.allUsers.pop(str(user.card.cardId))
            print('注销成功！')
            self.writeAllUers()

    #验证卡号、是否锁卡、密码
    def verification(self, function='other'):
        cardId = input('请输入卡号：')
        #验证是否存在该卡号
        user = self.allUsers.get(cardId)
        if not user: #如果没有这个用户信息，执行if语句
            print('该卡号不存在，查询失败')
            return 0
        #验证是否锁卡
        if function != 'unlockUser':
            if user.card.cardLock:
                print('此卡已锁定！请解锁后再进行其他操作')
                return 0
        #验证密码
        if function != 'transferMoney':
            if not self.chackPassword(user.card.cardPassword):
                user.card.cardLock = True
                print('密码输入错误，此卡已锁定！请解锁后再进行其他操作')
                self.writeAllUers()
                return 0

        '''
        #验证验证码，验证码错误，不让锁卡
        mobilePhon = MobilePhone(user.phone)
        mobilePhon.sendMassage()
        number = input('请输入验证码：')
        if MobilePhone.runNumber != number:
            print('验证码输入错误，操作失败')
            return 0
        '''
        return user

    #验证密码
    def chackPassword(self, realPassword, function='other'):
        if function != 'changePassword':
            for i in range(3):
                if i == 0:
                    tempPassword = input('请输入密码：')
                if i != 0:
                    tempPassword = input('请再次输入密码：')
                if tempPassword == realPassword:
                    return True
            return False
        else:
            for i in range(3):
                if i == 0:
                    tempPassword = input('请再次输入新密码：')
                if i != 0:
                    tempPassword = input('新密码不正确，请再次输入新密码：')
                if tempPassword == realPassword:
                    return True
            return False

    # 验证身份证
    def verificationIdCard(self, user):
        # 验证身份证，身份证错误，不让解锁
        tempIdCard = input('请输入您的身份证号：')
        if user != 0:
            if tempIdCard != user.idCard:
                print('身份证号输入错误，操作失败')
                return 0

    #生成卡号
    def randomCardId(self):
        strCard = ''
        while True:
            for i in range(18):
                # 随机生成一个数字
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                strCard += ch
            if not self.allUsers.get(strCard): #如果用户字典中的卡号不重复
                return strCard #则返回生成的字符串

    #读取用户信息文件
    def readAllUers(self):
        filePath = os.path.join(os.getcwd(), 'allUser.txt')
        with open(filePath, 'rb') as f:
            allUser = pickle.load(f)
        return allUser

    #记录用户信息文件
    def writeAllUers(self):
        filePath = os.path.join(os.getcwd(), 'allUser.txt')
        with open(filePath, 'wb') as f:
            pickle.dump(self.allUsers, f)
        print('用户信息已保存')