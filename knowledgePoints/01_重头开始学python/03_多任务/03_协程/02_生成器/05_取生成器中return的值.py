def create_fibonacii(n):
    current = 0
    a, b = 0, 1
    while current < n:
        yield a
        a, b = b, a+b
        current += 1
    return 'ok'


obj = create_fibonacii(5)


#解决Stoplteration：
while True:
    try:
        num = next(obj)
        print(num)
    except Exception as e:
        print(e.value)    #是因为捕获异常而停止的程序，因此在异常对象e的value属性中就保存了return的值
        break