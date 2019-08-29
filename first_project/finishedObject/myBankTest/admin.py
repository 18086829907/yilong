import time
class Admin(object):
    # 类属性可以在方法中被调用
    admin = 'admin'
    password = 'admin'

    def adminOption(self):
        inputAdmin = input('请输入管理员账号：')
        if inputAdmin != self.admin:
            print('账号输入有误！')
            return 1
        inputPassword = input('请输入管理员密码：')
        if inputPassword != self.password:
            print('密码输入有误！')
            return 1
        # 程序能执行到这里说明账号和密码都正确
        print('操作成功，请稍后......')
        time.sleep(2)
        return 0

    def printAdminView(self):
        print('************************************************')
        print('*                                              *')
        print('*                                              *')
        print('*             欢迎来到陈艺龙的私人银行             *')
        print('*                                              *')
        print('*                                              *')
        print('************************************************')


    def printSysFunctionView(self):
        print('************************************************')
        print('*                                              *')
        print('*        开户（1）                查询（2）       *')
        print('*        取款（3）                存款（4）       *')
        print('*        转账（5）                改密（6）       *')
        print('*        锁卡（7）                解锁（8）       *')
        print('*        补卡（9）                销户（0）       *')
        print('*                    退出(t)                    *')
        print('*                                              *')
        print('************************************************')