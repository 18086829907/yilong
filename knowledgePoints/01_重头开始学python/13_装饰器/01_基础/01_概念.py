# 首先弄明白
# ---第一波---
'''
def foo():
    print('foo')

foo  # 表示是foo变量指向了函数
foo()  # 表示是执行foo函数
'''
# ---第二播---
'''
def foo():
    print('foo')
foo = lambda x: x+1
foo(1)  # 执行lambda表达式，而不再是原来的foo函数，因为foo这个名字被重新指向了另外一个匿名函数
'''

# 再理解理解
# ---基础平台提供如下功能---
def f1():
    print('1')
def f2():
    print('2')
def f3():
    print('3')
def f4():
    print('4')
# ---业务部门A调用基础平台开发的功能---
f1()
f2()
f3()
f4()
# ---业务部门B调用基础平台开发的功能---
f1()
f2()
f3()
f4()

# 随着业务发展，业务部门AB的新员工，来了就调这些接口，基础平台的老大就让基础平台的职工B去设置权限
#   B的做法是跑到AB部门去，找到他们的员工，让他们自己加权限，但是业务部门的人答应的好好的，但实际工作时没有去加权限，B就被开了
# 之后，基础平台的老大，又让BB去做这事
#   BB的做法
def f1():
    #权限验证1
    #权限验证2
    #权限验证3
    print('1')
def f2():
    # 权限验证1
    # 权限验证2
    # 权限验证3
    print('2')
def f3():
    # 权限验证1
    # 权限验证2
    # 权限验证3
    print('3')
def f4():
    # 权限验证1
    # 权限验证2
    # 权限验证3
    print('4')
# ---业务部门A调用基础平台开发的功能，调用方式不变---
f1()
f2()
f3()
f4()
# ---业务部门B调用基础平台开发的功能，调用方式不变---
f1()
f2()
f3()
f4()

# 过了一周，BB又被开了
#   因为，如果接口有一万个，就要加一万行代码，如果一个接口需要加4条验证，就需要加4万行代码，冗余量太大
# 任务又交给BBB
def check_login():
    #验证权限
    pass
def f1():
    check_login()
    print('1')
def f2():
    check_login()
    print('2')
def f3():
    check_login()
    print('3')
def f4():
    check_login()
    print('4')
# ---业务部门A调用基础平台开发的功能，调用方式不变---
f1()
f2()
f3()
f4()
# ---业务部门B调用基础平台开发的功能，调用方式不变---
f1()
f2()
f3()
f4()

# 老大看他写的还是有些希望了，于是找他谈话，你做的相对其他人已经很好了，但是
#   写代码必须遵循开放封闭原则，不允许对已经写好的代码进行修改
# 老大给到他的解决办法
def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        func()
    return inner
@w1
def f1():
    check_login()
    print('1')
@w1
def f2():
    check_login()
    print('2')
@w1
def f3():
    check_login()
    print('3')
@w1
def f4():
    check_login()
    print('4')
# ---业务部门A调用基础平台开发的功能，调用方式不变---
f1()
f2()
f3()
f4()
# ---业务部门B调用基础平台开发的功能，调用方式不变---
f1()
f2()
f3()
f4()