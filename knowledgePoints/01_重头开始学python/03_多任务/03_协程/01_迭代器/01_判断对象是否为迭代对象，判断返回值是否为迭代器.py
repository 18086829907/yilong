#迭代器可以用来减少内存空间，还能够知道怎么生成数据的方式
# isinstance(obj, class)
# 功能
#   判断参数1是否与参数2的相关（子类，多层继承）
# 参数
#   obj：对象或返回值
#   class：类名


from collections import Iterable    #可迭代对象
print(isinstance([1,2,4], Iterable))    #判断[1,2,4]是否可迭代


from collections import Iterator    #迭代器
print(isinstance(iter([1,2,4]), Iterator))    #iter()函数，可以调用list对象中的__iter__()函数，其返回值为是迭代器对象
