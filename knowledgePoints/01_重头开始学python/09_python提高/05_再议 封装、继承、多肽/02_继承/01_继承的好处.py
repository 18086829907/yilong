class A(object):
    def fun(self):
        print('1')  # 如果后期需要对fun函数进行修改，则只需要父类中的fun函数，即可完成对实例b的fun()方法的修改

class B(A):
    pass  # 如果这里是复制的fun函数，则需要手动修改两次

b = B()
b.fun()
