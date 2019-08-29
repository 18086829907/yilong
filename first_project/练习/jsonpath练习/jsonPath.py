import jsonpath
import json
obj = json.load(open('book.json', 'r', encoding='utf8'))

# 从根部开始，store下面的book所有的字典值中的autor的字典值
# [*]代表查询列表中所有元素，book下面是一个列表，列表中存放了每本书的数据，因此[0]表示第一本数的数据，以此类推
# result = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(result)
#
# 从根部开始，所有位置查询作者
# 返回列表，列表元素为所有author的字典值
# result = jsonpath.jsonpath(obj, '$..author')
# print(result)
#
# 查询store下面所有节点，即book和bicycle，,[[{},{}...],{}]
# 返回列表，列表中有两个元素，第一个元素是book的字典值，第二个元素是bicyle的字典值
# result = jsonpath.jsonpath(obj, '$.store.*')
# print(result)
#
# 查询store下面所有的price
# 返回列表，列表中有price为键的字典值值，
# result = jsonpath.jsonpath(obj, '$.store..price')
# print(result) --> [8.95, 12.99, 8.99, 22.99, 19.95]
#
# 从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行索引（索引从0开始）
# 返回列表，列表元素为book的第三个字典值，
# result = jsonpath.jsonpath(obj, '$..book[2]')
# print(result)
#
# 从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行匹配操作，即[]也是一个列表，列表元素的数值对应book的值
# 返回列表，列表元素为book的第0个、第1个、第2个、第3个字典值，
# result = jsonpath.jsonpath(obj, '$..book[0,1,2,3]')
# print(result)
#
# 从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行切片操作
# 返回列表，列表元素为book的前3个字典值，
# result = jsonpath.jsonpath(obj, '$..book[:3]')
# print(result)
#
# 从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行索引操作，索引值为当前列表的长度-1的值
# 返回列表，列表元素为book的最后一个字典值，
# result = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(result)
#
# 从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行切片操作，索引值为当前列表中包含isbn的值
# 返回列表，列表元素为book的包含了isbn的字典值，
# result = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(result)
#
# 从根部开始，查询所有位置的book，book的值是一个列表，可以用列表操作符对其进行匹配操作，索引值为当前列表中价格小于10元的值
# 返回列表，列表元素为book的价格小于10元的字典值，
# result = jsonpath.jsonpath(obj, '$..book[?(@.price<10)]')
# print(result)
#
# 从根部开始，查询所有位置的所有的字典值
# 返回列表，第一个列表元素为第一层的字典值，即store的字典值；第二个元素为第二层第一个的字典值，即book的字典值；第三个元素为第二层第二个的字典值；第四个是第三层的第一个字典值
# result = jsonpath.jsonpath(obj, '$..*')
# print(result)