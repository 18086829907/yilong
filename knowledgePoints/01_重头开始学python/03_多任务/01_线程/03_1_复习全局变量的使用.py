num1 = 100
num2 = 100
nums = [1,2,3]

def mytest1():
    global num1
    num1 += 100

# def mytest2():    #不成立
#     num2 += 100

def mytest3():
    nums.append(4)    #可以不用加global的原因是未改变nums变量的指向，仅仅是修改了nums变量指向的值。

print(num1)
print(num2)
print(nums)

mytest1()
# test2()
mytest3()

print(num1)
# print(num2)
print(nums)

#函数中修改全部变量，到底是否需要使用global进行说明
#   看是否对全部变量的指向进行了修改
#       如果修改了指向，即让全局变量指向了一个新的地方，那么必须使用global
#       如果仅仅修改了其指向的空间中的数据，则不用必须使用global