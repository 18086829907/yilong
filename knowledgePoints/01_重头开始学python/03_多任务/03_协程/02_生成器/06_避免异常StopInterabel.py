def create_fibonacii(n):
    current = 0
    a, b = 0, 1
    while current < n:
        yield a    # 如果一个函数中有yield，不管yield的位置在哪儿，这个函数就不在是函数，而是一个生成器的模板
        a, b = b, a+b
        current += 1


obj = create_fibonacii(50)    #当生存器中值循环1此，即只生成了一个值，但是需要取第二个值时就会报错


# num = next(obj)
# print('obj1的第1个值：',num)
#
# num = next(obj)    #会报错
# print('obj1的第2个值：',num)


#解决Stoplteration：
while True:
    try:
        num = next(obj)
        print(num)
    except Exception as e:
        break