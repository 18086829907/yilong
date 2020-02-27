#用函数生成生成器
#   只要保证函数里有yield，函数就是一个生成器
def create_fibonacii(n):
    current = 0
    a, b = 0, 1
    while current < n:
        yield a    # 如果一个函数中有yield，不管yield的位置在哪儿，这个函数就不在是函数，而是一个生成器的模板
        a, b = b, a+b
        current += 1

# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
obj = create_fibonacii(10)


for i in obj:
    print(i)

#程序流程说明
#   1、create_fibonacii(10),看似是调用函数，其实它在生成一个对象（生成器对象，因为函数中有yield）
#   2、for 判断 obj是否为iterable，因为obj是生成器，生成器是特殊的迭代器，因此可以被循环
#   3、for调用obj对象，此时开始执行create_fibonacii函数，逐行执行其内的代码
#   4、当执行到yield语句时，程序暂停于此，并且将yield后面的值传给for中的i
#   5、执行for中的代码，当for中的代码执行完毕后，for开始循环，又调用obj对象
#   6、此时，进程从yield暂停的位置向下执行，当在while循环中有遇到yield时，程序又暂停，yield返回值
#   7、又开始执行for循环中的代码。。。