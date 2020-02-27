def create_fibonacii(n):
    current = 0
    a, b = 0, 1
    while current < n:
        yield a    # 如果一个函数中有yield，不管yield的位置在哪儿，这个函数就不在是函数，而是一个生成器的模板
        a, b = b, a+b
        current += 1

# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
obj1 = create_fibonacii(10)
obj2 = create_fibonacii(10)

num = next(obj1)
print('obj1的第1个值：',num)

num = next(obj1)
print('obj1的第2个值：',num)

num = next(obj2)
print('obj2的第个1值：',num)

num = next(obj1)
print('obj1的第3个值：',num)

num = next(obj1)
print('obj1的第4个值：',num)


#结论生成器模板可以创建多个独立的对象，都可以用for和next对其取值