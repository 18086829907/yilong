class MiniOS(object):
    def __init__(self, name):
        self.name = name
        self.apps = list()  # 安装的应用程序名称列表


    def __str__(self):
        return '{}安装的软件列表为{}'.format(self.name, str(self.apps))


    def install_app(self, app):  # app是形参，将来会被传入实例对象
        # 判断是否已经安装了软件
        if app.name in self.apps:
            print('已经安装了{}，无需再次安装'.format(app.name))
        else:
            app.install()  # 调用app实例对象的install.()方法，如果app实例对象重写过它的父类的install.()方法，则调用自己重写的install.()方法，如果传入的app实例对象没有重写install.()方法，则调用其父类的install.()方法
            self.apps.append(app.name)



class App(object):
    def __init__(self,name,version,desc):
        self.name = name
        self.version = version
        self.desc = desc


    def __str__(self):
        return '{}的当前版本是{}-{}'.format(self.name, self.version, self.desc)


    def install(self):
        print('将{}[{}]的执行程序复制到程序目录...'.format(self.name, self.version))



class Pycharm(App):
    pass



class Chrome(App):
    def install(self):  # 重写父类的install函数
        print('正在解压安装程序...')
        super().install()  # super()返回父类对象,super().install()是调用父类的install方法


if __name__ == '__main__':
    linux = MiniOS('linux')
    print(linux)  # 打印实例对象，会自动调用__str__方法，并打印__str__方法的返回值

    pycharm = Pycharm('PyCharm','1.0','python开发的IDE环境')
    chrome = Chrome('Chrome', '2.0', '谷歌浏览器')

    # linux.install_app(pycharm)
    linux.install_app(chrome)
    print(linux)


