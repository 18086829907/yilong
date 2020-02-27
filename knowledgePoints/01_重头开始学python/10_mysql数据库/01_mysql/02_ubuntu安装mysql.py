#安装mysql服务器
# sudo apt install mysql-server

#安装mysql客户端
# sudo apt install mysql-client

#卸载mysql服务器
# sudo apt remove mysql_server

#开启mysql服务
# sudo service mysql start

#停止mysql服务
# sudo service mysql stop

#重启mysql服务
# sudo service mysql restart

#查看进程中是否有mysql服务
# ps -aux | grep 'mysql'

#显示版本信息
# select version();

#配置
#   修改密码
#       sudo vim /etc/mysql/debian.cnf
#           password = 135cylpsx
#           password = 135cylpsx
#   配置远程可连接
#       # sudo vim /etc/mysql/mysql.conf.d/mysql.cnf +43
#           # bind = 127.0.0.1
#       # sudo mysql -uroot -p
#       mysql-> 135cylpsx
#       mysql-> show databases;
#       mysql-> use mysql;
#       mysql-> show tables;
#       mysql-> select user,host from user;
#       mysql-> update user set host='%' where user='root';
#       mysql-> flush privileges;

#安装Navicat
#    下载地址：https://www.navicat.com.cn/download/navicat-premium
#    下载的文件传到~/installed/中
#    $ cd ~/installed/
#    $ chmod +x navicat15-premium-cs.AppImage ./navicat15-premium-cs.AppImage  #添加执行权限
#    $ sudo ./navicat15-premium-cs.AppImage  # 执行文件
#Navicat破解方法
#    $ rm -rf ~/.config/navicat

#navicat连接mysql
#   连接-mysql
#       连接名：justin_mysql
#       主机：192.168.2.104  # 如果链接本机，使用127.0.0.1，不要使用localhost，因为localhost会有/var/lib/mysql/mysql.sock不存在的问题
#       端口：3306
#       用户名：root
#       密码：135cylpsx

#新建数据库
#   右键justin_mysql-新建数据库
#       常规
#           数据库名：justin_test
#           字符集：utf8  # 数据库字符设为utf8，在其中的表默认使用utf8
#           排序规则：utf8_general_ci

#新建表
#   justin_test-右键表-新建表
#       字段：id
#       类型：int
#       长度：0
#       不是null：勾选
#       键：点击（有钥匙），表示该字段为主键
#       默认值
#           自动递增：勾选
#           无符号：勾选
#   添加字段
#       字段：name
#       类型：varchar
#       长度：20
#       不是null：勾选
#   添加字段
#       字段：kongfu_id
#       类型：int
#       长度：
#       不是null：不勾选
#   保存
#       输入表名：heros

#进入表
#   justin_test-表-双击heros
#       对号：确认插入数据
#       加号：增加行
#       叉号：删除行
#       刷新：重新设计表字段时使用
#
#