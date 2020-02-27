-- 一台主服务器 n台从服务器
-- 所有的写操作，在主服务器中执行
-- 主服务器中的数据库的数据一变化，所有的从服务器同步更新数据
-- 从服务器里面的数据库也可能有好几个从数据库


-- 配置主从同步的基本步骤
-- 1、在服务器上，必须开启二进制日志机制和配置一个独立的ID
-- 2、在每一个从服务器上，配置一个唯一的ID，创建一个用来专门复制主服务器的账户
-- 3、在开始复制进程前，在主服务器上记录二进制文件的位置信息
-- 4、如果在开始复制之前，数据库中已有数据，就必须先创建一个数据快照（可以使用mysqldump导出数据库，或者直接复制数据文件）
-- 5、配置从服务器要连接的主服务器IP地址和登录授权，二进制日志文件名和位置


-- 具体步骤
-- 1.1(将所有的数据库都拷贝的步骤)
-- 在主ubuntu中执行命令
mysqldump -uroot -p135cylpsx --all-databases --lock-all-tables > ~/master_db.sql  # 备份所有数据库的所有文件
-- 在从ubuntu中执行命令
mysql -uroot -p135cylpsx < master_db.sql  -- 导出全部数据库，则不需要到从数据库中手动创建数据库，直接用这个命令即可


-- 1.2(只拷贝其中一个数据库的步骤，注意如果执行了1.1，就不用执行1.2了)
-- 在主ubuntu中执行命令
mysqldump -uroot -p134cylpsx jing_dong > jd.sql  -- 备份jing_dong数据库的所有数据，并导入jd.sql中
--在从ubuntu中
-- 将jd.sql文件传到从ubuntu中的~/sqlData
cd ~/sqlData
mysql -uroot -p
create databases jing_dong;
source jd.sql;


-- 2(配置主服务器)
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf +84
84 server-id      = 1
85 log_bin            = /var/log/mysql/mysql-bin.log
-- 保证84行和85行代码前没有注释
-- 重启服务器
sudo service mysql restart


-- 3(配置从服务器)
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf +84
84 server-id      = 2
85 #log_bin            = /var/log/mysql/mysql-bin.log
-- 注意1:84行，主从服务器的server_id的值可以是任何数字，但一定不能相同
-- 注意2：从服务器的85行一定不要开启log日志


-- 4(主服务器中，新建一个mysql用户，用于从服务器使用新用户登录，主服务器中的mysql)
-- step1：使用root登录
mysql -uroot -p
-- step2：创建账户并授予权限
grant replication slave on *.* to 'slave'@'%' identified by 'slave';
flush privileges;
show master status;  -- 从结果可得到，File=mysql-bin.000001; Position=747
exit


-- 5(修改从服务器中mysql的master信息)
mysql -uroot -p135cylpsx
stop slave;
change master to master_host='192.168.2.103', master_user='slave', master_password='slave', master_log_file='mysql-bin.000002', master_log_pos=154;
-- 注意1：master_host='主服务器的ip'
-- 注意2：如果mysql数据库都在虚拟机中，虚拟机必须使用桥接模式，因为要保持ip在同一个网段，才能正常通讯
-- 注意3：master_log_file和master_log_pos的值都是在主服务器mysql中，通过show master status;查询得到的


-- 6(验证同步)
-- 从服务器中
mysql -uroot -p
show slave status \G;
-- 返回结果中
Slave_IO_Running: YES
Slave_SQL_Running: YES
-- 这两个变量的值都是yes时表示同步成功
-- 如果是No，原因有可能是以下情况：
-- master_host、master_log_file、master_log_pos、创建用户权限写错了
-- 如果以上信息确认无误，尝试用一下办法解决
stop slave;                                                      
SET GLOBAL SQL_SLAVE_SKIP_COUNTER=1;
start slave;                                                      
show slave status \G;

