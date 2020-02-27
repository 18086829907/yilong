-- 索引是一个空间，它存在于表空间中。它存储着指向表中数据的引用指针。
-- 如果没有索引，数据库查询数据的方式是遍历，效率慢。
-- 如果有索引，查询数据的方式是先查索引，需要的数据是w开头的，那就找到w开头的索引所指向的数据，从这里开始遍历查，就能提高效率
-- 可以简单把索引理解为新华字典的目录

-- demo
create table test_index(title varchar(20));

-- python代码,给新建的数据表插入10万条数据
from pymysql import connet
def main():
    conn = connet(host='', ......)
    cursor = conn.sursor()
    for i in range(100000):
        cursor.execute("insert into test_index value ('ha-{}')".format(i))
    conn.commit()

-- 查询数据，检验是否插入成功
select count(*) from test_index;
select * from test_index;  -- 最后一条数据为：ha-99999

-- 开启运行时间检测
set profiling=1;
select * from text_index where title='ha-99999';  --查询最后一条数据
show profiles;  -- 查看查询所用时间；Duration字段记录了所用时间，单位为秒；结果为0.02906659

-- 为title字段创建索引
create index titel_index on test_index(title(20));  -- 20代表title的可变数据类型的长度，即varchar(20)中的20，如果title是int类型，则不需要传参

-- 再次查询，检验所用时间
select * from text_index where title='ha-99999';
show profiles;  -- 结果为0.00059275

-- 结论
-- 使用索引，查询结果快，不是用索引，查询结果慢

-- 索引的目的：提高查询的效率
-- 索引的原理：不断缩小查询关键词的搜索范围

-- sql中的索引是针对某个表中的数据中的某个字段而设立的
-- 语法 create index 索引名字 on 表名(字段());  -- 该字段的数据类型为数值类型，即int等
-- 语法 create index 索引名字 on 表名(字段(字符长度));  -- 该字段的数据类型为字符串类型，即varchar(20) or char(20)，字符长度就等于20
-- 创建了索引的字段，今后查询就快，没有创建索引的字段，查询就慢

-- 查看索引
show index from 表名;
-- 从结果中可以看到，所有的主键和外键都是自动添加索引的

-- 删除索引
drop index 索引名称 on 表名;

-- 创建索引的原则
-- 数据很大，而且这个字段经常用，就建索引，否则不建