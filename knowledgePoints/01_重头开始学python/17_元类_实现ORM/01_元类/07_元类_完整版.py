class A(object):
    num = 100

def print_a(self):
    print(self.num)

@staticmethod
def print_static():
    print('静态方法')

@classmethod
def print_class(cls):
    print(cls.num)

B = type('B', (A,) ,{'print_a':print_a,'print_static':print_static,'print_class':print_class})
b = B()
b.print_a()
b.print_static()
b.print_class()

# 元类创建类，类创建实例对象
print(b.__class__)  # 实例对象的创建者是类
print(b.__class__.__class__)  # 类的创建者是元类
print(b.__class__.__class__.__class__)  # 元类的创建者是元类
# 验证得知：元类有自我创建的能力