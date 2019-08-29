/*
#限制root登录连接ip
show databases;
use mysql;
show tables;
select user,host,password from user;
update user set host='127.0.0.1' where user='root'; 只保留一个root能登录的本地ip
insert into user(user,host) value(chognqin,'171.221.149.227') 允许一个用户用添加的本地id登录（只有重庆的一台本机能登录）
update user set password=password'admin' where user='root'; 修改root用户的登录密码
*/

#修改密码
#E:\mysql\soft\bin>mysqladmin -uroot -pcylpsx password 123456


#忘记密码
/*
#E:\mysql\soft\bin>mysql --skip-grant-tables
#C:\Users\Administrator>mysql
show databases;
use mysql;
show tables;
select user,host,password from user;
update user set passoword=password('admin') where user='root';
flush privileges; #更新权限
*/

create database test; #创建+数据库+名；
show databases; #显示+数据库；


/*数据库*/
use test; #使用+数据库名；
#创建+表+表名；（列名+类型+修辞）
drop database test; #删除+数据库+数据库名；

/*数据表*/
-- DDL 《data defination language》 数据定义语言 表的增删改
create table stu(id int(10) auto_increment primary key comment'用户id',
				 name varchar(10) not null comment'用户名',
                 password char(32) not null comment'用户密码', #32位是md5加密
                 mobile char(11) not null,
                 gender varchar(20) not null,
                 age int(10) unsigned not null comment'用户年龄',
                 emaill varchar(50) not null comment'用户邮箱',
                 balance decimal(10,2) not null default 0.00 comment'用户余额',
                 created_at timestamp not null comment'用户注册时间'
                 );
alter table stu add column gender1 varchar(20) not null after password; #改变+表+表名+加+列+列名+类型+修辞+之后+列名；
alter table stu drop gender1; #改变+表+表名+删除+列名；
alter table stu modify name varchar(50) not null; #改变+表+表名+修改+列名+需要修改的内容；
alter table stu change created_at created_time timestamp not null; #改变+表+表名+更改+原列名+替换列名+类型+修辞；
alter table stu rename to student; #改变+表+原表名+重命名+为+替换列名；
#show tables; #显示+表名；（当前数据库中的表名）
#show create table student; #显示+创建表+表名（显示当前数据库中被创建的表的字段的源代码）
desc student; #展示字段+表名；

-- DML 《data manipulation language》 数据操作语言 表中数据的增删改查操作
#插入值
insert into student values(1,'彭淑贤','135cylpsx','18086829907','女',8,'2476673550@qq.com',254.5,now()); #插入+进入之内+表名+值+（value1,value2,value3..） value值必须跟列名对应
insert into student(name,password,mobile,gender,age,emaill,balance,created_time) values('陈紫妍','135cylpsx','18086829907','女',8,'2476673550@qq.com',254.5,now()); #指定列名插入，可以只插入部分列名与之对应的值
insert into student(name,password,mobile,gender,age,emaill,balance,created_time) values('陈艺龙','135cylpsx','18086829907','男',30,'',0.0,now());
insert into student(name,password,mobile,gender,age,emaill,balance,created_time) values('李国琼','135cylpsx','18086829907','女',50,'',0.0,now());

#更新值
update student set age=50 where id=4; #更新+表名+设置+列名=value+哪（条件）+id=value；python：data[data['id']==4]
set sql_safe_updates = 0 ;#当不适用id为where判断条件时需要修改sql_safe_updates
update student set balance=600 where balance=0.00; #更新+表名+设置+列名=value+哪（条件）+列名=values Python：data[data['column']==00]
update student set emaill='417217170@qq.com' where emaill='';#更新+表名+设置+列名=value+哪+列名=value； 替换emaill字段中的空值
update student set balance=10000 where id in(2,3); #更新+表名+设置+列名=value+哪+id in（2,3）； 同时修改多个指定列
update student set balance=10000 where id between 2 and 4;#更新+表名+设置+列名=value+哪+在之间+value+和+value； 同时修改一定范围中的值
update student set password='135psxcyl',mobile='17311328850',age=30,balance=10000 where id=1; #同时修改多列字段值
set sql_safe_updates = 1 ;

#删除值
delete from student where id=2;#删除id=4的值
delete from student; #删除+从哪+表名； 删除数据表 保留id值
truncate student; #重置+表名 能重置id

select * from student; #选择 +*（所有行） +从哪里+表名；

-- DCL 《data control language》 数据控制语言

#查看有哪些权限
show databases;
use mysql;
select user,host from user;

#创建用户
create user'ordinary'@'%' identified by '123456'; #%指所有的ip都能登录

/*
修改用户连接ip
use mysql; #进入数据库
select user,host from user; #选择user表中的user和host字段
update user set host='localhost' where user='ordinary'; #更改ordinary用户的可登录ip
delete from user where user='ordinary'; #删除用户
*/

#给用户授权
grant update,insert,delete,select,alter,insert on test.* to 'ordinary'@'localhost'; #授权 权限1，权限2... on 数据库.表名（*代表所有） to '用户名'@'登录ip'
grant all on *.* to 'ordinary'@'localhost'; #授予所有数据库的所有表的所有权限给一个用户
grant update,insert,delete,select,alter,insert on test.* to 'ordinary1'@'localhost'; #直接授权给一个不存在的用户可以将创建和授权同时实现，这句话只支持5.6版本
flush privileges; #刷新权限

#收回权限
revoke select on test.* from 'ordinart'@'localhost'; #撤销 权限1 on 数据库.表名（*代表所有）from '用户名'@'登录ip'
flush privileges; #刷新权限

#查看用户权限
show grants for 'ordinary'@'localhost'; #显示 授权 的 '用户名'@'ip'；

#删除用户
drop user 'ordinary'@'localhost'; #删除 用户列表 '用户名'@'ip';

-- DQL 《data query language》 数据查询语言
use test;

#选择数据
select * from student;
select * from student where name='陈艺龙'; #student[student['name']=='陈艺龙']
select distinct mobile from student; #查询某字段中重复的值
select concat_ws('==',gender,age) as 性别和年龄 from student; #选择 连接_连接符号('连接符号', column1，coloumn2) 作为 新column 从 表名； 显示两个字段连接后数据，未修改原数据表中的数据
select name as user_name,age as user_age from student; #选择 column1 as column1_1 , column2 as column2_1 from 表名； 将字段名修改后查看字段数据，未修改原数据表中的数据
select * from student where name like '陈艺龙'; #data[data['name']=='陈艺龙']
select * from student where name like '陈%'; #%为正则化：陈%表示第一个是陈后面的是任意值，%陈表示最后一个是陈前面的是任意值，%陈%表示前面是任意值后面也是任意值

#排序
select id,name from student order by id asc; #data[['id','name']].sort_values(by='id', ascending=True, inplace=False)
select id,name from student order by id desc; #data[['id','name']].sort_values(by='id', ascending=False, inplace=False)

#运算
select count(*) from student; #data.groupby('id').count()['id']
select sum(age) as sum_age from student; #data.groupby('id').sum()['age']
select avg(age) as avg_age from student; #data.groupby('id').mean()['age']
select max(age) as max_age from student; #data.groupby('id').max()['age']
select min(age) as min_age from student; #data.groupby('id').min()['age']
select count(*) as totals,gender from student group by gender; #data.groupby('gender').count()
select gender from student group by gender having count(*)>1;  #data[data['gender']=='女'].count()
select count(*) as 女士总数 from student where gender='女'; #data[data['gender']=='女'].count()

#连接查询
select s.name,m.english,m.mathematics,m.chinese,m.stu_id from student as s,mark as m where s.id=m.stu_id; #pd.merge(student,mark,lift_on='id',right_on='stu_id') #内连接查询
select s.name,m.english,m.mathematics,m.chinese,m.stu_id from student as s inner join mark as m on s.id=m.stu_id; #pd.merge(student,mark,lift_on='id',right_on='stu_id') #内连接查询
select s.name,m.english,m.mathematics,m.chinese,m.stu_id from student as s left join mark as m on s.id=m.stu_id; #pd.merge(student,mark,lift_on='id',right_on='stu_id',how='student') #左连接查询
select s.name,m.english,m.mathematics,m.chinese,m.stu_id from student as s right join mark as m on s.id=m.stu_id; #pd.merge(student,mark,lift_on='id',right_on='stu_id',how='mark') #右连接查询

#联合查询
select name from student union all select mark from mark;

#子查询

select * from mark;
select * from student;
