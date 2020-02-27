#id(a)  # 功能:返回变量所指向的数据所在内存空间地址
#import copy
#c = copy.copy(a)  # 浅拷贝
#c = copy.deepcopy(a)  # 深拷贝

#浅拷贝
#   浅拷贝：赋值实现浅拷贝
#         a = [1,2,3]
#         b = a
#         print(id(a), id(b))  # id(a) == id(b), a和b都指向同一个列表数据

#   浅拷贝：copy.copy()
#         import copy

#       实验1
#         a = '1'
#         b = copy.copy(a)
#         print(id(a),id(b))  # id(a) == id(b), 当参数a指向字符串时，copy.copy()的返回值b指向原数据

#       实验2
#         a = (1,2)
#         b = copy.copy(a)
#         print(id(a),id(b))  # id(a) == id(b), 当参数a指向元组时，copy.copy()的返回值b是指向原数据的

#       实验3
#         a = [1,2]
#         b = copy.copy(a)
#         print(id(a),id(b))  # id(a) != id(b), 当参数a指向列表时，copy.copy()的返回值b不指向原列表数据，而是指向新的列表数据

#       实验4
#         a = (1,2)
#         b = (3,4)
#         c = (a,b)
#         d = copy.copy(c)
#         print(id(c),id(d))  # id(c) == id(d), 当参数c指元组时，copy.copy()的返回值d指向原列表数据，而是指向新的列表数据
#         print(id(a),id(d[0]))  # id(a) == id[d[0]]，a和d[0]都指向原列表数据
#         print(id(b),id(d[1]))  # id(b) == id[d[1]]，b和d[1]都指向原列表数据

#       实验5
#         a = [1,2]
#         b = [3,4]
#         c = [a,b]
#         d = copy.copy(c)
#         print(id(c),id(d))  # id(c) != id(d), 当参数c指向列表时，copy.copy()的返回值d不指向原列表数据，而是指向新的列表数据
#         print(id(a),id(d[0]))  # id(a) == id[d[0]]，a和d[0]都指向原列表数据
#         print(id(b),id(d[1]))  # id(b) == id[d[1]]，b和d[1]都指向原列表数据
#         #注意：copy.copy()
#           当传入参数是指向列表，而列表中又存放了引用时，copy.copy()的返回值会指向一个新的列表，但是这个列表中的引用，任然是指向其原数据

#       实验6
#         a = [1,2]
#         b = [3,4]
#         c = (a,b)
#         d = copy.copy(c)
#         print(id(c),id(d))  # id(c) == id(d), 当参数c指向元组时，copy.copy()的返回值d指向c指向的元组
#         print(id(a),id(d[0]))  # id(a) == id[d[0]]，a和d[0]都指向原列表数据
#         print(id(b),id(d[1]))  # id(b) == id[d[1]]，b和d[1]都指向原列表数据

#深拷贝
#       import copy
#
#       实验1
#         a = [1,2]
#         b = copy.deepcopy(a)
#         print(id(a),id(b))  # id(a) != id(b),当参数指向的是列表时, copy.deepcopy()返回值b指向新的列表数据

#       实验2
#         a = (1,2)
#         b = copy.deepcopy(a)
#         print(id(a),id())  # id(a) == id(b), 当参数指向的是元组时，copy.deepcopy()返回值b指向的是原数据

#       实验3
#         a = [1,2]
#         b = [3,4]
#         c = [a,b]
#         d = copy.deepcopy(c)
#         print(id(c),id(d))  # id(c) != id(d), 当参数指向的是列表时, copy.deepcopy()返回值d指向新的列表数据
#         print(id(a),id(d[0]))  # id(a) != id[d[0]], 说明a和d[0]指向不同一数据, 即copy.deppcopy()将引用指向的列表数据, 也重新复制了一份
#         print(id(b),id(d[1]))  # id(b) != id[d[1]], 说明a和d[1]指向不同一数据, 即copy.deppcopy()将引用指向的列表数据, 也重新复制了一份
#         #注意：当用copy.deepcopy()时，如果发现传入列表中有引用，则会将这个引用指向的数据拷贝一份，而不是只拷贝这个引用

#       实验4
#         import copy
#         a = [1,2]
#         b = [3,4]
#         c = (a,b)
#         d = copy.deepcopy(c)
#         print(id(c), id(d))  # id(c) != id(d), 当参数指向元组，而元组中有指向列表的引用，copy.deepcopy()的返回值d指向一个新的元组数据
#         print(id(a), id(d[0]))  # id(a) != id(d[0]), 当参数指向元组，而元组中有指向列表的引用，copy.deepcopy()的返回值d指向一个新的元组数据，元组中的引用也指向一个新的列表数据
#总结：
#   浅拷贝：不同的引用指向相同的数据，只要改变原数据，其所有的引用在被调用时，都会显示数据有改变
#   深拷贝：不同的引用指向不同的数据，其中一个数据发生变化，不影响其他引用指向的数据
#
#   copy.copy()：如果拷贝的数据类型全是不可变的，copy.copy()的返回值一定指向原数据
#   copy.deepcopy()：如果拷贝的数据中存在可变数据类型的指引，copy.deepcopy()一定递归的方式，将所有的数据深拷贝一份，包括不可变数据类型（元组），否则其返回值也是指向原数据
