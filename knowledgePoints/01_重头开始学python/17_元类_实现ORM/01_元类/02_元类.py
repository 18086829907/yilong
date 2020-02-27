# 类是一个对象
#   它主要用于创建实例对象

# 元类是一个特殊的类，是创造所有对象的类（包括创建：字符串、数字、元组、列表、集合、字典、函数、类）
#   它主要用于创建对象

# 创建流程
#   元类 --> 类 --> 实例对象


# 使用函数动态创建不同的类
'''
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

MyClass = choose_class('foo')
print(MyClass)
print(MyClass())
'''

# 使用type创建类
# type(类名, 由父类名称组成的元组（主要是针对继承的情况，此参数可以为空）, 包含属性的字典（名称和值）)
'''
class myTest1:
    num1 = 1
    num2 = 2
'''
# 等价于
'''
myTest2 = type('myTest2', (), {'num1':1, 'num2':2})
'''
# 验证
'''
help(myTest1)
help(myTest2)
'''
# 说明：class创建类的本质其实都是通过type()创建的

# type其实是个类
'''
help(type)
'''

# type()会根据传入的参数不同，而返回不同类，它本身有是类，因此type()就是元类
#   type的第三个参数是一个字典，字典中key可以指向对象，指向的是字符串、数字对象即是类属性，指向的是函数对象即是类方法，