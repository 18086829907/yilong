def create_fibonacii(n):
    print('--1--')
    current = 0
    a, b = 0, 1
    while current < n:
        print('--2--')
        yield a    # 如果一个函数中有yield，不管yield的位置在哪儿，这个函数就不在是函数，而是一个生成器的模板
        print('--3--')
        a, b = b, a+b
        current += 1
        print('--4--')

# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
obj = create_fibonacii(10)

num = next(obj)
print(num)

num = next(obj)
print(num)
