#【day5】创建变量、删除变量
#变量概述
#   程序可操作的存储空间的名称 or 程序运行期间能改变的数据 or 每个变量都有特定的类型
#作用：
#   将不同类型的数据存储到内存
#定义变量
#   变量名 = 初始值
#       初始值：为了确定变量的数据类型
#   age = 10
#数据的存储
#   变量 = 数据值
#注意：在使用变量前必须定义，否则会报错

'''
age = 18
print('age = ' , age)
'''
'''
del age
print(age) #nameerror:age is not definded
'''
'''
name = 'mia'
age = 9
print(name)

name = 'zengxiaoxuan'
age = 10
print(name)
'''

'''
name = 'mia'
del name
print(name)
'''

#【day6】连续定义变量
'''
num1 = 1
num2 = num1
num3 = num2
'''
'''
num1 = num2 = num3 = 1
print(num1, num2, num3)
'''
'''
money1 = 100
money2 = 100
money3 = 100
'''
#当赋的值相同，又需要赋值给多个变量时，需要用到连续定义变量
#格式：变量名1 = 变量名2 = 变量名3 = ..... = 初始值
'''
money1 = money2 = money3 = 100
print(money1, money2, money3)
'''

#【day7】交互式定义变量
'''
num1, num2 = 1, 2
print(num1, num2)
'''
#当赋值不同时，又需要赋值给多个变量时，需要用到交互式定义变量
#格式：变量名1， 变量名2 = 初始值1， 初始值2
'''
money1, money2 = 100, 1000
print(money1, money2)
'''