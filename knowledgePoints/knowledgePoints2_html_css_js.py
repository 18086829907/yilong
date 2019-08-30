#【day148】mysql
#数据库：存数据
#下载数据库安装包：
#https://www.mysql.com/
#   DOWNLOADS
#       windows
#           MySQL Installer
#               Download
#                   no thanks, just start my download
#双击安装文件
#   等待出现欢迎界面（中间会有提示，全部选择是）
#       License Agreement
#           i accept the license terms
#           Next
#       Choosing a Setup Type
#           Custom 自定义
#           Next
#       Select Procducts and Features
#           MySQL Servers
#               MySQL Server
#                   MySQL Server 8.0
#                       MySQL Server 8.0.16 - X64
#                           右向绿色箭头
#                               MySQL Server 8.0.16 - X64
#                                   只选择MySQL Server, Server data files,其他全部取消勾选
#                                       Next
#       Installation
#           Execute 等待安装
#               Next
#       Product Configuration
#           Next
#       High Availability
#           Next
#       Type and Networking
#           Config Type：Development Computer
#           TCP/IP
#           Port 3306    座机的mysql端口：80
#           Open Windows Firewall Ports for network access
#           Next
#       Authentication Method
#           Next
#       Accounts and Roles
#           password:135cylpsx4848@ 数据库密码 mysql密码
#           Next
#       Windows Service
#           Windows Service Name: MySQL80 可以修改也可以不修改，它是服务器的名字
#           Next
#       Apply Configuration
#           Execute
#           if not LIBEAY32.dll:
#               管理员身份执行cmd
#                   Dism /Online /Cleanup-Image /ScanHealth #检查系统文件是否与官方系统文件一致
#                   if 有文件损坏：
#                       Dism /Online /Cleanup-Image /CheckHealth #修复损坏文件
#                   DISM /Online /Cleanup-image /RestoreHealth #与官方匹配不同程序还原为官方文件
#                   重启电脑
#                   sfc /SCANNOW
#           一直Next or Finished
#添加环境变量
#   复制C:\Program Files\MySQL\MySQL Server 8.0\bin
#   小娜搜索 环境变量
#       点击环境变量
#           系统变量
#               Path
#                   编辑
#                       新建
#                           粘贴
#                               确定确定确定
#启动mysql的服务
#   管理员身份启动cmd
#       net start mysql80
#黑屏终端连接数据库
#   启动非管理员cmd
#       mysql -u root(用户名) -p
#           输入密码：135cylpsx4848@
#可视化工具navicat for mysql
#   连接
#       连接名：MySQL80
#       主机：localhost
#       端口：3306
#       用户名：root
#       密码：135cylpsx4848@
#       确定
# mysql的重装
#     1》停止MySQL服务
#     开始-》所有应用-》Windows管理工具-》服务，将MySQL服务停止。
#     2》卸载mysql server
#     控制面板\所有控制面板项\程序和功能，将mysql server卸载掉。
#     3》将MySQL安装目录下的MySQL文件夹删除（我的安装目录是C:\Program Files (x86)\MySQL）
#     4》运行“regedit”文件，打开注册表。
#     删除HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application\MySQL文件夹
#     删除HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\Eventlog\Application\MySQL文件夹。
#     删除HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog\Application\MySQL的文件夹。
#     如果没有相应的文件夹，就不用删除了。
#     5》删除C盘下的“C:\ProgramData\MySQL ”文件夹，如果删除不了则用360粉碎掉即可，
#     该programData文件默认是隐藏的，设置显示后即可见，或者直接复制 C:\ProgramData 到地址栏回车即可进入！
#     将整个MySQL文件夹删除掉。。。
#     6》开始-》所有应用-》Windows管理工具-》服务
#     如果已经将MySQL卸载，但通过“开始-》所有应用-》Windows管理工具-》服务”查看到MySQL服务仍然残留在
#     系统服务里。又不想改服务名，改怎么办呢。
#     只要在CMD里输入一条命令就可以将服务删除：
#     sc delete mysql //这里的mysql是你要删除的服务名
#     这样一来服务就被删除了。
#
#     然后，就可以重装MySQL数据库了！！！

#【day149】mysql
#mysql简介
#   数据库简介
#       概念
#           人类在进化的过程中，创造了数字、文字、符号等进行数据的记录，但是承受着认知能力和创造能力的提升，数据量越来越大，对于数据的记录和准确查找，成为了一个重大难题
#           计算机诞生后，数据开始在计算机中存储并计算，并设计出了数据库系统
#           数据库系统解决的问题：持久存储、优化读写、保证数据的有效性
#           当前使用的数据库，主要分为两类
#               文档型：如sqlfile，就是一个文件，通过对文件的复制完成数据库的复制
#               服务型：如mysql、postgre，数据存储在一个物理文件中，但是需要使用终端以tcp/ip协议连接，进行数据库的读写操作
#       三范式
#           概念：经过研究和对使用中问题的总结，对于设计数据库提出了一些规范，这些规范被称为范式
#           范式
#               第一范式（1NF）：列不可拆分
#               第二范式（2NF）：唯一标识
#               第三范式（3NF）：引用主键
#           说明：后一个范式，都是在前一个范式的基础上建立的
#       E-R模型
#           当前物理的数据库都是按照E-R模型设计的
#           E表示entry，实体
#           R表示relationship，关系
#           一个实体转换为数据库中的一个表
#           关系描述两个实体之间的对应规则，包裹
#               一对一
#               一对多
#               多对多
#           关系转换为数据库表中的一个列，在关系型数据库中一行就是一个对象
#       主要操作
#           数据库操作：创建、删除
#           表的操作：创建、修改、删除
#           数据的操作：增加、修改、删除、查询，简称crud cread replace update delete
#   数据完整性
#       概念
#           一个数据库就是一个完整的业务单元，可以包含多张表，数据被存储在表中
#           在表中为了更加准确的存储数据，保证数据的正确有效，可以在创建表的时候，为表添加一些强制性的验证，包括数据字段的类型，约束
#       字段类型
#           在mysql中包含的数据类型很多，这里主要列出常见的几种
#           类型
#               数字类型：int， decimal decimal(5,2)表示一共包含五位数，小数包含2位
#               字符串：char， varchar， text
#               日期：datetime
#               布尔：bit
#       约束
#           主键primary kay 主键只能有一个
#           非空 not null
#           唯一 unique 可以有多个，物理上存储的结构是由主键维护的
#           默认default
#           外键foreign key
#   设计表结构
#       学生表结构
#           id
#           name
#           gender
#           address
#       科目表结构
#           id
#           name
#   图形窗口操作
#       创建数据库
#       创建表
#       添加字段
#       逻辑删除 在表中增加一个字段isDelete bit 0(未删除) 1(已删除)


#【day150】sql语句
#基本命令
#   启动服务
#       说明：以管理员身份运行cmd
#       格式：net start 服务名称
#       示例：net start mysql80
#   停止服务
#       说明：以管理员身份运行cmd
#       格式：net stop 服务名称
#       示例：net stop mysql80
#   连接数据库
#       格式：mysql -u 用户名 -p
#       示例：mysql -u root -p
#       输入密码（135cylpsx4848@）
#   断开链接
#       quit
#       exit
#   查看版本
#       示例：select version();
#   显示当前时间
#       示例：select now();
#   远程链接
#       本地允许远程连接
#           #需要被链接的电脑修改host的值
#               mysql -u root -p
#               use mysql
#               update user set Host='%' where User='root';
#               管理员启动cmd
#               net stop mysql80
#               net start mysql80
#           #需要被链接的电脑修改防火墙规则
#               进入控制面板
#                   点击windows防火墙
#                       点击高级设置
#                           点击入站规则
#                               允许外部访问ipv4协议
#                                   同时选中3个文件和打印机共享（回显请求-ICMPV4-In）
#                                       在左边操作栏中点击启用规则
#                               允许外部访问3306端口
#                                   在操作栏中点击新建规则
#                                       选中端口点击下一步
#                                       在特定本地端口中输入3306点击下一步
#                                       选中允许连接点击下一步
#                                       选中域、专用、公用点击下一步
#       远程机连接本地mysql
#           格式：mysql -h 对方ip地址 -u 对方用户名 -p
#           示例：mysql -h192.168.0.102 -uroot -p
#           输入本地mysql密码

#
#数据库操作
#   创建数据库
#       格式：create database 数据库名 charset=utf8;
#       示例：create database shop charset=utf8;
#            create database scrapyTest default character set utf8 collate utf8_general_ci
#   删除数据库
#       格式：drop database 数据库名;
#       示例：drop database shop;
#   切换数据库
#       格式：use 数据库名;
#       示例：use shop;
#   显示所有数据库
#       show databases;
#   查看当前选择的数据库
#       select database();
#表操作
#   查看当前数据库中所有表
#       show tables;
#   创建表
#       格式：create table 表名(列 类型 属性);
#       示例：create table student(id int auto_increment primary key, name varchar(20) not null, age int not null, gender bit not null default 1, address varchar(20), isDelete bit default 0);
#       说明：自增长——auto_increment 主键——primary key 非空——not null
#   删除表
#       格式：drop table 表名;
#       示例：drop table production;
#   查看表结构(查看表字段)
#       格式：desc 表名;
#       示例：desc student;
#   查看建表语句
#       格式：show create table 表名;
#       示例：show create table student;
#   表重命名
#       格式：rename table 原表明 to 新表名;
#       示例：rename table student to newStudent;
#   修改表结构
#       格式：alter table 表名 add|change|drop 列名 类型;
#       示例1：alter table student add isDelete bit not null default 0;
#       示例2：alter table student drop isDelete;
#       示例3：alter table goods change 旧的列名 新的列名 varchar(500);
#       注意：在开发过程中不要去修改表字段，会引起数据报错，解决办法，在创建表结构时事先预留出空白字段
#数据操作命令
#   增
#       全列插入
#           格式：insert into 表名 values();
#           示例：insert into student values(0, 'tom', 1);
#           说明：主键是自动增长的，但是在全列插入时，需要用0来占位，插入成功后以实际数据为准，有默认值的列同样需要传入数据
#       缺省插入
#           格式：insert into 表名(列1, 列2) values(值1,值2);
#           示例：insert into student(name) values('jack');
#           说明：
#       同时插入多条数据
#           格式：insert into 表名 values(...),(...),...;
#           示例：insert into student values(0, 'mia', 0),(0, 'justin', 1);
#   删
#       格式：delete from 表名 where 条件;
#       示例：delete from student where id=2;
#       注意：删除数据不加where条件视为选择全部数据，谨慎
#
#   改
#       格式：update 表名 set 列1=值1, 列2=值2,... where 条件;
#       示例：update newstudent set age=10, address='chendu' where id=1;
#       注意：修改列数据不加where条件视为选在全部列数据，谨慎
#   查
#       格式：select * from 表名;
#       示例：select * from student;
#       说明：查询表中的全部数据
#查
#   基本语法
#       格式：select * from 表名;
#       示例：select * from newstudent;
#       示例：select name, age from newstudent;
#       示例：select name as a, age as b from newstudent;
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
#       模糊查询
#           格式：select * from 表名 where 列名 like '条件个数';
#           %
#               示例：select * from newstudent where name like '陈%';
#               说明：匹配任意多个任意字符
#           _
#               示例：select * from newstudent where name like '陈_';
#               示例：select * from newstudent where name like '陈__'; 只匹配2个任意字符
#               说明：匹配一个任意字符
#       范围查询
#           in
#               格式：select * from 表名 where 列名 in (2, 9, 10);
#               示例：select * from newstudent where age in (2, 9, 10);
#               说明：在一个非连续的范围内
#           between .. and ..
#               格式：select * from 表名 where 列名 between 10 and 40;
#               示例：select * from newstudent where age between 10 and 40;
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
#                   having是对group by的结果再进行筛选，默认值为1
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
#       示例：select * from newstudent where isDelete=0 order by age desc, id desc;
#   分页
#       格式：select * from 表名 limit start,end;
#       示例：select * from newstudent limit 0,3;
#       说明：start索引从0开始
#   关联
#       一对多
#           外键：
#               用来关联其他表的键值对
#               外键在多的表里面
#           建表语句
#               create table class(id int auto_increment primary key, name varchar(20) not null, stuNum int not null);
#           建关联表语句
#               格式：create table 表名(字段名1 类型 属性,... 外键字段名 类型 属性, foreign key(外键字段名) references 需关联表名(需关联字段名))
#               示例：create table students(id int auto_increment primary key, name varchar(20) not null, gender bit default 1, classId int not null, foreign key(classId) references class(id));
#           插入数据
#               insert into class values(0, '一班', 3),(0, '二班', 5),(0, '三班', 2),(0, '四班', 1);
#               insert into students values(0, 'justin', 1, 1), (0, 'xiaohua', 0, 1), (0, 'fangfang', 0, 1), (0, 'xianxian', 0, 2), (0, 'yuanyuan', 1, 2), (0, 'dingding', 1, 2), (0, 'qiqi', 1, 2), (0, 'saosao', 1, 2), (0, 'wanwan', 1, 3), (0, 'momo', 1, 3);
#           关联查询
#               格式：select 表1.段, 表2.段 from 表1 匹配方式 表2 on 表1.段=表2.段
#               关联查询分类
#                   表1 inner join 表2：表1与表2匹配的行会出现在结果集中
#                       需求：查询所有学生名字以及所在班级名字
#                       示例：select students.name, class.name from class inner join students on class.id=students.classId;
#                   表1 left join 表2：表1与表2匹配的行会出现在结果集中，外加表1中独有的数据，未对应的数据使用null填充
#                       需求：查询所有班级中还未招生的班级名称(左匹配，未匹配表1.Id = 表2.classId的数据)
#                       示例：select class.name,students.name from class left join students on class.id=students.classId;
#                   表1 right join 表2：表A与表B匹配的行会出现在结果集中，外加表2中独有的数据，未对应的数据使用null填充
#       多对多


#【day150】python与mysql交互

#链接数据库
'''
import pymysql
#参数1：mysql服务所在的主机ip
#参数2：用户名
#参数3：密码
#参数4：要连接的数据库名
#db = pymysql.connect('localhost', 'root', '135cylpsx4848@', 'productioninfomation')
db = pymysql.connect('192.168.0.105', 'root', '135cylpsx4848@', 'productioninfomation')
#创建一个cursor对象
cursor = db.cursor()
#需要执行的sql语句
sql = 'select version();' #查看当前版本号
#执行sql语句
cursor.execute(sql)
#获取返回的信息
data = cursor.fetchone()
print(data)
#断开链接
cursor.close()
db.close()
'''

#创建表
'''
import pymysql
db = pymysql.connect('172.20.10.2', 'root', '135cylpsx4848@', 'productioninfomation')
cursor = db.cursor()
#检查表是否存在，如果存在则删除
cursor.execute('drop table if exists bandcard;')
#创建表
sql = 'create table bandcard(id int auto_increment primary key, money int not null);'
cursor.execute(sql)
data = cursor.fetchone()
print(data)
cursor.close()
db.close()
'''

#插入数据
'''
import pymysql
db = pymysql.connect('172.20.10.2', 'root', '135cylpsx4848@', 'productioninfomation')
cursor = db.cursor()
sql = "insert into bandcard values(0, 100),(0, 200),(0, 300),(0, 400),(0, 500),(0, 600);"
try:
    cursor.execute(sql) #将数据写入缓存
    db.commit() #提交事务：将数据插入数据库
except:
    #如果提交失败，则回滚到上一次数据
    db.rollback()
data = cursor.fetchone()
print(data)
cursor.close()
db.close()
'''

#更新数据
'''
import pymysql
db = pymysql.connect('172.20.10.2', 'root', '135cylpsx4848@', 'productioninfomation')
cursor = db.cursor()
sql = "update bandcard set money=100 where id=2;"
try:
    cursor.execute(sql) #将数据写入缓存
    db.commit() #提交事务：将数据插入数据库
except:
    #如果提交失败，则回滚到上一次数据
    db.rollback()
data = cursor.fetchone()
print(data)
cursor.close()
db.close()
'''

#数据删除
'''
import pymysql
db = pymysql.connect('172.20.10.2', 'root', '135cylpsx4848@', 'productioninfomation')
cursor = db.cursor()
sql = "delete from bandcard where id=1;"
try:
    cursor.execute(sql) #将数据写入缓存
    db.commit() #提交事务：将数据插入数据库
except:
    #如果提交失败，则回滚到上一次数据
    db.rollback()
data = cursor.fetchone()
print(data)
cursor.close()
db.close()
'''

#数据查询
#fetchone()
#   功能：获取下一个查询结果集，结果集是一个对象
#fetchall()
#   功能：接收全部的返回的行
#rowcount()
#   功能：是一个只读属性，返回execute()方法影响的行数
'''
import pymysql
db = pymysql.connect('172.20.10.2', 'root', '135cylpsx4848@', 'productioninfomation')
cursor = db.cursor()
sql = "select * from bandcard where money>300;"
try:
    cursor.execute(sql)
    reslist = cursor.fetchall() #(('1','100'),('2','200'),('3','300'))
    for row in reslist:
        print('id={},money={}'.format(row[0], row[1]))
except:
    #如果提交失败，则回滚到上一次数据
    db.rollback()
cursor.close()
db.close()
'''
#【day】mysql数据导出导入
#导出数据
#   导出指定数据库
#       cmd：mysqldump -h 数据库所在ip -u 用户名 -p 数据库名> 导出的全路径文件名
#       #示例：mysqldump -u root -p asj > C:\Users\surface\Desktop\mysql导出\test.sql
#   导出指定数据表
#       cmd：mysqldump -h 数据库所在ip -u 用户名 -p 数据库名 表名> 导出的全路径文件名
#       示例：mysqldump -h localhost -u root -p asj foodtypes > C:\Users\surface\Desktop\mysql导出\test.sql
#导入数据
#   前提mysql中已经创建相应的数据库名
#   cmd：mysql -h 数据库所在ip -u root -p 数据库名 < 导入全路径文件名 --default-character-set=utf8
#   示例：mysql -h localhost -u root -p test < C:\Users\surface\Desktop\mysql导出\test.sql --default-character-set=utf8　

#【day151】封装数据库操作
#数据库：productioninfomation
#封装后的调用
'''
from myClass.mySql import MySql
mysql = MySql('172.20.10.2', 'root', '135cylpsx4848@', 'productioninfomation')
resFieldName = mysql.show_fieldName('students')
print(resFieldName)
resInfo1 = mysql.get_all('select * from students;')
print(resInfo1)
resInfo2 = mysql.get_all('select * from students where gender=0;')
print(resInfo2)
for row in resInfo2:
    print(row[1])
'''

#【day152】NoSQL
#简介
#   概述
#       NoSQL，全名为Not Only SQL，指的是非关系型的数据库
#       随着访问量的上升，网站的数据库性能出现了问题，于是NoSQL被设计出来
#   优点
#       高可扩展性
#       分布式计算
#       低成本
#       架构的灵活性，半结构化数据
#       没有复杂的关系
#   缺点
#       没有标准化
#       有限的查询功能(到目前为止)
#       最终一致是不直观的程序
#   分类
#       列存储
#           代表
#               Hbase
#               Cassandra
#               Hypertable
#           特点
#               顾名思义，是按列存储数据的。最大的特点是方便存储结构化和半结构化数据，方便做数据压缩，对针对某一列或者某几列的查询有非常大得人IO优势
#       文档存储
#           代表
#               MongoDB
#               CouchDB
#           特点
#               文档存储一般用类似json的格式存储，存储的内容是文档型的。这样也就有机会对某些字段建立索引，实现关系数据库的某些功能
#       key_value存储
#           代表
#               Tokyo Cabinet / Tyrant
#               Berkeley DB
#               MemcacheDB
#               Redis
#           特点
#               可以通过key快速查询到其value。一般来说，存储不管value的格式，照单全收。（Redis包含了其他功能）
#       图存储
#           代表
#               Neo4J
#               FlockDB
#           特点
#               图形关系的最佳存储。使用传统关系数据库来解决的话性能低下，而且设计使用不方便
#       对象存储
#           代表
#               db4o
#               Versant
#           特点
#               通过类似面向对象语言的语法操作数据库，通过对象的方式存储数据
#       xml数据库
#           代表
#               Berkeley DB XML
#               BaseX
#           特点
#               高效的存储XML数据，并支持XML的内部查询语法，比如XQuery,Xpath


#【day153】MongoDB
#简介
#   什么是MongoDB
#       MongoDB是由C++语言编写的，是一个基于分布式文件存储的开源数据库系统。在高负载的情况下，添加多的节点，可以保证服务器性能。
#       MongoDB旨在为WEB应用提供可扩展的高性能数据存储解决方案
#       MongoDB将数据存储为一个文档，数据结构由键值对组成。MongoDB文档类似与Json对象，即bjson。字段值可以包含其他文档，数组及文档数组。
#   主要特点
#       MongoDB提供了一个面向文档存储，基本思路就是将原来的'行'的概念换成了更加灵活的'文档'模型。一条记录可以表示非常复杂的层次关系。
#       MongoDB支持丰富的查询表达式。查询指令使用JSON形式的标记，可轻易查询文档中内嵌的对象及数组。
#       非常容易扩展。面对数据量的不断上涨，通常有两种方案，一种是购买更好的硬件，另一种是分散数据，进行分布式扩展，前者有非常大的缺点，因为硬件通常是有物理极限的，当达到极限以后，处理能力就不可能再进行扩展了。所以建议的方式是使用集群进行扩展。MongoDB所采用的面向文档的数据模型使其可以自动在多台服务器之间分割数据。它还可以平衡集群的数据和负载，自动重排文档
#       MongoDB支持各种编程语言：RUBY, PYTHON, JAVA, C++, PHP, C#等多种语言
#       丰富的功能：包括索引、存储JavaScript、聚合、固定集合、文件存储等
#       方便的管理，除了启动数据库服务器之外，几乎没有什么必要的管理操作。管理集群值只需要知道有新增的节点，就会自动集成和配置新节点
#安装
#   window
#       将bgdb.mis放在需要安装的路径目录下双击安装
#           勾选同意next
#               custon切换路径
#                   next -> finish
#   Linux
#       yum install mongodb
#概念
#   sql与mongodb的术语区别
#       SQL术语           MongoDB术语        解释说明
#       database         database           数据库
#       table            collection         数据库表/集合
#       row              document           数据记录行/文档
#       column           field              数据字段/域
#       index            index              索引
#       table joins                         链接表，mongodb不支持
#       primary key      primary key        主键，mongodb自动将_id字段设置为主键
#   数据样式区别
#       sql
#           id user_name age city
#           1  mark      30  chendu
#           2  justin    30  chendu
#       mongodb
#           {
#            '_id':ObjectId('123153624523456235'),
#            'user_name':'mark',
#            'age':'30',
#            'city':'chendu'
#           }
#           {
#            '_id':ObjectId('1231524536356463563'),
#            'user_name':'justin',
#            'age':'30',
#            'city':'chendu'
#           }
#   数据库
#       一个mongodb可以建立多个数据库
#       mongodb的单个实例可以容纳多个独立的数据库，每一个都有自己的集合和权限，不同的数据库也放置在不同的文件中
#       数据库也通过名字来标识。数据库名可以是满足以下条件的任意UTF-8字符串
#           数据库名取名规范
#               不能是空字符串('')
#               不能含有 '' (空格) . $ / \ \o(空字符)
#               应全部小写
#               最多64字节
#       有一些数据库名是保留的，可以直接访问这些特殊作用的数据库
#           admin
#               从权限的角度来看，这是'root'数据库。要是将一个用户添加到这个数据库，这个用户自动继承所有数据库的权限。一些特定的服务器端口命令也只能从这个数据库运行，比如列出所有的数据库或者关闭服务器。
#           local
#               这个数据库永远不会被复制，可以用来存储限于本地单台服务器的任意集合
#           config
#               当mongodb用于分片设置时，config数据库在内部使用，用于保存分片的相关信息
#   文档
#       概念
#           文档是mongodb中的最核心的概念，是其核心单元，我们可以将文档类比成关系型数据库中的每一行数据
#           多个键及其关联的值有序的放置在一起就是文档。mongodb使用bjson这种数据结构来存储数据和网络数据交换
#           BSON数据可以理解为在JSON的基础上添加了一些json中没有的数据类型
#           如果我们会JSON，那么BSON我们就已经掌握一半了，至于新添加的数据类型后面我会介绍
#       例子
#           {name:'张三', age:20, hobby:['看书','旅游','唱歌']}
#       注意
#           文档中的键/值对是有序的
#           文档中的值不仅可以是在双引导里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档）
#           mangodb区分类型和大小写
#           mongodb的文档不能有重复的键
#           文档的键是字符串。除了少数例外的情况，键可以使用任意UTF-8字符
#       文档键名规范
#           键不能包含\o(空字符)。这个字符用来表示键的结尾
#           不能使用$等有特殊意义，只有在特定环境下使用
#           以下划线'_'开头的键是保留的(不是严格要求)，最好不要_开头
#   集合
#       集合就是一组文档组合。如果将集合类比成关系型数据库中的行，那么集合就可以类比成数据库的表
#       在mongodb中的集合是无模式的，也就是说集合中存储的文档的结构可以是不同的，比如下面的两个文档可以同时存入到一个集合中
#           {'name':'justin'}
#           {'Name':'google','sex':'nan'}
#       注意
#           当第一个文档插入时，集合就会被创建
#       合法的集合名
#           集合名不能是空字符串''
#           集合名不能含有\o，这个字符表示集合名的结尾
#           集合名不能以'system.'开头，这是为系统集合保留的前缀
#           用户创建的集合名字不能含有保留字符
#   数据类型
#       string              字符串
#       integer             整型数值
#       Boolean             布尔值
#       Double              双精度浮点数 13-15位小数
#       Min/Max keys        将一个值与BSON(二进制的JSON)元素的最低值和最高值相对比
#       Arrays              用于将数组或列表或多个值存储为一个键，==python中的list
#       Timestamp           时间戳
#       Object              用于内嵌文档
#       Null                用于创建空值
#       Symbol              唯一值set
#       Date                日期时间
#       Object ID           对象id。用于创建文档的ID
#       Binary Data         二进制数据
#       Code                代码类型
#       Regular expression  正则表达式类型
#mongodb的使用
#   创建一个保存数据的目录data
#       db文件夹
#           D:\mongodb\data\db
#           存数据
#       log文件夹
#           存日志
#   创建一个mongodb服务器
#       启动mongod.exe
#           打开cmd
#               d:
#               cd D:\mongodb\Server\4.0\bin
#               dir
#               mongod.exe --dbpath=D:\mongodb\data\db
#           注意：打开了的黑屏终端千万别关，它是mongodb的服务器，另外需要再建立一个数据库服务器，也重复以上操作即可
#   配置mongodb的长期服务
#       在新建一个bin的同级目录logs
#           在logs中新建一个mongdb.log文件
#               管理员身份打开cmd
#                   mongod --bind_ip 0.0.0.0 --logpath "E:\mongoDB\logs\mongodb.log" --logappend --dbpath "E:\mongoDB\data\db" --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install
#                       无报错则成功
#   链接一个mongodb数据库服务器（终端打开mongodb）
#       win中搜索服务
#       启动MongoDB Server
#       打开cmd
#           d:
#           cd D:\mongodb\Server\4.0\bin
#           mongo.exe
#   mongodb小测试
#       show dbs 查看此服务器所有数据库
#   mongodb可视化工具
#       启动mongo服务器之后可以使用可视化工具
#       安装
#           mongochef
#               傻瓜式安装 中途需要改安装路径就修改
#       使用
#           进入安装路径
#               双击mongochef.exe
#                   点击第一个勾选
#                       签订保证协议
#                           点击connect
#                               newconnection
#                                   enter a name：随意取个名字
#                                   server：本机ip
#                                   port：27017
#                                   点save
#                                       选中你的mogodb链接器
#                                       点connect
#                                       注意:链接不上就重启一下黑屏的mongodb服务
#【day154】mongodb使用
#操作mongodb数据库
#   创建数据库（|切换到存在的数据库）
#       语法 use 数据库名
#       示例 use mydb
#       注意
#           如果数据库不存在则创建数据库名，否则切换到指定数据库
#           如果刚刚创建的数据库没显示在show dbs中，如果要显示该数据库，需要向刚刚创建的数据库中插入一些数据，才能看到
#   查看所有数据库
#       show dbs
#   查看当前正在使用的数据库
#       db
#       db.getName()
#   插入数据
#       语法：db.集合名.insert(字典数据)
#       示例：db.student.insert({name:'justin', age:18, gender:1, address:'chendu', isDelete:0})
#       说明：db就代表当前使用的数据库，student代表在这个数据库中的一个集合，插入BOSN文本
#       注意：插入数据mydb才会出现在show dbs的列表中
#   断开链接
#       exit
#   查看命令api
#       help
#   删除数据库
#       前提：使用当前数据库 (use 指定数据库名)
#       db.dropDatabase()
#集合操作
#   查看当前数据库下所有的集合
#       show collections
#   创建集合
#       创建空集合
#           语法 db.createCollection('集合名')
#           示例 db.createCollection('class')
#       插入数据创建
#           语法 db.集合名.insert(document)
#           示例 db.student.insert({name:'justin', age:18, gender:1, address:'chendu', isDelete:0})
#   删除当前数据库中的集合(删除集合)
#       语法 db.集合名.drop()
#       示例 db.class.drop()
#文档操作
#   插入文档
#       insert()
#           插入一个文本
#               语法 db.集合名.insert({a:'b'})
#               示例 db.student.insert({name:'mia', age:30, gender:0, address:'chendu', isDelete:0})
#           插入多个文本
#               语法 db.集合名.insert([{a:'b'},{c:'d'},...])
#               示例 db.student.insert([{name:'coco', age:9, gender:0, address:'chendu', isDelete:0},{name:'sofeiya', age:2, gender:0, address:'chendu', isDelete:0}])
#       save()
#           不指定_id
#               语法 db.集合名.save(文档)
#               示例 db.student.save({name:'wangwang', age:27, gender:1, address:'chendu', isDelete:0})
#           指定_id
#               功能 更新指定_id数据
#               示例 db.student.save({_id:ObjectId('5cd39add58191d90767d27fc'), name:'xiaxia', age:26, gender:0, address:'chendu', isDelete:0})
#   文档更新
#       update更新已存在的文档
#           语法 db.集合名.update(query, update, {upset:boolean, multi:boolean, writeConcern:document})
#           参数说明
#               query：update的查询条件，类似于sql里update语句内where后面的内容
#               update：update的对象和一些更新的操作符($set,$inc)等
#                   $set：直接更新
#                   $inc：在原有的基础上累后更新
#               upset：可选，mongodb默认false不插入。在更新数据时，mongodb发现文本中的值并不存在，是否当新数据插入，true为插入，false为不插入
#               multi：可选，mongodb默认false，则只更新按条件匹配到的第一条文档，如果为True，则更新匹配到的全部文档
#               writeConcern：可选，抛出异常的级别
#           示例
#               直改
#                   db.student.update({name:'mia'}, {$set:{age:10}})
#               值累加改
#                   db.student.update({name:'mia'}, {$inc:{age:10}})
#               全改
#                   db.student.update({name:'justin'}, {$set:{age:10}}, {multi:true})
#       save替换已存在的文档
#           语法 db.集合名.save(document, {writeConcern:document})
#           参数说明 writeConcern：可选，抛出异常的级别
#   文档删除
#       说明 在执行remove()函数前，先执行find()命令来判断执行的条件是否存在是一个良好的习惯
#       语法 db.集合名.remove(query, {justOne:boolean, writeConcern:document})
#       参数说明
#           qurey：可选，删除的文档的条件，不选则删除全部数据
#           justOne：可选，如果为True or 1，则只删除一个文档
#           writeConcern：可选，抛出异常的级别
#       示例 db.student.remove({name:'justin'}, {justOne:true})
#   文档查询
#       find()方法
#           查询集合下所有的文档
#               语法 db.集合名.find()
#               示例 db.student.find()
#           查询指定指定列
#               语法 db.集合名.find(query, {key1:1, key2:1})
#               参数说明
#                   query：条件
#                   key：要显示的字段
#                   1：要显示
#               示例 db.student.find({}, {name:1, age:1})
#               示例 db.student.find({gender:1}, {name:1, age:1})
#       pretty()方法
#           以json格式化的方式来显示文档
#               语法 db.集合名.find().pretty()
#               示例 db.student.find().pretty()
#       findOne()方法
#           显示查询结果的第一条文档
#               语法 db.集合名.findOne(条件)
#               示例 db.student.findOne({name:'justin'})
#       查询条件操作符
#           作用 条件操作符用于比较两个表达式，并从MongoDB集合中获取数据
#           > $gt
#               语法 db.集合名.find({key:{$gt:value}})
#               示例 db.student.find({age:{$gt:20}})
#           >= $gte
#               语法 db.集合名.find({key:{$gte:value}})
#           < $lt
#               语法 db.集合名.find({key:{$lt:value}})
#           <= $lte
#               语法 db.集合名.find({key:{$lte:value}})
#           >= and <=
#               语法 db.集合名.find({key:{$gte:value, $lte:value}})
#           == :
#               语法 db.集合名.find({key:value})
#           使用_id进行查询
#               语法 db.集合名.find({'_id':ObjectId('id值')})
#               示例 db.student.find({'_id':ObjectId('5cd39aa158191d90767d27f9')})
#           查询集合中数据总条数
#               db.student.find().count()
#           查询某个字段的值当中是否包含另一个值，模糊匹配
#               示例 db.student.find({name:/jus/})
#           查询某个字段的值是否以另一个值开头
#               示例 db.student.find({name:/^jus/})
#       查询逻辑
#           and
#               语法 db.集合名.find({条件1,条件2})
#               示例 db.student.find({gender:0, age:{$gte:20}})
#           or
#               语法 db.集合名.find({$or:[{条件1}, {条件2},...]})
#               示例 db.student.find({$or:[{age:2}, {age:27}]})
#           and 和 or 联合使用
#               语法 db.集合名.find({条件1,条件2,$or[{条件3},{条件4}]})
#       读取指定数量的数据记录
#           db.student.find().limit(2)
#       跳过指定数量数据
#           db.student.find().skip(3)
#       分页查询
#           db.student.find().limit(2)
#           db.student.find().skip(2).limit(2)
#       排序
#           语法 db.集合名.find().sort({key:1|-1})
#           示例 db.student.find().sort({age:1})
#           注意 1升序,-1降序

#【day155】python与Mongod交互
#插入文档
'''
from pymongo import MongoClient
#链接服务器
conn = MongoClient('localhost', 27017)
#链接数据库
db = conn.mydb
#获取集合
collection = db.student
#添加一条文档
collection.insert_one({'name':'陈艺龙', 'age':5, 'gender':1, 'address':'成都', 'isDelete':0})
#添加多条文档
collection.insert_many([{'name':'陈紫妍','age':6,'gender':0,'address':'成都','isDelete':0},{'name':'陈迪希','age':3,'gender':1,'address':'成都','isDelete':0}])
#断开服务
conn.close()
'''

#查询文档
'''
from pymongo import MongoClient
from bson.objectid import ObjectId #用于_id查询
conn = MongoClient('localhost', 27017)
db = conn.mydb
collection = db.student
#查询全部文档
res = collection.find()
for row in res:
    print(row)
    print(row['name'])
#查询部分文档(条件查询)
res = collection.find({'age':{'$gt':18}})
for row in res:
    print(row)
    print(row['name'])
#统计查询
res = collection.find({'age':{'$gt':18}}).count()
print(res)
#根据id查询
res = collection.find({'_id':ObjectId('5cd39c7d58191d90767d27fd')})
print(res[0])
conn.close()
'''

#排序
'''
from pymongo import MongoClient
from bson.objectid import ObjectId #用于_id查询
conn = MongoClient('localhost', 27017)
db = conn.mydb
collection = db.student
res = collection.find().sort('age', 1) #1为升序，-1为降序
for row in res:
    print(row['age'])
conn.close()
'''

#分页查询
'''
from pymongo import MongoClient
from bson.objectid import ObjectId #用于_id查询
conn = MongoClient('localhost', 27017)
db = conn.mydb
collection = db.student
res = collection.find().skip(3).limit(3)
for row in res:
    print(row)
conn.close()
'''

#更新
'''
from pymongo import MongoClient
conn = MongoClient('localhost', 27017)
db = conn.mydb
collection = db.student
collection.update({'name':'mia'}, {'$set':{'age':10}})
conn.close()
'''

#删除文档
'''
from pymongo import MongoClient
from bson.objectid import ObjectId #用于_id查询
conn = MongoClient('localhost', 27017)
db = conn.mydb
collection = db.student
collection.remove({"_id" : ObjectId("5cd39c7d58191d90767d27fd")})
conn.close()
'''

'''
#作业：封装python操作mongodb的类
'''

#【day156】redis
#安装
#   https://github.com/ServiceStack/redis-windows
#       clone or download
#           Download ZIP
#               解压文件
#                   downloads
#                       解压redis64-2.8.2101到d:\redis
#修改配置文件
#   Subline 打开 redis.windows.conf
#       在387行 写上 requirepass 135cylpsx4848@     这是在设置redis密码
#       在455行 写上 maxheap 1024000000
#       保存 如果遇到拒绝访问 就把该文件复制到其他盘符，修改完后再复制回安装目录下
#       #bind 127.0.0.1  注释掉主机ip后，就能远程访问此数据库了
#       port 6379   端口号
#       dbfilename dump.rdb    数据文件
#cmd启动服务再链接
#   启动redis服务 (redis启动服务)
#       d：
#       cd redis
#       redis-server.exe redis.windows.conf
#cmd链接服务 (redis链接服务器)
#   链接redis服务
#       windows
#           d:
#           cd redis
#           redis-cli.exe
#           auth '135cylpsx4848@'
#       linux
#
#cmd设置长期开启redis服务器
#   说明：在d:\redis目录下的cmd，
#   步骤
#       cmd中输入：redis-server --service-install redis.windows.conf --loglevel verbose
#       win搜索服务，在服务管理器中启动redis服务
#redis可视化工具redis-desktop-manager
#   安装
#       换路径 Next finished
#   链接服务器
#       connect to redis server
#           name justin
#           host localhost
#           port 6379
#           Auth 135cylpsx@
#           单击 左上角 justin
#           justin 右键 console （打开内置黑屏终端）
#数据操作
#   redis是KEY-VALUE的数据，所以每个数据都是一个键值对
#   键的数据类型是字符串
#   值的类型分五种
#       字符串string
#       哈希hash
#       列表list
#       集合set
#       有序集合zset
#   数据操作的全部命令（redis全部命令）
#       http://redis.cn/commands.html

#【day157】redis命令
#key
#   查找建，参数支持正则
#       语法keys pattern
#       示例keys *
#       示例keys [a-z]
#       示例keys na*
#   判断键是否存在，存在返回1，不存在返回0
#       语法 exists key1
#       示例 exists a
#   查看键对应value的类型
#       语法 type key
#       示例 type a
#   删除键及对应的值
#       语法 del key1 key2 ...
#       示例 del a b
#   设置过期时间，以秒为单位
#       语法 expire key seconds
#       示例 expire a 5
#   查看有效时间，以秒为单位
#       语法 ttl key
#       示例 ttl a
#string
#   概述
#       string是redis最基本的类型，最大能存储512MB的数据，string是二进制安全的，即可以存储任何数据，比如数字、图片、序列化对象等
#   设置
#       设置键值
#           语法 set key value
#           示例 set name justin
#       设置键值及过期时间，以秒为单位
#           语法 setex key seconds value
#           示例 setex age 10 5
#       设置多个键值
#           语法 mset key1 value1 key2 valu2...
#   获取
#       根据键获取值
#           语法 get key （key在返value，key不在返null）
#       根据多键获取多值
#           语法 mget key1 key2..
#   运算
#       要求 值是字符串类型的数字
#       将key对应的值+1
#           语法 incr key
#       将key对应的值-1
#           语法 decr key
#       将key对应的值加整数
#           语法 incrby key intnum
#       将key对应的值减整数
#           语法 decrby key intnum
#   其他
#       追加值
#           语法 append key value
#           示例 append name ' is good girl!'
#       获取值长度
#           语法 strlen key
#           示例 strlen name
#hash
#   概述
#       hash用于存储对象(类似理解为字典对象)
#           {name:'justin', age:18}
#   设置
#       设置单个值
#           语法 hset key field value
#           示例 hset a name justin
#           示例 hset a age 18 在a对应的value中再插入age 18
#       设置多个值
#           语法 hmset key filed1 value1 filed2 value2...
#           示例 hmset b name dx age 2
#   获取
#       获取一个属性的值
#           语法 hget key field
#           示例 hget b name
#       获取多个属性的值
#           语法 hmget key field field
#           示例 hmget b name age
#       获取hash中所有属性
#           语法 hkeys key
#           示例 hkeys b
#       获取hash中所有值
#           语法 hvals key
#           示例 hvals b
#       获取hash中所有属性和值
#           语法 hgetall key
#           示例 hgetall b
#       获取hash包含数据的个数
#           语法 hlen key
#           示例 hlen b
#   其他
#       判断属性是否存在 1存在 0不存在
#           语法 hexists key field
#           示例 hexists b name
#       删除属性及值
#           语法 hdel key field1 field2...
#           示例 hdel b age
#           示例 hdel a name age
#       返回值得字符串长度
#           语法 hstrlen key field
#           示例 hstrlen b name
#list
#   概述
#       列表的元素类型为string，按照插入顺序排序，在列表的头部或尾部添加元素
#   设置
#       在头部插入
#           语法 lpush key value1 value2 ...
#           示例 lpush l1 1
#       在尾部插入
#           语法 rpush key value1 value2 ...
#           示例 rpush l1 2
#       在一个元素的前或后插入一个新元素
#           语法 linsert key before|after pivot value
#           示例 linsert l1 before 1 4
#       设置指定索引的元素值
#           语法 lset key index value
#           示例 lset l1 2 50
#           注意 索引从0开始，也可以是负数，表示偏移量从list的尾部开始，-1表示最后一个元素
#   获取
#       移除并返回key对应的list的第一个元素
#           语法 lpop key
#           示例 lpop l1
#       移除并返回key对应的list的最后一个元素
#           语法 rpop key
#           示例 rpop l1
#       返回存储在key的列表中的指定范围的元素
#           语法 lrange key start end
#           示例 lrange l1 0 -1
#   其他
#       裁剪列表，保留选中部分，删除未选中部分
#           语法 ltrim key start and
#           示例 ltrim l1 0 1
#       返回存储在key里的list的长度
#           语法 llen key
#           示例 llen l1
#       返回列表中索引对应的值
#           语法 lindex key index
#           示例 lindex l1 1
#set
#   概述
#       无序集合，元素类型为string类型，而且元素具有唯一性
#   设置
#       添加元素
#           语法 sadd key member1 member2...
#           示例 sadd s1 justin mia
#   获取
#       返回key集合中所有元素
#           语法 smembers key
#           示例 smembers s1
#       返回key集合中元素个数
#           语法 scard key
#           示例 scard s1
#   其他
#       求多个集合的交集
#           语法 sinter key1 key2..
#           示例 sinter s1 s2
#       求多个集合的差集
#           语法 sdiff key1 key2
#           示例 sdiff s1 s2
#           注意 用key1 减去 key2
#       求多个集合的并集
#           语法 sunion key1 key2
#           示例 sunion s1 s2
#       判断元素是否在集合中
#           语法 sismember key member
#           示例 sismember s1 mimi
#           注意 0表示无 1表示有
#
#zset
#   概述
#       有序集合，元素类型为string，元素具有唯一性不能重复
#       每个元素会关联一个double类型的score(表示权重)，通过权重的大小排序，元素的score可以相同
#   设置
#       添加
#           语法 zadd key score1 member1 score2 member2 ...
#           示例 zadd zkey 1 a 2 b 3 c
#   获取
#       返回指定索引范围内的元素（索引从0开始，支持-1）
#           语法 zrange key start end
#           示例 zrange zkey 0 -1
#           示例 zrange zkey 0 2    #取key为z1的索引值为0到2的value，返回的value按照他们各自的得分升序排列，即得分低的排前面
#       返回有序集合key中，score在min和max之间的元素，分数由低到高排序
#           语法 zrangebyscore key min max
#           示例 zcountbyscore zkey 0 2
#       返回指定key中元素个数
#           语法 zcard key
#           示例 zcard zkey
#       返回有序集合key中，score在min和max之间的元素的个数
#           语法 zcount key min max
#           示例 zcount zkey 0 2
#       返回有序集合key中，成员menber的score值
#           语法 zscore key member
#           示例 zscore zkey zvalue
#   删除
#       删除指定的key对应的value
#           语法 zrem key value
#           示例 zrem zkey zvalue
#
#   运算
#       给指定键的值得增加得分
#           语法 zincrby key score value
#           示例 zincrby zkey 10 zvalue    #给key为zkey，value为zvalue的score增加10
#           示例 zincrby zkey -10 zvalue    #给key为zkey，value为zvalue的score减少10
#

#【day158】python与redis交互
'''
import redis
#链接
db = redis.StrictRedis(host='localhost', port=6379, password='135cylpsx4848@')
#方法一
#根据数据类型的不同，调用相应的方法
#写
#写字符串数据
db.set('str1', 'good')
db.hset('hash1', 'name', 'justin')
db.lpush('lis1', '1', '2', '3', '4')
db.rpush('lis2', '1', '2', '3', '4')
db.sadd('set1', '1', '2', '3', '4')
db.zadd('zKey', {'zValue':10}) #第一个参数是key，第二个参数是字典，字典中的key是集合zKey的值，字典中的value是zValue的分数。如果之前就存在同样的zValue，则会更新其得分
#读
print(db.get('str1'))
print(db.hget('hash1', 'name'))
print(db.lrange('lis1', 0, -1))
print(db.smembers('set1'))
print(db.zscore('zKey', 'zValue'))    #获取key为zKey,value为zValue的有序集合的score
print(db.zrangebyscore((zKey, minScore, maxScore))    #获取分数在min-max之间的所有value
print(db.zrevrange(zKey, 0, 100))    #zKey[0:100],返回value列表
print(db.zscore(zKey, zValue)):    #zKey是否存在zValue,存在返回1，不存在返回0
print(db.zscore(zKey, zValue))    #return score = {zKey:zValue}, 返回这个键值的得分
print(db.zcard(PROXY_KEY))    #返回指定key的元素个数

#方法二：pipeline()
#缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = db.pipeline()
pipe.set('str2', 'nice')
pipe.hset('hash2', 'name', 'mia')
pipe.lpush('lis3', '1', '2', '3', '4')
pipe.rpush('lis4', '1', '2', '3', '4')
pipe.sadd('set2', '1', '2', '3', '4')
pipe.execute() #将缓存到pipe的数据包发送给redis服务器，只发送一次请求
#算
db.zincrby(zKey, -1 ,zValue)    #将指定键值的得分减一，{zKey:zValue}['score'] = score - 1
db.zincrby(zKey, 1 ,zValue)    #将指定键值的得分加一，{zKey:zValue}['score'] = score + 1
#删
db.zrem(zkey, zvalue)    #删除指定键对应的值

'''
#封装redis

'''
作业：redis作为缓存使用终极版
细节：实现客户端登录和注册功能，要求注册信息存入redis和mysql，第二次登录时，从redis中去查询是否存在用户，如果不存在，则在mysql中查询，当redis中没有，而mysql存在时，则从mysql中提取出用户名和密码保存到redis中
见：finishedObject.chartRoom.chartRomm3.0.server.py/client.py
程序设计流程图见bilibili_p197
'''

#【day159】HTML5
#应用场景
#   网站是由域名、空间、web应用组成
#   网站的建设与开发，实际上就是对web应用的开发
#   web应用
#   web前段
#简介
#   html：hyper text markup language
#   w3c：万维网联盟
#注意
#   html不区分大小写
#   html属性名必须小写
#新特性
#   用于绘画的canvas标签
#   用于媒介回放的video和audio元素
#   对本地离线存储的更好支持
#   新的特殊内容元素(article、footer、header、nav、section) = div
#   新的表单控件(calendar、date、time、email、url、search)
#   浏览器支持(safari、chrome、firefox、opera、ie9)
#开发工具
#   hbuiler
#pc调试工具
#   谷歌
#手机调试工具
#   谷歌
#基本结构
#   <!DOCTYPE html>                   文档类型：一个文档类型标记是一种标准通用标记语言的文档类型说明，它的目的是要告诉标准通用标记语言解析器，它应该使用什么样的文档类型定义《DTD》来解析文档，即声明用html5的解析标准来解析我们的文件，
#   <html>
#      <head>                         网页头部
#           <meta charset='utf-8'>
#           <meta http-equiv='Content-Type' content='text/html;charset=gb2312'/> 搜索关键字
#           <meta name='keywords' content='龙良雨'/> 内容描述
#           <meta name='description' content='龙良雨是国内最...'/> 网页字符编码
#           <title>无标题文档</title>   标题标签
#      </head>
#      <body>                         网页主体
#          我的第一个网页
#      </body>
#   </html>
#文件的命名规则
#   文件名.html必须用英文
#   遵守标识符规则
#基本语法
#   <常规标签>
#       <标签 属性='属性值' 属性='属性值'></标记>
#   <空标签>
#       <标签 属性='属性值' />
#   说明：
#       写在<>的第一个单词叫标记或标签或元素
#       标记和属性用空格隔开，属性和属性值用等号连接，属性值必须放在" "号内
#       一个标记可以没有属性也可以有多个属性，属性和属性之间不分先后顺序
#       空标记没有结束标签，用'/'代替
#网页的基本标签
#   见hbuilder项目中
#   <!-- 注释 -->
#   <h1>    标题
#   <br>    换行
#   <hr>    水平线
#   <i>     斜线
#   <p>     段落
#   &nbsp;  空格
#   &gt;    >
#   &lt;    <
#   &quot;  引号
#   &copy;  版权符
#   <button> 按钮
#图像标签
#   常见的图像格式
#       JPG
#           internet上被广泛使用，采用的有损压缩，会造成图像的失真，压缩之后体积小，且比较清晰，适合在网页中使用
#       GIF
#           也在internet上被广泛使用，不仅支持透明色，还支持动画
#       PNG
#           兼具JPG和GIF的优势，同时具备GIF不具备的特性，唯一遗憾的是PNG是一种新型的图像格式，存在部分浏览器不支持的问题
#   <img src="" width="" height="" title="图片提示">
#链接标签
#   <a href="" target="_self">原窗口打开</a>
#   <a href="" target="_blank">新窗口打开</a>
#   <a href="mao1">跳转锚点</a>
#   <a name="mao1">设置锚点</a>
#   <a href="mailto:417217170@qq.com">发送邮件</a>
#无序列表
#   <ul><li></li></ul>
#   属性 type
#   值   disc实心圆    square实心方    circle空心圆
#有序列表
#   <ol><li></li></ol>
#   属性 type
#   值   1 A a I i
#定义列表
#   <dl>
#       <dt>树A级1</dt>
#       <dd>树B级1</dd>
#   </dl>
#表格
#   <table>
#       <tr>
#           <th>表头1</th>
#           <th>表头2</th>
#       </tr>
#       <tr>
#           <th>单元1</th>
#           <th>单元2</th>
#       </tr>
#   </table>
#   属性
#       table值 border边框厚度 cellspacing边框中间空间宽度 cellpadding字到边框的距离
#       tr th值 rowspan 跨行 colspan跨列
#web标准
#   结构 html5
#   表现 css3
#   行为 javascrip
#css简介
#   Cascading Style Sheets 层叠样式、WEB标准中的表现标准语言，主要对网页信息的显示进行控制。（装饰网页信息的显示样式）
#css样式
#   内部样式
#       语法
#           <style type="text/css">
#               /*css语句*/
#           </style>
#       注意 最好将内部样式写在header里
#   外部样式
#       创建外部样式表
#           在css文件夹中新建文件 xxx.css
#       导入外部样式表
#           <link rel="stylesheet" type="text/css" herf="路径/文件名.后缀">
#   行内样式
#       语法
#           <标签 style="属性:属性值 属性:属性值"></标签>
#           <标签 style="属性:属性值 属性:属性值"/>
#样式的优先级
#   行内样式优先级最高
#   内部样式和外部样式的优先级跟书写顺序有关，后书写的优先级最高
#css语法
#   selector {property:value; property:value;}
#   说明
#       每个css样式由3个部分组成：
#           选择器：找到要装饰的标签
#           属性：
#               color
#                   值：
#                       单词
#                       #000000 六位16进制数字
#                       rgb(255,255,255)
#               background-color
#               width
#                   值：
#                       100px 像素
#                       100em 字符
#                       % 百分比
#                       auto 自动
#               height
#       属性必须放在{}花括号内，属性和属性值用冒号链接
#       每条声明用分号结束
#       当一个属性有多个属性值的时候，属性值与属性值不分先后顺序
#       在书写样式过程中，空格，换行等操作不影响属性显示
#标签分类
#   块级标签
#       常见块级标签
#           <div></div>
#               最常用的块级标签
#               <dif id=""></div>
#               id属性 唯一属性 整个网页中id的值不能重复
#           <dl></dl>
#           <dt></dt>
#           <dd></dd>
#           <ol></ol>
#           <ul></ul>
#           <li></li>
#           <fielset></fielset>
#           <h1></h1>
#           <p></p>
#           <from></from>
#           <hr>
#           <colgourp>
#           <col>
#           <table></table>
#           <tr></tr>
#           <td></td>
#           <th></th>
#       说明
#           块级标签在网页中以块的形式显示，块即为矩形区域，独占一行
#           两个相邻块标签不会出现并列显示的想象
#           块级标签可以定义它的宽度和高度，不设置高度和宽度时，默认与父级标签一致
#           块级标签一般作为其他标签的容器，它可以容纳其他内联标签和其他块级标签，我们可以把块级标签比喻成一个盒子
#   行内标签
#       常见行内标签
#           <a></a>
#               去除a标签中的线，去线，去底线
#               <a style="text-decoration:none;"></a>
#           <span></span>
#               设置文字缩进
#               <span style="text-indent:50px;"></span>
#           <i></i>
#               倾斜字体
#           <em></em>
#               倾斜字体
#           <strong></strong>
#               字体加粗
#           <b></b>
#               字体加粗
#       说明
#           行内标签的表现形式始终以行内逐个进行显示
#           行内标签没有自己的形状，不能定义它的宽高，它显示的宽度和高度只能根据所包含的内容决定，它的最小内容单元也会呈现矩形形状
#           行内标签也会遵循盒模型的基本规则，如可以定义paddre border margin background
#   行内块级标签
#       常见行内块级标签
#           img
#           textarea
#           input
#           select
#           iframe
#       说明
#           它是块级标签和行内标签的混合体
#           可以设置宽高
#           不会独占一行
#           它会和其他行内标签在同一行按从左至右的顺序显示
#标签类型转换
#   style="display:inline;"
#   属性：display
#       值：
#           block 块级标签
#           inline 行内标签
#           inline-block 行内块级标签
#案例
#   修改自定义列表的行内样式display属性实现导航栏功能
#       <dl>
#    		<dd style="display: inline;">首页</dd>
#    		<dd style="display: inline;">关于我们</dd>
#    		<dd style="display: inline;">联系快递</dd>
#    		<dd style="display: inline;">产品大厅</dd>
#    		<dd style="display: inline;">新闻概况</dd>
#    		<dd style="display: inline;">招商加盟</dd>
#    		<dd style="display: inline;">下载中心</dd>
#    		<dd style="display: inline;">工具案例</dd>
#     	</dl>
#常见网页排版布局
#   见webStrom pageLayout
#注释
#   html <!-- -->
#   css  /**/


#【day159】css选择器
#css选择器
#   标签选择器
#       语法
#           标签名称{属性:属性值;}
#   id选择器
#       语法
#           #idName{属性:属性值;}
#       说明
#           最大用处是创建网页的外围结构，即页面布局
#   class选择器
#       语法
#           .className{属性:属性值;}
#       说明
#           class选择器更适合定义一类样式
#   *通配符选择器
#       语法
#           *{属性:属性值;}
#       说明
#           常用来重置样式
#   交集选择器
#       语法
#           选择器1选择器2{属性:属性值;}
#       说明
#           用于选择同时有多个选择器标记的标签
#   并集选择器
#       语法
#           选择器1,选择器2{属性:属性值;}
#       说明
#           当有多个选择器应用相同的样式时，可以将选择器用,号分开
#   后代选择器
#       语法
#           选择器1 选择器2{属性:属性值;}
#       说明
#           选择器1中包含的所有选择器2（包含多代）
#       示例
#           #box p{属性:属性值;}
#   子代选择器
#       语法
#           选择器1>选择器2{属性:属性值;}
#       说明
#           选择器1中的所有子一级选择器2
#   伪类选择器
#       a链接状态用法
#           a:link{属性:属性值;} 超连接的初始状态
#           a:visited{属性:属性值;} 超连接被访问后的状态
#           a:hover{属性:属性值;} 鼠标悬停，即鼠标划过超连接时的状态
#               用法见：webStrom\css\折叠菜单
#           a:active{属性:属性值;} 超连接被激活时的状态，即鼠标按下超连接的状态
#           说明
#               当这四个超连接伪类选择器联合使用时，应当注意他们的顺序
#               正确的顺序：a:link、a:visited、a:hover、a:active
#               顺序错误会导致样式失效
#               为了简化代码，可以把伪类选择符中相同的声明提出来放在a选择符
#               例如：a{color:red;} a:hover{color:green;}表示超连接的三种状态都相同，只有鼠标划过变色
#       a链接跳转锚
#           #mao:target{}
#           说明
#               此锚被跳转后，在此锚上执行css
#   弟弟选择器
#       语法
#           选择器1+选择器2{属性:属性值;}
#       说明
#           选择器2是选择器1下面紧挨着的选择器
#选择器的权重
#   说明
#       在css中，会根据选择器的权重来决定所定义样式的次序，具有更高权重的选择器的样式优先于具有较低权重选择器的样式，如果两个选择器的权重相同，那么后定义的选择器优先
#       css中用四位数字表示权重，权重的表达方式如：0000
#           标签选择器的权重    0001
#           class选择器的权重  0010
#           id选择器的权重     0100
#           属性选择器的权重    0010
#           伪类选择器的权重    0010
#           伪标签选择器的权重   0010
#           交集选择器的权重    为包含选择器的权重之和
#           子选择器的权重     0000
#           并集选择器的权重    0000
#           后代样式的权重     0000
#           行内样式的权重     1000
#       比较时从高位到低位（从A到D）分别比较，高位相同才需要比较低位

#【day160】列表、背景css声明
#列表css声明
#   css列表属性允许你放置，改变列表项标准，或者将图像作为列表项标志
#   属性
#       list-style
#           简写属性，用于把所有用于列表的属性设置于一个声明中
#       list-style-image
#           将图像设置为列表项标志
#           list-style-image:url(所使用的图片的路径及全称);
#       list-style-position
#           设置列表中列表项标志的位置
#           list-style-position:insert; /*项首符放置在文本以内，且环绕文本根据标记对齐*/
#           list-style-position:outside; /*默认值，项首符放置在文本的左侧*/
#       list-style-type
#           设置列表项标志的类型
#           none
#               无标记(列表去行首符)
#           disc
#               实心圆
#           circle
#               实心方
#           square
#               空心圆
#表格的css声明
#   border-spacing: 0;
#       功能：控制表格间空隙
#       说明：此属性需要给table标签
#背景的css声明
#   background
#       简写属性，作用是将背景属性设置在一个声明中
#       background:url(图片全路径) no-repeat center;
#   background-attachment
#       背景图像是否固定或者随着页面的其余部分滚动
#       background-attachment: scroll; 滚动
#       background-attachment: fixed; 固定
#   background-color
#       设置标签的背景颜色
#   background-image
#       把图像设置为背景
#       background-image: url(路径全称);
#   background-size
#       设置背景大小的宽高
#           background-size: 10px 10px;
#   background-position
#       设置背景图像的起始位置
#       background-position: left、center、right、数值1 top、center、botton、数值2
#       数值1和数值2都是center时写一个值就可以代表的是水平位置和垂直位置
#       右方向 下方向为正数
#   background-repeat
#       设置背景图像是否重复
#       background-repeat: no-repeat; 不平铺
#       background-repeat: repeat; 平铺
#       background-repeat: repeat-x; 横向平铺
#       background-repeat: repeat-y; 纵向平铺
#   img{opacity:0.4}
#       设置img标签加载的图片的透明度
#css中内容的显示和隐藏
#   display: none;
#       隐藏标签，在页面中不占位
#       案例见webStrom/css/折叠菜单
#   display: block;
#       显示标签
#   visibility: hidden;
#       隐藏标签，在页面中占位
#css画圆
#   border-radius: 100px;
#实战
#   折叠菜单
#       见webStrom
#   手风琴菜单
#       见webStrom
#   Tab菜单
#       见webStrom

#【day161】文本属性的声明
#font属性
#   font-size
#       大小
#           单位
#               em 当前文字字符大小
#               pt 绝对长度单位，表示有多少个点
#               px 相对长度单位，使用较广泛
#   font-family:"微软雅黑","宋体";
#       字体
#   font-weight
#       粗细
#           9个等级 100-900 默认400
#   font-style: italic;
#       倾斜
#
#   color
#       单词颜色
#       十六进制
#       RBG color: rgb(25,25,25)
#       RGBA color: rgba(25,25,25,0.5) a为alpha
#   line-height
#       行高
#           设置行高=标签高度，可以使文字垂直居中
#   font: style font-weight font-size line-height font-family;
#       简写
#text属性
#   text-align:left/right/center/justify;
#   vertical-align:top/botton/middle;
#   适用于：指定图片垂直对齐方式，相对与其他文字
#文本的修饰与运用规范
#   装饰线
#       text-decoration: none/underline/overline/line-through/bink;
#   缩进
#       text-indent: 10px;
#   英文单词字间距
#       word-spacing: 20px;
#   英文字母及汉字间距
#       letter-spacing: 10px;
#   大小写转换 首字母大写 全大写 全小写
#       text-transform: capitalize/uppercase/lowercase
#文字添加阴影 水平阴影值 垂直阴影值 模糊距离 阴影颜色
#   text-shadow:h-shadow v-shadow blur color;


#【day162】盒子模型
#CSS盒子模型基本概念
#   盒模型是css布局的基石，它是规定了网页元素如何显示以及元素间的相互关系
#   css定义所有的标签都有
#   边框border
#   外边距margin
#   内边距padding
#   内容区content
#盒的类型
#   标准模式
#   怪异模式针对ie而言的
#盒的内容
#   内容及标签块的溢出处理
#       overflow
#           overflow:visible
#               默认，内容不会被剪裁
#           overflow:hidden
#               内容被剪裁，其余内容不可见
#           overflow:scroll
#               内容被剪裁，滚动条显示其余内容
#           overflow:auto
#               如果内容被剪裁，则浏览器以滚动条显示其余内容
#           overflow-x:overflow
#               内容左右溢出，是否剪裁左右边缘内容
#           overflow-y:overflow
#               内容上下溢出，是否剪裁上下边缘内容
#   文字内容的溢出处理
#       text-overflow
#           text-overflow:clip;
#               修剪文本
#           text-overflow:ellipsis;
#               省略号显示溢出文本
#                   需要和另两个个属性一起用才能实现省略号显示溢出文本
#                       white-space: nowrap; 不换行，删除所有换行符
#                       overflow:hidden; 隐藏溢出文字
#           text-overflow:string;
#               指定字符串显示溢出文本
#css盒模型样式分类定义与应用
#   盒模型的宽度
#       选择器{width: 1620px}
#   盒模型的高度
#       选择器{height: 1px}
#   盒模型的背景
#       选择器{background-image: url(".png")}
#       选择器{background-color: green}
#   盒模型的边框
#       选择器{border: 1px}
#           border-style:;
#               样式：solid dashed dotted double none
#           border-width: 10px;
#           border-color: red;
#           边：线形 粗细 颜色
#               border: solid 10px red;
#               border - top: solid 10px yellow;
#               border - bottom: dashed 10px lime;
#               border - left: dotted 10px #00FFBB;
#               border - right: double 10px black;
#   盒模型的外边距
#       选择器{margin:1px}
#           用法
#               控制两个盒子之间的距离
#               浏览器中横向居中
#                   margin: 0 auto;
#           属性
#               margin: 1px;
#               margin-top: 1px;
#               margin-bottom: 1px;
#               margin-left: 1px;
#               margin-right: 1px;
#           属性值四种方式
#               四个值 上 右 下 左 margin: 1px 1px 1px 1px;
#               三个值 上 左右 下  margin: 1px 1px 1px;
#               两个值 上下 左右   margin: 1px 1px;
#               一个值 四个方向    margin: 1px;
#           注意
#               两个盒子之间的上下距离是取margin值较大者，而不是之和
#               两个盒子之间的左右距离是margin值之和
#   盒模型的内边距
#       选择器{padding:1px}
#           用法
#               用来调整内容在容器中的位置关系
#               用来调整子标签在父级标签中的位置关系
#               padding值是额外加载标签原有大小之上的，如想保证标签大小不变，需要从width和height上减掉后添加padding值
#           属性值的四种方式
#               四个值 上右下左 padding: 10px 10px 10px 10px;
#               三个值 上 左右 下 padding: 10px 10px 10px;
#               两个值 上下 左右 padding: 10px 10px;
#               一个值 四个方向 padding: 10px;
#           单独设置一个方向
#               padding-top: 10px;
#               padding-bottom: 10px;
#               padding-left: 10px;
#               padding-right: 10px;
#盒子尺寸的计算
#   盒宽 = 左右margin + 左右border + 左右padding +contentWidth
#   盒高 = 左右margin + 左右border + 左右padding +contentHeight
#   padding和margin会撑大盒子
#       根据外边距、内边距、边框大小来重新计算内容的宽高
#精灵图
#实战

#【day163】表格
#表格
#   表格标签
#       <table>
#           定义表格
#           属性
#           border
#           cellspcing
#           cellpadding
#       <caption>
#           定义表格标题
#       <thead>
#           定义表格头，表格分组标签，可将表格分割
#       <tfoot>
#           定义表格页尾，表格分组标签，可将表格分割
#       <tbody>
#           定义表格主体，表格分组标签，可将表格分割
#       <tr>
#           定义表格的行，
#       <th>
#           定义表格头，需要被<tr>包裹，
#       <td>
#           定义表格单元，需要被<tr>包裹
#       注意：tfoot thead tbody 要使用就必须按顺序一起使用
#   表重要属性
#       colspan = "value" 合并列
#       rowspan = "value" 合并行
#       align = "left/center/right" 水平对齐
#       valign = "top/bottom/middle/baseline" 垂直对齐
#       border = "1" 边框厚度
#       cellpadding = "1" 单元边沿与其内容之间的空白
#       sellspacing = "1" 单元格之间的空白
#   表格的css属性
#       caption-side:top/bottom/left/right;
#           设置表格标题放置的位置，left/right仅火狐支持
#       border-spacing:1px;
#           单元格之间的间距，必须给table标签添加
#       border-collapse:separate/colllapse
#           边框分开  /  边框合并
#       empty-cells:show/hide;
#           无内容单元格显示、隐藏
#       table-layout:auto/fixed;
#           auto
#               自动布局 列的宽度是由列单元格中没有折行的最宽的内容设定的，缺点加载较慢，需要在确定最终的布局前访问表格中的所有内容
#           fixed
#               固定表格布局 加快运行速度，允许浏览器更快的对表格进行布局，缺点，不太灵活
#   常见表格
#       细线表格
#       粗框细线表格
#       双线表格
#       宫字塔
#       单线表格
#       日历表格
#   表格实战
#       见webStrom


#【day164】表单
#表单作用: 收集用户信息
#表单组成:
#   表单域
#       语法
#           <form 属性名称="值"></form>
#       常见属性
#           规定表单名称
#               name="值"
#           提交表单URL
#               action="值"
#           提交方式
#               method="get/post"
#           规定在发送表单数据之前进行编码
#               enctyp="可能值"
#                   可能值
#                       "application/x-www-form-urlencoded"
#                       "multipart/form-data"
#                       "text/plain"
#           何处打开表单URL
#               target="_black/_self/_parent/_top"
#           是否启动表单自动完成
#               autocomplete="on/off"
#               h5新增功能，还不够智能，可能导致需要验证的信息不准确，比如验证用户输入的密码，密码输入的规范不正确，有时自动验证无法正确验证，我们一般还是用js写验证规则
#           不验证表单
#               novalidate="novalidate"
#               同上说明
#       示例
#           <from name="xxx" method="post" action="www.baidu.com/form" enctype="multipart" target="_self"></form>
#   表单控件
#       必须写在表单域中
#       文本框
#           <input type="text" [name=""] [value="默认值"] placeholder="请输入用户名">
#               name为json串的key
#               value为json串的value
#                   value值为文本框中输入的内容
#                   可以设置value的默认值
#               placeholder占位符
#               注意
#                   需要给服务器传输内容，就必须添加name属性
#       密码框
#           <input type="password" [name=""] [value="默认值"] [placeholder="密码"]>
#       搜索框
#            <input type="search" placeholder="">
#       提交按钮
#           <input type="submit" id="submit" name="submit" value="提交">
#               注意
#                   提交按钮一般放在表单的最后面，可以将所有信息一次性提交
#       重置按钮
#           <input type="reset" value="按钮内容">
#               说明
#                   重置按钮能重置同一个表单域中该重置按钮上面所有表单控件内容
#       单选框/单选框按钮
#           <input type="radio" name="xxx" value="" [checked="checked"]>
#               属性说明
#                   checked="checked" 默认选择此项
#               注意
#                   多个单选框为一组，这一组的name属性值必须相同
#       按钮
#           <input type="button" value="按钮内容">
#               说明
#                   按钮控件的功能需要自定义
#       复选框
#           <input type="checkbox" name="xxx" value="" [disabled="disabled"] [checked="checked"]>
#               属性说明
#                   disabled 禁用，不让勾选
#                       disabled = disable="disable" 只写 disabled即可，可以不写后面的值
#                   checked 必选项
#       滑块框
#           <input type="range" max="100" min="0" value="0" step="10">
#               属性说明
#                   step 调节滑块时，value变化的步长
#       上传文件筐(文件域)
#           <input type="file" name="uploadFile" multiple="multiple">
#               属性说明
#                   multiple 上传多个文件
#       图片域
#           <input type="image" width="100" height="100" border="2" src="上传图片">
#       日历控件
#           <input type="date">
#       周控件
#           <input type="week">
#       月控件
#           <input type="month">
#       当前时间控件
#           <input type="datetime-local">
#       时间控件
#           <input type="time">
#       颜色控件
#           <input type="color" value='#124643'>
#       时间格式验证控件
#           <input type="datetime">
#           说明
#               输入时间格式：如12:12:12，它将数据提交后会自动验证格式是否正确
#       邮箱格式验证控件
#           <input type="email">
#           说明
#               输入邮箱格式：417217170@qq.com，它将数据提交后会自动验证格式是否正确
#       电话格式验证控件
#           <input type="tel">
#           说明
#               输入电话格式：18086829907，它将数据提交后会自动验证格式是否正确
#       数字格式控件
#           <input type="number">
#           说明
#               可以点击增加减少按钮来控制框中的数字
#       下拉菜单
#           <select name="xxx" [placeholder="" onchange="function(){}" multiple="multiple"]>
#               <option>菜单内容</option>
#           </select>
#               onchange
#                   说明：下拉框选线选择事件，当手动选择一个下拉框选项时触发function函数
#               multiple
#                   说明：下来菜单可多选
#       多行文本框
#           <textarea name="xxx" cols="字符宽度" rows="行数"></textarea>
#               属性说明
#                   cols 文本框的宽
#                   rows 文本框的高
#               说明
#                   name属性在网页中不做显示，它用于发送给服务器的json串中的key值,value则是value值
#                       {name:value}
#       提示信息标签
#           <lable for="绑定控件id"></lable>
#           功能
#               label标签为页面上的其他标签指定提示信息，该信息会显示在页面上，当用户点击此标签时，光标会自动聚焦到label标签绑定的对应标签处
#实战
#   世纪佳缘
#       见webStrom


#【day165】浮动
#页面布局方式
#   文档流
#       文档流中标签框的位置由标签在HTML中的位置决定，块级标签从上到下依次排序，框之间的垂直距离由框的垂直margin值计算得到，行内标签在一行中水平布局。
#       文档流就是html文档中的标签，如块级标签，行内标签依据他们的显示属性，按照在文档中的先后次序依次显示。块级标签就占一行或多行，行内标签就和其他标签共处一行，一个萝卜一个坑。
#   浮动流
#       标签从正常的排列顺序被抽离
#           浮动可以使标签向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的表框为止。
#           由于浮动框不在正常文档流中，所以标准文档流中的块框表现得就像浮动框不存在一样
#       属性
#           float:left;
#               左浮动
#           float:right;
#               右浮动
#       注意
#           如果浮动行内标签，则需要指明一个明确的宽度，否则，它们会尽可能地窄
#标签浮动
#   第一个进入浮动流的标签会在它当行变成浮动框，它以下的在文档流的标签会自动往上补，第二个进入浮动流的标签，它的浮动框会碰到第一个浮动框为止
#   当一个标签浮动后，其下方装载文字的容器虽然会占据浮动标签原先的位置，但是其中的文字会一直围绕在浮动元素的周围，而不被浮动元素覆盖
#      div+div+span，如果第一个div浮动后，第二个div的height大于第一个div的height，span的内容显示在第二个div后，如果第二个的height要短，span则会进入浮动流，显示在第一个div后
#   将一个标签进行浮动操作，这个标签的上边缘依据是该标签所在文档流中上面标签块的下边缘
#   网格左右布局时需要再第二个div后面增加一个空白div高度和第一个div相同，目的是将第四个div挤出
#       案例见webstrom/浮动
#总结
#   浮动标签不在标准文档流中，所以浮动后面紧跟着的标签占据了浮动标签原先的位置
#   浮动是个比较特殊的个体，它虽然不在标准文档流中，但是仍然跟标准文档流相互影响
#   如果浮动前面的标签没有浮动属性，则浮动会另起一行在此标签下面浮动
#   当一个元素浮动之后，其下方载文字的容器虽然会占据浮动标签原先的位置，但是其中的文字会一直围绕在浮动标签周围，而不被浮动标签盖住
#浮动的副作用
#   背景不能显示
#       如果对父级设置了css背景颜色或背景图片，标签浮动后父级不能被撑开，而导致背景不能显示。
#   边框不能被撑开
#   margin padding 不能正常显示，特别是上下边的margin跟padding不能正常显示
#清除浮动
#   clear:left/right/both/none;
#       clear属性规定标签的哪一侧不允许其他浮动标签
#           left 不允许左侧存在浮动标签
#           right 不允许右侧存在浮动标签
#           both 左右都不允许存在浮动标签
#   其他清除浮动的方法
#       在父级标签添加最后一个子标签，子标签设置样式clear:both;
#       给父级标签设置高度
#       设置:after伪类选择器
#           div:after{display:block; clear:both; content:"";}
#       父级div定义overflow:hidden和zoom:1
#           zoom可以理解为权重
#               如果两个标签重叠，有zoom:1css样式的标签在上面
#实战
#   北融集团

#【day166】定位
#定位
#   概念
#       css定位(Position)属性允许你对标签进行定位
#       它允许你定义标签框相对于其正常位置应该出现的位置，或者相对于父标签、另一个元素甚至浏览器窗口本身的位置
#   一切皆为框：块框行内框
#   css框定位机制：普通文档流 浮动流 绝对定位
#position属性
#   值
#       relative
#           相对定位是以自身为基点，进行定位
#           相对定位的标签，相对于该标签原来位置的偏移
#               原来的位置起点是0,0,0,0 移动left 10px 相当于0,0,0,10px
#           因此标签的位置通过"left\top\right\bottom"属性进行规定
#           相对定律
#               设置了position属性值为relative的网页标签，无论是在标准文档流中还是在浮动流中，都不会对它的父级标签和相邻标签有任何影响，它只针对自身偏移
#           注意
#               在使用相对定位时，无论是否进行移动，标签仍然占据原来的空间。因此，移动标签会导致它要覆盖其他框
#       absolute
#           绝对定位是以父标签为基点，进行定位
#           使用了绝对定位的标签以它最近的一个已定位的祖先标签为基准进行偏移，如果没有已经定位的祖先标签，那么会以浏览器窗口为基准进行定位
#           绝对定位的标签从文档流中脱离，这意味着它们对其他标签的定位不造成影响
#           设置绝对定位的两个条件
#               必须给父级标签加position属性，一般建议值为relative
#               给子标签加绝对定位position:absolute，同时要加方向属性
#           经验
#               设置了绝对定位但没有设置偏移的标签将保持在原来的位置
#               这个性质在网页制作中可以用于需要使某个标签脱离标准流，而仍然希望它保持在原来的位置的情况
#           设置绝对定位的标签，相对于具有position定位属性的父级标签偏移
#           标签的位置通过"left\top\right\bottom"属性进行规定
#               left 10px 左侧距离
#               right 10px 右侧距离
#               top 10px 上侧距离
#               bottom 10px 下侧距离
#                   绝对定位类似坐标轴定位，如：左边距离以及下边距离确定就能定位一个标签
#       fixed
#           生成固定定位的标签，相对于浏览器窗口进行定位，
#           标签的位置通过"left\top\right\bottom"属性进行规定
#               固定客服框，固定副导航栏，固定移动端的等窗口的固定
#           固定定位定律
#               标签框的表现类似于将position设置为absolute，不过其的基点是浏览器窗口
#               固定定位是相当于当前窗口来进行的定位
#               固定定位标签不再占空间，层级要高于普通标签，跟浮动很像
#               固定定位标签，是一个块标签，换句话说，行内标签使用fixed定位，将转化为块标签
#           如果指定了fixed定位属性，并没有设置偏移量，则"原地不动"
#       static
#           默认值，没有定位(标签的位置通过"left\top\right\bottom")
#z-index属性调整同级定位标签的堆叠次序，（上一层）
#   设置标签的层叠顺序，值为无单位的整数，值较大的标签会叠加在值较小的标签之上
#   z-index属性值：整数，默认值为0，z-index值越大越靠上
#   注意：在position为static会忽略z-index的声明
#实战
#   下拉菜单
#   彭奶奶的童话世界

#【day167】浏览器表现标准规范
#浏览器兼容问题
#   不同的浏览器对同一段代码有不同的解析，造成了页面显示效果不统一的情况
#   在网站设计和制作过程中，做好浏览器兼容，才能够让网站在不同的浏览器下都正常显示
#   不同的浏览器对CSS解析不同
#   不同的浏览器的默认表现差别
#       IE默认margin
#       FF默认padding
#浏览器介绍
#   主流浏览器
#       火狐
#       谷歌
#       IE
#       Opera
#   最早浏览器和浏览器大战
#   浏览器内核
#兼容性处理
#CSS Hack
#IE6常见bug与Hack

#【day168】css统筹
#CSS文档统筹
#   整站里相同的CSS样式提取到一个样式表里，各个页面调用相同的样式文件即可
#   网站较大的情况下一般会把网站的头部，尾部单独分离出来，包括样式文件
#       根据页面类型分离文件
#       根据功能模块分离文件
#       根据标签类型分离文件
#       根据设备类型分离文件
#       根据代码规模综合分离文件
#网页自身优化
#CSS规范
#样式重置

#【day169】js简介
#什么是JavaScript
#   弱型语言
#   是一种基于对象和事件驱动并具有安全性能的脚本语言
#       基于对象
#           基于对象的编程语言没有提供抽象、继承、重载、等有关面向对象的许多功能。而是把其他语言所创建的复杂对象统一起来，从而形成一个非常强大的对象系统
#           基于对象的编程语言还是具有一些面向对象的基本特征。它可以根据需要创建自己的对象，从而进一步扩大语言的应用范围，增强编写功能强大的web文档
#       事件驱动
#           鼠标点击，键盘键入等启动预先设置的相应动作
#       脚本语言
#           不需要通过服务器来执行的属于前台的语言
#JavaScript作用
#   网页特效
#   表单验证
#   响应事件
#   其他
#JavaScript特点
#   基于对象
#   跨平台
#   改善用户体验
#   动态性
#JavaScript基本思想
#   网页都是由一个一个对象(如标签对象)构成的
#   对象都能够被js操作(改变状态)
#   我们通过js程序能决定怎么操作(改变状态)
#JavaScript历史
#   前世今生
#JavaScript组成
#   ECMAScript
#       变量
#       运算符与表达式
#       流程控制
#       函数
#       数组Array
#
#       字符串String
#       Math
#           数学函数
#       日期Date
#   BOM
#       使用js控制浏览器
#   DOM
#       使用js控制HTML页面中的标签
#JavaScript工作原理


#【day179】HTML中添加js代码、注释方式、输出方式
#<script>
#   document.write("<h1>justin</h1>") 在页面上打印内容,与其他两个打印的区别在于会渲染h1标签
#   console.log("<h1>mia</h1>")       将信息打印到检测中的console栏中
#   alert("<h1>coco</h1>")            在警示栏中打印输出
#   //                       单行注释
#   /**/                     多行注释，注意多行注释里面不要嵌套多行注释/* /**/ */
#</script>
#注意
#   当html中有多个script标签时，其中的js代码是从上到下依次执行
#导入外部js文件(js的导入)(导入js)
#   <script src="js/打印.js"></script>
#       在html中导入并执行js文件代码，js文件中的代码执行完，再执行html中的代码
#       注意script标签中有src属性，在其中的js代码失效
#           <script src="js/打印.js">console.log("justin")</script>
#           console.log("justin")不会执行
#js文件调用另外js文件中的方法
#   封装一个自己的js类库
#   在html中先导入这个js类库
#   再导入另外一个新的js文件
#   在js文件中就可以使用js类库中的方法了


#【day180】js中的数据类型
#基本数值
#   数字类型
#   字符串
#   布尔值
#   undefined
#       调用一个未被定义的变量或定义了却没赋值的变量会返回undefined数据类型，而undefined的值只有一个是undefined
#   null
#       只包含一个值的特殊数据类型，所谓的null值，通常是没有值或空值，不代表任何东西，null与undefined最大的区别在于，被赋于了null的变量通常我们认为是已经被定义了的变量
#非基本数据类型(对象)
#定义变量
#   无值定义
#       var 变量名;
#           当变量未赋值是，此变量时undefined数据类型，此时的值为undefined
#   赋值定义
#       var 变量名 = "字符串";
#       var 变量名 = 123;
#       var 变量名 = null;
#标识符
#   与python一样的规定
#   唯一一个区别
#       不能是js的关键字和保留字
#           保留字是保留起来以后可能会有具体功能
#查看变量数据类型的操作符
#   typeof()
#运算
#   var num1 = 10;
#   var num2 = 10;
#   var sum = num1 + num2;
#   console.log('sum =',sum);
#拼接
#   console.log('sum = ' + sum);
#       + sum是数字类型，会自动转成字符串类型，再与前面的字符串进行拼接
#数字类型的特殊值
#   var num1 = 1e309;
#   console.log(num1);
#   var num2 = Infinity;
#       当数值超过了js能表示的范围，就把这个数表示为Infinity，js能表达的最大范围不能超过1e309，即1*10^309
#   var num3 = num2 + 1;
#       Infinity + 任何数 都等于 Infinity
#数字类型的特殊值
#   var num1 = NaN;
#       NaN表示num1不是数字，但是它又是一个数字类型
#       特点
#           NaN具有传染性，NaN与任何值任何运算得到的结果都是NaN
#           NaN不等于NaN，console.log(NaN == NaN) return false
#           so 不能用NaN == NaN来判断一个值是否为NaN
#               console.log(isNaN(NaN)) return true 只能用此函数来判断数字是否为NaN
#定义字符串
#   var str1 = 'justin';
#   console.log(str1)
#定义布尔值
#   var t = true;
#   var f = false;
#真值和假值
#   用于if真假判断
#        假值：
#           0
#           0.0
#           ""
#           NaN
#           undefined
#           false
#           null
#        真值：
#           除了假值的值
#数据类型转换
#   其他数据类型转数字
#       parseInt()
#           功能
#               会试图将其收到的任何输入值(通常是字符串)转成整数类型，如果转换失败就返回NaN。
#           转换规则
#               如果第一个非空白字符是数字或者正负号则开始转换，直到碰到第一个非数字字符停止转换。如果第一个非空白字符不是数字或正负号，转换失败，返回NaN
#           用法
#               var str1 = '123';
#               var str2 = '12a3';
#               var num1 = parseInt(str1);
#           结果
#               console.log(parseInt(null));          NaN
#               console.log(parseInt(undefined));     NaN
#               console.log(parseInt(true));          NaN
#               console.log(parseInt(false));         NaN
#               console.log(parseInt('123'));         123
#               console.log(parseInt('12.3'));        12.3
#               console.log(parseInt('+123'));        123
#               console.log(parseInt('-123'));        -123
#               console.log(parseInt('   123'));      123
#               console.log(parseInt(''));            NaN
#               console.log(parseInt('   '));         NaN
#               console.log(parseInt('123abc'));      123
#               console.log(parseInt('123+123'));     123
#               console.log(parseInt('abc'));         NaN
#       parseFloat()
#           功能
#               将字符串小数转换成小数
#           转换规则
#               同parseInt()
#       Number()
#           console.log(Number(null));          0
#           console.log(Number(undefined));     NaN
#           console.log(Number(true));          1
#           console.log(Number(false));         0
#           console.log(Number('123'));         123
#           console.log(Number('12.3'));        12.3
#           console.log(Number('+123'));        123
#           console.log(Number('-123'));        -123
#           console.log(Number('   123'));      123
#           console.log(Number(''));            0
#           console.log(Number('   '));         0
#           console.log(Number('123abc'));      NaN
#           console.log(Number('123+123'));     NaN
#           console.log(Number('abc'));         NaN
#
#   其他数据类型转字符串
#       null -> String
#           var str1 = 'justin' + null;
#       undefined -> String
#           var str2 = 'justin' + undefined
#       Boolean -> String
#           var str3 = true.toString()
#           var str4 = false.toString()
#       Number -> String
#           var sum = 10;
#           console.log(sum.toString());
#   其他数据类型转布尔值
#       console.log(Boolean(''));
#       console.log(Boolean(null));
#       console.log(Boolean(undefined));
#       console.log(Boolean(0));
#       console.log(Boolean(NaN));
#       console.log(Boolean(false));
#           绝大多数Boolean转换后都是true，但以下6种不是
#               ''
#               null
#               undefined
#               0
#               NaN
#               false
#   字符串类型转JSON
#       var jsonObc = $.parseJSON(string)
#外部输入值，即input框
#   var num = parseInt(prompt('请输入数字：'));
#   console.log(num);
#运算符与运算表达式
#   区别
#       没有整除运算
#           var num1 = 10
#           var num2 = 3
#           var num3 = num1 / num2
#           console.log(num3) -> 3.33333332
#           console.log(parseInt(num3)) -> 3
#   其余同python的运算符与运算表达式相同
#   注意
#       任何数与NaN进行运算结果都是NaN
#       Infinity + (-Infinity) = NaN
#       Boolean/undefined/null + number
#           先将Boolean/undefined/null转换成数字类型再进行运算
#       String + (number/undefined/boolean/null)
#           将number/undefined/boolean/null转换成String再进行拼接
#自增自减运算符和自增自减运算表达式
#   var num1 = 10;
#   var num2 = 10;
#   自增
#       var a = num1++;
#           后加加的表达式的返回值是原num1的值
#       console.log(a);
#           ->10
#       console.log(num1);
#           ->11
#       var b = ++num2;
#       console.log(b);
#           ->11
#       console.log(num2);
#           ->11
#   自减
#       var a = num1--;
#           后加加的表达式的返回值是原num1的值
#       console.log(a);
#           ->10
#       console.log(num1);
#           ->9
#       var b = --num2;
#       console.log(b);
#           ->9
#       console.log(num2);
#           ->9
#符合运算符
#   += -= *= /=
#   var a = 1;
#   a += 1;
#   console.log(a)
#if语句
#   格式
#       if(条件判断表达式)
#           {语句}
#   示例
#       if(1)
#           {console.log('justin')}
#   逻辑
#       当程序遇到if语句时，先运算条件判断表达式，当表达式为真时，执行语句
#if-else语句
#   格式
#       if(条件判断表达式)
#           {语句1}
#       else
#           {语句2}
#   逻辑
#       当程序遇到if-else语句时，先运算条件判断表达式，当表达式为真时，执行语句1，表达式为假时，执行语句2
#   示例
#       var a = parseInt(prompt('请输入偶数：'));
#       if (a % 2 == 0)
#           {console.log('得到的是偶数')}
#       else
#           {'得到的是奇数'};
#关系运算符
#   > < >= <= != == ===
#   值等于
#       ==
#           console.log(1 == 1);
#           console.log(1 == '1');
#   绝对等于
#       ===
#           console.log(1 === '1');
#三目运算符
#   ?:
#   格式
#       表达式 ？表达式1 : 表达式2
#   功能
#       表达式的值为真，运算表达式1的值
#       表达式的值为假，运算表达式2的值
#   三目运算整体的值
#       如果表达式的值为真，则三目运算的值为表达式1的值，否则为表达式2的值
#   经验
#       三目表达式最好加括号
#   示例
#       console.log(1?2:3)
#       var a = 1?2:3
#       console.log(a)
#逻辑运算符
#   python
#       and or not
#   js
#       &&  ||  ！
#   功能用法同python
#   示例
#       if (1 && 1)
#           {console.log('真')}
#               一个假都为假
#       if (1 || 0)
#           {console.log('真')}
#               一个真都为真
#       if (!0)
#           {console.log('真')}
#               颠倒黑白

#【day181】语句
#if-else-if语句
#   python
#       if 表达式1:
#           语句1
#       elif 表达式2:
#           语句2
#       ...
#       else:
#           语句e
#   js
#       if (表达式1)
#           {语句1}
#       else if (表达式2)
#           {语句2}
#       ...
#       else
#           {语句e}
#switch语句
#   格式
#       switch (表达式) {
#           case 标号1:
#               语句1
#           case 标号2：
#               语句2
#           ...
#           default:
#               语句f
#
#   逻辑
#       当程序执行到switch语句时，首先计算表达式的值，然后用表达式的值去跟标号匹配，能匹配到哪个标号，就跳到哪个标号下，继续向下执行。如果一个标号都未匹配，则执行语句f
#   练习
#       终端输入数字，打印出对应的星期数及以下的全部内容
#break语句
#   功能
#       结束当前执行程序，常用于结束switch语句和for循环语句
#   练习
#       终端输入数字，打印出对应的星期数
#while语句
#   python
#       while 表达式:
#           语句
#   js
#       while (表达式)
#           {语句}
#do-while语句
#   格式
#       do
#           {语句}
#       while(表达式)
#   逻辑
#       当程序执行到do-while语句时，先执行do中的语句，再计算表达式的值，如果值为假，do-while语句结束，如果值为真，会一直执行do中的语句，执行完语句在计算表达式的值
#   示例
#       var num = 1;
#       var sum = 0;
#       do{
#           sum += num;
#           num++;
#       }while(num<=10)
#       console.log(sum)
#for语句
#   python
#       for 变量 in 集合：
#           语句
#   js
#       for (语句1; 表达式; 语句3){
#           语句2
#       }
#       逻辑
#           当程序执行到for语句时，先执行语句1且仅执行一次，在计算表达式的值，如果表达式的值为假，for语句结束，如果表达式的值为真，则执行语句2，执行完语句2再执行语句3，执行完语句3在计算表达式的值，如果为假，for语句结束，如果为真，执行语句2，再执行语句3，再计算表达式的值
#   示例1
#       var num = 1;
#       var sum = 0;
#       for (console.log('开始计算1到10之和'); num<=10; num++)
#           {sum += num}
#       console.log(sum)
#   示例2
#       var sum = 0;
#       for (var num = 1;; num<=10; num++)
#           {sum += num}
#       console.log(sum)
#for语句的死循环
#   for (;;){
#   }
#break语句
#    示例1
#        var a = 1;
#        while(a<=10){
#            a++;
#            if(a === 5){
#                break;
#            }
#        }
#        console.log(a);
#    示例2
#         var sum = 0;
#         for (var a=1; a<=10; a++){
#             sum += a;
#             if (a === 5){
#                 break;
#             }
#         }
#         console.log(sum);
#continue语句
#    示例1
#         var a = 0;
#         while(a <= 9){
#             a++;
#             if(a === 5){
#                 continue;
#             }
#             console.log(a);
#         }
#    示例2
#         var sum = 0;
#         for(var a = 1; a<=9; a++){
#             sum += a;
#             if(a === 5){
#                 continue;
#             }
#             console.log(sum);
#         }
#for-in语句
#   用法
#       往往被用来遍历某个数组找对象中的元素
#       数组的定义
#           var arr1 = [1,2,3,4,5];
#           var aer2 = ['a','b','c','d','e'];
#   格式
#       for(变量 in 数组){
#           语句
#      }
#   示例
#       for(var i in arr1){
#           console.log('index:' + i + ' ' + 'value:' + arr1[i])
#       }
#   注意
#       i得到的是数组中的下标，如果需要得到值，还需到原素组中去下标取值
#   练习
#       从控制台输入一个字符串，判断这个字符串中有多少个单词
#函数的声明
#   格式
#       python
#           def 函数名(参数列表):
#               函数体
#               return 表达式
#       js
#           function 函数名(形参列表){
#               语句;
#               return 表达式;
#           }
#   说明
#       function是函数的关键词
#       函数名：遵循标识符的规则
#       ()：参数列表的开始和结束
#           参数列表：函数从函数的调用者获得的信息，可以没有参数
#       {}：函数体的开始和结束
#       语句：函数封装的功能
#       return 表达式：return一般用于结束函数，并返回给函数的调用者一些信息，“表达式”即为要返回的数据
#       如果一个函数没有显示的返回return子句，我们就默认它的返回值为undefined
#   注意
#       在仅仅只声明之后是不会被执行的，只是说明有了一个能完成该功能的函数，还没有被使用
#无参无返回函数
#   function name(){
#       console.log('justin')
#   }
#   a = name();
#   console.log(a);
#有参有返回值函数
#   function sum(num1,num2,num3){
#       var a = num1 + num2 + num3
#       return a
#   }
#   var b = sum(1,2,3)
#   console.log(b)
#函数调用
#   格式
#       函数名(实参)
#       变量 = 函数名(实参)
#   本质
#       实参给形参赋值的过程
#   python的区别
#       多实参调用
#           实参的个数可以多于形参的个数,形参按照实战的顺序取值，多于的实参任然可以被取得
#           示例
#         function sum(num1, num2, num3){
#             var a = num1 + num2 + num3;
#             for (var i=0; i<arguments.length; i++){
#                 console.log(arguments[i])
#             }
#             return a;
#         }
#
#         var b = sum(1,2,3,4,5,6,7);
#         console.log(b);
#       arguments
#           概念
#               类似数组的对象
#返回值
#   return
#       将函数中的值返回个调用者
#变量的作用域
#   局部变量
#       仅在函数的作用域中使用
#   全局变量
#       顶头定义的变量
#       可以在全局使用
#       全局变量在函数域中可以进行修改，python需要声明全局变量global
#       示例
#           var num1=0;
#           function func(){
#               var num2 = 10;
#               console.log(num2);
#               num1 = 10;
#               p = 20; //在函数中没有有var定义的变量，默认为全局变量
#           }
#           func();
#           console.log(num1);
#           console.log(num2);
#           console.log(p);
#变量提升
#    程序首先会在函数中去寻找所有的变量定义，然后将变量的定义提升到函数的起始位置，因此在函数中在定义变量之前可以对这个变量进行调用,但它的值为undefined，因为仅仅提升了它的定义而没有提升它的赋值
#        示例
#             function func(){
#                 console.log(a);
#                 var a = 10;
#                 console.log(a);
#             }
#             func();
#函数也是一种数据
    # function mySum(num1, num2){
    #     var a = num1 + num2;
    #     return a;
    # }
    # var b = mySum;
    # console.log(b(1,2));
    # 因此函数可以当成参数传走
    # function myFunc(s,a,b){
    #     return s(a,b);
    # }
    # console.log(myFunc(b, 1,2));
#匿名函数
#   python
#       lambda 表达式
#   js
#       匿名函数就是一个没有名字的函数
#           var f = function(a,b){
#               return a + b;
#           }
#           console.log(f(1,2));
#       实际用法
#           匿名函数可以写在其他函数的调用中，当成参数传入其他函数
#               function func(num1, num2, fc){
#                   return fc(num1, num2)
#               }
#               var a = func(1,2,function (num1,num2) {
#                   return num1 + num2;
#               });
#               console.log(a);
#           定义匿名函数完成某些一次性任务，即即时函数
#               概念
#                   函数定义好之后立即执行
#               格式
#                   (匿名函数)(参数1，参数2)
#               示例
#                   (function(a,b){return a+b})(1,2)
#数组
#   本质
#       数组是js中的一个内置对象，可以存储多个不同类型的数据
#           console.log(typeof(arr))
#       内置对象
#           这个语言自带的一些对象，供开发者使用，这些对象提供了一些常用的或是基本而必要的功能
#           内置对象包括
#               Math
#               String
#                   普通字符串会被自动转成String对象，因此可以调用这个字符串对象的方法
#               Array
#               Date
#           对象包含属性方法
#   创建数组
#       var arr1 = ['a','b','c','d','e'];
#       var arr2 = new Array(1,2,3,'abc');
#           console.log(typeof(arr2));
#           arr2是数组对象，除了包含列表元素，还包括两个属性
#               length:0
#                   元素长度
#               __proto__:Array(0)
#                   类似指针
#           注意
#               创建可以由空元素填充的数组
#               var arr2 = new Array(5); //建议有5个元素
#               arr2[0] = 1;
#               arr2[5] = 2;
#   访问数组
#       下标取值
#           console.log(arr1[0])
#       下标赋值
#           arr1[0] = 1;
#           通过一个不存在的下标进行赋值,如果该下标与原数组的最后一个下标存在一定间隔，那这些间隔会本empyt填充
#           arr1[20] = 1;
#   数组的属性
#       数组的长度
#           arr1.length;
#           改变数组长度(增加)
#               增加的空元素为empty
#               arr1.length = 10;
#           改变数组长度(减少)
#               多于的直接截取掉
#               arr2.length = 3;
#   数组元素的更新
#       arr1[2] = 3;
#   数组元素的删除
#       用delete操作符删除特定的元素
#           delete arr1[2];
#           注意
#               arr1.length不变,删除的元素被empty填充
#   数组的遍历
#       遍历1
#           for (var i in arr1){
#               console.log('index:%s value:%d', i, arr[i])
#           }
#       遍历2
#           for (var i=0; i<arr1.length; i++){
#               console.log('index:%d value:%d', i, arr[i])
#           }
#       遍历3
#           arr.forEach(function(item){console.log(item)});
#               forEach封装了遍历功能,它的第一个参数是匿名函数,匿名函数在forEavh中被调用,最后将元素返回给itme形参,itme就是我们需要的arr的元素了
#   数组的方法
#       arr.push(item1, item2...)
#           功能：向数组的末尾插入元素
#           参数：数组元素
#           返回值：新数组
#       arr.unshift(item1, item2)
#           功能：向数组的头部插入元素
#           参数：数组元素
#           返回值：新数组
#       arr.pop()
#           功能：删除数组尾部元素
#           参数：无参数
#           返回值：删除元素
#       arr.shift()
#           功能：删除数组头部元素
#           参数：无参数
#           返回值：删除元素
#       arr.join(str)
#           功能：用参数字符串将数组中的元素拼接成一个新字符串
#           参数：用于拼接的字符串
#           返回值：拼接后的字符串，不会改变原数组
#       arr.reverse()
#           功能：将原数组的元素倒置
#           参数：无参数
#           返回值：元素倒置后原数组
#       arr.slice(starIndex, endIndex)
#           功能：截取元素
#           参数：开始下标，结束下标
#           返回值：截取到的元素数组组成的新数组
#           注意：新数组不包括arr[endIndex]元素，原数组不会改变
#       arr.splice(index, delCount, item1, item2...)
#           功能：在数组中插入或删除数组元素，如果要插入元素的话，delcount为0
#           必须参数：index下标,delCount个数
#           可选参数：item1,item2...
#           返回值：
#               插入元素，修改原函数，
#               删除元素，修改原函数，返回被删除的元素组成的新数组
#           示例
#               var arr = ['a','b','c','d','e']
#               在下标前插入元素
#                   arr.splice(1, 0, 'b', 'b')
#               删除元素
#                   arr.splice(1, 2)
#       arr.concat(arr1)
#           功能：将两个数组拼接
#           参数：一个或多个数组
#           返回值：新数组，数组元素是所有拼接的数组元素
#           注意：不改变原数组
#       arr.indexOf(item)
#           功能：从数组的头部开始查找目标元素，找到并返回第一个目标元素的下标，否则返回-1
#           参数：要查找的元素
#           返回值：下标或者-1
#       arr.lastIndexOf()
#           功能：从数组的尾部开始查找目标元素，找到并返回第一个目标元素的下标，否则返回-1
#           参数：要查找的元素
#           返回值：下标或者-1
#数组的冒泡排序
#   var arr = [5,4,3,2,1];
#   for (var i=0; i<(arr.length-1); i++){
#      for (var j=0; j<(arr.length-1-i); j++){
#          if (arr[j] - arr[j+1] > 0){
#              var tempty = arr[j];
#              arr[j] = arr[j+1];
#              arr[j+1] = tempty;
#          }
#      }
#   }
#   console.log(arr);
#数组的排序
#   升序
#       arr.sort();
#           默认升序，比较字符串的大小，而不是长度。
#               字符串的大小比较
#                   比较第一个的ASKII码值，相同在比较下一位的ASKII码值
#       本质
#           arr.sort(function(x,y){return x - y});
#   降序
#       arr.sort(function(x,y){return y - x});
#           #x代表索引为前一个的元素，y代表索引为后一个的元素
#           return x - y 代表 返回 x - y 的差
#           前后调换原则
#               差为正数，则sort得到正数参数，调换前后两个元素的位置顺序
#               差为负数，则sort得到负数参数，不调换前后两个元素的位置顺序
#   规则可以自定义
#       按照字符串长度升序
#           var arr = new Array('awfrq', 'sds', 'asdfff', 'ds', 'd');
#           arr.sort(function(x,y){return x.length - y.length});
#           console.log(arr);
#字符串
#   定义
#       var str1 = 'justin';
#           数据类型 string
#       var str2 = new String('justin')
#           数据类型 object
#   注意
#       string在被调用时，会转变成object类型，可以使用对象的属性和方法
#       字符串定义之后不可改变
#           str1[0] = 'z'
#   属性
#       str1.length
#   方法
#       str1.charAt(index)
#           功能：获取指定下标的元素
#       str1.charCodeAt(index)
#           功能：获取指定下标的字符的ASCII码
#           返回值：0~65535之间的整数
#       str1.fromCharCode(ASKII码)
#           功能：将ASKII码转成对应字符
#       str1.toLowerCase()
#           功能：所有大写转小写
#       str1.toUpperCase()
#           功能：所有小写转大写
#       str1.localeCompare(str2)
#           功能：比较str1和str2的大小
#           返回值：str1>str2 return 1 ; str1<str2 return -1 ; str1 = str2 return 0
#       str1.indexOf(str)
#           功能：正向查找
#       str1.lastIndexOf(str)
#           功能：返向查找
#       var str2 = str1.replace('oldStr','newStr')
#           功能：替换首个字符串
#           注意：替换全部内容只能结合正则全部替换
#       var str2 = str1.substring(startIndex[, endIndex])
#           功能：提取子串
#       var str2 = str1.substr(startIndex[, count])
#           功能：从startIndex开始提取count个元素
#       var str2 = str1.split(' ')
#           功能：字符串的分割
#Math对象
#   Math.round(3.6);
#       功能：四舍五入
#   Math.ceil(3.1);
#       功能：向上取整
#   Math.floor(3.1);
#       功能：向下取整
#   Math.max(1,2,3,4,5);
#       功能：最大值
#   Math.min(1,2,3,4,5);
#       功能：最小值
#   Math.abs(-3.4);
#       功能：绝对值
#   Math.pow(2,3);
#       功能：x的y次方
#   Math.sqrt(25);
#       功能：开方
#   parseInt(Math.random()*(y - x +1) + x);
#       功能：x到y之间的随机整数，包含x和y
#了解时间
#   格林尼治时间
#   世界协调时间：时间戳，距离1970年1月1日0点的毫秒数
#创建时间对象
#   当前时间
#       var d = Date()
#       var d = new Date()
#   设置时间
#       var d = new Date('2019-01-01 12:21:05')
#       var d = new Date('2019-01-01') 会加8小时
#       var d = new Date('2019-1-1')
#       var d = new Date('2019/01/01 12:21:05')
#       var d = new Date('2019/1/1 12:21:05')
#       var d = new Date(2015,5,21,5,23,7) 年月日十分秒，月从0开始，0为1月以此类推
#       var d = new Date(2000) 距离1970年1月1日0点2000毫秒的时间
#时间对象的方法
#   获取时间
#       d.getFullYear(); 年
#       d.getMonth(); 月
#       d.getDate(); 日
#       d.getDay(); 星期
#       d.getHours(); 时
#       d.getMinutes(); 分
#       d.getSeconds(); 秒
#       d.getMilliseconds(); 毫秒
#       d.getTime(); 时间戳
#   设置时间
#       d.setFullYear(2019); 年
#       d.setMonth(6); 月
#       d.setDate(21); 日
#       d.setHours(5); 时
#       d.setMinutes(21); 分
#       d.setSeconds(34); 秒
#       d.setMilliseconds(23); 毫秒
#       d.setTime(11231241241241); 时间戳
#   日期转换
#       d.toLocaleString()
#       d.toLocaleTimeString() 只包含时分秒
#       d.toLocaleDateString() 只包含年月日
#   日期运算
#       var d1 = new Date()
#       var d2 = new Date('2019-06-30 00:00:00')
#       d2 - d1 两个时间相距的秒数

#【day183】BOM
#简介
#   浏览器对象模型
#   本质
#       用于访问浏览器和计算机屏幕的对象集合，我们可以通过全局对象window来访问这些对象
#顶层对象(全局对象)
#   window
#       属性
#           window.document 页面文档集合
#           window.frames 浏览器框架集合
#           window.navigator 浏览器的描述信息
#           window.screen 屏幕描述信息
#           window.location
#               属性
#                   window.location.href = url
#                   说明：控制浏览器地址栏的内容，修改值来跳转页面
#               方法
#                   window.location.reload()
#                   说明：刷新页面,带缓存请求，先在缓存里查看是否有该页面，如果有从缓存中得到，否则请求服务器
#                   window.location.reload(true)
#                   说明：刷新页面,不带缓存请求，每次都请求服务器
#                   window.location.assign(url)
#                   说明：加载新的页面，即进入下一页
#                   window.location.replace(url)
#                   说明：加载新的页面，不在浏览器的历史记录表中留下记录
#           window.history
#               说明：操作历史记录
#               注意：assign加载的页面能留下历史记录，可以使用前进后退来跳转前后页面
#                    replace不会留下历史记录，不能使用前后跳转
#               属性
#                   window.history.length
#                   获取历史记录的长度
#               方法
#                   window.history.back()
#                       上一页
#                   window.history.forward()
#                       下一页
#                   window.history.go(num)
#                       到那一页
#                   window.history.open(url/.html, 'blank', 'width=200px, height=400px, top=0px, left=0px)
#                       在指定位置打开页面
#       方法
#           window.open(url, openMode, sizePosition);
#           window.close();
#       事件属性
#           页面完全加载完毕触发匿名函数
#               window.onload = function(){}
#               说明
#                   web中图片等所有内容加载完毕后执行
#           当滚动条滚动时触发事件
#               window.onscroll = function(){
#                   var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
#                   console.log('滚动条的高度：%d', scrollTop);
#               }
#           页面变化触发事件
#               window.onresize = function(){
#                   var w = document.documentElement.clientWidth || document.body.clientWidth || window.innerWidth;
#                   var h = document.documentElement.clientHeight || document.body.clientWidth || window.innerWidth;
#                   console.log('宽：%dpx 高：%d',w,h)
#               };
#页面跳转练习
#   见webStrom页面跳转
#定时器
#   间歇式定时器
#       概念
#           每隔一定时间执行一次函数
#       声明
#           每2000毫秒即2秒，执行一次函数
#           var time = window.setInterval(function(){
#               console.log('justin')
#           }, 2000);
#       清除定时器
#           window.clearInterval(time)
#   延时性定时器
#       概念
#           多少时间后触发一次
#       声明
#           3秒中后执行一次函数
#           var time = window.setTimeout(function(){
#               console.log('justing');
#           },3000);
#       清除定时器
#           clearTimeout('time')

#【day184】DOM
#概念
#   文档对象模型 document object model
#   DOM是访问HTML和操作HTML的标准
#类型
#   Core DOM
#       核心DOM
#       针对任何结构化文档的标准模型
#   XML DOM
#       针对XML文档的标准模型
#   HTML DOM
#       针对HTML文档的标准模型

#【day185】HTML DOM节点
#本质
#   js中的一个内置对象
#节点分类
#   文档节点
#       一整个html文档
#   标签节点
#       一整个标签
#   属性节点
#       标签的属性
#   文本节点
#       p标签中的文本
#   注释节点
#       <!--注释节点-->
#找节点
#   获取标签节点
#       标签的id获取
#           var tabNode = document.getElementById('idDiv');
#           对象的形式打印
#               console.log([tabNode])
#       标签的class获取
#           var tabNodeArray = document.getElementsByClassName('classDiv');
#       标签的name获取
#           var tabNodeArray = document.getElementsByName('inputText');
#       标签的tabName获取
#           var tagNodeArray = document.getElementsByTagName('div');
#   获取属性节点
#       标签节点.getAttributeNode('属性名')
#           var AttributeNode = tagNode.getAttributeNode("type");
#   获取属性节点的值
#       获取官方定义的属性
#           方法一
#               标签节点.属性名
#                   var tagNode = document.getElementById('id');
#                   var tNodeValue = tagNode.type;
#                   var vNodeValue = tagNode.value;
#                   var pNodeValue = tagNode.placeholder;
#           方法二
#               标签节点.getAttribute('属性名')
#                   var pNodeValue = tagNode.getAttribute('placeholder')
#                   注意
#                       此方法得到的是对应属性名的值
#                       也可以获取自定义属性
#                           var mNodeValue = tagNode.getAttribute('my')
#       属性节点的值修改
#           修改官方定义属性的值
#               标签节点.属性名 = 赋值
#                   tagNode.placeholder = '修改值';
#           修改自定义属性值和官方定义属性值
#               标签节点.setAttribute('属性名','修改值')
#                   tagNode.setAttribute('my','我是帅哥')
#       属性节点的增加
#           标签节点.setAttribute('新属性名','新值')
#               tagNode.setAttribute('self','我是超人')
#       属性节点的移除
#           标签节点.removeAttribute('属性名')
#               tagNode.removeAttribute('my');
#   获取文本节点(提取文本，提取文字)
#       标签节点.innerHTML
#           从标签节点的标签开始到标签结束的全部内容，包括换行符和空格，不包括标签本身
#               <div id="box">我是一个盒子</div>
#               var tagNode = document.getElementById('box');
#               var textNode = tagNode.innerHTML;
#       标签节点.outerHTML
#           从标签节点的标签开始到标签结束的全部内容，包括换行符和空格，包括标签本身
#               var textNode = tagNode.outerHTML;
#       标签节点.innerText
#           从标签节点的标签开始到标签结束的全部内容，不包括换行符和空格，不包括标签本身
#               var textNode = tagNode.innerText
#       修改文本节点
#           文本节点.innerHTML = '修改值'
#           textNode.innerHTML = '<h1>我是盒子它兄弟</h1>'
#   修改行内样式
#       获取行间样式
#           var sbc = 标签节点.style.backgroundColor
#           var sw = 标签节点.style.width
#           var sh = 标签节点.style.height
#       修改style属性节点的全值
#           tabNode.style = "width:100px;height:100px;background-color:red;"
#       修改style属性节点的单个样式
#           标签节点.style.样式
#               修改背景颜色
#                   tabNode.style.backgroundColor = '#125467'/'rgba(12,32,112,0.5)'/'blue';
#                   tabNode.style['backgroundColor'] = '#125467'/'rgba(12,32,112,0.5)'/'blue';
#               修改宽度
#                   tabNode.style.width = "200px";
#                   tabNode.style['width'] = "200px";
#               修改高
#                   tabNode.style.height = "200px";
#                   tabNode.style['height'] = "200px";
#   修改外部样式
#       获取外部样式
#           格式
#               window.getComputedStyle(tagNode, null).css样式
#           示例
#               var wbc = window.getComputedStyle('id', null).backgroundColor
#               war ww = window.getComputedStyle('id', null).width
#               war wh = window.getComputedStyle('id', null).height
#       修改外部样式
#           同样修改它的行间样式来覆盖外部样式
#               修改背景颜色
#                   tabNode.style.backgroundColor = '#125467'/'rgba(12,32,112,0.5)'/'blue';
#                   tabNode.style['backgroundColor'] = '#125467'/'rgba(12,32,112,0.5)'/'blue';
#               修改宽度
#                   tabNode.style.width = "200px";
#                   tabNode.style['width'] = "200px";
#               修改高
#                   tabNode.style.height = "200px";
#                   tabNode.style['height'] = "200px";
#   小结
#       标签节点
#           获取属性节点值
#           修改属性节点值
#               行间样式修改
#               外部样式修改
#           增加属性节点和值
#           移除属性节点
#           获取文本节点值
#           修改文本节点值
#层级关系（DOM树）
#    父节点
#        拥有任意数量的子节点
#    子节点
#        只能拥有一个父节点
#    兄弟节点
#        拥有相同父节点的同级节点
#    根节点
#        一个html文档一般只有一个根节点，根节点没有父节点，是最上层的节点
#    祖先节点
#        包含子节点的节点都可以叫祖先节点，其中包括了父节点
#    后代节点
#        一个节点内包含的所有节点，叫做后代节点，其中包括子节点
#层级关系（html树结构）
#    文档
#        根元素 <html>
#            标签节点 <head>
#                标签节点 <title>
#                    文本节点 文档标题
#            标签节点 <body>
#                标签节点 <a>
#                    属性节点 href
#                    文本节点 '我的链接'
#                标签节点 <h1>
#                    文本节点 我的标题
#层级关系属性
#    获取当前节点的所有子节点
#        var allChildNodeArray = Node.childNodes;
#    获取当前节点的第一个子节点
#        var firstChildNode = Node.firstChild;
#    获取当前节点的最后一个子节点
#        var lastChileNode = Node.lastChild;
#    获取该节点的文档根节点，相当于document
#        var rootNode = Node.ownerDocument;
#    获取当前节点的父节点
#        var parentNode = Node.parentNode;
#    获取当前节点的前一个同级节点
#        var previousNode = Node.previousSibling;
#    获取当前节点的后一个同级节点
#        var nextNode = Node.nextSibling;
#    获取当前节点的所有的属性节点
#        var allAttributeNodeArray = tagNode.attributes;
#节点的常用属性
#    node.nodeName
#        标签节点的nodeName值
#            标签名称
#        属性节点的nodeName值
#            属性名称
#        文本节点的nodeName值
#            #text
#        注释节点的nodeName值
#            #comment
#    node.nodeType
#        标签节点的nodeType值
#            1
#        属性节点的nodeType值
#            2
#        文本节点的nodeType值
#            3
#        注释节点的nodeType值
#            8
#    node.nodeValue
#        标签节点的nodeValue值
#            null
#        属性节点的nodeValue值
#            属性值
#        文本节点的nodeValue值
#            文本内容不包含html
#        注释节点的nodeValue值
#            注释内容
#    node.offsetLeft
#        当前节点的绝对位置左的值
#    node.offsetRight
#        当前节点的绝对位置右的值
#    node.offsetTop
#        当前节点的绝对位置上的值
#    node.offsetBottom
#        当前节点的绝对位置下的值
#    node.offsetWidth
#        当前节点的绝对宽度
#    node.offsetHeight
#        当前节点的绝对高度

#【day186】DOM节点动态操作
#创建标签节点
#   document.createElement('标签名');
#       var newTagNode = document.createElement('tagName');
#       newTagNode.id = 'newId';
#       newTagNode.className = 'newClassName';
#       newTagNode.style.backgroundColor = '#123456';
#插入节点（增加节点、添加节点）
#   获取父标签节点
#       var parentTagNode = document.getElementById('parentId')
#   添加标签节点
#       将新节点添加到某个节点的子节点列表的末尾
#           父标签节点.appendChild(新的标签节点);
#               parentTagNode.appendChild(newTagNode);
#   插入标签节点
#       将新节点添加到父节点的某个子节点的前面
#           父标签节点.insertBefore(新节点,子节点)
#               parentTagNode.insertBefore(newTagNode, childTagNode)
#   替换标签节点
#       将父节点中的某个子节点替换成新节点
#           父节点.replaceChild(新节点, 子节点)
#               parentTagNode.replaceChild(newTagNode, childTagNode)
#   复制标签节点
#       只复制本身
#           标签节点.cloneNode();
#       复制本身和子节点
#           标签节点.cloneNode(true);
#   删除节点（清除节点）
#       alert('删除节点');
#   删除父节点下的对应子节点
#       父节点.removeChild(子节点);
#           parentTagNode.removeChild(childTagNode);

#【day187】事件添加
#添加事件的方式
#   在标签属性中添加事件并直接写入js函数
#       格式
#           onclick = "alert('触发事件1')";
#   在标签属性中添加事件并导入js中的函数
#       格式
#           onclick = 'func()';
#           script src="jsCode.js"
#       this参数
#           this能将当前标签节点传入函数
#           <div onclick="func(this)"></div>
#           function func(TagNode){
#               this.style.backgroundColor = 'yellow';}
#   给对应的标签节点添加事件函数
#       格式
#           var divTagNode = document.getElementById('box')
#           divTagNode.onclick = function(){this.style.backgroundColor='yellow';}
#       优点
#           实现了js与html的分离
#       缺点
#           只能添加一个函数，添加第二个会覆盖第一个
#       删除事件
#           格式
#               divTagNode.onclick = null;
#   给标签节点添加多个事件函数——事件监听
#       格式
#           var divTagNode = document.getElementById('box')
#           divTagNode.addEventListener('事件名', 相应事件的函数, 事件流)
#               事件名
#                   click
#                   mouseover
#                   mouseout
#               函数名或匿名函数
#               事件流
#                   false
#                   true
#       优点
#           添加的函数之间互不影响
#       缺点
#           代码有点点长
#       示例
#           function event1(){this.style.backgroundColor='yellow'}
#           function event2(){this.style.backgourndColor='yellow'}
#           divTagNode.addEventListener('click', event1, false)
#           divTagNode.addEventListener('click', event2, false)
#       删除事件
#           格式
#               divTagNode.removeEventListener('事件类型', 函数名, false)
#           示例
#               divTagNode.removeEventListener('click', event1, false)
#事件概念
#   用户或者浏览器执行的某种动作
#       click 单击
#事件处理程序
#   响应事件的函数，事件处理程序的名字是以"on"开头的
#       onclick 单击后相应的事件函数
#this指针
#   在全局变量中使用代表window
#   在局部变量中可指普通函数的调用者
#       即指代标签节点
#       在HTML中标签的属性事件中传入this参数
#   在事件函数中指代调用者
#       即指代目标标签节点
#       在js中获取目标节点
#           调用方式一
#               tagNode = function event(){this.style.backgroundColor};
#           调用方式二
#               function event () { this.style.backgroundColor};
#               tagNode.addEventListener('click', event, false)


#【day189】事件类型
#聚焦事件
#   鼠标点击input控件时，产生聚焦事件
#       focus
#   鼠标点击input控件外时，产生离焦事件
#       blur
#单击与双击
#   单击
#       click
#   双击
#       dblclick
#   注意
#       单击和双击事件同时作用于标签节点时需要用定时器区别单击还是双击
#           var time;
#           function event1(){
#               clearTimeout(time);
#               time = window.setTimeout(function(){console.log('单击')},300);
#           }
#           function event2(){
#               clearTimeout(time);
#               console.log('双击');
#           }
#           tagNode.addEventListener('click', event1, false);
#           tagNode.addEventListener('dblClick', event2,false);
#鼠标事件
#   鼠标移入
#       mouseover
#           tagNode.addEventListener('mouseover', function event(e){}, false);
#   鼠标移出
#       mouseout
#           tagNode.addEventListener('mouseout', function event(e){}, false);
#   鼠标按下
#       mousedown
#           tagNode.addEventListener('mousedown', function event(e){}, false);
#   鼠标抬起
#       mouseup
#           tagNode.addEventListener('mouseup', function event(e){}, false);
#   鼠标移动
#       mousemove
#           tagNode.addEventListener('mousemove', function event(e){}, false);
#   常用鼠标事件对象属性
#       function event(e){
#           e.pageX   页面横坐标
#           e.pageY   页面纵坐标
#           e.screenX 屏幕横坐标
#           e.screenY 屏幕纵坐标
#           e.clientX 可视窗口横坐标
#           e.clientY 可视窗口纵坐标
#           e.offsetX 控件横坐标
#           e.offsetY 控件纵坐标
#           e.button  0左键 1中键 2右键
#       }
#键盘事件
#   按键按下
#       keydown
#           document.addEventListener('keydown', function event(e){}, false);
#   按键抬起
#       keyup
#           document.addEventListener('keyup', function event(e){}, false);
#   触发除ctrl、tab、caps、shift、alt、win、fn等非功能按键的其他所有按键，即只触发abc...123...
#       keypress
#           document.addEventListener('keypress', function event(e){}, false);
#   常用键盘事件对象属性
#       function event(e){
#           e.altKay
#               值
#                   true:Alt+key
#                   false:key
#           e.shiftKay
#               值
#                   true:Shift+key
#                   false:key
#           e.ctrlKay
#               值
#                   true:Ctrl+key
#                   false:key
#           e.key 键盘按下的键
#           e.keyCode 键盘按下的键的ASKII码
#       }
#下拉菜单事件
#   <select onchange='function'><option></option></select>
#   下拉菜单选择事件
#       onchange
#           当我们选择一个下拉菜单选项时触发此事件，即下来菜单的值发生变化触发事件
#键盘应用下的例子
#事件流
#   事件捕获阶段
#       从外层执行到里层
#   处于目标阶段
#
#   事件冒泡节点
#       从里层处理到外层
#验证事件流
#   见webStrom
#事件对象
#   屏蔽冒泡
#       document.getElementById('idName').onclick = function(e){e.stopPropagation()}
#       调用了此方法的标签就不会将事件冒泡到外层
#   阻止默认行为
#       a标签有默认跳转页面行为
#       当我们不需要跳转时，它任然会跳转，因此我们需要干掉默认行为
#拖拽练习
#轮播图
#飞机大战

#【day190】JQuery
#jquery选择器
#   是什么
#       JQuery选择器是jQuery库中非常重要的部分之一。它支持网页开发者所熟知的CSS的语法，能够轻松快速地对页面进行设置。jQuery选择器是打开高效开发jQuery之门的钥匙
#       jQuery选择器的语法格式为：$(selector).methodName();
#           selector是一个字符串表达式，用于识别DOM中的标签，然后使用jQuery提供的方法集合加以设置
#           多个jQuery操作可以以链的形式串起来，语法如下
#               $(selector).method1().Method2().Method3();
#   优势
#       代码更简单
#           在JQuery库中封装了大量可以直接通过选择器调用的方法或函数，使我们仅使用简单的几行代码就可以实现比较复杂的功能
#           例如
#               可以使用$('#id')代替javaScrip代码中的document.getElementById()函数，即通过id来获取标签节点，
#               可以使用$('tagName')代替js中的document.getElementByTagName()函数，即通过标签名称获取HTML标签节点等
#       支持css1到css3
#           jQuery选择器支持CSS1到CSS3几乎所有的选择器，以及jQuery独创的高级且复杂的选择器，因此有一定css经验的开发人员可以很容易的切入到jQuery的学习中来
#           一般来说，使用css选择器时，开发人员需要考虑主流的浏览器是否支持某些选择器。但在jQuery中，开发人员则可以放心的使用jQuery选择器，无需考虑浏览器是否支持这些选择器，这极大的方便了开发者。
#       完善的检测机制
#           传统的js代码中，给页面中的标签节点设定某个事务时必须先找到该标签节点，然后赋予相应的事件或属性；如果该标签节点在页面中不存在或已被删除，那么浏览器会提示运行出错之后的信息，这会影响代码的执行。因此，为避免显示这样的出错信息，通常要先检测该标签节点是否存在，如果存在，再执行它的属性或事件代码。
#   分类
#       基础选择器
#           ID选择器
#               使用公式：$(#id)
#               示例：var a = $('#box') 获得id属性值为box的元素
#               js：document.getElementById('idName')
#           元素选择器
#               使用公式：$('tagName')
#               示例：var a = $('div') 获取所有div元素
#               js：document.getElementByTagName('TagName')
#           类名选择器
#               使用公式：$('className')
#               示例：var a = $('.c3') 获取所有类名为c3的元素
#               js：document.getElementByClassName('className')
#           复合选择器
#               使用公式：$('selector1, selector2, selector3...')
#               示例：var a = $('#box,.c3,div') 获取id为box和所有类名为c3，以及所有div的元素
#           通配符选择器
#               示例：var a = $('*')
#               说明：取得页面上所有的DOM元素集合的jQuery包装集
#       层次选择器
#           后代选择器
#               使用公式：$('parent child')
#               示例：$('ul li')
#               说明：取得ul下所有的li（包含多代）
#           子代选择器
#               使用公式：$('parent>child')
#               示例：$('ul>li')
#               说明：取得ul下子一代的li
#           弟弟选择器
#               使用公式：$('选择器1+选择器2')
#               说明：选择器2是选择器1同级下一个紧挨着的选择器
#           弟弟们选择器
#               使用公式：$('选择器1~选择器2')
#               说明：选择器1和选择器2是同级元素，匹配选择器1下面的所有选择器2元素
#       过滤选择器
#           简单过滤器
#               简单过滤器是指以冒号开头，通常用于实现简单过滤效果的过滤器
#           :first
#               简称：首项选择器
#               说明：匹配找到的第一个元素，它是与选择器结合使用的
#               示例：$('tr:first') //匹配表格第一行
#           :last
#               简称：末项选择器
#               说明：匹配找到的最后一个元素，它是与选择器结合使用的
#               示例：$('tr:last') //匹配表格最后一行
#           :even
#               简称：偶数选择器
#               说明：匹配所有索引值为偶数的元素，索引值从0开始
#               示例：$('tr:even') //匹配索引值为偶数的行
#           :odd
#               简称：奇数选择器
#               说明：匹配所有索引值为奇数的元素，索引值从0开始
#               示例：$('tr:odd') //匹配索引值为奇数的行
#           :eq(index)
#               简称：索引选择器
#               说明：匹配一个给定索引值的元素
#               示例：$('div:eq(1)') //匹配第二个div元素
#           :gt(index)
#               简称：大于范围选择器
#               说明：匹配所有大于给定索引值的元素
#               示例：$('span:gt(0)') //匹配索引大于0的span元素（大于零不包含零）
#           :lt(index)
#               简称：小于范围选择器
#               说明：匹配所有小于给定索引值的元素
#               示例：$('span:lt(2)') //匹配索引小于2的span元素（小于2不包含2）
#           :header
#               简称：标题选择器
#               说明：匹配如h1,h2,h3...之类的标题元素
#               示例：$(':header') //匹配全部的标题元素
#           :not(selector)
#               简称：过滤器
#               说明：在选定的选择器元素中去掉所有给定选择器的元素
#               格式：$('选择器1:not(选择器2)')
#               示例：$('input:not(:checked)') //匹配没有被选中的input元素
#           :animated
#               简称：动画选择器
#               说明：匹配所有正在执行动画效果的元素
#               示例：$('div:animated') //匹配正在执行的动画的div元素
#       内容过滤器
#           内容过滤器就是通过DOM元素包含的文本内容以及是否含有匹配的元素进行筛选
#           :contains(text)
#               简称：包含文本选择器
#               说明：匹配包含给定文本的元素
#               示例：$("li:contains('word')") //匹配含有'word'文本内容的li元素
#           :empty
#               简称：空文本选择器
#               说明：匹配所有不包含子元素或文本的空元素
#               示例：$('td:empty') //匹配不包含子元素或者文本的单元格
#           :parent
#               简称：非空元素选择器（父级元素选择器）
#               说明：匹配含有子元素或者文本的元素
#               示例：$('td:parent') //匹配不为空的单元格，即在该单元格中包含子元素或文本
#           :has(selector)
#               简称：包含元素选择器
#               说明：匹配含有选择器所匹配元素的元素
#               示例：$("td:has(p)") //匹配表格的单元格中含有<p>标记的单元格
#       可见性过滤器
#           元素的可见状态有两种，分别是隐藏状态和显示状态。可见性过滤器就是利用元素的可见状态匹配元素的
#           :visible
#               说明：匹配所有的可见元素
#           :hidden
#               说明：匹配所有不可见元素
#               注意：在应用:hidden过滤器时，display属性是none以及input元素的type属性为hidden的元素都会被匹配到
#       表单对象的属性过滤器
#           表单对象的属性过滤器通过表单元素的状态属性(例如选中、不可用等状态)匹配元素
#           :checked
#               说明：匹配所有被选中的元素
#               示例：$('input:checked') //匹配所有被选中的input元素
#           :disabled
#               说明：匹配所有不可用元素
#               示例：$('input:disabled') //匹配所有不可用的input元素
#           :enabled
#               说明：匹配所有可用元素
#               示例：$('input:enabled') //匹配所有可用的input元素
#           :selected
#               说明：匹配所有下拉菜单选中的option元素
#               示例：$('select option:selected')
#       子元素选择器
#           子元素选择器就是筛选给定某个元素的子元素，具体的过滤条件有选择器的种类而定
#           :first-child
#               说明：匹配所有给定元素的第一个子元素
#               示例：$('ul li:first-child') //匹配ul元素中的第一个子元素li
#           :last-child
#               说明：匹配所有给定元素的最后一个子元素
#               示例：$('ul li:last-child') //匹配ul元素中的最后一个子元素li
#           :only-child
#               说明：如果某个元素是它的父元素中唯一的子元素，那么将会被匹配。如果父元素中含有其他元素，则不会匹配
#               示例：$('ul li:only-child') //匹配只包含一个li的ul中的li
#           :nth-child(index/even/odd/equation)
#               说明：匹配每个父元素下的第index个子或奇偶元素，index从1开始，
#               示例：$('ul li:nth-child(2)') //匹配所有ul中index为2的li
#               示例：$('ul li:nth-child(even)') //匹配所有ul中index为奇数的li

#       属性选择器
#           [attribute]
#               简称：包含属性选择器
#               说明：匹配包含给定属性的元素
#               示例：$('div[name]') //匹配包含name属性的div
#           [attribute = 'value']
#               简称：属值等选择器
#               说明：匹配属性值为value的元素
#               示例：$("div[name='justin']") //匹配name属性值为justin的div
#           [attribute != 'value']
#               简称：属性值不等于选择器
#               说明：匹配属性值不等于value的元素
#               示例：$("div[name!='justin']") //匹配name属性值不为justin的div
#           [attribute *= 'value']
#               简称：包含值选择器
#               说明：匹配属性值包含value的元素
#               示例：$("div[name *= 'justin']")
#           [attribute^='value']
#               简称：开头值选择器
#               说明：匹配属性值为value开头的元素
#               示例：$("div[name ^= 'justin']")
#           [attribute$='value']
#               简称：结尾值选择器
#               说明：匹配属性值为value结尾的元素
#               示例：$("div[name $= 'justin']")
#           [attribute1='value1'][attribute2='value2'][attribute3='value3']
#               简称：复合属性选择器
#               说明：匹配同时满足多个条件的元素
#               示例：$("div[id='1'][name='2'][class='3']") //匹配id=1，name=2，class=3的所有div
#       表单选择器
#           表单选择器是匹配经常在表单内出现的元素。但是匹配的元素不一定在表单中
#           :input
#               简称：input选择器
#               说明：匹配所有的input元素
#               示例：$(':input') //匹配说有的input元素
#                    $('form :input') //匹配所有form中的所有input元素
#           :button
#               简称：普通按钮选择器
#               说明：匹配所有的普通按钮，即type="button"的input元素
#               示例：$(':button') //匹配所有的普通按钮
#           :checkbox
#               简称：复选框选择器
#               说明：匹配所有的复选框
#               示例：$(':checkbox') //匹配所有的复选框
#           :file
#               简称：文件域选择器
#               说明：匹配所有的文件域
#               示例：$(':file') //匹配所有的文件域
#           :hidden
#               简称：隐藏内容选择器
#               说明：匹配所有的不可见元素，或者tyle为hidden的元素
#               示例：$('hidden') //匹配所有的隐藏域
#           :image
#               简称：图片域选择器
#               说明：匹配所有的图片域
#               示例：$(':image') //匹配所有的图片域
#           :password
#               简称：密码框选择器
#               说明：匹配所有的密码域
#               示例：$(':password') //匹配所有的密码域
#           :radio
#               简称：单选框选择器
#               说明：匹配所有的单选框按钮
#               示例：$('radio') //匹配所有的单选按钮
#           :reset
#               简称：重置按钮选择器
#               说明：匹配所有的重置按钮，即type="reset"的input元素
#           :submit
#               简称：提交按钮选择器
#               说明：匹配所有的提交按钮，即type="submit"的input元素
#               示例：$('reset') //匹配所有的提交按钮
#           :text
#               简称：单行文本选择器
#               说明：匹配所有的单行文本框
#               示例：$(':text') //匹配所有的单行文本框
#   选择器中的注意事项
#       选择器中含有特殊符号的注意事项
#           示例：<div id="mr#soft">justin</div>
#           正确提法：$('#mr\\#soft')
#           示例：<div id="mrsoft(1)">justin</div>
#           正确提法：$('#mrsoft\\(1\\)')
#       选择器中含有空格的注意事项

#【day191】jQuery对象和DOM对象
#获取$标签对象
#   格式
#       var 变量名 = $('css选择器')
#   示例
#       var idName = $('#idName')
#jQuery对象与DOM对象之间的转换
#   jQuery对象转DOM对象
#       var jsDiv = jqDiv[0]
#       var jsDiv = jqDiv.get(0)
#   DOM对象转jQuery对象
#       var jqDiv = $(jsDiv)
#jQuery常用方法
#   元素内容操作
#       文本内容
#           元素的起始标记和结束标记之间的内容，不包标记和子元素，只包含文本内容
#               设置文本内容
#                   var jqIdName = $('#idNmae').text('<h1>文本内容</h1>')
#                   注意：当有多个元素时，此方法会将所有元素的文本内容进行赋值
#                        元素原来的内容将被新设置的内容替换掉，包括所有子元素
#                        设置文本内容时，即使内容包含html代码，也将被认为是普通文件，并不能被作为html代码被浏览器解析
#               提取文本内容
#                   var jqIdName = $('#idNmae').text()
#                   注意：当有多个元素时，只提取第一个元素的文本内容
#                       怎么提取第二个元素
#                           var jqIdName2 = $('#idNmae:ep(1)').text()
#       html内容
#           元素的起始标记和结束标记之间的内容，包含标记和子元素
#               设置文本内容
#                   var jqIdName = $('#idNmae').html('<h1>文本内容</h1>')
#                   注意：当有多个元素是，此方法会将所有元素的文本内容进行赋值
#                        设置html内容时，包含html代码，将被认为是DOM元素，会被作为html代码被浏览器解析
#               提取文本内容
#                   var jqIdName = $('#idNmae').html()
#                   注意：当有多个元素时，只提取第一个元素的文本内容
#                       怎么提取第二个元素
#                           var jqIdName2 = $('#idNmae:ep(1)').html()
#   元素值操作
#       文本框的值
#           设置<input type="text">的value值
#               var jqValue = $('input').val('417217170')
#               注意：当有多个input时，$('input').val()赋值会将全部input都赋值
#           提取<input type="text">的value值
#               var value1 = $('input').val()
#               注意：当有多个input时，只提取第一个input的value值
#                   怎么提取第二个元素
#                       var value2 = $('#idNmae:ep(1)').val()
#       复选框的值
#           设置<input type="checkbox" value='a'>的value值
#               var jqValue = $('input[type="checkbox"]').val(['a','b'])
#               注意：当有多个复选框时，$('input[type="checkbox"]').val(['a','b'])设置的值与复选框的value值相同，则选中该选项
#           提取<input type="checkbox">的value值
#               var value1 = $('input[type="checkbox"]').val()
#               注意：当有多个复选框时，只提取第一个input的value值
#                   怎么提取第二个元素
#                       var value2 = $('input[type="checkbox"]:ep(1)').val()
#       单选框的值
#           设置<input type="radio" value="a">的value值
#               var jqValue = $('input[type="radio"]').val(['a'])
#               注意：当.val([a])设置值时，变量a的值与input中value值相同时，该单选按钮被选中
#           提取<input type="radio">值
#               var value1 = $('input[type="radio"]').val()
#               注意：当有多个input时，只提取第一个input的value值
#                   怎么提取第二个元素
#                       var value2 = $('input[type="radio"]:ep(1)').val()
#       下拉菜单的值
#           设置select的value值
#               var jqValue = $('select').val(['列表选项2'])
#               注意：当给下来菜单select赋值时，赋的值与option的value相同时，则选中该选项。
#           提取select的value值
#               var value1 = $('select').val()
#               注意：当select有多个option的value时，只提取第一个option的value值
#                   怎么提取第二个元素
#                       var value2 = $('select:ep(1)').val()
#       小技巧：获得dom的jquery对象
#           $('div').val('')
#           可以方便查看此dom的属性
#
#   节点操作
#       jquery新增节点
#           jquery新增元素节点
#               var jqElement = $('<p></p>')
#               插入节点
#                   $('div').append(jqElement)
#                   注意：如果有多个div则将会被插入多个jqElement
#           新增文本节点
#               var jqText = $('<h1>justin</h1>')
#               插入节点
#                   $('div').append(jqText)
#           新增属性节点
#               var jqAttr = $('<span id='s1'></span>')
#               插入节点
#                   $('div').append(jqAttr)
#       节点插入
#           在元素内部插入
#               为所有匹配到的元素内部末尾追加内容
#                   $('div').append(jqElement)
#                   jqElement.appendTo($('div'))
#               为所有匹配到的元素内部开始追加内容
#                   $('div').prepend(jqElement)
#                   jqElement.prependTo($('div'))
#           在元素外部插入
#               为所有匹配到的元素之后追加内容
#                   $('div').after(jqElement)
#                   jqElement.insertAfter($('div'))
#               为所有匹配到的元素之前追加内容
#                   $('div').before(jqElement)
#                   jqElement.insertBefore($('div'))
#       删除节点
#           删除匹配到的元素，包括该元素中的后代元素
#               $('div p').remove()
#               注意：
#           删除匹配到的元素，包括该元素中的后代元素
#               $('div p').detach()
#           清空匹配到的元素的内容，不删除标记
#               $('div p').empty()
#       复制节点
#           $('div p').clone()
#       带事件复制节点
#           $('div p').clone(true)
#       替换节点
#           $('div p').replaceAll(selector)
#               将匹配到的元素全部替换掉selector匹配到的元素
#               注意：替换元素将被删除
#           $('div:first').replaceWith('<div>123</div>')
#               将参数中的新元素替换掉匹配到的元素
#       遍历节点
#           $('p').each(function(index){$(this).attr('title','我是第'+(index+1)+'个')})
#               index表示下标，第一次遍历时，index=0...
#       外层包裹节点
#           $('span').wrap('<p></p>')
#       去除外层包裹
#           $('span').unwrap()
#       内部包裹节点
#           $('span').wrapInner('<b></b>')
#       整体包裹
#           $('#div1 span').wrapAll('<p></p>')
#   增加类名属性
#       var jqClassName = $('#div1').addClass('className1')
#           css类可以先写好，同过改变元素的class，从而给元素设置css样式
#   删除类名属性
#       var jqClassName = $('#div1').removeClass('className1')
#   智能增删类名属性
#       $('#div1').toggleClass('className1' [,true(增加类名)/,false(删除类名)])
#       说明：$('button').bind('click',function(){$('#div1').toggleClass('className1')})
#            当我第一次点击此按钮时，会给#div1设置className。点击第二次的时候会删除此className
#   增加或修改属性和属性值
#       格式：var jqId = $('#id').attr('属性','属性值')
#       示例：var jqId = $('#id').attr('class','c1')
#   增加或修改样式属性和样式属性的值
#       $(#div1).css('background-color','yellow')
#       $(#div1).css('position','relative')...
#   获取样式属性的值
#       var color = $(#div1).css('background-color')
#   添加事件
#       $('button').bind('click',function(){$(this).addClass()})

#【day192】jQuery事件
#触发事件的方法
#   页面加载完毕事件
#       $(document).ready(function(){})
#       简写
#           $().ready(function(){}) //$()不带参数默认是document
#           $(function(){})
#       说明
#           dom元素载入完毕后就能执行
#           在一个页面中可以调用多个$(document).ready(function(){})而且先执行前面的后执行后面的，互不影响
#           $(function(){})的效率快，因为它是等所有dom元素完全下载到浏览器就执行，而不用等dom元素所关联的图片等文件加载完毕再执行
#           今后所有的js和jq代码都写在这方法的函数体里
#       注意
#           唯一缺陷在于可能出现元素的关联文件尚未下载完全的情况，若此时要获取图片的高度或宽度属性是未必会有效的
#   页面加载事件
#       如果出现以上问题可以给img等元素执行.load()方法
#           $('img').load(function(){})
#       将.load()方法使用在window上
#           $(window).load(function(){})
#               等价于window.onload = function(){}
#   聚焦事件
#       $('#d1').focus(fn)
#   离焦事件
#       $('#d1').blur(fn)
#   元素值变事件
#       $('#d1').change(fn)
#   单击事件
#       $('#d1').click(fn)
#   双击事件
#       $('#d1').dblclick(fn)
#   异常处理事件
#       $('#d1').error(fn)
#   键盘按键按下事件
#       $('#d1').keydown(fn)
#   键盘按键抬起事件
#       $('#d1').keyup(fn)
#   键盘按下抬起事件
#       $('#d1').keypress(fn)
#   加载完毕事件
#       $('#d1').load(fn)
#   鼠标按下事件
#       $('#d1').mousedown(fn)
#   鼠标点击释放事件
#       $('#d1').mouseup(fn)
#   鼠标移动事件
#       $('#d1').mousemove(fn)
#   鼠标移入事件
#       $('#d1').mouseover(fn)
#   鼠标移出事件
#       $('#d1').mouseout(fn)
#   鼠标移入移出事件
#       $('#d1').hover(function(){console.log('鼠标移入')},function(){console.log('鼠标移出')})
#       注意：不要移入触发事件函数时，需要用null补位
#   窗口大小改变事件
#       $('#d1').resize(fn)
#   滚动条变化事件
#       $('#d1').scroll(fn)
#   文本查看事件（包括在input中和textarea中）
#       $('#d1').select(fn)
#   表单提交事件
#       $('#d1').submit(fn)
#   元素卸载事件
#       $('#d1').unload(fn)
#绑定事件
#   bind
#       $('#id').bind('click'[,data],fn())
#       data可将外部值传入fn中
#       问题：效率问题——它采用隐式迭代，点击一次匹配的标签，它会将所有匹配到的标签的bind都再执行一次，也就是说你给4个标签绑定了事件，触发一个，虽然只能看见触发了一次事件，但其实它触发了4次
#            对于尚未存在的标签无法绑定事件
#       适用：给有id属性的标签添加事件
#   delegate
#       $('div').delegate('p', 'click', function(){})
#       说明：给div绑定事件，让div中的p去执行事件触发，触发点击事件，事件函数
#            采用的是事件委托的方式，将事件委托给父级元素，当点击父级元素时，以冒泡的形式将事件传递给对应的子元素，让子元素来触发事件函数
#       问题：如果dom层级比较深，它需要一层一层往里传也比较消耗资源
#       适用：dom层级不深的父元素
#       适用事件：mousedown mouseup keydown keypress keymove 因为事件必须能够冒泡
#   on
#       $('div').on('click', 'p', function(){})
#       说明：跟delegate原理相同，仅仅只是将参数掉了一下位子
#   one
#       $('button').one('click',function(){})
#       说明：绑定一次性事件
#   总结
#       选择器匹配到的元素比较多时，不要用bind()迭代绑定
#       用id选择器时，可以用bind()
#       需要给动态添加的元素绑定时，用on()
#       on()方法的dom树不要太深
#       尽量用on()
#事件移除
#   移除bind绑定的事件
#       $('div p').unbind('click')
#   移除delegate绑定的事件
#       $('div p').undelegate('p', 'click')
#   移除on绑定的事件
#       $('div p').off('click', 'p')
#模拟用户行为的操作触发事件
#   trigger('模拟事件', ['传参1','传参2'])
#       var even = $('button').bind('click', function(e, mag1, mag2){console.log(mag1, mag2)})
#       even.trigger('click', ['justin', 'good']) //模拟人点击按钮
#       当标签为a时会有默认行为跳转，在模拟行为事件中返回一个false，即可阻止默认行为执行
#           $('a').bind('click', fn(){return false}).trigger('click')
#   TriggerHandle()
#       用法同trigger一模一样
#       区别：它不会导致浏览器同名的默认行为被执行，而trigger会导致同名的默认行为被执行
#模拟用户行为的鼠标悬停事件
#$('#b1').hover(function(){console.log('鼠标移入')},function(){console.log('鼠标移出')});


#【day193】jQuery事件对象
#$('#div1').bind('click', function(e){console.log(e)});
#事件对象的常用属性
#   点击事件对象
#       e.type //触发事件的类型
#       e.target //触发事件的当前dom元素
#       e.relatedTarget
#           $('button').bind('mouseover',function(e){e.relatedTarget})事件时，其值为从哪个dom移入到按钮dom
#           $('button').bind('mouseout',function(e){e.relatedTarget})事件时，其值为从按钮dom移出到哪个dom
#       e.pageX //鼠标离页面左端的距离
#       e.pageY //鼠标离页面顶端的距离
#   键盘事件对象
#       同js
#   鼠标事件对象
#       同js
#阻止冒泡事件
#   方式一
#       e.stopPropagation()
#           说明：在不需要冒泡的函数中添加此方法
#               $('#d1').bind('click', function(e){
#                   $(this).css('background-color','blue');
#                   e.stopPropagation() //阻塞冒泡事件
#               });
#               $('body').bind('click', function(){$(this).css('background-color','red')});
#   方式二
#       return false
#           说明：在不需要冒泡的函数中添加此方法
#                特别强大，可以阻止默认行为和事件冒泡
#               $('#d1').bind('click', function(e){
#                   $(this).css('background-color','blue');
#                   return false //阻塞冒泡事件
#               });
#               $('body').bind('click', function(){$(this).css('background-color','red')});
#阻止默认行为
#   $('a').bind('click', function(e){
#       var d = window.confirm('网页有病毒！确认是否继续')
#       if (d === false) {
#           //e.stopPropagation() 阻止事件冒泡
#           //e.preventDefault() 阻止默认行为
#           return false 阻止事件冒泡又阻止默认行为
#       }
#   })


#【day194】动画效果
#元素隐藏
#   $('#button').bind('click', function(){$('#div').hide(1000[,fn])})
#       说明:点击按钮，div在1000毫米内消失
#           预设值
#               'slow'    600ms
#               'normal'  400ms
#               'fast'    200ms
#           fn 当元素消失后调用
#元素显示
#   $('#button').bind('click', function(){$('#div').show(1000[,fn])})
#           说明:点击按钮，div在1000毫米内显示
#元素显示和隐藏切换
#   $('#button').bind('click', function(){$('#div').toggle(1000[,fn])})
#       说明:点击按钮，点一下div是显示的，则在1000毫米内隐藏，再点一下按钮，div在1000毫米内出现
#元素淡入
#   $('#button').bind('click', function(){$('#div').fadeIn(1000[,fn])})
#       说明:点击按钮，点一下div在1000毫米内淡入
#元素淡出
#   $('#button').bind('click', function(){$('#div').fadeOut(1000[,fn])})
#       说明:点击按钮，点一下div在1000毫米内淡出
#淡入淡出切换
#   $('button').bind('click', function(){$('#div').fadeToggle(1000[,fn])})
#透明度设置
#   $('#button').bind('click', function(){$('#div').fadeTo(1000, 0.1)})
#       点击按钮后，1秒内div的透明度达到0.1
#       注意：透明度若为0，其位置保留
#向上滑动隐藏
#   $('#button').bind('click', function(){$('#div').slideUp(1000[,fn])})
#       点击按钮后，1秒内div的高度向上逐渐减少直到隐藏div
#向下滑动显示
#   $('#button').bind('click', function(){$('#div').slideDown(1000[,fn])})
#       点击按钮后，1秒内div的高度向下逐渐增加直到显示div
#滑动显示隐藏切换
#   $('#button').bind('click', function(){$('#div').slideToggle(1000[,fn])})
#       点击按钮后，1秒内div的高度向下逐渐增加直到显示div
#       注意：按钮显示的名称可以使用回调函数设置值，源码见jQueryBaseCode
#自定义动画
#   $('body').css('position','relative')
#   var a = $('div').css('position','absolute').css('left',0).css('top',0).animate({left:'200px'},1000).delay(1000).animate({left:'+=200px'},1000,[,fn])
#       说明：给body设置position属性
#            给div设置css属性，可以在css中设置
#            1000毫秒后移动到left为200px的位置
#            动画延迟1000毫秒
#            1000毫秒后移动到left为当前位置+200px的位置（可+= 可-=）
#   停止自定义动画
#       $('#button').bind('click', function(){a.stop(true,true)})
#           点击按钮停止自定义动画
#           stop的第一个参数表示是否清空当前动画队列（多个animate会有多个动画被放入队列中，如果参数为false，则只停止第一个动画，其余的动画继续执行）
#           stop的第二个参数表示是否将元素回档到当前动画的结束位置，如果为true，则回到动画的结束位置，如果为false，则立即停止在当前位置
#   判断正在执行的动画
#       $('#button').bind('click', function(){
#           if (!a.is(':animated')){
#               console.log('动画不执行是，此按钮可用')
#           }
#       })


#【day195】apache安装与配置
#apache软件下载
#   http://httpd.apache.org/ -> Download -> Files for Microsoft Windows -> Apache Lounge -> httpd.2.4.39-win64-VC15.zip
#       将压缩包解压到目标文件（可其他盘符）
#           Apache24 -> conf -> sublime打开httpd.conf -> ctrl+f 搜索 SRVROOT -> 将其值改为当前apache的安装路径D:/apache/Apache24（注意斜杠是正斜杠/）
#               创建一个Apache24同级目录justin
#                   httpd.conf -> 搜索DocumentRoot -> 将DocumentRoot "${SRVROOT}/htdocs"和<Directory "${SRVROOT}/htdocs">的值修改为DocumentRoot "D:/apache/justin"和<Directory "D:/apache/justin">
#                       如果端口号80被占用则该为1024以上的端口号 -> httpd.conf -> 搜索Listen -> 将Listen 80 改为 Listen 8080
#                           搜索LoadModule ssl_module > 将LoadModule ssl_module modules/mod_ssl.so注释掉
#                               保存配置

#【day196】启动apache
#管理员身份打开cmd -> 进入cd D:\apache\Apache24\bin -> 输入httpd.exe
#   if 报错msvcr110文件丢失:
#       网络下载此文件
#       复制到C:\Windows\System32中
#   if AH00558: httpd.exe: Could not reliably determine the server's fully qualified domain name, using 192.168.0.102. Set the 'ServerName' directive globally to suppress this message:
#       httpd.conf搜索ServerName -> 将ServerName www.example.com:80 修改为ServerName localhost:80 并且去掉#
#   if (OS 10048)通常每个套接字地址(协议/网络地址/端口)只允许使用一次。  : AH00072: make_sock: could not bind to address [::]:8080:
#       httpd.conf -> 搜索Listen -> 将Listen 8080 改为 Listen 80
#   if 光标换行 and 不能键入任何信息:
#       安装成功
#       打开浏览器输入http:localhost测试你的服务器
#       if ctrl + c:
#           exit httpd.exe
#安装成功后
#双击D:\apache\Apache24\bin\ApacheMonitor.exe
#   左键单击apache图标 -> apache -> start
#       if 出现The requested operation has failed 提示:
#           修改conf的端口号
#           重启apache
#           点击apache start
#   启动成功即可通过ip或localhost访问本机服务器
#   D:/apache/justin在这个配置的文件夹中放入html即可在浏览器中访问这些网页

#【day197】网络编程的一些概念
#url
#   统一资源定位符，是互联网上资源的地址
#   http:// www.aspxfans.com :8080/ news/ index.asp ?boardID=5&ID=23453&page=1 #name
#   协议     域名也可以是ip     端口号（如果不写，默认为80端口）  目录   文件名     参数                        锚
#同源策略
#   同协议 同域名或ip 同端口
#   json数据文件和html文件只有同源，html才能访问到json数据文件，即在html中发起一个网络请求，这个请求的url必须跟自己的协议、域名、端口相同才能访问得到另一个放在apache服务器上的文件
#apache和浏览器的工作原理（页面加载流程）
#   1、浏览器首先在本地的hosts文件中查找域名对应的ip地址
#   2、如果没有在本地查找到域名对应的ip地址，就去DNS服务器中去查找
#   3、拿到ip地址后，通过ip地址就能链接web服务器（对方电脑），链接后就发送一条流形式的html协议，告诉服务器我要访问哪个文件的请求，就开始等待服务器发送信息
#   4、服务器接收到消息之后，就开始解析数据流，解析之后，服务器就知道浏览器想要访问哪个文件，就去服务器本地将这个文件读成json数据流，之后再以流的形式将数据流发送给浏览器
#   5、浏览器接收到数据流之后，开始解析数据流，最后将解析出的html、css、js等代码渲染到浏览器页面中，完成访问

#【day197】$(document).ajax 网络请求
#通过发起网络请求实现动态加载数据
#   滚轮绑定的事件/按钮绑定的事件都可以触发事件函数，事件函数中就可以写入ajax，给服务器发送请求
#   其中success为服务器返回消息成功后的触发，此事的事件函数的参数dada就是json串，通过字典访问的形式就能拿到我们需要的数据集合，再通过遍历创建元素就能插入到页面中进行显示
#   $.ajax({type:'get',   //网络请求的形式 post请求不会把data贴到网址上发送，而是单独打包发送，适用于密码发送
#           url:'http://192.168.0.102:8090/json/caidanJson.json'   //要访问的服务器目录文件
#           data:{a:1, b:2}   //给服务器发送的数据
#           dataType:'json',  //传送数据的类型
#           success: function(data, textStatus){
#                   console.log(textStatus) //它仅仅只是显示连接成功与否的状态
#                   var caiDanArray = data['breakfast_menu']['food'];  //这个data就是服务器给浏览器返回的数据
#                   for (var i=0; i<caiDanArray.length; i++){   //遍历获取数据
#                       //新建元素并插入到dom中
#                       $('#d'+(i+1)).append($('<h1>' + caiDanArray[i]['name'] + '</h1>')).fadeIn(1000);
#                       $('#d'+(i+1)).append($('<p>' + caiDanArray[i]['description'] + '</p>')).fadeIn(1000);
#                       $('#d'+(i+1)).append($('<p>' + caiDanArray[i]['calories'] + '</p>')).fadeIn(1000);
#                       $('#d'+(i+1)).append($('<p>' + caiDanArray[i]['price'] + '</p>')).fadeIn(1000);
#               }   //请求成功后触发的函数
#           })
#发送请求后常用的事件触发
#   success 成功的回调
#   error   失败的回调
#
#【day198】表单序列化
#form表单的序列化
#   将fomr中的控件的name值作为键，控件里面的value作为值，生成并返回字典
#html
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>sublime</title>
    #     <link rel="stylesheet" href="css/sublime.css">
    # </head>
    # <body>
    #     <form action="#" id="testForm">
    #         用户名：<input type="text" id="username" name="username">
    #         <br>
    #         性别：<input type="text" id="sex" name="sex">
    #         <br>
    #         年龄：<input type="text" id="age" name="sex">
    #         <br>
    #         邮箱：<input type="text" id="email" name="sex">
    #         <br>
    #         地址：<input type="text" id="address" name="sex">
    #         <br>
    #         内容：<textarea id="content" name="content" cols="30" rows="10"></textarea>
    #         <br>
    #         <input type="button" id="button" name="button" value="提交">
    #         <br>
    #         <div id="responseText"></div>
    #     </form>
    # </body>
    # <script src="js/jQuery.js"></script>
    # <script src="js/sublime.js"></script>
    # </html>
#form序列化提交
    # $(function () {
    #     $('#button').bind('click', function(){
    #         $.ajax({
    #             type:'post',
    #             url:'#',
    #             data:$('#testForm').serialize(),
    #             dataType:'json',
    #             success:function(data,textStatus){
    #                 console.log(textStatus);
    #                 var html = '';
    #                 html += '用户名：' + data.username + '<br>';
    #                 html += '性别' + data.sex + '<br>';
    #                 html += '年龄' + data.age + '<br>';
    #                 html += '邮箱' + data.email + '<br>';
    #                 html += '内容' + data.content + '<br>';
    #                 $('#responseText').html(html);
    #             }
    #         })
    #     })
    # });
#序列化的优势在于提取表单val时不需要找到每个控件提取它的值，而只需要找到表单调用serialize方法即可提取出所有的表单控件的值
#   $('form').serialize() === {username:$('#username').val(),
#                               sex:$('#sex').val(),
#                               age:$('#age').val(),
#                               email:$('#email').val(),
#                               address:$('#address').val(),
#                               content:$('#content').val()}

#【day199】网络请求前触发的事件，网络请求成功后触发事件
# $(document).ajaxStart(function(){$('#div').html('正在获取数据..').show(1000)})
# $(document).ajaxStop(function(){$('$#div').html('数据获取成功').slideDown(1000)})
# 常用于友好提示

#【day200】h5c3
#h5新标签
#    结构化标签
#        <article>   文章
#        <aside>     列表
#        <footer>    页脚
#        <header>    页眉
#        <nav>       导航
#        <section>   块
#    非结构化标签
#        <audio>     音频
#        <video>     视频
#        <canvas>    画布
#        <command>
#        <datalist>  文本框下拉提示
#           与input联用的下拉信息提示，将id属性值设置为input的list属性值就能实现文本框下拉提示，要显示的内容用option的value显示
#               <input type= "text" list="data" placeholder="1">
#               <datalist id="data">
#                   <option value="1"></option>
#                   <option value="2"></option>
#                   <option value="3"></option>
#               </datalist>
#        <details>   下拉显示
#           示例
#               <details>
#                   <summary>喜欢的水果</summary>
#                   <p>香蕉</p>
#               </details>
#        <figure>   插图的说明
#        <mark>     加强语气
#        <progress> 进度条
#           与定时器联用就能出现效果
#               <progress max="100" value="0">
#               <script>
#                   var num=0;
#                   setInterval(function(){
#                       $(progress).val(''+num)
#                       num++
#                   },1000)
#               </script>
#        <source>   音频视频中使用的
#        <time>     日期
#h5表单的新特性和函数
#    placeholder=''      默认显示
#    autocomplete='on'   自动补全
#        <form autocomplete='on'> form表单下所有的input都开启自动补全功能
#        <input autocomplete='on'> 该input下开启自动补全功能
#    autofocus='autofocus'  自动聚焦
#    required='required' 必填项
#    pattern='正则表达式'  只能输入正则表达式对应的内容
#    form='idName'       书写在from表单外的input可以添加此属性，属性值等于form表单的id，则表示该input在form中
#    disable='disable'   禁用
#    readonly='readonly' 只读
#    multiple='multiple' 多选
#    draggble='true'     可拖拽
#h5拖放API
#   拖放事件
#       dragstart
#           网页元素开始拖动时触发
#       drag
#           被拖动的元素在拖动过程中持续触发
#       dragenter
#           被拖动的元素进入目标元素时触发，应在目标元素监听该事件
#       dragleave
#           被拖动的元素离开目标元素时触发，应在目标元素监听该事件
#       dragover
#           被拖动的元素停留在目标元素之中时持续触发，应在目标元素监听该事件
#       drop
#           被拖动元素或文件系统选中的文件，拖放落下时触发
#       drogend
#           网页元素拖动结束时触发
#   拖放事件实现的步骤
#       将想要拖放的对象元素的draggable属性设为true
#       拖动什么 —— ondragstart 和 setData()
#       拖放何处 —— ondragover
#       进行放置 —— ondrop 和 getData()
#实现：图片来回拖放，源码见webStrom的图片拖拽.html

#【day201】css3的新特性
#新选择器（css选择器）
#   属性选择器
#       p[class]{}
#       p[class = 'itme']{}
#       p[class != 'itme']{}
#       p[class *= 'itme']{}
#       p[class ^= 'itme']{}
#       p[class $= 'itme']{}
#   结构性伪类选择器
#       a:link
#       a:visited
#       a:hover
#       a:active
#       div:first-line{}     选中元素中的第一行文字
#       div:first-letter{}   选中元素中的第一个文字
#       p:before{content:'插入文字' color:'red'}   选中元素中文本的前面加入文本（content内容可以插入空内容之再设置它的display为block相当于一个div，对其可以设置宽高背景颜色定位等）
#       p:after{content:'插入文字' color:'red'}   选中元素中文本的后面加入文本
#       :root{}                页面根元素
#       #div1 p:not('#p2'){}   排除指定的元素
#       :empty{}               内容为空白的元素
#       div:target{}           给跳转当前锚元素设置css
#       :first-child{}         第一个子元素
#       :last-child{}          最后一个子元素
#       :nth-child{n}          第n个元素
#       :nth-last-child{}      倒数第n个元素
#       :nth-child{odd}        奇数元素
#       :nth-child{even}       偶数元素
#       :nth-of-type{n}        在其父元素下，找指定元素的第n个
#       :nth-last-of-type{}    在其父元素下，找指定元素的倒数第n个
#       :only-child{}          仅有一个子元素
#   UI状态伪类选择器
#       :hover{}                    移入时的样式修改
#       :active{}
#       input:focus{}               聚焦时修改样式
#       :disabled{}                 禁用状态下的样式修改
#       :enabled{}                  可用状态下的样式修改
#       :read-only{}                有readonly='readonly'属性时的样式修改
#       :read-write{}               可读可写时的样式修改
#       :checked{}                  选中状态下的样式修改
#       :indeterminate
#       #item1 ~ p                  通用兄弟元素选择器 #itme1 下面的所有的p
#新的特性
#   文字与字体相关样式
#       给文字添加阴影
#           语法：text-shadow:length1 length2 length3 color;
#           说明：length1 必选参数 指阴影离开文字的横方向位移，正数为向右
#                length2 必选参数 指阴影离开文字的纵方向位移，正数为向下
#                length3 可选参数 指阴影的模糊半径，值越大，模糊的范围越大。省略参数则默认为0，代表阴影不向外模糊
#                color   可选参数
#       指定多个阴影语法
#           text-shadow:length1 length2 length3 color1, length4 length5 length6 color2;
#       文字自动换行
#           word-break:normal     使用浏览器默认的换行规则
#                      break-all  只允许单词内换行
#                      keep-all   只能在半角空格或连字符处换行
#       文字溢出处理
#   盒阴影
#       box-shadow:length1 length2 length3 color;
#   盒内阴影
#       box-shadow:inset length1 length2 length3 length4 color;
#   圆角
#       border-radius:
#       可以是1值 2值 3值 4值
#   使用图像边框
#       border-image
#   背景图像大小设置
#       background-size
#   背景图片放置的位置
#       background-origin:content-box; 放置在内容区域
#                         padding-box; 放置在padding区域
#                         border-box;  放置在border区域
#   渐变颜色
#       线性渐变
#           background: linear-gradient(to bottom,red,yellow,green...) //渐变方向（bottom/top/left/right/left bottom/left top/right bottom/right top/），第一种颜色，第二种颜色
#       径向渐变
#           background: radial-gradient(circle 50px,pink,green) //径向渐变的形状 circle圆形 直径大小 ellipse椭圆形
#       文字颜色渐变（彩色文字、霓虹文字）
#           background: linear-gradient(45deg, pink, yellow, green);
#           -webkit-background-clip: text; //规定背景的绘制区域 border-box padding-box content-box text 背景被裁剪到边框盒/内边距框/内容框/文本
#           -webkit-text-fill-color: transparent; //文字填充上颜色
#       重复渐变
#           background: repeating-radial-gradient(deepskyblue 10px, white 20px); //注意：前面的宽度要比后面的小
#     animation: run 3s infinite
#     @keyframes run {
#         from{
#             transform: rotate(0deg);
#         }
#         to{
#             transform: rotate(360deg);
#         }
#     }
#综合应用
#案例

#【day202】flex布局
#概念
#   flex是Flexible Box的缩写，意为"弹性布局"，也叫"响应式布局"，用来为盒状模型提供最大的灵活性，任何一个容器都可以指定为Flex布局，即display:flex; 行内元素也可以使用flex布局，即display:inline-flex;
#       注意：设为flex布局以后，子元素的float、clear和vertical-align属性将失效
#   采用flex布局的元素，称为flex容器(flex container)，简称'容器'，它的所有子元素自动成为容器成员，称为flex项目（flex item），简称‘项目’
#   容器默认存在两个轴，水平的主轴（main axis）和垂直的交叉轴（cross axis）。主轴的开始位置（与边框的交叉点）叫做main start，结束位置叫做main end；交叉轴的开始位置叫做cross start，结束位置叫做cross end。
#   项目默认沿主轴排列，单个项目占据的主轴空间叫做main size，占据的交叉空间叫做cross size
#语法
#   新flex布局
#       display:flex;
#       justify-content:center;
#       align-items:center
#       align-content
#       flex-wrap
#       flex-flow
#       flex-direction
#   旧flex布局
#       display:flex-box, box
#       box-pack:center
#       box-align:center
#       box-direction, box-orient
#父级元素必须设置的显示方式
#   display:flex;
#6大容器属性
#   以下6个属性设置在容器上，定义容器中的项目的对齐方式
#       方向与换行属性
#           flex-direction:row/column/row-reverse/column-reverse;
#               效果：子元素按行方向排列/列方向排列/行方向并倒置/列方向并倒置
#               注意：设置在父级元素上
#           flex-wrap:nowrap/wrap/warp-reverse;
#               功能：当子元素在一条轴线上宽度或高度超出父元素的宽度或高度如何换行
#               值：nowrap 不换行，宽或高自动缩小
#                   warp   子元素排不下就换行，第二行从父元素高度的一般开始排
#                   warp-reverse 子元素从底部开始往右排，排不下就换行，第二行从父元素高度一般的地方开始往右排，可让没超父元素的子元素到底部
#           flex-flow:row nowrap;
#               说明：它是flex-direction和flex-wrap的合写
#       行方向上的对齐方式属性
#           justify-content:flex-start/flex-end/center/space-between/space-around/space-evenly
#               功能：项目在行方向上的对齐方式
#               值：flex-start 对齐横轴的开始，即左对齐
#                   flex-end  对齐横轴的结尾，即右对齐
#                   flex-center 居中对齐
#                   space-evenly 所有空隙均分
#                   space-around 项目收尾空隙为固定值，其余均分
#                   space-between 项目收尾空隙为零，其余均分
#                   stretch 默认选线
#       单列方向上的对齐方式属性
#           align-items:flex-start/center/flex-end/baseline/stretch;
#               功能：定义项目在列方向上如何对齐
#               值：flex-start 对齐纵轴的开始，即上对齐
#                   center 上下居中对齐
#                   flex-end 对齐纵轴的结尾，即下对齐
#                   baseline 对齐第一个项目的top,向左看齐
#                   stretch 默认，项目的上面空隙为零，其余均分
#       多轴列方向上的对齐方式属性
#           align-content:flex-start/flex-end/center/space-evenly/space-around/space-between;
#               功能：定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用
#               值：flex-start 项目向上对齐
#                   flex-end 项目向下对齐
#                   center 项目上下居中对齐
#                   space-evenly 项目空隙均分
#                   space-around 项目收尾空隙固定，其余均分
#                   space-between 项目收尾空隙为零，其余均分
#                   stretch 默认，项目的上面空隙为零，其余均分
#6大项目属性
#   以下6个属性设置在容器上，定义容器中的项目的对齐方式
#       排序属性
#           order:1;
#               功能：定义了项目的排列顺序，给所有需要排序的项目添加编号属性值，数值越小越靠前
#       比例放大属性
#           flex-grow:1;
#               功能：给项目增加此属性后，项目之间的留白部分(如果有)会被填充满，而项目的宽度或高度会按照其值的比例进行放大，因此不需要设置项目的宽或高，只需要设置其容器的宽或高即可
#               用法：将flex-grow的值都设为1，则可将div平均分布在容器中（横向则横向平均分，纵向则纵向平均分）
#       比例缩小属性
#           flex-shrink:1;
#               功能：定义项目的缩小比例，默认为1，即如果超出容器，该项目按其设置的比例缩小
#       项目自定义宽或高属性
#           flex-basis:50px;
#               功能：有多于空间，给需要设置宽或高的项目设置固定宽或高，其余在按等比例缩放的数值填充
#       单独项目列方向布局
#           align-self: flex-start/center/flex-end

#【day203】移动端布局（手机端布局）
#视口
#   viewport
#       移动端屏幕比pc端屏幕小很多，因此一个针对桌面设计的界面不一定（或完全不）能很好的使用到移动端。所以，响应式来了
#       <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
#                   视口                  伸缩比例     1表示不伸缩   最大伸缩          最小伸缩        是否使用伸缩    不使用
#像素
#   css中的1px是设备上的1px吗？
#   两种像素
#       设备像素
#           设备屏幕的物理像素，任何设备的物理像素的数量都是固定的
#       css像素
#           为web开发者创造的，在css(JavaScript)中使用的一个抽象的层
#rem布局
#   rem是字体大小单位
#       定义子元素的字体大小与父级元素的字体大小的倍数
#       示例
#           #html{font-size:12px}
#           #box p{font-size:1rem}
#           此时 12px = 1rem
#
#           #html{font-size:16px}
#           #box p{font-size:1rem}
#           此时 16px = 1rem
#           计算 20px = (20/16)rem = 1.25rem
#   响应式设置html的字体大小
#       $(function(){document.documentElement.style.fontSize = innerWidth / 10 + 'px'});
#案例
#   见webStrom-手机端布局
#媒体查询
#   在css中设置媒体查询
#   @media (max-width: 700px){
#       #d1{
#           width: 100px;
#       }
#   }
#   说明：if 最大宽度（屏幕宽度）== 700px:
#           #d1的width = 100px
#【day204】多媒体
#视频播放
#   <video src="video/Django基本流程走通01.mp4" id="vid" controls="controls" width="1000px" height="500px"></video>
#       属性：controls="controls" 是否在视频播放窗口显示自带的媒体按钮
#            $('video')[0].duration 视频总时长
#            $('video')[0].currentTime 视频播放当前时间
#            $('video')[0].volume 音量
#       方法：$('video')[0].play() 开始播放
#            $('video')[0].pause() 视频暂停
#            $('video')[0].webkitRequestFullScreen() 全屏
#            $('video')[0].addTextTrack() 向视频中添加新的文本轨迹
#            $('video')[0].load() 重新加载一个视频元素
#音频播放
#   <audio src='.mp3' loop="loop" autoplay="autoplay"></audio>
#   属性：loop='loop' 循环播放
#        autoplay='autoplay' 自动播放
#        muted = true/false 是否静音
#        $('audio')[0].currentTime  当前播放时间
#        $('audio')[0].duration 当前音频的总时长
#   方法：$('audio')[0].play() 播放音乐
#        $('audio')[0].pause() 音乐暂停
#格式问题
#   <video width="500" height="500" controls="controls">
#       <source src="movie.ogg" type="video/ogg">
#       <source src="movie.mp4" type="video/mp4">
#   </video>
#   说明：规定视频使用什么格式播放

#【day205】css3动画
#如何做动画
#   transform-origin:
#       功能：修改基准点
#       语法：transform-origin:left,top //基准点在水平方向上的位置，在垂直方向上的位置
#   transform-start:
#       功能：给父级元素的css属性，使其子元素为3d对象,即让子元素在3d空间
#       语法：transform-start:preserve-3d
#   perspective:
#       功能：给腹肌元素的css属性设置透视距离、镜头距离，使其子元素的透视视角变化
#       语法：perspective: 1200px;
#   transform:
#       功能：2D实现缩放
#       语法：transform:scale(5) //水平垂直缩放5倍
#            transform:scale(5,0.5) //水平缩放5倍，垂直缩放0.5倍
#       功能：2D实现倾斜
#       语法：transform:skew(45deg) //水平方向的倾斜角度（沿-x轴方向倾斜）
#            transform:skew(45deg,45deg) //水平方向的倾斜角度（沿-x轴方向倾斜），垂直方向的倾斜角度（沿-y轴方向倾斜）
#       功能：2D实现移动
#       语法：transform:translate(100px) //水平方向上的移动距离
#            transform:translate(100px, 100px) //水平方向的移动距离，垂直方向的移动距离
#       功能：3D实现按元素的x轴、y轴、z轴进行旋转
#       语法：transform:rotateX(45deg);
#            transform:rotateY(45deg);
#            transform:rotateZ(45deg);
#            transform:rotateX(45deg rotateY(45deg) rotateZ(45deg);
#       功能：3D实现按元素的x轴、y轴、z轴的角度比例进行旋转
#            transform:rotate3d(1,0.5,1,45deg) //x轴角度占比：y轴角度占比：z轴角度占比 = 1:1:1 = 45deg(1/(1+0.5+1)) : 45deg(0.5/(1+0.5+1)) : 45deg(1/(1+0.5+1))
#            图像的3d比例和谐，图像看起来不走形
#       功能：3D实现按元素的x轴、y轴进行倾斜
#       语法：transform:skewX(45deg) //-x轴方向倾斜
#            transform:skewY(45deg) //-y轴方向倾斜
#       功能：3D实现按元素的x轴、y轴、z轴进行移动
#       语法：transform:translateX(50px);
#            transform:translateY(50px);
#            transform:translateZ(50px);
#       功能：3D实现按元素的x轴、y轴、z轴进行移动
#       语法：transform:translate3d(1rem,1rem,1rem)
#   动画@keyframes规则，animation属性
#       功能：通过定义多个关键帧以及定义每个关键字中元素的属性值来实现在页面上产生更为复杂的动画效果
#       定义动画过程：
#           @keyframe 关键帧集合名{创建关键帧的代码}
#           示例：@keyframe animation1{
#                   0%{background-color: lime;}
#                   50%{background-color: yellow;}
#                   100%{background-color: green;}
#               }
#               @keyframe animation2{
#                   from{left:0%}
#                   to{left:82%}
#               }
#           百分数说明：if duration == '2s':
#                         0%-50% = 0s-1s
#                         50%-100% = 1s-2s
#       绑定动画属性，绑定即执行动画效果
#           #d1{
#               animation:name duration timing-function delay iteration-count direction;
#           }
#               值：name 规定需要绑定到选择器的 keyframe 名称
#                  duration 规定完成动画所花费的时间，以秒或毫秒计
#                  timing-function 规定动画的速度曲线
#                       linear  动画从头到尾的速度是相同的
#                       ease  默认。动画以低速开始，然后加快，在结束前变慢
#                       ease-in 动画以低速开始
#                       ease-out  动画以低速结束
#                       ease-in-out  动画以低速开始和结束
#                       cubic-bezier(n,n,n,n) 在cubic-bezier函数中自己的值。可能的值是从 0 到 1 的数值。
#                  delay 规定在动画开始之前的延迟
#                  iteration-count 规定动画应该播放的次数
#                       1 默认
#                       n 可以写任意整数
#                       infinite 无限循环播放
#                  direction 规定是否应该轮流反向播放动画
#                       normal 默认值。动画应该正常播放，0%-50%-100%
#                       alternate 交替更改动画的执行方向，0%-50%-100%-50%-0%-50%-100%
#                       reverse 反方向执行动画，100%-50%-0%
#                       alternate-reverse 从反方向开始交替更改动画执行的方向 100%-50%-0%-50%-100%
#   过渡transition
#       功能：指定元素某个属性的开始值和结束值，定义从属性开始值平滑过渡到属性结束值值（相当于给一个元素的属性设置了一种定时器，当这个属性通过伪类触发或者事件触发改变时，该元素的原属性值平滑过渡到修改属性值）
#       语法：transition:property duration timing-function delay;
#       值：  property 表示对哪个属性操作
#            duration 表示在多久时间内完成属性值得平滑过渡
#            timing-function 表示通过什么方法平滑过渡
#            delay 表示延迟多长时间开始执行特效
#       示例：#d1{
#               transition:height 1000ms linear 1000ms
#           }
#            #d1:hover{
#               height: 2rem;
#            }
#       分别对应4个属性：
#           transition-property:
#               值：all 代表所有属性
#               说明；当我们需要修改多个属性值时，可以all来代表所有需要修改的属性
#           transition-duration:
#           transition-timing-function:linear/ease/ease-in/ease-out/ease-in-out/cubic-bezier(n,n,n,n)
#               值 linear 规定以相同速度开始至结束的过渡效果，等于cubic-bezier(0,0,1,1)
#                  ease 规定慢速开始，然后变快，然后慢速结束的过渡效果，等于cubic-bezier(0.25,0.1,0.25,1)
#                  ease-in 规定以慢速开始的过渡效果，等于cubic-bezier(0.42,0,1,1)
#                  ease-out 规定以慢速结束的过渡效果，等于cubic-bezier(0,0,0.58,1)
#                  ease-in-out 规定以慢速开始和结束的过渡效果，等于cubic-bezier(0.42,0,0.58,1)
#                  cubic-bezier(n,n,n,n) 在cubic-bezier函数中定义自己的值。可能的值是 0 至 1 之间的数值
#           transition-delay:
#   RequestAnimationFrame
#   setInterval
#   动画算子
#   动画库如jquery封装，Velocity.js

#【day206】触屏事件 手机事件 移动端事件
#touch.js
#什么是触屏事件
#   手指在屏幕上滑动，带来的一些效果
#   方便我们的操作
#   指尖上的行动
#分类以及触发时机
#   touchstart事件
#       事件命名：按下事件
#       触发时机：当手指触摸屏幕时候触发，即使已经有一个手指放在屏幕上也会触发
#       示例：$('#d1').on('touchstart',function(e){console.log(e)})
#   touchend事件
#       事件命名：抬起事件
#       触发时机：当手指从屏幕上离开的时候触发
#       示例：$(document).on('touchend',function(e){console.log(e)})
#   touchmove事件
#       事件命名：移动事件
#       触发时机：当手指在屏幕上滑动的时候连续地触发。在这个事件发生期间，调用
#       示例：$('#d2').on('touchmove',function(){console.log('手指移动')});
#   preventDefault事件
#       触发时机：可以阻止滚动
#   touchcancel事件
#       触发时机：当系统停止跟踪触摸的时候触发
#跟踪触屏的特性,事件对象e的属性
#   touches
#       表示当前跟踪的触摸操作的touch对象的数组
#       e.touches
#   targetTouches
#       特定于事件目标的Touch对象的数组
#       e.targetTouches
#   changedTouches
#       表示自上次触摸以来发生了什么改变的Touch对象的数组
#       e.changedTouches
#Touch事件对象e的属性的值
#   clientX
#       触摸目标在视口中的X坐标
#       console.log(e.touches[0]['clientX'])
#   clientY
#       触摸目标在视口中的Y坐标
#       console.log(e.touches[0]['clientY'])
#   identifier
#       标识触摸的唯一ID
#       console.log(e.touches[0]['identifier'])
#   pageX
#       触摸目标在页面中的X坐标
#       console.log(e.touches[0]['pageX'])
#   pageY
#       触摸目标在页面中的Y坐标
#       console.log(e.touches[0]['pageY'])
#   screenX
#       触摸目标在屏幕中的X坐标
#       console.log(e.touches[0]['screenX'])
#   screenY
#       触摸目标在屏幕中的Y坐标
#       console.log(e.touches[0]['screenY'])
#   target
#       触摸的DOM节点目标
#       console.log(e.touches[0]['target'])
#jqueryMobile的触屏事件
#案例
#   按下并触发出现跟随手指小球
#       见webStrom-触屏事件1
#   手机界面菜单的滑动和点击
#       见webStrom-触屏事件2

#【day207】bootstrap3.3.7
#下载
#   https://www.bootcss.com/ -> bootstrap3中文文档 -> 下载Bootstrap -> 下载Bootstrap
#       将下载好的文件解压
#           解压文件中的css文件夹以及js文件夹，它们中的文件分别布置到webstrom的css和js中
#载入bootstrap
#在html中
#<!DOCTYPE html>
#<html lang="zh-CN"> //注意lang的值为zh-CN
#    <head>
#       <!--手机端布局 可缩放-->
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <!--手机端布局 不可缩放-->
#       <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
#       <!--导入bootstrap css-->
#       <link href="css/bootstrap.min.css" rel="stylesheet">
#       <!--导入jquery-->
#       <script src="js/jQuery.js"></script>
#       <!--导入bootstrap js-->
#       <script src="js/bootstrap.min.js"></script>
#    </head>
#    <body>
#       <!--Bootstrap需要为页面内容和栅格系统包裹一个.container容器 或 .container-fluid容器
#       <div class="container"></div> //类用于固定宽度并支持响应式布局的容器
#       <div class="container-fluid"></div> //类用于 100% 宽度，占据全部视口（viewport）的容器
#    </body>
#</html>

#【day208】django基础流程
#简介
#   是一个开放源代码的web应用框架，由python写成
#   初次发布于2005年7月，并于2008年9月发布了第一个正式版1.0
#MVC
#   概述
#       一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚焦到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑，MVC被独特的发展起来用于映射传统的输入、处理和输出功能在一个逻辑的图形化用户界面的结构中
#   核心思想
#       解耦
#   编程模式
#       Model(模型)
#           是应用程序中用于处理应用程序数据逻辑的部分
#           通常模型对象负责在数据库中存取数据
#       View(视图)
#           是应用程序中处理数据显示的部分
#           通常视图是依据模型数据创建的
#       Controller(控制器)
#           是应用程序中处理用户交互的部分
#           通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据
#   流程
#       用户->发起查询数据的http请求->Controller捕捉请求->指挥Model在数据库中获取需求数据->Controller获取数据->指挥View展示数据->用户查询到数据
#   优点
#       降低各功能模块之间的耦合性，方便变更，更容易重构代码，最大程度上实现了代码的重用
#MTV
#   概述
#       本质上与MVC模式没有什么差别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同
#   编程模式
#       Model(模型)
#           负责业务对象与数据库的对象(ORM)
#       Template(模板)
#           负责如何把页面展示给用户
#       View(视图)
#           负责业务逻辑，并在适当的时候调用Model和Template
#   注意
#       Django还有一个url分发器，它的作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template
#   流程
#       用户输入url->url控制器->Template根据url匹配相应的View->相应View发送获取数据命令给Model->Model到数据库中取数据->Model将数据返回个View->View将数据渲染到Template中->Template将完整页面展示给用户
#安装
#   pip install Django
#创建项目
#   黑屏终端创建
#       在合适位置创建一个目录
#       打开黑屏终端进入到上一步创建的目录下
#       django-admin startproject projectName(可自由修改)
#       目录层级说明
#           porjectName
#               __init__.py
#                   一个空文件，它告诉python这个目录应该被看做一个python包
#               settings.py
#                   项目配置文件
#               urls.py
#                   url管理器，项目的URL声明——匹配视图
#               wsgi.py
#                   项目与WSGI兼容的Web服务器入口
#           manage.py
#               命令行工具，可以使我们用多种方式对django项目进行交互
#       可用pycharm打开第一个目录，即导入到pycharm
#   pycharm社区版中创建
#       new project
#           django
#           修改路径
#           勾选 Inherit global site-packages
#           create
#               右键点击venv目录
#                   单击Open in Terminal                                 bz1
#               django-admin startproject project(项目名称可自由修改)      bz2
#               cd project    #cd到有manage.py 的文件中                   bz3
#               python manage.py startapp app_asj(应用名称可自由修改)      bz4
#基本操作
#   设计表结构
#       班级表结构
#           表名设计
#               create table grades(
#                   字段设计
#                   主键    id int auto_increment primary key,
#                   班级名称 gName varchar(20) not null,
#                   成立时间 gDate varchar(20) not null,
#                   女生总数 gGirlNum int not null,
#                   男生总数 gBoyNum int not null,
#                   是否删除 isDelete bit default 0
#               );
#       学生表结构
#            表名设计
#                create table students(
#                   字段设计
#                   主键    id int auto_increment primary key,
#                   学生姓名 sName varchar(20) not null,
#                   学生性别 sGender bit not null,
#                   学生年龄 sAge int not null,
#                   学生简介 sContent varchar(20) not null,
#                   所属班级 sGrade varchar(20) not null,
#                   是否删除 isDelete bit default 0
#               );
#   配置数据库
#       注意:Django默认使用SQLite数据库
#           在settings.py 搜索 databases 即可查看到默认的数据库是SQLite
#       配置mysql数据库
#           给django项目配置python对数据库的调用包——PyMySQL
#               工程目录下的__init__.py中写入                    bz5
#                   import pymysql
#                   pymysql.install_as_MySQLdb()
#           将settings.py 中的 databases字典修改为：             bz6
#               示例：
#                   DATABASES = {
#                       'default': {
#                           'ENGINE': 'django.db.backends.mysql',
#                           'NAME': 'asj', #'NAME'为要操作的数据库名字（前提是有，在mysql中自己新建的空数据库，没有表）
#                           'USER': 'root', #配置数据库的用户名
#                           'PASSWORD': '135cylpsx4848@', #配置数据库的密码
#                           'HOST': 'localhost', #配置服务器主机ip
#                           'PORT': '3306', #配置mysql的端口，默认3306
#                        }
#                   }
#               格式：
#                   DATABASES = {
#                       'default': {
#                           'ENGINE': 'django.db.backends.数据库（mysql、redis、mongodb、gre）',
#                           'NAME': '空数据库名', #'NAME'为要操作的数据库名字（空数据库，没有表）
#                           'USER': '数据库名', #配置数据库的用户名，mysql是root
#                           'PASSWORD': '服务器密码', #配置数据库的密码
#                           'HOST': '数据库服务器ip', #配置服务器主机
#                           'PORT': '端口', #配置mysql的端口，默认3306
#                        }
#                   }
#   创建应用
#       在一个项目中可以创建多个应用，每个应用进行一种业务处理
#       如何创建应用
#           打开cmd
#               进入创建的目录first_django_project中的django项目目录，即first_django
#                   输入python manage.py startapp myApp1 #用python执行manage.py文件传个参数startapp表示在创建应用，最后设置一个应用名        bz7
#                       if django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3. == '报错':
#                           打开C:\Users\surface\Anaconda3\Lib\site-packages\django\db\backends\mysql\base.py
#                               将以下两行代码注释掉
#                                   if version < (1, 3, 13):
#                                       raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
#                       else:
#                            创建成功
#                            django项目文件夹中，即first_django出现应用文件夹
#                                应用中的文件说明
#                                    migrations文件夹
#                                    __init__.py 包文件声明
#                                    admin.py 配置站点
#                                    apps.py
#                                    models.py 写模型的文件
#                                    tests.py
#                                    views.py 写视图的文件
#   激活应用
#       其本质就是将应用myApp1追加到配置文件中
#       setting.py 搜索 INSTALLED_APPS
#           INSTALLED_APPS = [
#               'django.contrib.admin',
#               'django.contrib.auth',
#               'django.contrib.contenttypes',
#               'django.contrib.sessions',
#               'django.contrib.messages',
#               'django.contrib.staticfiles',
#               'myAdd1',
#               'asj',           bz8
#           ]
#   定义模型
#       概述
#           有一个数据表，就对应一个模型
#           模型本质就是一个类
#           模型类的属性对应表的字段
#       在models.py中定义模型
#           目的
#               与数据库进行交互
#           导入模块
#               from django.db import models       bz9
#                   目的：模型类要继承models.Model类
#               创建一个类，可用于数据的创建以及查询
#               class myManager(models.Manager):    bz10
#                   def createGrade(self, name, girlNum, boyNum, createTime, lastTime, isDelete=False):
#                       gra = self.model()
#                       gra.gName = name
#                       gra.gGirlNum = girlNum
#                       gra.gBoyNum = boyNum
#                       gra.gCreateTime = createTime
#                       gra.gLastTime = lastTime
#                       gra.gIsDelete = isDelete
#                       gra.save()
#                       return gra
#               class Grades(models.Model): #创建对应表名的类
#                   myGraObjects = myManager()
#                   gName = models.CharField(max_length=20, db_column='班级名称') #定义此属性的类型为CharField，即字符串类型，参数为设置其的最大长度20
#                   gDate = models.DateTimeField(db_column='创建时间') #时间类型
#                   lastTime = models.DateTimeField(auto_now=True, db_column='修改时间')
#                   gGirlNum = models.IntegerField(db_column='女生总数') #数字类型
#                   gBoyNum = models.IntegerField(db_column='男生总数') #数字类型
#                   isDelete = models.BooleanField(default=False, db_column='是否删除') #布尔值类型，还有一个NullBooleanField()此函数有三个值：null、true、false
#                   def __str__(self): #重新打印此类的显示格式
#                       return self.gName
#                   class Meta:
#                       db_table = 'grades' #数据库中数据表的名字
#                       ordering = ['id'] #获取数据时的排列方式是以id字段的升序排列
#               class Students(models.Model):      bz11
#                   myStuObjects = myManager()
#                   sName = models.CharField(max_length=20, db_column='姓名')
#                   sGender = models.BooleanField(default=True, db_column='性别') #True男生 False女生
#                   sAge = models.IntegerField(db_column='年龄')
#                   sContent = models.CharField(max_length=20, db_column='简介')
#                   isDelete = models.BooleanField(default=False, db_column='是否删除')
#                   sGrade = models.ForeignKey('Grades', on_delete=models.CASCADE, db_column='班级名称') #表关联-外键('外键所在类对象的名字，即关联表名称'，级联删除) #级联删除的意思是，主表删除后，此字段也将自动删除
#                   lastTime = models.DateTimeField(auto_now=True, db_column='修改时间') #时间类型，自动保存最后一次修改数据的时间，比如修改学生名字，修改的时间会自动保存到lastTime中
#                   createTime = models.DateTimeField(auto_now_add=True, db_column='创建时间') #时间类型，创建学生对象时自动记录当前时间
#                   def __str__(self):
#                       return self.sName
#                   class Meta:
#                       db_table = 'students'
#                       ordering = ['id']
#               说明
#                   这样就创建了一个类，对应数据库中表的类，类属性对应表中的字段
#                   类属性中不规定主键，它会自动生成主键，而且值为自动增加
#   在数据库中生成表
#       方法一：可视化
#       方法二：黑屏终端
#       方法三：manage.py 代码生成
#           创建迁移文件
#               在django项目目录下 输入 python manage.py makemigrations     bz12
#                   if '报错' = "query = query.decode(errors='replace')AttributeError: 'str' object has no attribute 'decode'":
#                       单击 "C:\Users\surface\Anaconda3\lib\site-packages\django\db\backends\mysql\operations.py" 进入文件
#                           将query = query.decode(errors='replace')修改为
#                               query = query.encode(errors='replace')
#                               再输入 python manage.py makemigrations
#                                   print('create model 表名1')
#                                   print('create model 表名2')
#                                   myApp1 -> migrations 生成了迁移文件 0001_initial.py
#                   else:
#                        print('create model 表名1')
#                        print('create model 表名2')
#                        myApp1 -> migrations 生成了迁移文件 0001_initial.py
#               说明
#                   迁移文件会自动生成创建数据表的代码
#                   此时数据库中还没有生成数据表
#           执行迁移
#               python manage.py migrate        bz13
#               说明：相当于执行了sql语句创建表，此时数据库中就会自动创建以上两张表
#               注意：如果操作出错，需要从新执行执行迁移时会报错No migrations to apply
#                   解决办法
#                       删除 $'migrations __initial.py'
#                       进入django项目所在的数据库
#                       删除上一次执行生成的表
#                       删除django_migration表中对应的应用名称的所有记录，即delete from django_migration where app='myApp1';
#   数据操作
#       说明
#           通过执性迁移创建的表名都是带了应用名称的，他们其实是django项目中myApp1应用中modles模块中的类实例化对象，以后我们在程序中进行操作数据，其本质就是操作这些实例化对象的属性或方法，即from myApp1.models import Grades, myApp1_Grades = Grades()
#       方式一：python IDE操作数据
#           进入python shell
#               python manage.py shell
#                   输入 from myApp1.models import Grades,Students #从myApp1包中的models模块中导入Grades，Students类 ，因为需要实例化他们的对象，要操作他们的属性和方法从而达到操作数据的目的
#                   输入 from django.utils import timezone #这是django目录下的工具类 django包.utils模块 导入 timezone类
#                   输入 from datetime import * #*代表全部引入
#           基本操作
#               查询所有数据
#                   格式：类名.objects.all()
#                   说明：这个是Grades类的隐藏属性,它有一个all方法，能查看到Grades表中所有数据，等于select * from Grades;
#                        在python中用此方法获得的数据存在在一个列表中，可对其进行索引切片操作
#                   示例：Grades.objects.all()
#               添加数据
#                   本质：创建一个模型类的对象实例
#                   格式：实例化对象名称 = 类名()，实例化对象.属性 = 值
#                   示例：
#                       grade1 = Grades()
#                       grade1.gName = 'python_01'
#                       grade1.gDate = datetime(year=2019,month=6,day=17)
#                       grade1.gGirlNum = 3
#                       grade1.gBoyNum = 70
#                       grade1.save() #将数据存入数据库
#                   说明：一个实例化对象代表数据库中的一条数据
#                   注意：此时调用Grades.objects.all(),能打印有数据的对象显示，但看不了具体数据
#                            为了能查看具体数据，则需要修改models.py中每个对象的
#                               def __str__(self):
#                                   return '班级名称：{}，建立时间：{}，女生总数：{}，男生总数：{}，是否删除：{}'.format(self.gName, self.gDate, self.gGirlNum, self.gBoyNum, self.isDelete)
#                        每当修改models.py后，需要重启当前shell
#                            exit()
#                            python manage.py shell
#                        重启后需要重新导入包
#                        再调用Grades.objects.all()
#               查看某个对象，即查询对应数据
#                   格式：类名.objects.get(pk=id数)
#                   示例：Grades.objects.get(pk=2) #查询id=2的数据,g = Grades.objects.get(pk=2),以后对此条数据进行增删改查，只需要对其变量名进行调用即可
#               修改数据
#                   格式：模型实例化对象.属性 = 新值
#                        模型实例化对象.save()
#                   示例：grade2.gBoyNum = 60
#                        grade2.save()
#               删除数据(物理删除)
#                   格式：模型示例化对象.delete()
#                   示例：grade2.delete()
#                   说明：逻辑删除就是修改isDelete的值
#               关联数据
#                   准备工作：增加学生表数据
#                       grade1 = Grades.objects.get(pk=1)
#                       stu1 = Students()
#                       stu1.sName = '陈艺龙'
#                       stu1.sGender = True
#                       stu1.sAge = 30
#                       stu1.sContent = '我叫陈艺龙'
#                       stu1.isDelete = False
#                       stu1.sGrade = grade1 #此学生的班级为grade1的id号（外键）
#                       stu1.save()
#                   获得关联对象的集合
#                       格式：数据示例化对象 = 类名1.objects.get(pk=idNum)
#                            数据实例化对象.类名2_set.all() #类名2是类名1的关联表，类名2为小写
#                       需求：获得python04Class班级的所有学生
#                       示例：grade1 = Grades.objects.get(pk=idNum)
#                            grade1.students_set.all()
#                   创建关联表中的数据
#                       格式
#                       需求：创建学生'陈紫妍'，属于'python04Class'
#                       示例：stu2 = grade1.students_set.create(sName=u'陈紫妍', sGender=False, sAge=9, sContent='我叫陈紫妍', isDelete=False)
#                       注意：此方法不需要些外键，外键自动生成
#                            此方法不用seve，将数据直接保存到数据库
#       方式二：代码操作数据
#   启动服务器
    #       格式：python manage.py runserver ip:port      bz14
#       说明：ip可以省略，代表本机ip
#            端口号默认是8000
#       示例：python manage.py runserver #本机测试
#            if '报错' == '目标计算机积极拒绝，无法连接':
#                cmd -> net start mysql80 #启动mysql的服务
#            print('http://本机ip:端口号')
#            在浏览器中输入此http即可访问
#       注意：这是一个纯python写的，轻量级的web服务器，而且仅仅在开发测试中使用
#            今后在浏览器中访问服务器，必须先启动服务器
#   Admin站点管理
#       概述
#           内容发布
#               负责添加、修改、删除内容（内容为数据库中真正的数据）
#               它就是方便我们管理和维护数据库的数据而写的可视化界面
#           公共访问
#       如何内容发布
#           配置admin应用
#               在settings.py文件中的INSTALLED_APPS中添加'django.contrib.admin'（其实会自动配置）
#           创建管理员用户
#               if local中在运行服务:
#                   再点加号增加一个local
#               python manage.py createsuperuser         bz15
#                   输入用户名(默认当前电脑用户名):justin
#                   输入email(随便写一个邮箱)：417217170@qq.com
#                   输入10位以上的密码：135cylpsx4848@
#                   再次输入：135cylpsx4848@
#                   print('Superuser created successfully')
#           进入管理界面
#               http:127.0.0.1:8000/admin
#               输入账号和密码
#           汉化管理界面
#               将settings.py中LANGUAGE_CODE = 'en-us'修改为：
#                   LANGUAGE_CODE = 'zh-Hans'        bz16
#               将settings.py中TIME_ZONE = 'UTC'修改为:
#                   TIME_ZONE = 'Asia/Shanghai'       bz17
#               刷新管理界面即可显示中文
#           管理数据表
#               在admin.py中注册你的模型（注册模型）        bz18
#                   from .models import Grades, Students #导入同级目录下的models中的两个类
#                   admin.site.register(Grades) #注册班级表
#                   admin.site.register(Students) #注册学生表
#                   刷新admin界面，就会出现以上两张表
#           自定义管理页面
#               自定义班级表的显示方式
#                   在admin.py中
#                   class GradesAdmin(admin.ModelAdmin):
#                       #列表页属性
#                       list_display = ['pk', 'gName', 'gDate', 'gGirlNum', 'gBoyNum', 'isDelete'] #显示列表（要显示的字段）
#                       list_filter = ['gName'] #列表过滤器(过滤条件)
#                       search_fields = ['gName'] #查找数据(查找条件)，此时是按照名字搜索
#                       list_per_page = 5 #分页,每5条数据一页
#
#                       #添加、修改页属性(点击增加GRADES进入添加页，点击pk号进入修改页)
#                       fields = ['gGirlNum', 'gBoyNum', 'gName', 'gDate', 'isDelete'] #规定增加页中增加字段的先后顺序,注意不要增加pk，因为pk为自动增加的，所以不能添加到手动增加页
#                       fieldsets = [
#                           ('Number', {'fields': ['gGirlNum', 'gBoyNum']}),
#                           ('base', {'fields': ['gName', 'gDate', 'isDelete']})
#                       ] #给属性分组
#                       注意：fields和fieldsets不能同时使用
#                   admin.site.register(Grades, GradesAdmin)
#                       注意：在自定义增加页面中就能增加数据，保存后直接追加到数据库
#               自定义学生表的显示方式
#                   class StudentAdmin(admin.ModelAdmin):
#                       list_display = ['pk', 'sName', 'sGender', 'sAge', 'sContent', 'isDelete', 'sGrade']
#                       list_filter = ['sName']
#                       search_fields = ['sName']
#                       list_per_page = 5
#                       #fields = ['sGrade', 'sName', 'sGender', 'sAge', 'sContent', 'isDelete']
#                       #fieldsets = [
#                           #('base', {'fields': ['sName', 'sGender', 'sAge']}),
#                           #('Number', {'fields': ['sGrade', 'sContent', 'isDelete']}),
#                           #]
#                   admin.site.register(Students, StudentAdmin)
#               自定义班级表的增加页面中的关联对象
#                   需求：创建一个班级时，可以直接创建几个学生
#                   在admin.py中
#                   class StudentAppend(admin.TabularInline/.StackedInline): #admin.StackedInline 添加信息栏不同的显示方式
#                       model = Students #使用Students这个模型
#                       extra = 2 #每次创建班级时创建2个学生
#                   class GradesAdmin(admin.ModelAdmin):
#                       #在自定义班级表的类中追加一条以下代码
#                       inlines = [StudentAppend] #在班级增加页面中增加两行增加学生信息的可视化界面
#                   说明：在创建班级时就能增加学生信息，并且直接保存到数据库
#               数据字段的显示问题
#                   在admin.py的
#                   class StudentAdmin(admin.ModelAdmin):
#                       #一、布尔值的显示问题
#                       #封装自定义函数
#                       def gender(self):
#                           if self.sGender: #当前对象的sGender字段为True
#                               return '男'
#                           else:
#                               return '女'
#                       gender.short_description = '性别' #设置列表页面的列名称，即修改gender字段的字段名
#                       #在列表显示项目中，将'sGender'替换为自定义函数名
#                       list_display = ['pk', 'sName', gender, 'sAge', 'scontent', 'isDelete', 'sGrade']
#                       #二、修改列名的显示问题
#                       def id(self):
#                           return self.pk #当前对象的pk字段
#                       id.short_description = 'Id'
#                       注意将列表显示中的'pk'替换为自定义函数名
#                       list_display = [id, 'sName', gender, 'sAge', 'scontent', 'isDelete', 'sGrade']
#                       #执行动作栏的显示位置
#                       actions_on_top = False #上端不显示
#                       actions_on_bottom = True #下端显示
#                   admin.site.register(Students, StudentsAdmin) #完成注册
#           使用装饰器完成表注册
#               以后不用写：admin.site.register(Students, StudentsAdmin)
#               改为在
#               @admin.register(Students)#Students是模型
#               class StudentAdmin(admin.ModelAdmin):
#                   ...
#   视图的基本使用
#       概述
#           在django中，视图对web请求进行回应
#           本质就是python中的一个函数，
#       定义视图
#           在myApp1中的views.py文件中定义
#           from django.http import HttpResponse        bz19
#           def index(request): #request为请求体，请求体是客户端给服务端发送的数据
#               return HttpResponse('justin is good man!') #给客户端浏览器返回的数据
#           说明：创建视图后，它的作用是，当你访问http://127.0.0.1:8000就能自动显示返回justin is good man的页面
#       配置url
#           在myApp1目录下的新建urls.py        bz20
#                   app_name= 'asj'
#                   from django.urls import path
#                   from . import views
#                   urlpatterns = [
#                       path('', views.index, name='index')
#                       ]
#
#           在first_django目录下的urls.py        bz21
#                   from django.urls import path, include
#                   from django.contrib import admin
#                   urlpatterns = [
#                       path('admin/', admin.site.urls),
#                       path('', include('myApp.urls', namespace='asj')) #无论url怎么样都能匹配到，即都执行myApp1.urls下的视图
#                   ]
#           匹配和接收客户端传来的url中的值
#               在views.py中再定义一个视图        bz22
#                   def detail(request, num): #此处的num参数为'<int:num>'捕获url中的整数数字
#                       return HttpResponse('detail-{}'.format(num))
#               在myApp1中的urls.py再匹配一个url
#                   from django.urls import path
#                   from . import views
#                   urlpatterns = [
#                       path('', views.index), #匹配空值，显示views.index视图
#                       path('<int:num>/', views.detail), #端口号后匹配一个数字，捕获并赋值给num，num可以传递给视图进行页面显示
#                   ]
#   模板的基本使用
#       概述
#           是html页面，可以根据视图中传递过来的数据进行填充
#       创建模板目录
#           在工程目录下新建文件夹templates，与应用文件夹同级       bz23
#           再在templates中新建文件夹myApp1        bz24
#       配置模板路径
#           修改settings.py中的TEMPLATES变量
#           TEMPLATES = [
#               {
#                   'BACKEND': 'django.template.backends.django.DjangoTemplates',
#                   'DIRS': [os.path.join(BASE_DIR,'templates')],  bz25   #在此处将模板目录添加到列表中，BASE_DIR是django项目目录，即D:\qian_feng_education\first_project\first_django_project\first_django
#                   'APP_DIRS': True,
#                   'OPTIONS': {
#                       'context_processors': [
#                           'django.template.context_processors.debug',
#                           'django.template.context_processors.request',
#                           'django.contrib.auth.context_processors.auth',
#                           'django.contrib.messages.context_processors.messages',
#                       ],
#                   },
#               },
#           ]
#           WSGI_APPLICATION = 'django_project.wsgi.application'
#       定义模板
#           在templates下的myApp1下创建2个html模板文件
#               grades.html
#               students.html
#               在html中书写要显示数据，数据用模板语法显示
#           模板语法
#               {{输出值\可以是变量\可以是一个对象.属性}}
#               {%执行代码段%}
#           示例
#               <body>
#                   <h1>班级信息列表</h1>
#                   <ul>
#                       {%for grade in grades%} #执行一个循环，每循环一次创建一个li>a，grades为python中的列表
#                       <li>
#                           <a href="#">{{grade.gName}}</a> #grade是models.py中的对象,grade.gNames是班级信息
#                       </li>
#                       {%endfor%} #循环结束
#                   </ul>
#               </body>
#           需求：127.0.0.1:8000/grades/,页面显示所有班级数据
#               配置myApp1下的urls分发器
#                   from django.urls import path
#                   from . import views
#                   urlpatterns = [
#                       path('', views.index),
#                       path('<int:num1>/<int:num2>/', views.detail),
#                       path('grades/', views.grades)
#                   ]
#               定义新视图
#                   from .models import Grades
#                   def grades(request):
#                       gradesList = Grades.objects.all() #从模型中取得所有grades的数据对象，存入了gradesList中
#                       return render(request, 'myApp1/grades.html', {'grades':gradesList}) #将reder返回值返回给浏览器，reder的返回值是html，html是'myApp1/grades.html'模板中渲染得到的，其中的{%for grade in grades%}遍历数据是{'grades':gradesList}传递进去的，即在模板中遍历的列表名是字典的键
#           需求：127.0.0.1:8000/students/，页面显示所有的学生数据
#               定义模板
#                   <body>
#                       <h1>学生名字</h1>
#                       <ul>
#                           {%for student in students%}
#                           <li>
#                               {{student.sName}}-{{student.sAge}}-{{student.sGrade}}
#                           </li>
#                           {%endfor%}
#                        </ul>
#                   </body>
#               配置url
#                   from django.urls import path
#                   from . import views
#                   urlpatterns = [
#                       path('', views.index),
#                       path('<int:num1>/<int:num2>/', views.detail),
#                       path('grades/', views.grades),
#                       path('students/', views.students),
#                       ]
#               定义视图
#                   from .models import Students
#                   def students(request):
#                       studentsList = Students.objects.all()
#                       return render(request, 'myApp1/students.html', {'students': studentsList})
#           需求：在127.0.0.1:8000/grades/中，点击班级显示班级对应的学生信息
#               修改grades模板的a标签
#                   <body>
#                       <h1>班级信息列表</h1>
#                       <ul>
#                           {%for grade in grades%}
#                           <li>
#                               <a href="{{grade.id}}/">{{grade.gName}}</a>
#                           </li>
#                           {%endfor%}
#                       </ul>
#                   </body>
#               配置url分配器
#                   from django.urls import path
#                   from . import views
#                   urlpatterns = [
#                       path('', views.index),
#                       path('<int:num1>/<int:num2>/', views.detail),
#                       path('grades/', views.grades),
#                       path('students/', views.students),
#                       path('grades/<int:num3>/', views.gradesStudents), #匹配的是127.0.0.1:8000/grades/数字/
#                   ]
#               定义视图
#                   def gradesStudents(request, num3):
#                       grade = Grades.objects.get(pk=num3) #获得对应班级对象
#                       studentsList = grade.students_set.all() #获得对应班级下的所有学生对象列表
#                       return render(request, 'myApp1/students.html', {'students': studentsList})
#使用拷贝过来的django项目的使用方法
#   在settings.py里修改数据库名和密码
#   在数据库中创建对应空白数据库
#   删除迁移文件
#   创建迁移文件
#   执行迁移
#   启动服务
#   浏览器测试

#【day209】django的模型
#功能
#    Django的模型对各种数据库提供了很好的支持，它为这些数据库提供了统一的调用API，因此我们可以根据不同的需求选择不同的数据库
#配置数据库
#    工程目录下的__init__.py中
#        import pymysql
#        pymysql.install_as_MySQLdb()
#    settings.py的DATABASE中配置数据库
#        DATABASES = {
#            'default': {
#            'ENGINE': 'django.db.backends.mysql',
#            'NAME': 'django_database',
#            'USER': 'root',
#            'PASSWORD': '135cylpsx4848@',
#            'HOST': 'localhost',
#            'PORT': '3306',
#            }
#        }
#模型开发流程
#    配置数据库
#    定义模型类
#        一个模型类都在数据库中对应一张数据表
#    生成迁移文件
#    执行迁移生成数据表
#    使用模型了进行增删改查
#ORM
#    概述：对象-关系-映射
#    任务：根据对象的类型生成表结构
#         将对象、列表的操作转换为sql语句
#         将sql语句查询到的结果转换为对象或列表
#    优点：极大的减轻了开发人员的工作量，而且不需要面对因数据库的变更而修改代码
#定义模型
#    模型、属性、表、字段间的关系
#        一个模型类在数据库中对应一张数据表，在模型类中定义的属性，对应该模型对照表中的一个字段
#    定义属性
#        概述
#            django根据属性的类型确定一下信息
#                当前选择的数据库支持字段的类型
#                渲染管理表单时使用的默认html控件
#                在渲染站点最低限度的验证
#            django会为表增加自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后，则django不会再生成默认的主键列
#            属性名限制
#                遵循标识符规则
#                由于django的查询方式，不允许使用连续的下划线
#        库
#            定义属性时，需要字段类型，字段类型被定义在django.db.models.fields目录下，为了方便使用，被导入到django.db.models中
#            使用方式
#                导入from django.db import models
#                通过models.Field创建字段类型的对象，赋值给属性
#        逻辑删除
#            对于重要数据都做逻辑删除，不做物理删除，实现方式是定义isDelete属性，类型为BooleanField,默认值为False
#        字段类型
#            AutoField
#                一个根据实际id自动增长的integerField，通常不指定如果不指定，一个主键字段将自动添加到模型之中
#            CharField(max_length=字符长度)
#                字符串，默认的表单样式是 TextInput
#            TextField
#                大文本字段，一般超过4000字节使用，默认的表单控件是Textarea
#            IntegerField
#                整数
#            DecimalField(max_digits=None, decimal_places=None)
#                使用python的Decimal实例表示的十进制浮点数
#                参数说明
#                    DecimalField.max_digits
#                        位数总数
#                    DecimalField.decimal_places
#                        小数点后的数字位数
#            FloatField
#                使用python的float实例来表示的浮点数
#            BooleanField
#                True/False 字段，此字段的默认表单控制是ChenckboxInput
#            NullBooleanField
#                支持null、true、false三种值
#            DateField(auto_now=False, auto_now_add=False) #参数可写，可不写
#                使用python的datetime.date实例表示的日期，只有日期
#                参数说明
#                    DateField.auto_now
#                        每次保存对象时，自动设置该字段的当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false
#                    DateField.auto_now_add
#                        当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前时间，默认为false
#                说明
#                    该字段默认对应的表单控件是一个TextInput，在管理员站点添加了一个JavaScript写的日历控件，和一个"Today"的快捷按钮，包含了一个额外的invalid_date错误消息键
#                注意
#                    auto_now_add, auto_now, and default 这些设置是相互排斥的，他们之间的任何组合将会发生错误的结果
#            TimeField
#                使用python的datetime.time实例表示的时间，只有时间，参数同DateField
#            DateTimeField
#                使用python的datetime.datetiem实例表示的日期和时间，日期和时间都有，参数同DateField
#            FileField
#                一个上传文件的字段
#            ImageField
#                继承了FileField的所有属性和方法，但是它对上传的对象进行验证，确保它是个有效的image
#        字段选项
#            概述
#                通过字段选项，可以实现对字段的约束
#                在字段对象时通过关键字参数指定
#                其本质是字段类型函数的参数
#            null
#                如果为True，而且该值未被赋值或没有默认值，则Django将空值以NULL存储到数据库中，默认值是False
#            blank
#                如果为True，则该字段允许为空白，默认为Fasle
#            注意
#                null是数据库范畴的概念，blank是表单验证范畴的概念
#            db_column
#                字段的名称，如果未指定，则使用属性的名称
#            db_index
#                若值为True，则在表中会为此字段创建索引
#            default
#                默认值
#            primary_key
#                若为True，则该字段会成为模型的主键字段
#            unique
#                如果为True，这个字段在表中必须有唯一值，即唯一约束
#        关系
#            分类
#                ForeignKey: 一对多，将外键字段定义在多的端中
#                ManyToManyField: 多对多，将外键字段定义在两端中
#                OneToOneField: 一对一，将字段定义在任意一端中
#            用一访问多
#                格式：对象.模型类小写_set
#                示例：grade.students_set
#            用一访问一
#                格式：对象.模型类小写
#                示例：grade.students
#            访问id
#                格式：对象.属性_id
#                示例：student.sgrade_id
#   创建模型
#   元选项
#        概念：在模型类中定义一个Meta类，用于设置元信息
#        class Students(models.Model):
#            class Meta:
#                db_table = 'students'
#                    定义数据表名，推荐使用小写字母，数据表名默认为应用名小写_类名小写
#                ordering = ['id'] #按id字段的升序获取数据的排序顺序
#                ordering = ['-id'] #按id字段的降序获取数据的排序顺序
#                    对象的默认排序字段，获取对象的列表时使用
#                注意：排序会增加数据库的开销（消耗资源）
#   模型成员
#       类属性
#            隐藏类属性
#                objects
#                    本质是models.Manger()的实例化对象
#                    作用是与数据库进行交互
#                    常用方法
#                        objects.all()
#                        bojects.get(pk=num)
#                    当定义模型时，没有指定管理器，则django为模型创建一个名为objects的管理器
#            自定义管理器
#                class Students(models.Model):
#                    stuObjects = models.Manager()
#                注意：当我们在模型中自定义了管理器后，django就不在为当前类生成objects管理器了
#            自定义管理器Manager()类
#                模型管理器，即Manager类是Django与数据库进行交互的接口，一个模型类可以有多个模型管理器
#                作用
#                    向管理器类中添加额外的方法
#                        创建对象的方法
#                    修改管理器返回的原始查询集
#                        重写get_queryset()方法
#                在模型中
#                    class StudentsManager(models.Manager):
#                        def get_queryset(self):
#                            return super(StudentsManager, self).get_queryset().filter(isDelete=False) #super(StudentsManager, self)是原始的查询集，.filter(isDelete=False)保留isDelete等于False的数据
#                    class Students(models.Model):
#                        stuObjects = StudentsManager() #自定义管理器 = 自定义管理器Manager类
#                说明：此时Students.stuObjects.all()或Students.stuObjects.get(pk=1),只能查询出isDelete是False的数据
#       创建对象
#           目的：向数据库中添加对象
#           说明：当创建对象时，django不会对数据库进行读写操作，当调用save()方法时，才与数据库交互，将对象保存到数据库表中
#           注意：__init__方法已经在父类models.Model中使用了，在自定义的模型中无法使用，因此我们实例化的对象都是空对象，我们还要为其类属性添加值，最后在save()
#           方法
#               在模型类中增加一个类方法
#                   class Students(models.Model)
#                       @classmethod
#                       def createStudent(cls, name, age, gender, content, grade, createTime, lastTime, isDelete=False): #cls为class Students()这个类
#                           stu = cls(sName=name, sAge=age, sGender=gender, sGrade=grade, scontent=content, sCreateTime=createTime, sLastTime=lastTime, sIsDelete=isDelete)
#                           return stu
#                   需求：127.0.0.1:8000/addStudent/1/,增加一个学生信息
#                       配置url
#                           path('addStudent/1/', views.addStudent1)
#                       配置视图
#                           def addStudent1(request):
#                               gra = Grades.GraObjects.get(pk=1)
#                               stu = Students.createStudent('杰西卡1', 2, 0, '我叫杰西卡', gra, '2019-06-18 12:12:12', '2019-06-18 12:12:12')
#                               stu.save()
#                               return HttpResponse('已经添加杰西卡1')
#               在自定义管理器中添加一个方法
#                   class myManager(models.Manager):
#                       def get_queryset(self):
#                           return super(myManager, self).get_queryset().filter(sIsDelete=False)
#                       def createStudent(self, name, age, gender, content, grade, createTime, lastTime, isDelete=False):
#                           stu = self.model()
#                           stu.sName = name
#                           stu.sAge = age
#                           stu.sGender = gender
#                           stu.sConted = content
#                           stu.sGrade = grade
#                           stu.sCreateTime = createTime
#                           stu.sLastTime = lastTime
#                           stu.sIsDelete = isDelete
#                           stu.save()
#                           return stu
#                   需求：127.0.0.1:8000/addStudent/2/,增加一个学生信息
#                       配置url
#                           path('addStudent/2/', views.addStudent2)
#                       配置视图
#                           def addStudent2(request):
#                               gra = Grades.GraObjects.get(pk=1)
#                               stu = Students.myStuObjects.createStudent('杰西卡2', 2, 0, '我叫杰西卡', gra, '2019-06-18 12:12:12', '2019-06-18 12:12:12')
#                               return HttpResponse('已经添加杰西卡2')
#       模型查询
#           查询集
#               概述
#                   表示从数据库中获取的对象集合，即super(myManager, self).get_queryset()
#                   查询集可以有多个过滤器
#                   过滤器就是一个函数，它是基于所给参数限制查询结果
#                   从sql的角度来说，查询集等价于select语句，过滤器则是where条件
#               在管理器上调用过滤器方法，返回查询集
#                   class myManager(models.Manager):
#                       def get_queryset(self):
#                       return super(myManager, self).get_queryset().filter(sIsDelete=False)
#               查询集经过过滤器筛选后返回新的查询集，所以我们可以写成链式调用
#                   super(myManager, self).get_queryset().filter(sIsDelete=False).filter(sGender=False)
#               惰性执行数据访问
#                   创建查询集不会带来任何数据库的访问，直到调用数据时才会访问数据库
#               直接执行数据访问
#                   迭代
#                   序列化
#                   与if合用
#               返回查询集（多条数据）的方法称为过滤器
#                   all()
#                       功能：返回查询集中所有数据
#                       用法：stu = Students.myStuObjects.all()
#                   filter()
#                       功能：返回符合条件的数据
#                       用法：
#                           super(myManager, self).get_queryset().filter(键=值)
#                           super(myManager, self).get_queryset().filter(键=值, 键=值) #两条件为且的关系
#                           super(myManager, self).get_queryset().filter(键=值).filter(键=值) #两条件为且的关系
#                   exclude()
#                       功能：过滤掉符合条件的数据
#                       用法：super(myManager, self).get_queryset().exclude(键=值)
#                   order_by()
#                       功能：排序
#                       用法：
#                           stu = Students.myStuObjects.all().order_by(键)
#                           stu = Students.myStuObjects.all().order_by(-键)
#                   values()
#                       功能：一条数据就是一个对象(字典)，返回一个装满多个对象(字典)的列表，即[{'姓名':'陈艺龙'},{'性别':'男'}]
#                       用法：Student.myStuObjects.values()
#               返回单个数据的方法
#                   get(pk=1)
#                       功能：返回一个满足条件的对象
#                       用法：stu = Students.myStuObjects.get(键=值)
#                       注意：
#                           如果没有找到符合条件的对象，django.core.exceptions.ObjectDoesNotExist异常
#                               捕获异常处理
#                                   from django.core.exceptions import ObjectDoesNotExist
#                                   def studentsGetTry(request):
#                                       try:
#                                           stu = Students.myStuObjects.get(pk=100)
#                                       except ObjectDoesNotExist:
#                                           return HttpResponse('未查询到结果')
#                           如果找到多个符合条件的对象，也会引发django.core.exceptions.MultipleObjectsReturned异常
#                               捕获异常处理
#                                   from django.core.exceptions import MultipleObjectsReturned
#                                   def studentsGetTry(request):
#                                       try:
#                                           stu = Students.myStuObjects.get(sGender=False)
#                                       except MultipleObjectsReturned:
#                                           stu = Students.myStuObjects.filter(sGender=False)
#                                           return HttpResponse('查询到多个结果')
#                   count()
#                       功能：返回当前查询集中的对象个数
#                       用法：Grades.objects.count()
#                       返回值：4
#                   first()
#                       功能：返回查询集中的第一个对象
#                       用法：Grades.objects.first()
#                   last()
#                       功能：返回查询集中的最后一个对象
#                       用法：Grades.objects.last()
#                   exists()
#                       功能：判断查询集中是否有数据
#                       用法：Grades.objects.exists()
#                       返回值：查询集中有数据返回True,反之，则返回False
#               限制查询集
#                   概述：查询集返回的是列表，可以使用下标的方法进行限制,等价于SQL中的limit语句
#                   注意：下标不能是负数
#                   需求：127.0.0.1:8000/studentsPage/index/，只显示前5条数据
#                       配置url
#                           path('studentsPage/index/', views.studentsIndex)
#                       添加视图
#                           def studentsIndex(request):
#                               studentsList = Students.myStuObjects.all()[0:5]
#                               return render(request, 'myApp/students.html', {'students': studentsList})
#                   需求：数据分页显示，127.0.0.1:8000/studentsPage/1/ ,显示1到5条数据
#                        数据分页显示，127.0.0.1:8000/studentsPage/2/ ,显示6到10条数据
#                        ...
#                       配置url
#                           path('studentsPage/<int:page>/', views.studentsPage)
#                       添加视图
#                           0-5 5-10 10-15 15-20 20-25
#                            1   2     3     4     5
#                           5(page-1),5page
#                           def studentsPage(request, page):
#                               studentsList = Students.myStuObjects.all()[5*(page-1) : 5*page]
#                               return render(request, 'myApp/students.html', {'students': studentsList})
#               查询集的缓存
#                   概述
#                       每个查询集都包含一个缓存，来最小化的对数据库访问
#                           在新建的查询集中，缓存首次为空，第一次对查询集求值时，会发生数据缓存，django会将查询出来的数据做一个缓存，并返回查询结果，以后的查询直接使用查询集的缓存
#               字段查询
#                   概念
#                       说明：实现了SQL中的where语句，作为filter()、exclude()、get()的参数
#                       属性查询
#                           语法：模型类中的属性名称__比较运算符 = 值
#                           示例：filter(sAge__gt = 20) #年龄大于20的数据
#                       外键查询：
#                           语法：模型类中的属性名_id = 值
#                           示例：filter(sGrade_id = 1) #班级为1班的数据
#                       转义查询
#                           说明：sql中，where like='陈%'中的%号是占位符，如果需要匹配%则需转义，即\%
#                                django中，.filter(sName__contains = '陈%')中的%就是%不用转义,也就是说此刻匹配的是陈%的数据
#
#                   比较运算符
#                       exact
#                           功能：等于判断，大小写敏感
#                           示例：.filter(sIsDelete=False)
#                       contains
#                           功能：是否包含，大小写敏感
#                           示例：.filter(sName__contains = '陈')
#                       startswith
#                           功能：以value开头的数据
#                           示例：.filter(sName__startswith = '杰')
#                       endswith
#                           功能：以value结尾的数据
#                           示例：.filter(sName__endswith = '雪')
#                       以上四个运算符加上i，则不区分大小写
#                           iexact
#                           icontains
#                           istartswith
#                           iendswith
#                       isnull
#                           功能：空值
#                           示例：.filter(sName__isnull = True)
#                       isnotnull
#                           功能：非空值
#                           示例：.filter(sName__isnotnull = True)
#                       in
#                           功能：是否包含在范围内
#                           示例：.filter(pk__in = [1,2,3,4,5])
#                       gt
#                           功能：大于
#                           示例：.filter(sAge__gt = 10)
#                       gte
#                           功能：大于等于
#                           示例：.filter(sAge__gte = 10)
#                       lt
#                           功能：小于
#                           示例：.filter(sAge__lt = 10)
#                       lte
#                           功能：小于等于
#                           示例：.filter(sAge__lte = 10)
#                       year
#                           功能：年
#                           示例：.filter(sCreateTime__year=2019)
#                       month
#                           功能：月
#                           示例：.filter(sCreateTime__month=6)
#                       day
#                           功能：日
#                           示例：.filter(sCreateTime__day=18)
#                       week_day
#                           功能：周
#                           示例：.filter(sCreateTime__week_day=2)
#                       hour
#                           功能：时
#                           示例：.filter(sCreateTime__hour=22)
#                       minute
#                           功能：分
#                           示例：.filter(sCreateTime__minute=53)
#                       second
#                           功能：秒
#                           示例：.filter(sCreateTime__second=18)
#                       跨关联表查询
#                           处理join查询
#                               语法：模型类名__属性名__比较运算符
#                           需求：127.0.0.1:8000/grades/,页面显示包含姓陈同学信息的班级名称
#                           示例
#                               创建视图
#                                   def grades(request):
#                                       gradesList = Grades.myGraObjects.filter(students__sName__contains='陈')
#                                       return render(request, 'myApp/grades.html', {'grades':gradesList})
#                       查询快捷
#                           pk
#                               代表主键，id是主键代表id，其他字段是主键则代表其他字段
#                   聚合函数
#                       在视图中导入聚合函数
#                           from django.db.models import Max
#                           注意：需要什么聚合函数都在这里引入，from django.db.models import Max, Min...
#                       aggregate()
#                           功能：返回聚合函数的值
#                           返回值：是聚合函数得到的值，不是整条数据
#                       Avg()
#                           功能：求平均值
#                       Count()
#                           功能：求和
#                       Max()
#                           功能：求最大值
#                           示例：studentsList = Students.myStuObjects.aggregate(Max('sAge'))
#                                return HttpResponse(studentsList['sAge__max'])
#                       Min()
#                           功能：求最小值
#                       Sum()
#                           功能：求和
#                       Count()
#                           功能：求和
#                       Count()
#                           功能：求和
#                   F对象
#                       可以使用模型的A属性与B属性进行比较，即一条数据中的两个值比较
#                           需求：127.0.0.1:8000/grades/,页面显示女生比男生多的班级
#                           示例
#                               配饰url
#                                   path('grades/', views.grades),
#                               创建视图
#                                   from .models import Grades
#                                   from django.db.models import F
#                                   def grades(request):
#                                       gradesList = Grades.myGraObjects.filter(gGirlNum__gt = F('gBoyNum'))
#                                       return render(request, 'myApp/grades.html', {'grades':gradesList})
#                       可以支持F对象的算术运算
#                           说明：给F('gBoyNum')+2,相当于给数据字段为gBoyNum的值都加了2，因此之前一班女生20人，男生18人，男生加上2之后，和女生人数一样多，一班数据就不被筛选保留
#                           gradesList = Grades.myGraObjects.filter(gGirlNum__gt = F('gBoyNum')+2)
#                       可以支持时间的加减运算
#                   Q对象
#                       概述
#                           过滤器的方法中的关键字参数，支持且条件，支持或条件, 支持非条件
#
#                       或条件
#                           需求：127.0.0.1:8000/studentsSearch/,页面显示班级为3班或4班的学生
#                           示例
#                               创建视图
#                                   from .models import Students
#                                   from django.db.models import Q
#                                   def studentsSearch(request):
#                                       studentsList = Students.myStuObjects.filter(Q(sGrade=3) | Q(sGrade=3))
#                                       return render(request, 'myApp/students.html', {'students': studentsList})
#                       非关系
#                           需求：127.0.0.1:8000/studentsSearch/,页面显示班级为非3班的学生
#                           示例
#                               创建视图
#                                   from .models import Students
#                                   from django.db.models import Q
#                                   def studentsSearch(request):
#                                       studentsList = Students.myStuObjects.filter(~Q(sGrade=3))
#                                       return render(request, 'myApp/students.html', {'students': studentsList})

#【day210】django的视图
#概述
#    作用：视图接受web请求并响应web请求
#    本质：python中的函数
#    响应
#        网页
#           重定向
#           错误视图
#               404
#                   url未匹配成功
#               500
#                   服务器内部错误
#               400
#
#        JSON数据
#           ajax请求
#        过程
#            用户在浏览器中输入网址
#                www.zgjc.com/justin/index.html
#                将网址传递给django
#            django获取网址信息
#                去掉ip和端口
#                将虚拟路径与文件名，即justin/index.html传递给url管理器
#            url管理器逐个匹配urlconf
#                记录视图函数名
#                将函数名传递给视图管理器
#            视图管理器找到对应的视图去执行
#                返回响应函数给浏览器
#url配置
#    配置流程
#        指定根级url
#            setting.py中 ROOT_URLCONF = 'project.urls'
#            默认实现
#        ulrs.py中的urlpatterns
#            一个url实例的列表
#            存放所有url对象
#                正则表达式
#                    注意事项
#                        如果想要从url中获取一个值需要对表达式加()
#                            re_path(r'grades/(\d+)', view.grades)
#                        在表达式的最后加/
#                            path('students/', view.grades)
#                        正则前需要加r表示不转义
#                            re_path(r'justin/', view.grades)
#                视图名称
#                    include()
#                        功能：匹配的视图在参数指定的文件中去找
#                名称
#        引入其他url配置
#            在应用中创建urls.py文件，在这个文件定义本应用下的url配置
#                from django.urls import path
#                from . import views
#                urlpatterns = [
#                    path('', views.index),
#                    path('<int:num1>/', views.detail),
#                    path('grades/', views.grades),
#                    path('students/', views.students),
#                    path('grades/<int:num2>/', views.gradesStudents),
#                    path('addStudent/1/', views.addStudent1),
#                    path('addStudent/2/', views.addStudent2),
#                    path('studentsGetTry/', views.studentsGetTry),
#                    path('studentsPage/index/', views.studentsIndex),
#                    path('studentsPage/<int:page>/', views.studentsPage),
#                    path('studentsSearch/', views.studentsSearch),
#                ]
#            在工程目录下的urls.py文件中使用include('myApp.urls')方法实现
#                from django.contrib import admin
#                from django.urls import path, include
#                urlpatterns = [
#                    path('admin/', admin.site.urls),
#                    path('', include('myApp.urls', namespace='myApp'))
#                ]
#        匹配过程
#            总urls.py -> urls.py分发器 -> 视图
#    url的反向解析(url的反向代理)
#        概述
#            如果在视图、模板中使用了硬编码链接,即模板中使用a标签进行页面，href='grades/'，当url配置发生改变，则需要将所有a标签的链接手动修改，工作量大
#            反向解析能够在url配置发生改变，则通过url配置的名称，动态生成链接的地址
#                示例
#                    总urls.py
#                        path('justin', include('myApp.urls', namespace='myApp'))
#                    分发器
#                        path('justinPage/', views.index, name='index')
#            使用方式
#                使用url模板时
#视图函数
#    定义视图
#        本质
#            函数
#                参数
#                    request
#                        是一个HttpReques实例
#                        是一个请求对象，是浏览器发送过来的请求体
#                        浏览器发送过来的信息都保存在request实例中
#                        叫什么名都可以
#                    通过正则表达式/<int:num>获取的参数url中的数据参数
#        位置
#            一般在views.py文件下，且django建议全在views.py下定义
#            还能新建views1.py中定义，在url分配器中再导入此视图文件即可，但不建议
#    错误视图
#        404
#            在找不到网页时返回，即url匹配不成功，即未找到合适的视图
#            定义位置
#                templates目录下定义404.html
#                   <!DOCTYPE html>
#                   <html lang="en">
#                   <head>
#                       <meta charset="UTF-8">
#                       <title>404页面</title>
#                   </head>
#                   <body>
#                       <h1>页面丢失</h1>
#                       <h2>{{request_path}}</h2> //request_path为用户访问的url，导致错误的网址
#                   </body>
#                   </html>
#            settings.py中配置404
#                DEBUG = False
#                    如果为True，永远不会调用404界面
#                ALLOWED_HOSTS = ['*']
#                    允许任何人访问 = ['访问所有页面']
#            注意
#                html名字必须叫404
#                不用给此模板配置视图和url，django会自动将404错误匹配到该模板
#        500
#            在视图代码中出现错误(服务器代码)
#        400
#            错误出现在用户的操作
#            爬虫
#            错误cookie
#       403
#           将settings.py中的MIDDLEWARE中的'django.middleware.csrf.CsrfViewMiddleware'注释掉
#           示例
#               MIDDLEWARE = [
#                   'django.middleware.security.SecurityMiddleware',
#                   'django.contrib.sessions.middleware.SessionMiddleware',
#                   'django.middleware.common.CommonMiddleware',
#                   #'django.middleware.csrf.CsrfViewMiddleware',
#                   'django.contrib.auth.middleware.AuthenticationMiddleware',
#                   'django.contrib.messages.middleware.MessageMiddleware',
#                   'django.middleware.clickjacking.XFrameOptionsMiddleware',
#               ]
#HttpRequest对象
#   概述
#       服务器接收http请求(ajax请求)后，django会根据报文(数据流)创建HttpRequest对象
#       django会调用视图函数，并将HttpRequest对象通过形参request传递给视图函数
#       因此，视图函数的第一个参数就是HttpRequest对象
#   对象：
#       HttpRequest对象
#           说明：是浏览器发送给服务器的数据
#           属性
#               path
#                   请求的完整路径(不包括ip和端口)
#               method
#                   请求的方式
#                       get
#                       post
#               encoding
#                   表示浏览器提交的数据的编码方式
#                       utf-8
#               GET
#                   类似字典的对象，包含了get请求的所有参数
#                       即http://127.0.0.1:8000/attribles/?a=1中的a=1
#                         http://127.0.0.1:8000/attribles/?a=1&a=2
#                   本质：QueryDict对象
#                       方法
#                           get()
#                               功能：根据键获取值(如果相同键传两次值，获取最后一次传的值)
#                               说明：只能获取一个值
#                               需求：获取http://127.0.0.1:8000/attribles/?a=1&b=2中，ab的值
#                               示例：a = request.GET.get('a')
#                                    b = requets.GET.get('b')
#                           getlist()
#                               功能：将键的值以列表的形式返回(一键对应两值，传两次相同键不同值的情况)
#                               说明：可以获取多个值
#                               需求：获取http://127.0.0.1:8000/attribles/?a=1&a=2中，a的所有值
#                               示例：aList = requets.GET.getlist('a')
#
#               POST
#                   类似字典的对象，包含了post请求的所有参数
#                   本质：QueryDict对象
#                       方法
#                           get()
#                           getlist()
#                   需求：使用表单提交实现post请求，并获取数据
#                   示例
#                        配置url.py
#                            path('register/', views.register),
#                            path('register/post/', views.registerPost)
#                        创建视图
#                            def register(request):
#                                return render(request, 'myApp/register.html')
#                            from .models import Students
#                            def registerPost(request):
#                                sName = request.POST.get('sName')
#                                sAge = int(request.POST.get('sAge'))
#                                sGender = int(request.POST.get('sGender'))
#                                scontent = request.POST.get('scontent')
#                                sGrade = int(request.POST.get('sGrade'))
#                                gra = Grades.myGraObjects.filter(gIsDelete=False).get(pk=sGrade)
#                                Students.myStuObjects.createStudent(sName, sAge, sGender, scontent, gra)
#                                return HttpResponse('提交成功')
#                        创建模板
#                            <body>
#                                <h1>学生信息注册</h1>
#                                <form action="post/" method="post">
#                                    <lable for="1">学生姓名：</lable>
#                                    <input id="1" type="text" name="sName">
#                                    <br>
#                                    <lable for="2">学生年龄：</lable>
#                                    <input id="2" type="text" name="sAge">
#                                    <br>
#                                    <span>学生性别：</span><br>
#                                    <lable for="3">男</lable>
#                                    <input id="3" type="radio" name="sGender" value="1">
#                                    <lable for="4">女</lable>
#                                    <input id="4" type="radio" name="sGender" value="0">
#                                    <br>
#                                    <lable for="5">学生简介：</lable>
#                                    <textarea id="5" name="scontent" cols="23" rows="5"></textarea>
#                                    <br>
#                                    <lable for="6">学生班级：</lable>
#                                    <input id="6" type="text" name="sGrade">
#                                    <br>
#                                    <input type="submit" value="提交">
#                               </form>
#                             </body>
#               FILES
#                   类似字典的对象，包含了所有上传的文件
#               COOKIES
#                   字典，包含所有的cookie
#                       cookie就是字典数据,字典中的一对键值对就是一个cookie
#                       每次http请求都会默认携带所有cookie，发送给服务器
#                   cookie取值
#                        request.COOKIES['sessionid']
#                        说明：session的key被存储在request.COOKIES['sessionid']中
#               session
#                   类似字典的对象，表示当前会话
#                   key和value被存储在mysql -> django -> django_session中
#                   设置值
#                       request.session['userName'] = '陈艺龙'
#                   取值
#                       request.session.get('userName','游客')
#
#           方法
#               is_ajax()
#                   功能：如果是通过XMLHttpRequest发起的，返回True
#                   作用：如果是True,我们一般返回json数据
#
#HttpResponse对象
#    概述
#        作用
#            给浏览器返回数据
#        说明
#            HttpRequest由django创建，HttpResponse由程序员创建
#    返回用法
#        不调用模板
#            from django.http import HttpResponse
#            def index(request):
#                return HttpResponse('直接返回字符串')
#        调用模板
#            使用render()方法
#                原型
#                    render(request, templateName[, context])
#                作用
#                    结合数据和模板返回一个html页面
#                参数
#                    request
#                        请求体对象
#                    templateName
#                        模板路径
#                    context
#                        传递给需要渲染在模板上的数据
#                示例
#                    from django.shortcuts import render
#                    def studentsIndex(request):
#                        studentsList = Students.myStuObjects.all()[0: 5]
#                        return render(request, 'myApp/students.html', {'students': studentsList})
#    属性
#        content
#            表示返回内容
#        charset
#            表示返回内容的编码格式
#                utf-8
#        status_code
#            表示响应的状态码
#                https://www.cnblogs.com/xflonga/p/9368993.html
#                200
#                301 请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL访问此资源，
#                    处理方式：永久重定向
#                302 请求到的资源艾一个不同的URL处临时保存
#                    处理方式：临时重定向
#                304 请求到的资源未更新
#                    处理方式：丢弃，使用本地缓存
#                403 禁止访问
#                    处理方式：丢弃
#                404 没有找到
#                    处理方式：丢弃
#                500 服务器内部错误
#        content-type
#            表示指定输出的MIME类型
#                指定html，浏览器就渲染页面
#                指定JSON，

#        response属性的使用
#            示例
#                配置url
#                    path('response/', views.response)
#                创建视图
#                    from django.http import HttpResponse
#                    def response(request):
#                        res = HttpResponse()
#                        res.content = b'good'
#                        print(res.content)
#                        print(res.charset)
#                        print(res.status_code)
#                      # print(res.content-type)
#                        return res
#    方法
#        init()
#            使用页面内容实例化HttpResponse对象
#        write(content)
#            以文件的形式写入数据
#        flush()
#            以文件的形式输出缓冲区
#        set_cookie(key, value='token', max_age=None, exprise=None)
#            增加cookie
#            示例
#                配置url
#                    path('addCookie', views.myCookie)
#                创建视图
#                    def addCookie(request):
#                        res = HttpResponse()
#                        res.set_cookie('justin', 'good')
#                        res.write('设置成功')
#                        return res
#            打印cookie
#            示例
#                配置url
#                    path('printCookie', views.printCookie)
#                创建视图
#                    def printCookie(request):
#                        cookie = request.COOKIES
#                        res = HttpResponse()
#                        try:
#                            res.write('<h1>'+cookie['justin']+'</h1>')
#                        except KeyError as e:
#                            res.write('<h1>csrftoken:'+cookie['csrftoken']+'</h1><h1>sessionid:'+cookie['sessionid']+'</h1>')
#                        return res
#        delete_cookie(key)
#            删除cookie
#            示例
#                配置url
#                    path('deleteCookie/', views.deleteCookie)
#                创建视图
#                    def deleteCookie(request):
#                        res = HttpResponse()
#                        res.delete_cookie('justin')
#                        res.write('删除成功')
#                        return res
#            注意：删除一个不存在的key，就当什么也没发生
#    HttpResponse子类HttpResponseRedirect
#      功能：重定向——服务器端的跳转
#      需求：127.0.0.1:8000/redirect1/,显示redirect1/redirect2/的视图
#      示例
#          配置url
#              path('redirect1/', views.redirect1),
#              path('redirect1/redirect2/', views.redirect2),
#          创建视图
#                from django.http import HttpResponseRedirect
#                def redirect1(request):
#                    res = HttpResponseRedirect('redirect2/')
#                    return res
#                def redirect2(request):
#                    res = HttpResponse()
#                    res.write('我是重定向后的页面')
#                    return res
#      简写：redirect(to)
#      需求：127.0.0.1:8000/redirect1/,显示redirect1/redirect2/的视图
#      示例
#          配置url
#              path('redirect1/', views.redirect1),
#              path('redirect2/', views.redirect2),
#          创建视图
#              from django.shortcuts import redirect
#              def redirect1(request):
#                  res = HttpResponse()
#                  res.write('我是主页')
#                  return res
#              def redirect2(request):
#                  return redirect(to='/redirect1/')
#    HttpResponse子类JsonResponse
#        功能：返回json数据，一般用于异步请求(ajax请求)
#        方法
#            __init__(self,data)
#            参数
#                data
#                    字典对象
#        注意
#            Content-type类型为application/json
#        示例
#            from django.http import JsonResponse
#            def jsonResponse(request):
#                if request.is_ajax():
#                    jsonData = JsonResponse({'a':{'b':'1','c':'1'}})
#                return jsonData
#状态保持
#    概念
#        http协议是无状态的，每次请求都是一次新的请求，它不记得以前的请求
#        客户端与服务端的一次通信就是一次会话
#        实现状态保持，在客户端或者服务端存储有关会话的数据
#        存储的方式
#            cookie
#                概念
#                    每次客户端发起的http请求携带的字典数据
#                存储位置
#                    所有的数据存储在客户端，不要存储敏感的数据
#            session
#                概念
#                    字典对象
#                    它的key存储在cokie中键为sessionid的值
#                    cookie = {'sessionid':'i040kr12tci92ov3t9gnuxy98oo292mb'}
#                    默认保存时长：半月
#                存储位置
#                    所有的数据存储在服务端的数据库中
#    目的：在一段时间内，跟踪请求者的状态，可以实现跨页面访问当前的请求者数据
#    注意：不同的请求者不会共享这个数据，与请求者一一对应的
#    启用session
#        settings.py
#            INSTALLED_APPS = ['django.contrib.sessions']
#                默认启用
#            MIDDLEWARE = ['django.contrib.sessions.middleware.SessionMiddleware']
#                默认启用
#    使用session
#        启用session后，每个HttpRequest对象都有session属性，它的值是一个字典的对象
#            字典对象方法
#                request.session['userName'] = '陈艺龙'
#                    功能：session存储数据，即增加字典的key和value
#                    key的保存位置：
#                        mysql -> database: django -> table: django_session -> 字段: session_key
#                        cookie['sessionId']
#                    存储方式：base64编码，可以用base64解码看其内容
#                get(key, default=None)
#                    功能：根据键获取，session值
#                    参数
#                        default=None
#                           默认返回，即get的key在session字典中不存在，不报错，默认返回None
#                    示例：userName = request.session.get('userName', '游客')
#                    说明：如果session中key'userName'不存在,则变量userName的值为'游客'
#                clear()
#                    功能：清空所有会话，即清空session的所有值
#                flush()
#                    功能：删除当前的会话并删除会话的cookie
#                logout()
#                    功能：删除当前会话的session
#                    示例
#                        配置url
#                            path('main/exit/', views.exit)
#                        创建视图
#                        from django.contrib.auth import logout
#                        def exit(request):
#                            logout(request)
#                            return redirect(to='/main/')
#    需求：http://127.0.0.1:8000/main/进入首页，欢迎游客，点击登录，跳转到http://127.0.0.1:8000/main/signIn/，在登录界面中输入名字和密码，点登录后，再回到http://127.0.0.1:8000/main/，欢迎登录的用户名，点退出，则欢迎游客
#        配置url
#            path('main/', views.main),
#            path('main/signIn/', views.signIn),
#            path('main/signIn/showMain/', views.showMain),
#            path('main/exit/', views.exit)
#        创建视图
#            from django.shortcuts import render, redirect
#            from django.contrib.auth import logout
#            def main(request):
#                userName = request.session.get('userName','游客')
#                return render(request, 'myApp/main.html', {'userName':userName})
#            def signIn(request):
#                return render(request, 'myApp/signIn.html')
#            def showMain(request):
#                userName = request.POST.get('userName')
#                password = request.POST.get('password')
#                request.session['userName'] = userName
#                return redirect(to='/main/')
#            def exit(request):
#                logout(request)
#                return redirect(to='/main/')
#        创建模板
#            main.html
#                <body>
#                    <h1>欢迎：{{userName}}</h1>
#                    <a href="signIn/">登录</a>
#                    <a href="exit/">退出</a>
#                </body>
#            signIn.html
#                <body>
#                    <form action="showMain/" method="post">
#                        <input type="text" name="userName" placeholder="用户名">
#                        <input type="password" name="password">
#                        <input type="submit" value="登录" >
#                    </form>
#                </body>
#    修改保持状态时长
#        即修改session过期时间
#            set_expiry(value)
#                如果不设置两星期后过期
#                value
#                   整数
#                      value=10，则10s过期
#                       示例
#                           request.session.set_expiry(10)
#                   时间对象
#                      value='2020-6-29'，则到2020-6-29过期
#                       示例
#                           request.session.set_expiry(value)
#                   0
#                      value=0，则关闭浏览器时失效
#                       示例
#                           request.session.set_expiry(0)
#                   None
#                      value=None，则永不过期
#                       示例
#                           request.session.set_expiry(None)
#    使用redis缓存session
#        cmd安装库
#            pip install django-redis-sessions == 0.6
#            pip install django-redis-sessions == 0.5.6
#        setting.py的最后插入
#            0.6版本 seting设置如下
#                SESSION_ENGINE = 'redis_sessions.session'
#                SESSION_REDIS = {
#                    'host': 'localhost',
#                    'port': 6379,
#                    'db': 0,
#                    'password': '135cylpsx4848@',
#                    'prefix': 'session',
#                    'socket_timeout': 1
#                }
#            0.5.6版本 seting设置如下        bz26
#                SESSION_ENGINE = 'redis_sessions.session'
#                SESSION_REDIS_HOST = 'localhost'
#                SESSION_REDIS_PORT = 6379
#                SESSION_REDIS_DB = 0
#                SESSION_REDIS_PASSWORD = '135cylpsx4848@'
#                SESSION_REDIS_PREFIX = 'session'

#【day211】django的模板
#概述
#定义模板
#    变量
#       本质：视图传递给模板的数据
#       名字：遵循标识符规则
#       语法：{{var}}
#       说明：html会去计算var的值，然后将值替换掉{{var}},渲染到模板中
#       注意：var 没有值时，{{var}}为空字符串，在页面中不显示
#       .语法
#           格式：{{字典.键}} or {{对象.属性}} or {{列表.下标}}
#           说明
#               html首先会将stu看成字典，sName是key，执行的是stu[sName]
#               如果不符合字典规则，则把stu看成对象，sName是属性或方法，执行的是stu.sName
#                   stu是实例化对象，则可调用其方法，{{stu.getName}}
#                       注意：这里调用的方法是不能有参数的方法
#               如果不符合对象规则，则把stu看成数组（列表），sName是下标数字，执行的是stu[sName]
#           示例
#               配置url
#                   path('Template/', views.Template)
#               创建model
#                   class Students(models.Model):
#                       ...
#                       def getName(self):
#                       return self.sName
#               创建views
#                   from .models import Students
#                       def Template(request):
#                       student = Students.myStuObjects.get(pk=1)
#                       return render(request, 'myApp/Template.html', {'stu':student})
#               创建template
#                   <body>
#                       <h1>{{stu.sName}}</h1>
#                   </body>
#     标签
#         语法：{% tag %}
#         作用
#             在输出中创建一些文本
#             逻辑控制和循环控制
#         标签
#             if
#                 格式
#                    {%if 表达式%}
#                    语句
#                    {%endif%}
#             else
#                 格式
#                    {%if 表达式%}
#                    语句1
#                    {%else%}
#                    语句2
#                    {%endif%}
#             elif
#                 格式
#                    {%if 表达式1%}
#                    语句1
#                    {%elif 表达式2%}
#                    语句2
#                    ...
#                    {%elif 表达式n%}
#                    语句n
#                    {%else%}
#                    语句n+1
#                    {%endif%}
#                 示例
#                     <body>
#                         <h1>{{num}}</h1>
#                         <h1>
#                             {%if num%}
#                             我是一号
#                             {%endif%}
#                         </h1>
#                         <h1>第一次获取：{{stu.sName}}</h1>
#                         <h1>第二次获取：{{stu.getName}}</h1>
#                     </body>
#             for
#                 格式1
#                     {%for 变量 in 列表%}
#                         语句
#                     {%endfor%}
#                 格式2
#                     {%for 变量 in 列表%}
#                         语句1
#                     {%empty%}
#                         语句2
#                     {%endfor%}
#                     说明：当列表为空或不存在时时执行语句2
#                 用法
#                     {{forloop.counter}}
#                     说明：循环次数变量值，用在{%for i in list%}和{%endfor%}的中间，等价于n，
#                         n = 0
#                         for i in range(5):
#                             n+=1
#                             print(n)
#                 示例
#                     <body>
#                         <h1>学生名字</h1>
#                         <ul>
#                             {%for student in students%}
#                             <li>
#                                 {{forloop.counter}}--{{student.sName}}-{{student.sAge}}-{{student.sGrade}}
#                             </li>
#                             {%empty%}
#                             <li>目前没有学生</li>
#                             {%endfor%}
#                          </ul>
#                     </body>
#             comment
#                 作用：书写注释内容
#                 示例
#                     {%comment%}
#                         <h1>不会显示</h1>
#                         {{stu.sName}}
#                     {%endcomment%}
#             ifequal
#                 作用：判断是否相等
#                 格式
#                     {%ifequal 值1 值2%}
#                         语句
#                     {%endifequal%}
#             ifnotequal
#                 作用：判断是否不等
#                 格式
#                     {%ifnotequal 值1 值2%}
#                         语句
#                     {%endifnontequal%}
#             include
#                 作用：加载模板并以标签内的参数渲染
#                 格式：{%include "模板路径" 参数1 ... 参数n%}
#             url
#                 作用：反向解析
#                 格式：{%url 'namespace:name' 参数%}
#             csrf_token
#                 作用：用于跨站请求伪造保护
#                 格式：{%csrf_token%}
#             block 、extends
#                  作用：用于模板的继承
#             autoescape
#                  作用：用于html转义
#     过滤器
#         语法：{{var|过滤器}}
#         作用：在变量被显示前修改它
#         本质：过滤器是函数，可以传参，参数用引号阔起来
#         lower
#             功能：小写
#         upper
#             功能：大写
#             示例
#                 <h1>未过滤：{{str}}</h1>
#                 <h1>过滤：{{str|upper}} 在显示前就被修改为大写</h1>
#         join
#             功能：链接列表元素，形成新字符串
#             格式：{{列表|join:"-"}}
#             等价：['a','b','c'].join('-') return 'a-b-c'
#             示例
#                 视图：render(request, 'myApp/Template.html', {'list':['a','b','c']})
#                 模板：<h1>{{list|join:'-'}}</h1> return <h1>a-b-c</h1>
#         default
#             功能：当变量不存在或为false或为空时，可以设置显示默认值
#             格式：{{var|default:'默认值'}}
#             示例：<h1>{{justin|default:"默认值"}}</h1>
#         date
#             功能：设定时间格式
#             格式：{{dateVal|date:'y-m-d'}}
#         escape
#             功能：HTML转义
#         add
#             功能：加减运算
#             示例
#                 <h1>{{num|add:'10'}}</h1>
#                 <h1>{{num|add:'-10'}}</h1>
#         widthratio
#             功能：乘除运算
#             示例
#                 <h1>{%widthratio 5 1 3%}</h1> //(5/1)*3 = 5*3 = 15
#                 <h1>{%widthratio 15 3 1%}</h1> //(15/3)*1 = 15/3 = 5
#         divisibleby
#             功能：取模运算，能整除返回True，否则返回False
#             示例1
#                <h1>{4|divisbleby:2}</h1> 返回True
#                <h1>{5|divisbleby:2}</h1> 返回False
#             示例2
#                <body>
#                    <h1>学生名字</h1>
#                    <ul>
#                        {%for student in students%}
#                            {%if forloop.counter|divisibleby:2%}
#                                <li style="color: red">{{forloop.counter}}--{{student.sName}}-{{student.sAge}}-{{student.sGrade}}</li>
#                            {%else%}
#                                <li style="color: blue">{{forloop.counter}}--{{student.sName}}-{{student.sAge}}-{{student.sGrade}}</li>
#                            {%endif%}
#                        {%empty%}
#                            <li>目前没有学生</li>
#                        {%endfor%}
#                     </ul>
#                </body>
#     注释
#        单行注释 {#注释内容#}
#        多行注释
#           {%comment%}
#               <h1>不会显示</h1>
#               {{stu.sName}}
#           {%endcomment%}
#反向解析
#    概述
#        项目层级
#            总urls.py对应很多应用urls，每个应用urls又对应很多视图或模板，模板中又有非常多的a标签
#        硬编码
#            当我们采用硬编码，能够实现页面间的调转，但是我们有可能会修改总urlsde名和应用urls名，即修改匹配的url路径
#            一旦遇到修改名字的情况，就需要去每个a中修改对应的url名，工作量非常大
#        解决方法
#            每个a都采用动态生成url，即{%url 'namespace:name' parameter%}
#                参数
#                    namespace
#                        概述：命名空间，是总url的唯一标识，可以把它看成一个id变量名,在总urls.py中定义
#                    name
#                        概述：命名空间，是分url的唯一标识，可以把它看成一个id变量名,在分urls.py中定义
#                        注意：如果定义了namespace,就必须在分urls.py中，设置app_name = 'namespace的值'
#                    parameter
#                        概述：是数字，是用来传递给name的，如果设置了parameter，则需要再配置name时用<int:num>接收
#    定义
#        配置总ulrs.py
#            path('abc1/', include('myApp.urls', namespace='myApp'))
#        配置分ulrs.py
#            from . import views
#            app_name = 'myApp' 建议跟应用名字一致
#            path('', views.index),
#            path('abc2<int:numPage>/', views.myAppPage, name='myAppPage'),
#        配置views
#            from django.shortcuts import render
#            def myAppPage(request, number):
#                return render(request, 'myApp/page.html', {'num':number})
#        template中
#            index.html
#                <a href="{%url 'myApp:myAppPage' 1%}">跳转</a>
#            page.html
#                <h1>调转至此</h2>
#    页面流程
#        用户输入127.0.0.1:8000/abc1/，进入主页
#        点击a标签，跳转到127.0.0.1:8000/abc1/abc21/,即page.html
#    url匹配流程
#        127.0.0.1:8000/abc1/在总urls.py中匹配,进入分myApp下的urls.py,又被分urls.py匹配显示index.html
#        点击a标签，a标签动态生成href="/abc1/abc21/",即跳转127.0.0.1:8000/abc1/abc21/，被分urls.py匹配进入page.html
#    动态生成规则说明
#        href="{%url 'myApp:myAppPage' 1%}"
#            myApp的取值为总urls.py中设定了namespace='myApp'的path的第一个参数字符串
#            myAppPage的取值为总urls.py中设定了name='myAppPage'的path的第一个参数字符串，其中<int:numPage>代表一个数字，这个数字的值等于{%url '...' 1%}中的参数,即1
#    总结
#        不管怎么修改path中的url匹配名称，都不用手动去修改a标签的href，因为href是动态生成的
#模板继承
#    作用：减少页面内容的重复定义，实现页面的重用
#    标签
#        block
#            功能：在父模板中预留区域，子模板去填充
#            语法
#                {% block 标签名%}
#                {% endblock 标签名%}
#        extends
#            功能：继承模板，需要写在模板文件的第一行
#            语法
#                {% extends '父模板路径' %}
#        示例
#            父模板 base.html
#                <body>
#                    <div id="box">
#                        <div id="header"></div>
#                        <div id="main">
#                            {%block main1%}
#                            {%endblock main1%}
#                            <hr>
#                            {%block main2%}
#                            {%endblock main2%}
#                        </div>
#                        <div id="footer"></div>
#                    </div>
#                </body>
#            子模板 subTemplate1.html
#                {% extends 'myApp/
#                base.html'%}
#                {%block main1%}
#                    <h1>我是{{num}}号坑</h1>
#                    <h1>真1.1</h1>
#                {%endblock main1%}

#                {%block main2%}
#                    <h1>我是{{num}}号坑</h1>
#                    <h1>真1.2</h1>
#                {%endblock main2%}
#            配置url
#                path('subTemplate<int:pageNum>/', views.subTemplate, name='subTemplate')
#            创建视图
#                def subTemplate(request, pageNum):
#                    if pageNum == 1:
#                        html = render(request, 'myApp/subTemplate1.html', {'num': pageNum})
#                    elif pageNum == 2:
#                        html = render(request, 'myApp/subTemplate2.html', {'num': pageNum})
#                    return html
#html转义
#    render(request, 'myApp/Template', {'code':'<h1>justin is good man!</h1>'}
#    {{code}} 普通字符串
#    {{code|escape}} 会自动执行转义普通字符串
#    将code转义为html代码
#        1、{{code|safe}}
#        2、
#           {%autoescape off%} 设置将自动转义关闭的标签
#               {{code}}
#           {%endautoescape%}
#CSRF
#    跨站请求伪造
#        某些恶意网站包含链接、表单、按钮、js利用登录的用户在浏览器中认证，从而攻击服务
#            示例
#                保存表单页面的源代码本地运行，将表单提交的本地服务器地址根换为原网络服务器地址
#                循环验证登录用户名和密码，从而破解用户名密码
#                这样的过程就叫恶意攻击
#    防止恶意攻击的方法
#        在settings.py的MIDDLEWARE中增加
#            'django.middleware.csrf.CsrfViewMiddleware', 默认已添加
#            但是会出现本网站的表单也被csrf阻止了，无法提交
#                解决办法,在自己的表单中增加标签{% csrf_token %}
#                    <form>{% csrf_token %}</form>
#                        但是没有绝对的安全，只要赋值源代码时将以下代码一起复制，同样可以用上面赋值源代码的形式恶意攻击其他人网站
#                           <input type="hidden" name="csrfmiddlewaretoken" value="YoMMWfAlIhrffVztpFa4nyUkwnjmsGqU06nyux9yKWeFnAjL6VoqSkb2OiD5FgYj">
#验证码
#    作用：在用户注册、登录页面的时候使用，为了防止暴力请求，减轻服务器的压力，也是防止csrf的一种方式
#    需求：127.0.0.1:8000/mainApp/verifyForm/,进入验证码输入页面，即myApp/verifyForm页面，该页面中能自动生成验证码图片，验证码输入正确，跳转登录成功页面，验证码输入错误，重定向到输入验证码页面，并显示验证码验证失败
#        配置url
#            path('verifyImage/', views.verifyImage, name='verifyImage'),
#            path('verifyForm/', views.verifyForm, name='verifyForm'),
#            path('checkForm/', views.checkForm, name='checkForm')，
#        创建views
#            def verifyImage(request):
#                #引入绘图模块
#                from PIL import Image, ImageDraw, ImageFont
#                #引入随机函数模块
#                import random
#                #定义变量，用于画面的背景色、宽、高
#                bgcolor = (random.randrange(20,100), random.randrange(20,100), random.randrange(20,100))
#                width = 100
#                height = 50
#                #创建画面对象
#                im = Image.new('RGB', (width, height), bgcolor)
#                #创建画笔对象
#                draw = ImageDraw.Draw(im)
#                #调用画笔的point()函数绘制噪点
#                for i in range(0, 100):
#                    xy = (random.randrange(0, width), random.randrange(0, height))
#                    fill = (random.randrange(0,255), 255, random.randrange(0,255))
#                    draw.point(xy, fill=fill)
#                #定义验证码储备值
#                myStr = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
#                #随机抽取四个值作为验证码
#                rand_str = ''
#                for i in range(0,4):
#                    rand_str += myStr[random.randrange(0, len(myStr))]
#                #构造字体对象
#                font = ImageFont.truetype(r'C:\Windows\Fonts\Arial\arial.ttf', 40) #在本机字体库中选中任意一种字体，字体大小为40
#                #构造字体颜色
#                fontcolor1 = (255, random.randrange(0,255), random.randrange(0,255))
#                fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
#                fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
#                fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
#                #绘制4个字
#                draw.text((5,2), rand_str[0], font=font, fill=fontcolor1)
#                draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
#                draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
#                draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
#                #释放画笔
#                del draw
#                #存入session, 用于做进一步验证
#                request.session['verifyCode'] = rand_str
#                #内存文件操作
#                import io
#                buf = io.BytesIO()
#                #将图片保存在内存中，文件类型为png
#                im.save(buf, 'png')
#                #将内存中的图片数据返回给客户端，MIME类型为图片png
#                return HttpResponse(buf.getvalue(), 'image/png')
#
#            def verifyForm(request):
#                flag = request.session.get('flag')
#                if flag==False:
#                    flag = '验证失败,请重新输入'
#                    request.session.clear()
#                else:
#                    flag = ''
#                return render(request, 'myApp/verifyForm.html', {'flag': flag})
#
#            def checkForm(request):
#                code1 = request.POST.get('verifyCode')
#                code2 = request.session.get('verifyCode')
#                if code1.lower() == code2.lower():
#                    return HttpResponse('验证成功')
#                else:
#                    request.session['flag'] = False
#                    return redirect(to='/mainApp/verifyForm/')
#        创建template
#            <body>
#                <form action="{%url 'myApp:checkForm' %}" method="post">
#                    {%csrf_token%}
#                    <input type="text" name="verifyCode">
#                    <img src="{%url 'mainApp:verifyImage' %}" alt="验证码">
#                    <input type="submit" value="登录">
#                    <span>{{flag}}</span>
#                </form>
#            </body>

#【day212】django模板的高级扩展
#静态文件
#    css,js,image,json,font等文件
#    存放位置django工程文件夹下新建文件夹static，再在static下创建对应模板的目录（注意，如果有base.html，应答为它创建一个目录来存放它的css、js等，目录名叫main），再在此目录下，复制携带了bootstrap、swiper、jquery、reset文件以及自定义当前模板.css和自定义当前模板.js的css，js，img，json，fonts等文件件      bz27
#    配置settings.py，最后插入 STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]      bz28
#    在html中导入css文件
#        <!DOCTYPE html>
#        {%load staticfiles%}  加载静态文件夹        bz29
#        <html lang="en">
#        <head>          bz30
#            <meta charset="UTF-8">
#            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
#            <title>Title</title>
#            <link href="{%static 'myApp/css/reset.css'%}" rel="stylesheet">
#            <link href="{%static 'myApp/css/swiper.min.css'%}" rel="stylesheet" >
#            <link href="{%static 'myApp/css/bootstrap.min.css'%}" rel="stylesheet">
#            <script src="{%static 'myApp/js/jQuery.js'%}"></script>
#            <script src="{%static 'myApp/js/bootstrap.min.js'%}"></script>
#            <script src="{%static 'myApp/js/swiper.min.js'%}"></script>
#        </head>
#        <body>
#            <img id="logoImg" src="{%static 'myApp/img/logo.png'%}" width="30" height="30" alt="logo">
#        </body>
#中间件
#    概述
#        一个轻量级、底层的插件，可以介入django的请求和响应
#    请求响应流程
#        a发出请求（发出url）- b匹配url - c执行视图 - d匹配模板 - e返回模板
#    本质
#        一个python类
#            方法
#                __init__
#                    不需要传参数，服务器响应第一个请求的时候自动调用，用于确定是否启用该中间件
#                process_request(self, request)
#                    调用位置
#                        在每发出一次请求到匹配url之前每个中间件的process_request方法都会被调用，即每个a-b阶段每个中间件的process_request方法都会被调用
#                    返回结果
#                        None或HttpResponse对象
#                process_view(self, request, view_function, view_args, view_kwargs)
#                    调用位置
#                        在每匹配一个url到执行视图之前每个中间件的process_view方法都会被调用，即每个b-c阶段每个中间件的process_view方法都会被调用
#                    返回结果
#                        None或HttpResponse对象
#                process_template_response(self, request, response)
#                    调用位置
#                        在每次执行视图刚完到匹配模板之前每个中间件的process_template_response方法都会被调用，即每个c-d阶段每个中间件的process_template_response方法都会被调用
#                    返回结果
#                        None或HttpResponse对象
#                process_response(self, request, response)
#                    调用位置
#                        在每次匹配模板到返回模板之前每个中间件的process_response方法都会被调用，即每个d-e阶段每个中间件的process__response方法都会被调用
#                    返回结果
#                        HttpResponse对象
#                process_exception(self, request, exception)
#                    调用位置
#                        在视图抛出异常时调用
#                    返回结果
#                        HttpResponse对象
#    中间件各方法执行位置
#        a发出url - process_request() - b匹配url - process_view() - c执行视图 - process_template_response() - d匹配模板 - process_response() - e返回模板
#自定义中间件
#    django工程目录下，新建middleware，再在middleware下，新建对应应用名目录，即myApp，再在此目录下，新建文件myMiddle.py      bz31
#    myMiddle.py中      bz32
#        from django.utils.deprecation import MiddlewareMixin
#        class MyMiddle(MiddlewareMixin):
#            def process_request(self, request):
#                print(request.GET.get('a'))
#            def process_view(self, request, view_function, view_args, view_kwargs):
#                pass
#            def process_template_response(self, request, response):
#                pass
#            def process_response(self, request, response):
#                return response
#    使用中间件：配置settings.py的MIDDLEWARE = ['middleware.myApp.myMiddle.MyMiddle']        bz33
#    返爬虫技术就是把每个方法的request拿出来研究一下，有问题就返回None即可
#上传图片
#    概述
#        文件上传时，文件数据存储在request.FILES属性中
#    文件保存位置
#        在static文件夹中新建upfile文件夹，用于存储接收上传的文件        bz34
#    配置setting.py文件最后插入
#       MDEIA_ROOT = os.path.join(BASE_DIR, 'static/upfile')      bz35
#    需求：127.0.0.1:8000/mainApp/upfile/,进入文件上传页面,点击上传，文件从本地保存到服务器下，即static/upfile中，保存成功跳转保存成功页面
#        配置url
#            path('upfile/', views.upfile, name='upfile'),
#            path('savefile/', views.savefile, name='savefile')
#        创建视图
#            def upfile(request):
#                return render(request, 'myApp/upfile.html')
#
#            import os
#            from django.conf import settings #在视同中使用settings.py中的变量
#            def savefile(request):
#                if request.method == 'POST':
#                    file = request.FILES['upfile'] #接收到的文件是以流的方式进行接收的
#                    toPath = os.path.join(settings.MDEIA_ROOT, file.name)
#                    with open(toPath, 'wb') as f:
#                        for fileInfo in file.chunks(): #chunks()方法的功能是将数据流以段的方式接收，并接收一段保存到列表中一段，写入文件一段
#                            f.write(fileInfo)
#                    return render(request, 'myApp/savefile.html')
#                else:
#                    return HttpResponse('上传失败')
#        配置模板
#            <body>
#                <form action="{%url 'mainApp:savefile'%}" method="post" enctype="multipart/form-data">
#                    {%csrf_token%}
#                    <input type="file" name="upfile" multiple="multiple">
#                    <input type="submit" value="提交">
#                </form>
#            </body>
#分页
#    Paginator对象
#        创建对象
#            格式：Paginator(列表, 整数)
#            参数
#                列表：要显示的所有数据(数据库中的数据)
#                整数：一页显示多少数据量
#            返回值：返回一个分页对象
#        属性
#            count 对象总数
#            num_pages 页面总数
#            page_range 页码列表
#        方法
#            page(num) 获得一个page对象
#                注意：如果提供的页码不存在，会抛出'InvalidPage'异常
#        异常
#            InvalidPage 当向Page()传递的是一个无效的页码时抛出
#            PageNotAnInteger 当向Page()传递的不是一个整数时抛出
#            EmptyPage 当向page()传递一个有效值，但是该页面没数据时抛出
#
#    Page对象
#        概述：真正存放分页数据的对象
#        创建对象：Paginator对象的page()方法返回得到Page对象
#        属性
#            object_list 当前页上所有的数据(对象)列表
#            number 当前页的页码值
#            paginator 当前Page对象关联的Paginator
#        方法
#            has_next() 判断是否有下一页，如果有返回True
#            has_previous() 判断是否有上一页，如果有返回True
#            has_other_pages() 判断是否有上一页或下一页，如果有返回True
#            next_page_number() 返回下一页的页码，如果下一页不存在抛出InvalidPage异常
#            previous_page_number() 返回上一页的页码，如果上一页不存在抛出InvalidPage异常
#            len() 返回当前页的数据(对象)个数
#    Paginator对象与Page对象关系
#        如图所示ppt
#    需求：实现分页
#        配置url
#            path('studentspage/<int:studentspage>/', views.studentspage, name='studentspage')
#        创建views
#            from django.shortcuts import render
#            from .models import Students
#            from django.core.paginator import Paginator
#            def studentspage(request, studentspage):
#                # 所有学生数据
#                allSutdentList = Students.myStuObjects.all().filter(sIsDelete=False)
#                # 创建Paginator对象
#                paginator = Paginator(allSutdentList, 5)
#                # 获得所有页码
#                allPageList = paginator.page_range
#                # 创建Page对象
#                page = paginator.page(studentspage)
#                # 获得当前页码
#                currentPage = page.number
#                # 获得当前页的数据
#                currentPagedataList = page.object_list
#                # 判断是否有上一页,有则获取上一页页码，无则获取当前页码
#                if page.has_previous():
#                    previous_page = page.previous_page_number()
#                else:
#                    previous_page = page.number
#                # 判断是否有下一页,有则获取下一页页码，无则获取当前页码
#                if page.has_next():
#                    next_page = page.next_page_number()
#                else:
#                    next_page = page.number
#                return render(request, 'myApp/studentspage.html',
#                              {'currentPageList': currentPagedataList, 'allPageList': allPageList, 'next_page': next_page,
#                               'previous_page': previous_page, 'currentPage': currentPage})
#        创建template
#            {%load staticfiles%}
#            <!DOCTYPE html>
#            <html lang="en">
#            <head>
#                <meta charset="UTF-8">
#                <meta name="viewport" content="width=device-width, initial-scale=1">
#                <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
#                <title>Title</title>
#                <link href="{%static 'myApp/css/bootstrap.min.css'%}" rel="stylesheet">
#                <link href="{%static 'myApp/css/style.css'%}" rel="stylesheet">
#                <script src="{%static 'myApp/js/jQuery.js'%}"></script>
#                <script src="{%static 'myApp/js/bootstrap.min.js'%}"></script>
#            </head>
#            <body>
#                <!--导入当前页的数据-->
#                <ul>
#                    {%for i in currentPageList%}
#                        <li>{{i.sName}}-{{i.sAge}}-{{i.sGender}}-{{i.scontent}}-{{i.sGrade}}-{{i.sCreateTime}}-{{i.sLastTime}}-{{i.sIsDelete}}</li>
#                    {%endfor%}
#                </ul>
#                <!--设置分页按钮-->
#                <nav aria-label="Page navigation">
#                    <ul class="pagination">
#                        <!--上一页-->
#                        <li>
#                            <a href="{%url 'myApp:studentspage' previous_page%}" aria-label="Previous">
#                                <span aria-hidden="true">&laquo;</span>
#                            </a>
#                        </li>
#                        <!--页码-->
#                        {%for pageNum in allPageList%}
#                            {%if pageNum == currentPage%}
#                                <li><a class="btn btn-primary btn-sm active disabled" role="button" href="{%url 'myApp:studentspage' pageNum%}">{{pageNum}}</a></li>
#                            {%else%}
#                                <li><a class="btn btn-primary btn-sm" role="button" href="{%url 'myApp:studentspage' pageNum%}">{{pageNum}}</a></li>
#                            {%endif%}
#                        {%endfor%}
#                        <!--下一页-->
#                        <li>
#                            <a href="{%url 'myApp:studentspage' next_page%}" aria-label="Next">
#                                <span aria-hidden="true">&raquo;</span>
#                            </a>
#                        </li>
#                    </ul>
#                </nav>
#            </body>
#           </html>
#ajax
#    需要动态生成，请求的Json数据
#    需求：客户端点击按钮，发送ajax请求，服务器生成Json数据返回客户端
#        配置url
#            path('ajaxStudents/', views.ajaxStudents),
#            path('ajaxStudents/studentsinfo/', views.studentsinfo, name='studentsinfo')
#        创建视图
#            def ajaxStudents(request):
#                return render(request, 'myApp/ajaxStudents.html')
#            from django.http import JsonResponse
#            def studentsinfo(request):
#                stus = Students.myStuObjects.all().filter(sIsDelete=False)
#                listData = []
#                for stu in stus:
#                    listData.append([stu.sName, stu.sAge])
#                return JsonResponse({'data':listData})
#        创建template
#            <!DOCTYPE html>
#            {%load staticfiles%}
#            <html lang="en">
#            <head>
#                <meta charset="UTF-8">
#                <meta name="viewport" content="width=device-width, initial-scale=1">
#                <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
#                <title>ajax</title>
#                <link href="{%static 'myApp/css/bootstrap.min.css'%}" rel="stylesheet">
#                <link href="{%static 'myApp/css/style.css'%}" rel="stylesheet">
#                <script src="{%static 'myApp/js/jQuery.js'%}"></script>
#                <script src="{%static 'myApp/js/bootstrap.min.js'%}"></script>
#                <script src="{%static 'myApp/js/ajaxStudents.js'%}"></script>
#            </head>
#            <body>
#                <h1>学生信息列表</h1>
#                <button id="btn">显示数据</button>
#                <div id="info"></div>
#            </body>
#            </html>
#        创建js
#            $(function(){
#                var n = 0
#                $('#btn').on('click', function(){
#                    if (n === 0){
#                        $.ajax({
#                            type:'get',
#                            url:"studentsinfo/",
#                            dataType:'json',
#                            success: function(data, textStatus){
#                                console.log(data)
#                                var studentsinfo = data['data'];
#                                console.log(studentsinfo)
#                                for (var i=0; i<studentsinfo.length; i++){
#                                    $('#info').append($('<span>' + studentsinfo[i][0] + '</span>'));
#                                    $('#info').append($('<span>' + studentsinfo[i][1] + '</span><br>'));
#                                }
#                            }
#                        })
#                    }
#                    n += 1
#                })
#           })
#富文本
#    安装
#        pip install django-tinymce
#    在站点中使用
#        配置settings.py文件
#            添加应用
#                INSTALLED_APPS = ['tinymce']
#            设置富文本模式
#                TINYMCE_DEFAULT_CONFIG = {
#                   'theme':'advanced', #最全模式
#                   'width':600,
#                   'height':400,
#                }
#        增加模型
#            from tinymce.models import HTMLField#大文本数据类型
#            class Text(models.Model):
#                str1 = HTMLField()
#            python manage.py makemigrations
#            python manage.py migrate
#        站点注册模型
#            from .models import Text
#            admin.site.register(Text)
#        站点中就能使用富文本了，增加数据保存后，可在mysql数据库中的django->myapp_text表中查询
#    在自定义视图中使用
#        需求：页面中显示富文本,提交后，保存到数据库，并且在显示页面显示输入内容
#        配置url
#            path('edit/', views.edit),
#            path('editSubmit', views.editSubmit, name='editSubmit')
#        创建视图
#            def edit(request):
#                return render(request, 'myApp/edit.html')
#
#            def editSubmit(request):
#                contend = request.POST.get('contend')
#                request.session['contend'] = contend
#                return render(request, 'myApp/editshow.html', {'contend':contend})
#        创建模板
#            富文本显示窗口
#                 <!DOCTYPE html>
#                 <html lang="en">
#                 <head>
#                     <meta charset="UTF-8">
#                     <title>富文本</title>
#                     <script type="text/javascript" src="/static/tiny_mce/tiny_mce.js"></script>
#                     <script type="text/javascript" >
#                         tinyMCE.init({
#                             'mode':'textareas', <!--让textareas标签变成富文本-->
#                             'theme':'advanced',
#                             'width':800,
#                             'height':600,
#                         })
#                     </script>
#                 </head>
#                 <body>
#                     <form action="{%url 'myApp:editSubmit'%}" method="post">
#                         {%csrf_token%}
#                         <textarea name="contend" id="" cols="30" rows="10">justin is good man!</textarea>
#                         <input type="submit" value="提交">
#                     </form>
#                 </body>
#                 </html>
#            富文本提交后显示内容的窗口
#                 <body>
#                     {%autoescape off%}
#                     {{contend}}
#                     {% endautoescape %}
#                 </body>
#celery
#    问题
#        用户发起request，并且要等待response返回，但是在视图中有一些耗时的操作，导致用户可能会等待很长时间才能接受response，这样用户体验很差
#        网站每隔一段时间要同步一次数据，但是http请求是需要触发的，不可能让用户随时刷新网页
#    解决
#        将耗时的操作放到celery中执行，相当于两进程，一个负责用户体验，一个负责执行任务
#        使用celery定时执行数据同步
#    概论
#        任务task
#            本质：python函数，将耗时操作封装成一个函数
#        队列queue
#            将要执行的任务放到队列里
#        工人worker
#            负责执行队列中的任务
#        代理(工头)broker
#            负责调度，在部署环境中使用redis
#    安装
#        pip install celery
#        pip install celery-with-redis
#        pip install django-celery
#    配置settings.py      bz36
#        INSTALLED_APPS = ['djcelery']
#        import djcelery
#        djcelery.setup_loader() #初始化队列
#        BROKER_URL = 'redis://:135cylpsx4848@@127.0.0.1:6379/0'
#                     '数据库://:数据库的密码    @ip地址    :端口/redis的数据库库号'
#        CELERY_IMPORTS = ('myApp.task')
#                           应用名.文件名（定义任务函数的文件名）
#    在应用目录下创建task.py文件        bz37
#    直接迁移，生成celery需要的数据库表
#        python manage.py migrate    bz38
#        迁移之后mysql中就会出现很多关于djcelery的表
#    在工程目录下的工程目录中的新建celery.py文件，内容如下：     bz39
#        from __future__ import absolute_import
#        import os
#        from celery import Celery
#        from django.conf import settings
#
#        os.environ.setdefault('DJANGO_SETTINGS_MODULE','whthas_home.settings')
#
#        app = Celery('portal')
#        app.config_from_object('django.conf:settings')
#        app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)
#
#        @app.task(bind=True)
#        def debug_task(self):
#            print('Request: {0!r}'.format(self.request))
#    在工程目录下的工程目录中的__init__.py添加
#        from .celery import app as celery_app       bz40

#【day212】移动端正式项目
#数据分析及准备
#    轮播数据
#        数据格式
#            第一条
#            img：http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg
#            name:酸奶女王
#            trackid:21870
#            第二条
#            img：http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg
#            name:果冻女王
#            trackid:21871
#            说明：将数据这样写一个说明，并且设置一个trackid号，这个id号是为了对应点击图片后的跳转页面url
#        插入数据库
#            insert into asj_wheel(img, name, trackid) values('http:....jpg', '酸奶女王', '21870'),('http:....jpg', '果冻女王', '21871')
#    商品数据
#        插入数据库
#            insert into asj_goods(productid, productimg, productname, productlongname, isxf, pmdesc, specifics, price, marketprice, categoryid, childcid, childcidname, dealerid, storenums, productnum) values('5676','http:...jpg','达利园，好吃点，...','达利园好吃点高纤...',0,0,'110g', 3.50, 3.5000, 103451, 103544, '饼干糕点')
#    在mysql创建一个实战项目使用的数据库
#搭建项目框架
#    步骤一：1 2 5 6 7 8 14 19 20 21 22 23 24 25 26 27 28 29 30 34 35
#在asj下的urls.py中，设置底部菜单页面的url
#     from django.urls import path
#     from . import views
#     urlpatterns = [
#         path('home/', views.index, name='home'),
#         path('market/', views.index, name='market'),
#         path('cart/', views.index, name='cart'),
#         path('mine/', views.index, name='mine'),
#         path('base/', views.base, name='base')
#     ]
#创建视图
#     from django.shortcuts import render
#
#     def home(request):
#         return render(request, 'asj/home.html', {'Title':'主页'})
#
#     def market(request):
#         return render(request, 'asj/market.html', {'Title':'闪送超市'})
#
#     def cart(request):
#         return render(request, 'asj/cart.html', {'Title':'购物车'})
#
#     def mine(request):
#         return render(request, 'asj/mine.html', {'Title':'我的'})
#
#     def base(request):
#         return render(request, 'asj/base.html', {'Title':'基础模板'})
#创建模板及继承模板
#     base.html
#         <!DOCTYPE html>
#         {%load staticfiles%}
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
#             <title>{{Title}}</title>
#             <link href="{%static 'main/css/reset.css'%}" rel="stylesheet">
#             <link href="{%static 'main/css/swiper.min.css'%}" rel="stylesheet" >
#             <link href="{%static 'main/css/bootstrap.min.css'%}" rel="stylesheet">
#             <link href="{%static 'main/css/base.css'%}" rel="stylesheet">
#             <script src="{%static 'main/js/jQuery.js'%}"></script>
#             <script src="{%static 'main/js/bootstrap.min.js'%}"></script>
#             <script src="{%static 'main/js/swiper.min.js'%}"></script>
#             <script src="{%static 'main/js/base.js'%}"></script>
#             {%block linkscript%}
#             {%endblock linkscript%}
#         </head>
#         <body>
#             <div id="box">
#                 <header>
#                     <nav class="navbar navbar-default">
#                       <div class="container-fluid">
#                         <!-- Brand and toggle get grouped for better mobile display -->
#                         <div class="navbar-header">
#                           <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
#                             <span class="sr-only">Toggle navigation</span>
#                             <span class="icon-bar"></span>
#                             <span class="icon-bar"></span>
#                             <span class="icon-bar"></span>
#                           </button>
#                           <a class="navbar-brand" href="#">Brand</a>
#                         </div>
#
#                         <!-- Collect the nav links, forms, and other content for toggling -->
#                         <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
#                           <ul class="nav navbar-nav">
#                             <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
#                             <li><a href="#">Link</a></li>
#                             <li class="dropdown">
#                               <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
#                               <ul class="dropdown-menu">
#                                 <li><a href="#">Action</a></li>
#                                 <li><a href="#">Another action</a></li>
#                                 <li><a href="#">Something else here</a></li>
#                                 <li role="separator" class="divider"></li>
#                                 <li><a href="#">Separated link</a></li>
#                                 <li role="separator" class="divider"></li>
#                                 <li><a href="#">One more separated link</a></li>
#                               </ul>
#                             </li>
#                           </ul>
#                           <form class="navbar-form navbar-left">
#                             <div class="form-group">
#                               <input type="text" class="form-control" placeholder="Search">
#                             </div>
#                             <button type="submit" class="btn btn-default">Submit</button>
#                           </form>
#                           <ul class="nav navbar-nav navbar-right">
#                             <li><a href="#">Link</a></li>
#                             <li class="dropdown">
#                               <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
#                               <ul class="dropdown-menu">
#                                 <li><a href="#">Action</a></li>
#                                 <li><a href="#">Another action</a></li>
#                                 <li><a href="#">Something else here</a></li>
#                                 <li role="separator" class="divider"></li>
#                                 <li><a href="#">Separated link</a></li>
#                               </ul>
#                             </li>
#                           </ul>
#                         </div><!-- /.navbar-collapse -->
#                       </div><!-- /.container-fluid -->
#                     </nav>
#                 </header>
#
#                 <div id="main">
#                     {%block main%}
#                     {%endblock main%}
#                 </div>
#
#                 <footer>
#                     <a class="home" href="{%url 'asj:home'%}" role="button">
#                         <dl>
#                             <dt><span></span></dt>
#                             <dd>主页</dd>
#                         </dl>
#                     </a>
#                     <a class="market" href="{%url 'asj:market'%}" role="button">
#                         <dl>
#                             <dt><span></span></dt>
#                             <dd>闪送超市</dd>
#                         </dl>
#                     </a>
#                     <a class="cart" href="{%url 'asj:cart'%}" role="button">
#                         <dl>
#                             <dt><span></span></dt>
#                             <dd>购物车</dd>
#                         </dl>
#                     </a>
#                     <a class="mine" href="{%url 'asj:mine'%}" role="button">
#                         <dl>
#                             <dt><span></span></dt>
#                             <dd>我的</dd>
#                         </dl>
#                     </a>
#                 </footer>
#             </div>
#         </body>
#         </html>
#     home.html
#         {%extends 'asj/base.html'%}
#         {%load staticfiles%}
#         {%block linkscript%}
#             <link rel="stylesheet" href="{%static 'home/css/home.css'%}">
#             <script src="{%static 'home/js/home.js'%}"></script>
#         {%endblock linkscript%}
#         {%block main%}
#         <h1>主页</h1>
#         {%endblock main%}
#     market.html
#         {%extends 'asj/base.html'%}
#         {%load staticfiles%}
#         {%block linkscript%}
#             <link rel="stylesheet" href="{%static 'market/css/market.css'%}">
#             <script src="{%static 'market/js/market.js'%}"></script>
#         {%endblock linkscript%}
#         {%block main%}
#         <h1>闪送超市</h1>
#         {%endblock main%}
#     cart.html
#         {%extends 'asj/base.html'%}
#         {%load staticfiles%}
#         {%block linkscript%}
#             <link rel="stylesheet" href="{%static 'cart/css/cart.css'%}">
#             <script src="{%static 'cart/js/cart.js'%}"></script>
#         {%endblock linkscript%}
#         {%block main%}
#         <h1>购物车</h1>
#         {%endblock main%}
#     mine.html
#         {%extends 'asj/base.html'%}
#         {%load staticfiles%}
#         {%block linkscript%}
#             <link rel="stylesheet" href="{%static 'mine/css/mine.css'%}">
#             <script src="{%static 'mine/js/mine.js'%}"></script>
#         {%endblock linkscript%}
#         {%block main%}
#         <h1>我的</h1>
#         {%endblock main%}
#
#创建模型迁移执行迁移
#    步骤：9 10 11 12 13
#用insert into将轮播数据插入数据库
#搭建继承模板页面
#

#【day】github
#注册
#   账号：18086829907
#   密码：135cylpsx
#   邮箱：417217170@qq.com
#下载
#   https://git-scm.com/download/win
#安装
#   https://www.cnblogs.com/wj-1314/p/7993819.html
#打开Git Bash
#   设置
#       配置用户名(Git Bash)
#           git config --global user.name "18086829907"
#       配置邮箱(Git Bash)
#           git config --global user.email "417217170@qq.com"
#版本库
#   什么是版本库
#       又名仓库，可以理解成一个目录，这个目录里面的所有文件都可以被git管理起来，每个文件的修改、删除,git都能跟踪，以便任何时刻都有一个追踪历史，或者在将来某个时刻可以还原
#   创建版本库
#       在一个合适的地方，创建一个空目录 d:\gitKu
#       cd 进入该目录$ cd d:/gitku/    可以将文件夹拖拽到gitbash生成路径
#       $ pwd 显示当前工作路径
#       使用 $ git init 命令把这个目录变成git可以管理的仓库
#       $ ls -a 显示 当前目录 上级目录 当前目录中的文件(隐藏文件)   -> ./  ../  .git/
#       $ cd .git/ 进入.git文件
#       $ ls   查看文件中的内容
#       $ cd .. 返回上级目录
#       注意：千万不要手动修改.git目录里面的文件
#   把文件添加到版本库
#       在仓库目录中创建一个justin.txt文件
#           在文本文件中添加任意内容内容（用subline打开）
#       把文件添加到仓库
#           git add justin.txt   #git add .  将工作区的所有文件提交到工作区中的缓存区
#       把文件提交到仓库，并给文件打上标签——"第一次提交" 今后在正式开发过程中标签应该写上，本次代码增加的功能，即功能日志
#           git commit -m "第一次提交"     #git commit -m . "将所有修改过的内容提交到版本区"
#               提示 [master (root-commit) a37e933] 第一次提交 1 file changed, 1 insertion(+) create mode 100644 justin.txt即成功提交
#               说明：$ git commit可以进入vim界面，在vim中书写功能更新日志 书写完之后写入并退出(:wq)就返回到bash界面
#   时光穿梭机
#       git status
#           功能：查看仓库当前状态是否有改变
#           返回：如果仓库中的文件被修改过，返回文件被修改过的提示信息
#           示例：git status
#       git diff
#           功能：查看仓库文件被修改前和被修改后的内容
#           示例：git diff
#       注意：修改过后的代码，确认无误后，需要手动提交到仓库中进行管理
#           git add justin.txt
#           git commit -m "第二次提交"
#           注意：刚提交后，仓库外和仓库内的代码是一致的，所以git status的状态是working tree clean
#       git log
#           功能：显示从最近到最远的提交日志
#       git log --pretty=oneline
#           功能：查看日志，只显示日志的编号和功能日志
#       git log --graph
#           功能：查看分支合并图，以树状结构显示
#       git reset --hard HEAD^
#           功能：版本回退，回退后，文件会自动修改到上个版本
#           说明：^回退一个版本，^^回退两个版本
#           示例：git reset --hard HEAD^
#                git reset --hard HEAD^^
#       git reset --hard HEAD~n
#           功能：版本回退到上n个版本
#           示例：git reset --hard HEAD~100
#       git reset --hard HEAD 具体版本号
#           功能：根据具体版本号回退或前进
#           示例：git reset --hard HEAD a37e9339f315f7198c3d2f4e69af0f7006a30077
#           注意：版本号不用写全，写4-5个即可切换
#               示例 git reset --hard HEAD a37e93
#       git reflog
#           功能：查看所有执行过的git命令,以及每次修改后的版本号
#           示例：git reflog
#       git checkout -- 文件名.后缀
#           功能：撤销
#           说明
#               文件修改后未添加到缓存区，执行git checkout,文件回退到当前指针指向的版本库中的代码文件
#               文件修改后添加到了缓存区，却没有添加到版本区，此时再修改文件代码，即原文件的代码、缓存区中文件代码、版本区文件代码都不一致，执行撤销，回退到缓存区代码
#               总之，就是让文件回退到最后一次git add或最后一次git commit时的状态
#   远程仓库
#       创建SSH Key
#           git bash中输入：ssh-keygen -t rsa -C "417217170@qq.com"
#           记录.shh目录位置，即第一次出现的路径 /c/Users/surface/.ssh/id_rsa
#           进入.ssh目录：cd /c/Users/surface/.ssh/
#               pwd 查看当前工作路径
#               ls 查看当前目录中的所有文件
#                   id_rsa 私钥
#                   id_rsa.pub 公钥
#               ll 查看私钥权限
#               cat id_rsa 查看私钥内容
#               cat id_rsa.pub 查看公钥内容
#                   将公钥内容拷贝到subline中的一个新建文件中（不要用txt文本文件）
#                   将公钥写入github官网
#                       作用：定义你可以往你的账户中写代码
#                       注意：将代码上传到官网，电脑必须有私钥，也就是说公司的电脑，家里的电脑都需要安装上私钥
#                       步骤
#                           打开www.github.com
#                               点击右上角粉红色类似衣服的下拉图标
#                                   再点击settings
#                                       在右侧导航栏中点击SSH and GPG keys
#                                           点击New SSH key
#                                               title 取一个名字
#                                                   说明：1、clone时本地仓库的目录名 2、www.github.com/用户名/title 即www.github.com/18086829907/justin
#                                               key 粘贴公钥
#                                               点击Add SSH key
#       测试密钥是否通过
#           $ ssh -T git@github.com
#               yes
#                   提示Hi 18086829907! You've successfully authenticated 表示成功
#                       再次刷新刚才添加公钥的网页
#       删除密钥
#           $ cd /c/Users/surface/.ssh/
#           $ rm -rf .ssh
#       创建远程仓库
#           点击猫的头像
#               start a project
#                   在Repository name设置一个名字 justin
#                   选择public
#                       选项说明
#                           public 你上传上去的代码，任何人随便下载
#                           private 付费选项，指定人才能下载
#                   勾选Initialize this repository with a README
#                       选项说明：初始化
#                   Add.gitignore 选择None
#                       说明：表示不用上传到官网的文件
#                   点击Create repository
#       关联远程仓库
#           git remote add origin 远程仓库地址
#               获取远程仓库地址
#                   在远程仓库页面点击 clone or download
#                   点击Use SSH
#                   点击复制按钮
#               回到本地仓库文件夹
#                   $ cd /d/gitku
#                   $ git remote add origin git@github.com:18086829907/justin.git
#       删除关联
#           git remote rm origin
#       拉取远程仓库内容到本地库
#           git pull origin 分支名
#               注意
#                   如果出现fatal: refusing to merge unrelated histories
#                   $ git pull origin master --allow-unrelated-histories
#                   $ :q 退出vim
#       推送本地库内容到远程库
#           git push origin 分支名
#           注意：第一次推送必须先执行一次拉取，否则会报错，因为远程仓和本地仓不一致
#       忽略特殊文件 .gitignore
#           作用：记录不往官网上推送的文件名，往官网上推送的时候，被记录了的文件就不会被推送上去
#           注意：不上传的文件在拉取的时候也不会拉取到，因此不要胡乱删除不上传文件，以免文件丢失
#           示例：
#               $ touch .gitignore 在当前目录创建普通文件.gitignore
#               $ touch bao
#               subline打开.gitignore 在其中输入bao
#               $ git add .
#               $ git commit -m . "提交到版本区"
#               $ git push origin master
#
#       从零开发（克隆远程库 克隆库）
#           先在官网上创建远程库
#           打开git bash
#           cd到一个目录中
#           使用git clone 远程库地址在此目录中创建本地库
#               示例：git clone git@github.com:18086829907/justin.git
#           再进行公钥的配置
#       分支管理
#           作用：假设你准备开发一个新功能，但是需要两周才能完成，第一周写了50%，如果立即提交，由于代码还没写完，不完整的代码库会导致别人不能干活了。如果代码全部写完再一次提交，又会存在丢失每天进度的巨大风险，
#                有了分支，可以避免上面的问题。创建一个属于自己的分支，别人看不到，还继续在原来的分支上正常工作，而我们在自己的分支上干活，想提交就提交，直到开发完毕后，在一次性合并到原来的分支上，这样，既安全，又不影响他人工作
#           特点：git的分支是与众不同的，无论创建、切换和删除分支，git在非常短的时间内就能完成!无论版本库是1个文件还是1万个文件
#           实现分支管理：
#               本质：不把代码commit到主分支上，而是提交到自己创建的分支上面
#                   marster主分支
#                       概念：git自带的分支，在版本回退中，每次提交，git都把它们串成一条时间线，在git里，这个分支叫主分支，即master分支。HEAD严格来说不是指向提交，而是指向master，master才是指向提交的，所以，HEAD指向的就是当前分支
#                            每次提交，master轴会越来越长
#               创建分支
#                   本地分支创建
#                       git branch 分支名
#                       示例
#                           $ cd /d/justin
#                           $ git branch jus
#                   远程分支创建
#                       在远程仓库中点击Branch:master下拉菜单
#                       搜索中搜索本地分支名
#                       如果没有该分支，则提出create branch 分支名
#                       点击提示即可创建
#               切换分支
#                   git checkout 分支名
#               创建并切换到新分支上
#                   git checkout -b 分支名
#               查看所有分支以及当前分支
#                   git branch
#                   说明：当前分支前会注明*号
#               将自建分支的内容合并到marster分支上
#                   git merge 分支名
#                   示例
#                       git checkout master
#                       git merge jus
#           分支提交和推送
#               分支修改内容的提交步骤
#                   $ git checkout 分支名 即在自创分支下
#                   $ git add .
#                   $ git commin
#                       vim 中输入功能更新日志
#                           i 插入模式
#                           :wq 写入并退出
#                   $ git push origin jus #远程仓库需要先创建好
#           分支拉取或克隆
#               $ cd cd /d/gitdata    进入工作目录
#               $ git clone git@github.com:18086829907/justin.git    克隆（克隆的是远程主分支的内容）
#               $ cd justin    进入数据仓
#               $ git checkout -b jus 创建分支并进入
#               $ git pull origin jus 拉取远程jus分支
#           分支完成工作工作流
#               在分支上
#               $ git add .    #将修改后的文件添加到工作区的缓存区
#               $ git commit -m "jus完成功能更新"     #将缓存区的文件备份到版本区
#               $ git push origin jus     #将jus分支版本区的文件推送到远程jus分支上
#               $ git checkout marster     #切换到主分支
#               $ git merge jus    #合并jus分支的版本区的文件到主分支的版本区
#               $ git push origin marster      #将主分支版本区的文件推送到远程marster分支上
#           mia工作流（第二个程序员的git工作流, 完整git工作流）
#               本地找到一个合适的路径创建一个gitdata文件
#               $ cd /d/gitdata
#               $ git clone git@github.com:18086829907/justin.git
#               $ git checkout -b mia
#               创建远程mia分支（项目经理的工作，注意：在创建远程分支时，远程分支会克隆远程master分支）
#               $ git pull origin mia (需要保持远程分支和本地自创分支数据一致，因此需要先拉取一次远程分支)
#               while True:
#                   书写工作代码
#                   $ git add .
#                   $ git commit
#                       i 插入模式
#                       书写更新日志
#                       esc
#                       :wq
#                   $ git push origin mia
#                   if n == '二号程序员的功能更新完善，测试无误'：
#                       break
#               $ git checkout master
#               $ git merge mia
#               $ git push origin master
#               if 需要主分支上其他人的功能模块:
#                   $ git pull origin master
#                   $ git checkout mia
#                   $ git merge master
#           删除分支
#               删除本地分支
#                   git branch -d 分支名
#               删除远程分支
#                   git push origin :分支名
#                   git push origin --delete 分支名
#   工作流详见ppt
#       注意：不管在公司工作，还是在家中工作，一定要注意，都需要在各自的仓库分支中工作，切记，切记
#       冲突：主分支版本区代码和分支版本区代码不一致
#            即，主分支中书写了代码并且备份到了版本区，分支中又书写了代码并且备份到了版本区
#            再在主分支中合并分支代码时，文件中就会显示冲突的代码，此时需要手动调整冲突代码
#   分支策略
#       master分支作为上线版本代码集合
#       副master分支策略
#           项目经理在github上创建一个dev分支
#           小伙伴在自创分支中干活，都把自己的代码集合合并提交到dev分支上
#           在dev分支上确定能上线的代码文件集合，
#           最后由项目经理审核，将dev分支pull下来，合并到master上，最后提交到远程master分支
#           完成版本1.0
#   标签管理
#       意义：发布一个版本时，我们通常先在版本库中打一个标签(tag)，这样，就唯一确定了打标签时刻的版本，将来无论什么时候，取某个标签的版本，就是把那个打完标签的时刻的历史版本取出来，所以，标签也是版本的一个快照
#       打标签
#           *原型：git tag 标签名
#           示例：git tag
#       查看所有标签
#           原型：git tag
#           示例：git tag
#       指定commit id
#           原型：git tag 标签名 commitID
#           示例：
#       指定标签信息
#           原型：git tag -a 标签名 -m "标签信息"
#           标签
#       切换到指定标签
#           *原型：git checkout 标签名
#           示例：
#       查看说明文字
#           原型：git show 标签名
#           示例：
#       删除标签
#           原型：git tag -d 标签名
#           示例：
#       推送标签到远程
#           *原型：git push origin 标签名
#           示例：
#       一次性推送全部尚未推送到远程的本地标签
#           原型：git push origin --tags
#           示例：
#       删除已推送到远程的标签
#           先本地删除
#               *原型：git tag -d 标签名
#               示例：
#           再从远程删除
#               *原型：git push origin :refs/tag/标签名
#               示例：



#【day】初始tornado
#概念
#   全称Tornado Web Server，是一种Web服务器软件的开源版本
#   特点
#       作为Web框架，是一个轻量级的web框架，其拥有异步非阻塞IO的处理方式
#       作为Web服务器，Tornado有较为出色的抗负载能力，官方用nginx反向代理的方式部署Tornado和其他Python Web应用框架进行对比，结果最大浏览量超过第二名近40%
#   使用场景
#       用户量大，高并发
#       大量的HTTP持久链接
#           使用同一个TCP链接来发送和接收多个HTTP请求/应答，而不是为每一个新的请求/应答打开新的链接的方式
#           对于HTTP1.0，可以在请求的包头（header）中添加Connection:keep-Alive=
#           对于HTTP1.1，所有的链接默认都是持久连接
#   C10K：上面的高并发问题，通常用C10K这一概念来描述，C10K-Concurrently handing ten thousand connections,即并发10000个链接。对于单台服务器而言，根本无法承担，而采用多台服务器分布式又意味着高昂成本
#   性能：Tornado在设计之初就考虑到了性能因素，旨在解决C10K问题，这样的设计使得其成为一个拥有非常高性能的解决方案（服务器与框架的集合体）
#与django对比
#   django
#       django是走大而全的方向，注重的是高效开发，它最出名的是其全自动化的管理后台：只需要使用起ORM，做简单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台
#       django提供的方便，也意味着django内置的ORM跟框架内的其他模块耦合程度高，应用程序必须使用django内置的ORM，否则就不能享受到框架内提供的种种基于其ORM的便利
#       特点
#           session功能
#           后台管理
#           ORM
#   Tornado
#       Tornado走的是少而精的方向，注重的是性能优越，它最出名的就是异步非阻塞的设计方式
#       特点
#           HTTP服务器
#           异步编程
#           WebSoockets
#安装
#   pip install tornado
#   说明
#       Tornado应该运行在类Unix平台，在线上部署时为了最佳的性能和扩展性，仅推荐Linux和BSD(因为充分利用linux的epol工具和bsd的kqueue工具，是Tornado不依靠多进程/多线程而达到高性能的原因)
#       对于MAC OS X，虽然也是衍生自BSD并且支持kqueue,但是其网络性能通常不太给力，因此仅推荐用于开发
#       对于windows，Tornado官方没有提供配置支持，但是也可以运行起来，不过仅推荐在开发中使用
#   测试
#         import tornado.web #tornado的基础web框架模块
#         import tornado.ioloop #tornado的核心IO循环模块，封装了Linux的epoll和BSD的kquque，是tornado高效的基础
#
#         #类比django中的视图，是一个业务处理类
#         class IndexHandler(tornado.web.RequestHandler):
#             #处理get请求的
#             def get(self, *args, **kwargs):
#                 #对应http请求的方法
#                 self.write('jusint is good man') #给客户端响应的数据
#             #处理post请求的
#             def post(self, *args, **kwargs):
#                 pass
#
#         if __name__ == '__main__':
#             #实例化一个应用的对象
#             #Application:是tornado web框架的核心应用类，是与服务器对应的接口
#             #里面保存了路由映射表
#             app = tornado.web.Application([
#                 (r'/', IndexHandler)
#             ])
#             #示例化对象的listen方法，功能创建一个http服务器额实例，并绑定了端口
#             #注意：此时服务器
#             app.listen(8000) #监听端口
#             #.IOLoop.current()返回当前线程的IOloop实例，返回一个对象，当前线程读写操作的对象
#             #.start()：启动IOLoop实例的I/O循环，同时开始了监听
#             tornado.ioloop.IOLoop.current().start()
#
#   高性能原理
#       详见Tornado高效原理图
#   Httpserver类
#       本质：服务器类
#       引入模块：import tornado.httpserver
#       实例化：httpserver = tornado.httpserver.Httpserver(app)
#           参数app：包含了路由映射表的应用，app=tornado.web.Application([(r'/', IndexHandler)])
#       实例化后的属性
#       实例化后的方法
#           listen()
#               功能：监听端口号
#               原型：httpserver.listen(数字类型的端口号)
#               示例：httpserver.listen(8000)
#           bind()
#               功能：绑定端口号
#               原型：httpserver.bind(数字类型的端口号)
#               示例：httpserver.listen(8000)
#           start()
#               功能：监听端口号
#               原型：httpserver.start(num_processes)
#               参数：启动进程的个数，默认为1
#                       值>0：创建对应个数个子进程
#                       值为None或<=0：开启对应硬件机器的cup核心数个子进程，即本机为八核cup,就开启8个进程
#               示例：httpserver.start(5)
#       说明
#           app.listen(8000)启动服务器代码简洁但默认是单进程模式
#           使用实例化服务器类才能启动多线程模式，但是由于一些问题，不建议使用以上方式启动多进程
#               问题一：每个子进程都会从父进程中复制一份IOLoop的实例，如果在创建子进程前修改了IOLoop，会影响所有的子进程，耦合度太高
#               问题二：所有的命令都是由一个命令启动的，无法做到在不停止服务的情况下修改代码
#               问题三：所有进程共享一个端口，想要分别监控很困难
#           启动多进程的方式为手动启动
#               从多个黑屏终端启动多次tormado的python代码
#opthions
#   本质：tornado.opthins模块
#   动态生成端口号

#【day】