#遵循范式
# 第一范式：强调的是列的原子性，即列不能够再分成其他几列
#   error:
#             content
#             张三、10086、山东
#   correct:
#             name tel  addr
#             张三 10086 山东
# 第二范式：在满足第一范式的基础上，有两个条件，1、必须有主键，2、没有包含主键的列必须完全依赖主键，而不能只依赖一部分
#   error:
#             OrderID ProductID UnitPrice Discount Quantity ProductName
#             1001    7654      18.6      0.8      4        洗发水
#             错误原因：OrderID和ProductID都是主键，但是洗发水仅用ProductID就能描述清楚，即只依赖ProductID，也就是部分依赖主键
#   correct:
#             OrderID ProductID Discount Quantity
#             1001    7654      2        4
#             ProductID UniPrice ProductName
#             7654      18.6     洗发水
#             正确原因：第一个表，主键为OrderID ProductID，Discount Quantity这两个非主键的字段完全依赖于主键
#             正确原因：第二个表，主键为ProductID，UniPrice ProductName这两个非主键的字段完全依赖于主键
# 第三范式：满足第二范式的基础上，另外非主键列必须直接依赖与主键，不能存在传递依赖。即不能存在：非主键列A依赖非主键B，非主键B依赖主键的情况
#   error:
#             OrderID OrderDate             CustomerID CustomerName CustomerAddr    CustomerCity
#             1001    2017-01-01 12:12:12PM 12352      laowang      xx市xx县xx镇xx村 山东
#             错误原因：CustomerName、CustomerAddr、CustomerCity依赖于非主键CustomerID，而非主键CustomerID依赖主键OrderID
#   correct:
#             OrderID OrderDate             CustomerID
#             1001    2017-01-01 12:12:12PM 12352
#             CustomerID CustomerName CustomerAddr    CustomerCity
#             12352      laowang      xx市xx县xx镇xx村 山东