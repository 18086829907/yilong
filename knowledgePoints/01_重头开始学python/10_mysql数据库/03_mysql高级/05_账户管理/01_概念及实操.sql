-- 账户级别分类：
-- 服务实例级账号
-- 数据库级别账号
-- 数据表级别账号
-- 字段级别的权限
-- 存储程序级别的账号

-- 前情提要
use mysql;
show talbes;
select user,host,authentication_string from user;  -- user字段：表示可以登陆mysql的用户 host字段：表示可以从哪里登录（%：从任何网段登录，localhost：只能从本机登录）authentication_string字段：密码

desc user;  -- 查看所有用户

-- 创建用户&授予权限
grant 权限列表 on 数据库.数据表 to '用户名'@'允许访问主机' identified by '密码';
grant 权限列表 on 数据库.* to '用户名'@'允许访问主机' identified by '密码';
grant 权限列表 on 数据库.数据表1,数据库.数据表2 to '用户名'@'访问主机' identified by '密码';
grant select on stock_db.* to 'slave'@'%' identified by 'slave';

-- demo
-- 创建一个laowang 的账号，密码为123456，只能通过本地访问，并且只能对 jing_dong 数据库中的所有表进行 读 操作

-- step1：使用root登录
mysql -uroot -p

-- step2：创建账户并授予权限
grant select on jing_dong.* to 'laowang'@'localhost' identified by '123456';
exit

-- step3：测试登录和测试权限
mysql -ulaowang -p
123456
select databases;  -- 这个语句的结果，只有jing_dong数据库
use jing_dong;
show tables;
select * from goods;
update goods set price=2299 where id=1;  -- 这句话会报错，没有权限

-- demo
-- 创建一个可以在任何地方登录的名为'laoli'的账户，只对京东数据库中所有表有所有权限
grant all privileges on jing_dong.* to 'laoli'@'%' identified by '123456';

-- 修改权限
grant 权限名称 on 数据库.数据表 to '账户名'@'主机' with grant option;
grant select,insert on jing_dong.* to 'laochen'@'localhost' with grant option;
flush privileges;  -- 刷新权限

-- 修改密码
update user set authentication_string=password('123') where user='laowang';
flush privileges;

-- 远程登录（危险慎用）
vim /etc/mysql/mysql.conf.d/mysql.cnf +43
# bind_addres = 127.0.0.1
sudo mysql -ulaongli -p123456 -h192.168.1.1  -- 其他任意地方都能用这个命令，连接192.168.1.1电脑的数据库
-- 只要别人知道你的ip，你的端口号，你的用户名，你的密码，就能登录你的数据库
-- ip用扫面器可以扫出来，端口用端口扫描器扫出来，用户名一般都有root，密码用暴力破解（网上下载好几G的密码本）

-- 如果要远程登录，一般使用ssh远程登录ubuntu，再用ubuntu本地登录数据库

-- 删除账户
drop user '用户名'@'主机'



-- root密码忘记了怎么办？
-- 1.修改配置参数 /etc/my.cnf
-- 在[mysqld] 下面加上:
skip-grant-tables
-- 2.重启mysql
service mysqld restart
-- 3.注意事项：此时所有用户登录当前数据库都是免密码的，所以此时数据库的安全性是非常低的。
-- 4.修改密码
mysql -uroot -p
update mysql.user set password=password('123456') where user= 'root';
flush privileges;
-- 5.去掉参数
-- a.密码修改好了之后，去掉配置文件中的 skip-grant-tables
-- b.再次重启数据库。