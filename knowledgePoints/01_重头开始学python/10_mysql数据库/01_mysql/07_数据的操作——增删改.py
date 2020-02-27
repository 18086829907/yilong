#数据操作命令
#   增
#       全列插入
#           格式：insert into 表名 values(值1, 值2, 值3);
#           示例：insert into student values(0, 'tom', 1);
#           说明：主键是自动增长的，但是在全列插入时，需要用0来占位，插入成功后以实际数据为准，有默认值的列同样需要传入数据
#           占位符：0，null，default
#           枚举类型：下标从1开始
#       部分插入
#           格式：insert into 表名(列1, 列2) values(值1,值2);
#           示例：insert into student(name, age) values('jack', 2);
#           说明：
#       多行插入
#           全列插入
#               格式：insert into 表名 values(值1, 值2, 值3),(值1，值2, 值3);
#               示例：insert into student values(0, 'tom', 1), (0, 'jory', 1);
#           部分插入
#               格式：insert into 表名(列1, 列2) values(值1, 值2),(值1,值2),...;
#               示例：insert into student(name, age) values('mia', 9),('justin', 32);
#   删
#       物理删除
#           格式：delete from 表名 where 条件;
#           示例：delete from student where id=2;
#           注意：删除数据不加where条件视为选择全部数据，谨慎
#       逻辑删除
#           alter table student add is_delete bit default 0;  # bit 比特类型，注意mysql中查询时，is_dalete字段不会显示，因为mysql中只显示大于1字节的数据，而0=1bit，1字节=8比特，因此不会显示0
#           update student set is_delete=1 where id=1;
#   改
#       格式：update 表名 set 列1=值1, 列2=值2,... where 条件;
#       示例：update newstudent set age=10, address='chendu' where id=1;
#       注意：修改列数据不加where条件视为选在全部列数据，谨慎
#   查
#       格式：select * from 表名;
#       示例：select * from student;
#       说明：查询表中的全部数据