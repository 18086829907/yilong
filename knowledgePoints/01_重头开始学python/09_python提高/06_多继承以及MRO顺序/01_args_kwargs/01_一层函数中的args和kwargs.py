def fun(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


fun(1,2)  # 至少将非*号参数传完
print('-'*5)
fun(1, 2, '多余的无名参数1传入args', '多余的无名参数2传入args', parameter1='多余的关键字参数1传入kwargs', parameter2='多余的关键字参数2传入kwargs')

#调用函数时，多传入的没有名字的参数，全部添加到一个元组中，并用args变量名指向这个元组
#调用函数时，多传入的有名字的参数，全部添加到一个字典中，并用kwargs变量名指向这个字典