#表操作
#   查看当前数据库中所有表
#       show tables;

#   创建表
#       格式：create table 表名(列 类型 属性);
#       示例1
#       create table student(
#           id int unsigned auto_increment primary key not null,
#           name varchar(20) not null,
#           age tinyint unsigned default 0,
#           height decimal(5,2)
#           gender enum('男','女', '中性','保密') default '保密',
#           cls_id int unsigned,
#           address varchar(20),
#           isDelete bit default 0
#       );
#       示例2
#       create table classes(
#           id int unsigned not null auto_increment primary key,
#           name varchar(30)
#       )
#       说明：自增长——auto_increment 主键——primary key 非空——not null
#   查看表结构(查看表字段)
#       格式：desc 表名;
#       示例：desc student;
#   修改表结构
#       添加字段
#           格式：alter table 表名 add 列名 类型;
#           示例：alter table student add isDelete bit not null default 0;
#       修改字段-重命名版
#           格式：alter table 表名 change 原列名 新列名 类型及约束;
#           示例：alter table student change birthday birth datetime not null;
#       修改字段-不重命名版
#           格式：alter table 表名 modify 列名 类型及约束;
#           示例：alter table student modify birth date not null;
#       删除字段
#           格式：alter table 表名 drop 列名 类型;
#           示例：alter table student drop isDelete;
#   删除表
#       格式：drop table 表名;
#       示例：drop table production;
#   查看建表语句
#       格式：show create table 表名;
#       示例：show create table student;
#   表重命名
#       格式：rename table 原表明 to 新表名;
#       示例：rename table student to newStudent;
