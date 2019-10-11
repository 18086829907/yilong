show databases;
use mysql;
create user 'justin'@'%' identified by '135cylpsx4848@';
update user set host='%' where user='justin';
show tables;
desc user;
select host,user from user;
grant all on *.* to 'justin'@'%';
flush privileges;