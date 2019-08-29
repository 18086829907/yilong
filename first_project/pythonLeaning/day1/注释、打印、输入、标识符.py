#【day1】注释(已授)
#
'''
注释
'''

#【day2】print()打印(字符串，整数，浮点数，运算, 变量，布尔值)(已授)
'''
print('陈紫妍很漂亮')
print('陈紫妍很漂亮' , '陈迪希很漂亮')
print('陈紫妍的年龄是' , 9)
print(123)
print(123.123)
print(18+2)
print('18+2')
'''

'''
作业：复制
print('陈紫妍很漂亮' , '陈迪希很漂亮')
print('陈紫妍的年龄是' , 9)
print(123)
print(123.123)
print(18+2)
print('18+2')
'''

#【day3】input()作用：从外部获取变量的值(已授)
'''
age = input() #等待输入(),输入的内容可以保存在age里
print('陈紫妍的年龄是' , age)
'''
'''
age = input('请输入您的年龄:')
print('陈紫妍的年龄是' , age)
'''
'''
age = input('用户输入的所有内容都会是字符串')
'''
'''
#欢迎界面
print('欢迎来到大鱼吃小鱼')
name = input('请输入玩家的名字:')
age = input('请输入玩家的年龄：')
height = input('请输入玩家的身高：')
print('玩家的名字是：', name)
print('玩家的年龄是：', age)
print('玩家的身高是：', height)
'''

#【day4】标识符(已授)
#规则：
#   只能由字母、数字、下划线组成
#   开头不能是数字
#   不能是python的关键字(已经被定义了功能的字符)
#       import keyword print(keyword.kwlist)
#           ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#   区分大小写
#   见名知意思
#   驼峰原则
#        首单词小写，从第二个单词开始，首字母大写
#        cylIsGoodman
#作用：
#   给变量、函数等命名的

'''
作业判断一下是否为标识符
adb
12cdb
False
_abc
abc123
___nameAge
_abc_123
%$12ab
123abc
a_c_1
'''