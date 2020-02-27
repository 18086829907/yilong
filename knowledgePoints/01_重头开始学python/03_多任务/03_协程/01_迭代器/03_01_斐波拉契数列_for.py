#斐波拉契数列
#   第一个是0，第二个时是1，其余的都是其前两个数之和
#       0,1,1,2,3,5,8,13
a = 0
b = 1

num = list()
for i in range(10):
    num.append(a)
    a, b = b, a+b

print(num)