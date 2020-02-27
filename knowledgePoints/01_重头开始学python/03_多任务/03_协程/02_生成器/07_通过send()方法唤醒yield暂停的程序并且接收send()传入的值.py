def create_fibonacii(n):
    current = 0
    a, b = 0, 1
    while current < n:
        k = yield a
        print('新传入的值为：',k)
        a, b = b, a+b
        current += 1

obj = create_fibonacii(10)
print(next(obj))
print(obj.send('123'))

#流程
#   1、生成器模板创建一个生成器对象obj
#   2、next调用obj，执行create_finonacii函数中的代码
#   3、遇到k = yield a时，先执行等号右边，yield使函数内的进程暂停，并且把a的值传给next中的obj，next就能返回obj的值，并且能打印这个值
#   4、obj.send()又唤醒函数内的进程，并且将yield a替换为send传入的参数值。即，执行k = yield a，现在执行的是=号左边，即 k = '123'
#   5、就能打印出k的值了

#注意
obj1 = create_fibonacii(2)
obj1.send('哈哈')    #程序会报错，因为第一次启动，是从函数的第一句话开始执行，此处没有任何变量来接收'哈哈'这个值，因此会报错

#如果第一次实在想用send，参数换成None
obj1 = create_fibonacii(2)
obj1.send(None)

#一般第一次取值都用next()

#那什么时候用send呢？一般需要将值传入函数时使用