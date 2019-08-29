'''
用户
类名：User
属性：姓名 身份证 电话号 卡
行为：

卡
类名：Card
属性：卡号 密码 余额
行为：

提款机
类名：ATM
属性：用户字典
行为：开户 查询 取款 存款 转账 改密 锁卡 解锁 补卡 销户 退出

管理员
类名：Admin
属性：账号 密码
行为：管理员界面 管理员验证（登陆、退出） 系统功能界面
'''

from admin import Admin
from atm import ATM
import time
import pickle
import os
def main():
    admin = Admin()  # 创建界面对象
    admin.printAdminView()  # 打印欢迎界面
    if admin.adminOption():  # 管理员登陆True 1 ; False 0
        return -1  #return有结束函数的作用

    allUser = {}
    atm = ATM(allUser)
    allUser = atm.readAllUers()
    atm = ATM(allUser)
    #存储所有用户的信息

    #print(atm.allUsers) #查看所有用户卡号
    while True:
        admin.printSysFunctionView()  #打印功能界面
        option = input('请输入您的操作：')
        if option == '1':
            atm.createUser() #开户

        elif option == '2':
            atm.searchUserInfo() #查询

        elif option == '3':
            atm.getMoney() #取款

        elif option == '4':
            atm.saveMoney() #存款

        elif option == '5':
            atm.transferMoney() #转账

        elif option == '6': #改密
            atm.changePassword()

        elif option == '7': #锁卡'
            atm.lockUser()

        elif option == '8': #解锁
            atm.unlockUser()

        elif option == '9': #补卡
            atm.newCard()

        elif option == '0': #销户
            atm.killUser()

        elif option == 't': #退出
            if not admin.adminOption():  #not 0 ：True
                # 将当前系统中的用户信息保存到文件中
                atm.writeAllUers()
                return 0

        time.sleep(5)

if __name__ == '__main__':
    main()