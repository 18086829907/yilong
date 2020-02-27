# 多模块开发套路
#   main.py  # 用于调用其他模块
#   各个小功能放到单独的模块中
#   公用的数据单独放到一个模块中

# 易错点
#   a.py
#       from b import d
#       improt c
#       d = True
#       c.fun()
#   b.py
#       d = False
#   c.py
#       from b import d
#       def fun()
#           print(d)
#   在a.py中通过from b import c
#       当使用这种方式在a.py中导入b.d时，其实是在a.py本地定义了一个新的全局变量a.d来指向了b.d中的False
#           在a.py中，对a.d = True，其实是让a.d指向了True，而没有修改b.d指向False
#               再调用c.fun()打印，结果是False。因为c.d指向的b.d的值，即指向False，
# 为了避免以上错误，尽量使用import b，如果要修改b.d的指向，则用b.d = True