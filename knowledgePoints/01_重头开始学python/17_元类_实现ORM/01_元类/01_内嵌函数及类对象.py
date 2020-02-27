# 1、内嵌函数
#     没有定义就可以调用的函数
#     原理是运行时，python解释器自动加载一个模块，模块中就对这些内建函数进行了定义
'''
print()
'''
# 2、globals()
#     返回一个字典，字典中key是变量名，value是对应的对象（包括字符串、数字、元组、列表、集合、字典、函数，类）
#     只要在字典key中的变量名都可以被调用
'''
a = '123'
b = 123
c = (1,2)
d = [1,2]
e = {1,2}
f = {'a':'b'}
def AAA():
    pass
class AAAAAA():
    pass
for key,value in list(globals().items()):
    print(key,value)
'''

# 3、对变量取值或调用的本质：
#   所有的全局变量python都存储于globals()的字典中
#       当对一个对象取值或调用时，本质是用变量名作为key到globals()返回的字典中去取value
#       字典的特性是：key不能相同，value可以相同
#       因此，变量名不能相同，不同的变量名可以指向同一个对象

# 4、取出内嵌模块
#   在globals()返回的字典中有一个key是__builtins__
#   __builtins__对应着builtins模块，这个模块中就包含了所有的内嵌函数
'''
myBuiltins = globals()['__builtins__'] # myBuiltins此时就是内嵌函数的模块
'''

# 5、查看模块对象中的函数名以及其所对应的对象的方法：
#   语法：模块.__dict__
#   实例：myBuiltins.__dict__
#   返回：所有内嵌函数的函数名和函数对象的字典
'''
for i,j in myBuiltins.__dict__.items():
    print(i,':',j)
'''
# 6、查看所有的内嵌函数名

name_inner_built = list(globals()['__builtins__'].__dict__.keys())
for i in name_inner_built:
    print(i)


# 7、验证内嵌函数
# globals()['__builtins__'].__dict__['print']('123')

# 8、因此
#   内嵌函数的查询路径，先从globals()的字典中去找
#       如果在globals()的字典中有值
#           则取出对象进行调用
#       如果没有值
#           再从内嵌模块中的字典中去找
#               如果找到
#                   则取出对象进行调用
#               如果没找到
#                   报错未定义这个变量
'''
if print in globals().keys():
    print = globals()['print']
else:
    if print in globals()['__builtins__'].__dict__.keys():
        print = globals()['__builtins__'].__dict__['print']
    else:
        raise NameError
'''

# 9、类就是一个对象
'''
class OBJ(object):
    pass
myOBJ = OBJ()
print(myOBJ)
#<__main__.OBJ object at 0x7f8f2f33e748>
'''
# 在class定义一个类时，globals()的字典中就会有{'OBJ':<__main__.OBJ object at 0x7f8f2f33e748>}
#   因此验证了，类也是一个对象