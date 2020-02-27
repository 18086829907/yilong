#查
#   基本语法
#       格式：select * from 表名;
#       示例：select * from newstudent;
#       示例：select name, age from newstudent;
#       示例：select name as a, age as b from newstudent;
#       示例：select tudent.name as a, newstudent.age as b from student, newstudent;
#       示例：select s.name as a, ns.age as b from student as s, newstudent as ns;
#       说明：
#           from关键字后面是表名，表示数据的来源
#           select后面写表中的列名，如果是*表示在结果集中显示表中的所有列
#           在select后面的列名部分，可以用as为列名起别名，这个别名显示在结果集中
#           如果要查询多个列，之间使用逗号分割
#   消除重复行 去重 查询不重复的数据
#       格式：select distinct 列名 from 表名;
#       示例：select distinct isDelete from student;
#   条件查询
#       语法
#           格式：select * from 表名 where 条件1;
#           示例：select * from newstudent where isDelete=0;
#       比较运算符
#           = select * from newstudent where age=30;
#           > select * from newstudent where id>3;
#           <
#           >=
#           <=
#           != select * from newstudent where address != 'chendu';
#       逻辑运算符
#           格式：select * from 表名 where 条件1 逻辑运算符 条件2;
#           and
#               示例：select * from newstudent where id>2 and gender=0;
#           or
#               示例：select * from newstudent where age<5 or age>20;
#           not
#               示例：select * from newstudent where not age>18 and gender=2;  # 不大于18岁，并且是女性
#               示例：select * from newstudent where not (age>18 and gender=2);  # 不在 18岁以上的女性 即 小于18岁的男性
#       模糊查询
#           like
#               格式：select * from 表名 where 列名 like '条件个数';
#               %
#                   示例：select * from newstudent where name like '陈%';  # 陈开头
#                   示例：select * from newstudent where name like '%陈%';  # 包含陈
#                   说明：匹配任意多个任意字符
#               _
#                   示例：select * from newstudent where name like '陈_';  #
#                   示例：select * from newstudent where name like '陈__';  # 只匹配2个任意字符
#                   说明：匹配一个任意字符
#               至少两个：select * from newstudent where name like '__%';
#           rlike
#               格式：select * from 表名 where 列名 rlike '';
#               示例：select name from student where name rlike '^周.*'  # 以周开头的
#               示例：select name from student where name rlike '^周.*轮$'  # 以周开头的，以伦结尾的
#       范围查询
#           in
#               格式：select * from 表名 where 列名 in (2, 9, 10);
#               示例：select * from newstudent where age in (2, 9, 10);
#               示例：select * from newstudent where age not in (2, 9, 10);
#               说明：在一个非连续的范围内
#           between .. and ..
#               格式：select * from 表名 where 列名 between 10 and 40;
#               示例：select * from newstudent where age between 10 and 40;
#               示例：select * from newstudent where age not between 10 and 40;
#               示例：select * from newstudent where not age between 10 and 40;
#               失败示例：select * from newstudent where age not (between 10 and 40);
#               说明：在一个连续范围内
#       空判断
#           is null
#           格式：select * from 表名 where 列名 is null;
#           示例：select * from newstudent where address is null;
#           注意：null 和 '' 是不同的,插入空值要用null
#       非空判断
#           is not null
#           格式：select * from 表名 where 列名 is not null;
#           示例：select * from newstudent where address is not null;
#           注意：null 和 '' 是不同的,插入空值要用null
#       优先级
#           小括号 not 比较运算符 逻辑运算符
#           注意：and比or优先级高，如果同时出现并希望先选or，需要结合括号()来使用
#   聚合
#       说明：为了快速得到统计的数据，提供了5个聚合的函数
#           count(*) 求数据总行数,括号中可以写*(任意一列)和列名
#               示例：select count(*) from newstudent;
#           max(列名) 求此列的最大值
#               示例：select max(age) from newstudent where gender=0;
#           min(列名) 求此列的最小值
#               示例：select min(age) from newstudent where gender=0;
#           sum(列名) 求此列的和
#               示例：select sum(age) from newstudent;
#           avg(列名) 求此列的平均值
#               示例：select avg(age) from newstudent;
#   分组
#       说明：
#           按照字段分组，表示此字段相同数据会被放到一个集合中。
#           分组后，只能查询出相同数据列，对于有差异的数据列无法显示在结果集中
#           可以对分组后的数据进行统计，做聚合运算
#       需求：查询男女生总数
#           格式：select 列,聚合(列) from 表名 group by 列;
#           示例：select gender, count(id) from newstudent group by gender;
#       需求：不同年龄组中的男女生总数
#           格式：select 列, 聚合(列) from 表名 group by 列,列...;
#           示例：select age, gender, count(id) from newstudent group by age, gender;
#       分组后的数据筛选
#           需求：从男女生总数中筛选出女生总人数
#           格式：select 列, 聚合(列) from 表名 group by 列, 列 having 列=1;
#           示例：select gender, count(id) from newstudent group by gender having gender=0;
#               having 与 where的区别
#                   where是对from后面指定的表进行筛选，属于对原始数据的筛选
#                   having是对group by的结果再进行筛选，默认值为1（可以将having理解为管道，前面select查询出来的结果，通过having传给后面的条件，实现结果再处理的目的）
#           需求：从不同年龄组中的男女生总数中再筛选出总人数大于等于3的组
#           格式：select 列, 聚合(列) as 别名 from 表名 group by 列, 列 having 别名>5;
#           示例：select age, gender, count(id) as total from newstudent group by age, gender having total>=3;
#   排序
#       格式：select * from 表名 order by 列1 asc|desc, 列2 asc|desc,...;
#       说明：
#           将数据按照列1进行排序，如果某些列1的值相同，则按照列2进行排序，如果某些列2的值相同，则按照列3进行排序...
#           默认按照从小到大排序（升序）
#           asc升序
#           desc降序
#       需求：将没有被删除的数据按照年龄的降序和id的降序排序
#       示例：select * from newstudent where isDelete=0 order by age;  # age 后面没有指定升序降序，默认为升序
#       示例：select * from newstudent where isDelete=0 order by age desc;
#       示例：select * from newstudent where isDelete=0 order by age desc, id desc;  # obder by 支持插入多个字段，当第一个排序条件出现相同值时，这些相同值再按照第二个排序条件进行排序
#   分页
#       格式：select * from 表名 limit [start,]count;
#       示例：select * from newstudent limit 2;  # 只显示2条数据
#       示例：select * from newstudent limit 0,3;  # 从0开始，即第一条开始，显示3条数据，即显示[0:3]
#       示例：select * from newstudent limit 1,3;  # 从1开始，即第二条开始，显示3条数据，即显示[1:4]
#       页码公式：select * from 表名 limit (第n页-1)*每页的个数, 每页的个数
#       示例：select * from newstudent limit (1-1)*20, 20  # 第一页的start=0，每页显示的个数count=20，
#       示例：select * from newstudent limit (2-1)*20, 20  # 第一页的start=20，每页显示的个数count=20，
#       说明：start为数据的索引，从0开始，
#       注意：where、order by、limit只能按照这样的顺序书写
#   关联
#       外键：
#           用来关联其他表的键值对
#           外键在多的表里面
#       建表语句
#           create table class(id int auto_increment primary key, name varchar(20) not null, stuNum int not null);
#       建关联表语句
#           格式：create table 表名(字段名1 类型 属性,... 外键字段名 类型 属性, foreign key(外键字段名) references 需关联表名(需关联字段名))
#           示例：create table students(id int auto_increment primary key, name varchar(20) not null, gender bit default 1, classId int not null, foreign key(classId) references class(id));
#       插入数据
#           insert into class values(0, '一班', 3),(0, '二班', 5),(0, '三班', 2),(0, '四班', 1);
#           insert into students values(0, 'justin', 1, 1), (0, 'xiaohua', 0, 1), (0, 'fangfang', 0, 1), (0, 'xianxian', 0, 2), (0, 'yuanyuan', 1, 2), (0, 'dingding', 1, 2), (0, 'qiqi', 1, 2), (0, 'saosao', 1, 2), (0, 'wanwan', 1, 3), (0, 'momo', 1, 3);
#       关联查询
#           格式：select 表1.段, 表2.段 from 表1 匹配方式 表2 on 表1.段=表2.段
#           格式：select 别名1.段, 别名2.段 from 表1 as 别名1 匹配方式 表2 as 别名2 on 别名1.段=别名2.段
#           匹配方式：inner join、left join、right join
#           关联查询分类
#               select * from 表1 inner join 表2 on 表1.段=表2.段
#                   说明：用表1.段中的值去与表2.段中逐一匹配，将匹配到了的数据拼接后，显示出来
#                   需求：查询所有学生名字以及所在班级名字
#                   示例：select students.name, class.name from class inner join students on class.id=students.classId;
#               select * from 表1 left join 表2 on 表1.段=表2.段
#                   说明：表1与表2匹配的行会出现在结果集中，外加表1中独有的数据，未对应的数据使用null填充
#                   需求：查询所有班级中还未招生的班级名称(左匹配，未匹配表1.Id = 表2.classId的数据)
#                   示例：select class.name,students.name from class left join students on class.id=students.classId;
#               表1 right join 表2：表A与表B匹配的行会出现在结果集中，外加表2中独有的数据，未对应的数据使用null填充
#   自关联
#       设计自关联表
#           设计省市区的自关联表
#               id name  p_id
#               1  四川省 null
#               2  成都市 1
#               3  高新区 2
#               4  双流区 2
#               5  简阳市 1
#           设计人事管理的自关联表
#               id name  p_id
#               1  陈总   null  # 最高级别
#               2  张经理 1  # 陈总的下属
#               3  李经理 1  # 陈总的下属
#               4  高经理 1  # 陈总的下属
#               5  明总   null  # 最高级别
#               6  王经理 5  # 明总的下属
#               7  小张   2  # 张经理的下属
#       当在一张表中，一个字段关联另一个字段，叫做自关联
#