#【day】Zookeeper在Linux系统安装
#打开vmware，创建虚拟机，加载centos镜像
#网络适配器说明
#   桥接
#       虚拟机相当于是一台真实机，光猫连接路由，路由连接两台电脑（真实机与虚拟机），一单拔掉外网网线，真虚两台主机不能使用局域网
#   NAT
#       真实机和虚拟机共享一个网卡，真机能上网，虚拟机就能上网
#   仅主机模式
#       虚拟机与真实际用一个网线连接，拔掉外网网线，真虚两台主机任然能使用局域网
#虚拟网络编辑器
#   点击更改设置
#       选择VMnet1-仅主机模式
#           修改子网IP的网段为25网段，即192.168.25.0
#               说明：正常应用开发时，任意网段都能用，之所以改为25是因为后期有一个DNS的服务，这个服务器本身有一个装好的镜像，这个镜像的网段就是25，如果不是25网段就无法与之连接
#           点击应用和确定
#点击虚拟机的网络适配器
#   选择仅主机
#       点击确定
#启动虚拟机，xshell连接
#   sudo su
#安装jdk
#   下载jdk
#       下载地址：http://www.oracle.com/technetwork/java/javase/downloads/index.html
#       点击Java SE 8u221的JDK Download
#           登录oricon
#               账户：417217170@qq.com
#               密码：135CYLpsx4848@
#       将jdk-8u221-linux-x64.tar.gz传入/root/software
#       复制一份jdk到/usr/local/src/作备份
#           cp jdk-8u221-linux-x64.tar.gz /usr/local/src/
#       创建java文件夹
#           mkdir /usr/java
#       复制一份jdk到/usr/java
#           cp jdk-8u221-linux-x64.tar.gz /usr/java/
#   解压JDK
#       cd /usr/java
#       tar -zxvf jdk-8u221-linux-x64.tar.gz
#       删除JDK安装包
#           rm -f jdk-8u221-linux-x64.tar.gz
#   配置JDK环境变量
#       vim /etc/profile
#           java environment
#           export JAVA_HOME=/usr/java/jdk1.8.0_221
#           export CLASSPATH=.:${JAVA_HOME}/jre/lib/rt.jar:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar
#           export PATH=$PATH:${JAVA_HOME}/bin
#   检验环境变量是否成功和生效
#       source /etc/profile    #重新生效环境变量文件
#       java -version
#安装zookeeper
#   下载地址：https://archive.apache.org/dist/zookeeper/
#   把apache-zookeeper-3.5.5.tar.gz的压缩包上传到/root/software

#   mkdir /root/software/zookeeper
#   mv apache-zookeeper-3.5.5.tar.gz /root/software/zookeeper
#   cd zookeeper
#   tar -zxvf apache-zookeeper-3.5.5.tar.gz
#   cd apache-zookeeper-3.5.5/
#   mkdir data
#   cd conf
#   mv zoo_sample.cfg zoo.cfg
#   vim zoo.cfg
#       将dataDir=/tmp/zookeeper
#       改为dataDir=/root/software/zookeeper/apache-zookeeper-3.5.5/data
#   cd ..
#   cd bin
#   ./zkServer.sh
#   /zkServer.sh start
#   /zkServer.sh status
#