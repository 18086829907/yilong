#【day】linux
#VMware
#   安装
#       见书签栏-博客教学-linux
#     新建虚拟机（虚拟电脑）
#       Ctrl + n
#           自定义(高级)
#               下一步
#               下一步
#                   稍后安装操作系统
#                       下一步
#                           客户机操作系统：Linux
#                           版本：CentOS 7 64位
#                               下一步
#                                   修改虚拟机名称：justin
#                                   修改虚拟机安装位置
#                                       下一步
#                                           处理器数量：2
#                                           每个处理器的内核数量：2
#                                               下一步
#                                                   点击最大推荐内存标尺
#                                                       下一步
#                                                           使用网络地址转换（NAT）
#                                                               LSI Logic
#                                                                   下一步
#                                                                       SCSI
#                                                                           下一步
#                                                                               创建新虚拟磁盘
#                                                                               将虚拟磁盘拆分成多个文件
#                                                                                   下一步
#                                                                                       选择linux系统安装路径
#                                                                                           下一步
#                                                                                               自定义硬件
#                                                                                                   声卡
#                                                                                                       移除
#                                                                                                   打印机
#                                                                                                       移除
#                                                                                                   关闭
#                                                                                                   完成
#    在虚拟机中安装linux系统
#        见书签栏-博客教学-linux-Centos7超详细过程
#    登录contos系统
#        localhost:$ root
#        Password:$ 135cylpsx4848@
#        $ systemctl restart network    #加载网卡
#        $ sudo yum install net-tools    #安装ifconfig工具包
#        $ ifconfig    #复制ens333中的inet的值，即ipv4 192.168.0.103
#    打开Xsheel新建会话并连接
#        名称：firstCentOs
#        主机：192.168.0.103
#        双击会话-点击确定-用户名：root-密码：135cylpsx4848@

#linux目录结构
#   / 跟目录
#   /etc 配置文件
#   /home 所有普通用户的家目录
#   /root root用户的跟目录
#   /var 系统一般运行时需要改变的数据
#   /usr 应用程序相关目录命令、函数库、共享包、内核源码
#   $ tree #以树状结构展示目录结构，安装：yum install tree
#三种网络模式
#   -bridged(桥接方式，默认使用vmnet0虚拟网卡)
#   -nat(网络地址转换模式，默认使用vmnet8虚拟网卡)
#   -host-noly(仅主机模式，默认使用vmnet1虚拟网卡)
#常用命令
#   帮助命令
#       $ man ls #帮助文档，查看命令的文档
#           说明：进入man之后点h，也能进入帮助文档
#       $ ls --help #进入命令的帮助文档，可查命令的参数
#   命令格式
#       command [-option] [path]
#       [] 可选
#       option 可以是多个
#   系统级别的命令
#       $ uname -a #显示系统及版本的所有信息
#       $ uname -r #显示内核版本
#       $ uname -m #显示计算机是多少位的系统
#       $ cat /etc/redhat-release #查看linux的版本名 --> CentOS Linux release 7.6.1810
#       $ hostname #查看主机名 --> localhost.localdomain
#       $ hostname justin #临时性修改主机名为justin
#       $ vi /etc/sysconfig/network #永久修改主机名
#       $ ifconfig #查看当前网卡的信息；说明：ipV4是ens33：intet下显示的ip
#       $ ifconfig -a #查看所有网卡的信息
#       $ ifconfig eth0 #查看指定网卡的信息
#       $ uptime #显示当前时间，系统使用时间，用户登录数，平均负载（不能超过）
#       $ free #显示当前磁盘及内存使用空间情况
#       $ cat /proc/cpuinfo #查看cpu使用情况的详细信息
#       $ top #启动任务管理器
#       $ last #查看历史登录信息
#       $ tty #当前登录模式pts/0图形界面登录 pts/3命令符模式登录
#       $ cal #显示日历
#       $ date #查看当前时间
#       $ date -s '2019-07-19' #设置当前的日期，设置之后date查看的时间就是从2019-07-19的00:00:00开始计时
#       $ date -s '19:10:10' #设置当前时间的时分秒
#       $ ps -ef #查看当前的所有进程
#       $ ps -aux #查看所有用户正在运行的进程
#       $ pstree -p #树的形式查看进程
#       $ ps -ef | grep mysql #查看当前指定应用所运行的进程，本质是模糊匹配CMD字段
#           管道：概念|前的命令的返回值传送给后面的命令做进一步处理
#       $ grep sshd /var/log/boot.log #在boot文件中过滤出包含sshd内容的代码
#       $ grep -r sshd /var/log #在某个目录下递归查看其中所有文件，是否包含sshd的代码，如果有则显示其文件名和所在文件中的行数
#           常用于报错之后，不知道报错代码在哪个文件中，便可用此方法搜索
#       $ top #动态查询进程的运行情况及消耗cpu情况和内存消耗情况
#           返回值
#               top：动态当前时间；动态运行时间；用户数；平均负载——1分钟的负载、5分钟的负载、15分钟的负载；
#               Tasks：进程总数；在运行进程数；休眠运行进程数；停止运行进程数；僵尸进程数；
#               cpu(s):按1就能展开查看所有的cpu核的消耗情况-用户所占cpu%；系统所占cpu%；闲置cpu%；硬件使用cpu%；软件使用cpu%，虚拟机使用cpu%
#               Mem：内存总数；已使用内存数；闲置内存数；
#               Swap：缓冲区总数；剩余总数；使用总数；缓存使用总数
#       $ sync #将数据有内存同步到硬盘中，执行了sync才能执行reboot
#       $ reboot #重新启动Linux操作系统
#       $ stutdown -h now #设定几小时后关机
#       $ kill -9 pid #结束指定的进程；示例：kill -9 2191
#   网络连接
#       $ systemctl restart network #重新加载网卡，在无界面linux系统中使用，使用后服务器才能上网，此时xshell才能连接该服务器
#       $ sudo yum install net-tools #重新安装ifconfig命令
#       $ jps #显示所有正在运行的java进程 （需要安装了jdk才能使用该命令）
#       $ ping 192.168.0.106 #查看ip是否通信。可ping网关、外网、宿主机ip
#   磁盘操作
#       $ df -h #显示磁盘分区信息
#       $ mkfs.ext4 /dev/sdb1 #格式化硬盘分区
#       $ fdisk -l #查看磁盘分区
#       $ fdisk /dev/sdb #硬盘分区
#       $ du -h /var/log/ #分别显示指定目录下所有文件使用磁盘空间的大小
#       $ du -h -s /var/log/ #显示指定目录下所有文件使用磁盘空间大小的总和
#       $ mount /dev/sr0 /mnt/cdrom #挂载光驱，将光驱的内容，挂载到/mnt/cdrom中。当服务器插入一个u盘或硬盘时不能直接识别，需要使用挂载才能读出里面的内容
#       $ mount -o remount rw/ #重新挂载，或者将根目录以读写方式重载
#       $ umount/media/umnt #卸载，怕掉u盘后执行
#       $ fscy -y /dev/sda1 #修复的可以是分区也可以是目录，最好在单用户模式下使用，参数-y表示遇到问题自动回复yes
#       $ pvdisplay #查看物理磁盘
#       $ lvdisplay #查看逻辑卷
#       $ lvextend #查看扩展卷
#   用户和组的操作
#       $ cat /etc/passwd #查看所有用户的用户信息
#       $ cat /etc/shadow #查看所有用户的密码（非明文）
#       $ ll /home/ #查看所有用户名，即home下面的目录名
#       $ useradd justin #创建justin为用户名的用户,可选参数-u 指定uid；-d 指定宿主目录；-s 指定使用shell；-e 指定用户过期时间；-g 指定基本组；-G指定附加组
#       $ cat /etc/group #查看用户的分组信息
#       $ gpasswd -a justin admin #将用户justin添加到用admin的组里
#       $ groups justin #查看用户在哪些组里
#       $ gpasswd -d justin admin #将用户justin从用户admin的组里删除
#       $ userdel -f -r justin #删除用户justin，-f强制删除，-r同时删除宿主目录，即删除/home/justin
#       $ id admin #查看用户admin的信息信息
#       $ groupadd admin01 #仅创建用户组，不创建用户
#       $ useradd -G justin01 justin #创建用户justin，并将用户justin加入justing01组中
#       $ passwd justin #更改密码，注意用户名可以省略，默认修改root用户的密码
#       $ userdel justin #指定删除用户
#       $ usermod -L justin #锁定用户，禁止其登录
#       $ su #切换到root用户
#       $ su justin #切换当前用户为justin
#       $ whoami #查看哪个用户在线
#   文件操作
#       $ cd /home/ #进入操作
#       $ pwd #查看当前工作目录
#       $ ll #查看当前目录中所有的目录名称
#       $ mkdir mia #在当前工作目录创建mia文件目录
#       $ mkdir ./deasy #在当前工作目录创建mia文件目录
#       $ mkdir -p ./coco/mia #递归创建文件目录，即连续创建文件目录
#       $ makdir ./test1 ./test2 #在当前目录创建两个文件目录test1和test2
#       $ touch ./file.txt #创建文件
#       $ vi file.log #在当前目录中创建文件，并进入编辑模式
#       $ echo '1234567890' >> ./file02 #创建file.txt文件并输入空到文件中
#       $ cat ./file02 #查看file02文件中的内容
#   列出文件和目录列表
#       $ ls #列表形式显示当前目录中的所有目录及文件
#       $ ls -a #显示出当前目录下的所有目录及文件，包括隐藏文件
#       $ ll -h #以人类能读懂的文件大小显示当前目录下所有文件
#   文本编辑器
#       $ vim file03 #进入file03的编辑模式，如果file03不存在，则无法保存写入内容
#       $ vi file04 #进入file04的编辑模式，如果file04不存在则创建
#       $ i #进入书写模式
#       $ ESC #退出书写模式
#       $ :q #退出
#       $ :w #保存
#       $ :wq #保存退出
#       $ :q！ #强制退出
#   文件内容查看
#       $ cat -n ./file01 #查看内容时显示行号
#       $ cat ./file01 #查看内容不显示行号
#   文件内容分段显示
#       $ head ./file01 #默认查看文件首10行
#       $ head -5 ./file01 #查看文件首5行
#       $ tail ./file01 #默认查看文件尾10行
#       $ tail -5 ./file01 #查看文件首5行
#       $ tail -f ./file01 #动态监听file01文件，file01中新添加了内容，可以被监听到
#       $ more ./file01 #百分比查看，不能回滚看
#       $ less ./file01 #能回滚看
#       $ vi ./file01 #进入编辑模式查看文件内容
#       $ vim ./file01 #进入编辑模式查看文件内容
#   复制文件
#       $ cp ./test1/file01 ./test2 #将test1下的file01文件复制到test2目录下
#   复制目录
#       $ cp -r ./test1 ./test2 #将test1目录复制到test2中
#   多个复制
#       $ cp -r ./mia/file02 ./test1 ./coco #将mia目录中的file02文件和test1目录复制到cooc目录下
#   剪切、重命名文件或目录
#       $ mv ./test2 ./test1 #将目录test2剪切到test1中
#       $ mv ./abc/a ./test1 #将目录abc下的a目录剪切到test1中
#       $ mv ./test1 ./test2 ./test3 #将目录test1和目录test2剪切到test3
#       $ mv ./test1/abc ./test2/bcd #将目录test1下面的abc文件剪切到test2目录中，并重命名为bcd文件
#       $ rename #批量重命名
#   重定向和追加
#       $ echo '123' >> /home/abc #在abc文件中的最后一行追加123
#       $ echo '123' > /home/abc #重写abc中的内容
#   屏幕打印
#       $ echo '123' #在屏幕中打印123
#   删除
#       $ rm ./file03 #删除file03文件
#       $ rm -r #删除目录
#       $ rm -f #强制删除
#       $ rm -rf ./mia #递归强制删除，不在询问是否要删除某个文件或目录
#   打包压缩、查找
#       $ tar -z #压缩
#       $ tar -c #打包
#       $ tar -x #解包
#       $ tar -f #必须要
#       $ tar -C #指定解包位置
#       $ tar -v #输出信息
#       $ tar -zcvf ./deasy/mia.tar ./mia/ #将mia目录以及mia目录下的所有文件及目录打包压缩到deasy目录下的mia.tar文件中
#       $ tar -zcvf ./text.tar ./text1 ./test2 #将多个文件进行打包压缩
#       $ tar -zcvf file.tar *.jpg #将所有的jpg文件打包压缩到file.tar
#       $ tar -zxvf ./deasy/mia.tar #将mia.tar解压解包mia目录以及mia目录下的所有文件
#       $ tar -zxvf ./deasy/mia.tar -C ./miaC #将deasy下的mia压缩文件，解压解包到指定miaC目录中
#   查找、检索、搜索
#       $ which reboot #查看reboot命令所在文件路径
#       $ whereis reboot #查看reboot命令所在文件路径已经其安装文件目录路径
#       $ updatedb #是locate命令有效
#       $ locate file1 #查找file1文件所在文件路径，查询更快，因为是通过数据库查询
#       $ find / -name file1 #在指定目录下查找指定条件——名字为file1的文件路径
#   清屏
#       $ clear#
#   设置别名
#       $ alias #查看所有别名
#       $ alias cle=clear #将clear命令设置cle临时别名
#       $ unalias cle #取消cle临时别名
#       $ vi ~/.bashrc #家目录下都有一个环境变量配置文件，针对当前用户
#           添加 alias cle='clear' #设置永久别名
#           ESC
#           :wq
#       $ source ~/.bashrc #保存bashrc所做的修改
#   特殊符号
#       $ cd ~ #进入当前用户的家目录
#       $ cd - #回退到上一次的所在位置
#       $ cd .. #回退到上一层
#       $ cd ../.. #回退到上两层
#       $ cd . #进入当前目录
#   防火墙
#       $ sudo yum install firewalld    #安装firewalld，当出现
#       $ sudo systemctl start firewalld
#       $ sudo systemctl enable firewalld
#       $ sudo systemctl status firewalld    #查看当前服务器防火墙状态
#       $ firewall-cmd --state #查看当前服务器防火墙状态
#       $ systemctl stop firewalld.service #临时关闭防火墙
#       $ systemctl start firewalld.service #开启防火墙
#       $ systemctl restart firewalld.service #重启防火墙
#       $ firewall-cmd --list-all #查看防火墙规则
#       $ firewall-cmd --permanent --list-ports #查看防火墙开启的端口
#       $ firewall-cmd --permanent --add-port=8080/tcp #防火墙开启8080端口
#       $ firewall-cmd --permanent --remove-port=8080/tcp #防火墙移除8080端口
#       $ firewall-cmd --reload #重启防火墙（）
#       参数说明
#           firewall-cmd是linux提供的操作firewall的一个工具
#           --permanent：表示设置为持久
#   普通用户设置root权限
#       $ su
#       $ visudo -f /etc/sudoers #进入sudoers的编辑模式
#           增加justin用户的sudo权限为all
#               在root ALL=(ALL) ALL下增加
#                 justin ALL=(ALL) ALL
#           设置justin用户的sudo权限免密
#               在%wheel ALL=(ALL) ALL下增加
#                 jusint ALL=(ALL) ALL
#           :wq #保存退出
#       $ su justin #切换到justin用户
#       $ sudo rm -rf ./test #justin用户用sudo权限删除属于root的文件目录
#具体知识点
#   常见目录介绍
#       /bin：存放常用命令，普通用户也可执行
#       /dev：存放设备文件
#       /boot：存放内容及引导系统程序文件
#       /home：普通用户主目录的默认存放位置
#       /lib：库文件存放目录
#       /tmp：存放临时文件
#       /usr：系统存放程序的目录
#   修改root密码
#       方法见书签栏/博客教学/linux/root密码修改
#   linux磁盘分区格式
#       概念：规定文件的存储读写方式
#       包括：ext4 ext3 ext2 vfat(fat32)
#   windows磁盘分区格式
#       包括：ntfs fat32(限制拷贝2g以上，如果需要拷贝2g以上，使用convert转换格式)
#   用户和组的操作
#       账户包括
#           超级用户：root uid=0
#           普通账户：      uid>=500
#           系统账户：      uid=1~499
#           保存账户信息的位置：/etc/passwd
#           保存账户密码信息的位置：/etc/shadow
#           root用户的家目录：/root
#           普通用户xxx的家目录：/home/xxx
#软件安装管理（安装应用程序）
#   二进制程序的安装
#       详见书签栏-博客教学-linux-linux系统下安装jdk
#       $ java -version #先执行以下java应用 参数为-version，如果安装jdk则报错，如果安装了jdk返回去版本号
#   Rpm 程序安装(后缀名为*.rpm)
#       rpm命令格式：rpm [选项] [文件1] [文件2]
#       rpm工具功能
#           查询
#               $ rpm -q telnet-server xinetd
#               $ rpm -qa | grep mysql #在所有搜索出来的应用文件和安装包文件中查询mysql信息
#               $ rpm -qi 软件名 #已安装
#               $ rpm -ql 软件名 #安装位置
#               $ rpm -qf 目录 #目录是由哪个安装包所创建的
#           安装
#               $ rpm -ivh nc-1.84-22.el6.x86_64.rpm
#           升级(自动卸载老版本，安装新版本)
#               $ rpm -Uvh nc-1.84-22.el6.x86_64.rpm
#           刷新
#               $ rpm -Fvh nc-1.84-22.el6.x86_64.rpm
#           卸载
#               $ rpm -e nc
#       #查询应用是否安装

#       #安装应用

#       #验证是否安装成功
#           $ rpm -Vp nc-1.84-22.el6.x86_64.rpm
#       #更新软件包
#
#       注意：rpm有非常强的包依赖问题，比如安装gcc之前就需要安装其他很多包
#           示例：$ rpm -ivh gcc-9.1.1-2.fc31.aarch64.rpm #使用包管理工具安装gcc应用
#               需要先安装
#                   lib64mpfr4-3.1.5-1.mga6.x89-64.rpm
#   Yum 在线安装(本质也是rpm)
#       从光盘安装
#           本地源
#               挂载光盘
#                   /mnt/cdrom #所有的安装文件都加载到了cdrom下
#                   注意：如果不是加载系统安装包需要createrepo
#                       示例
#                           $ mkdir /home/software
#                           将*.rpm放入这个目录下
#                           $ createrepo /home/software
#                           接着下面的命令配置指定software目录的yum配置文件
#               创建自定义yum文件
#                   $ cd /etc/yum.repos.d/ #系统默认网络源的存放位置
#                   $ mkdir bak
#                   $ cp *.repo bak/ #备份系统默认网络源
#                   $ rm -rf *.repo #删除系统默认网络源
#                   $ vim dvd.repo #创建自己的网络源
#                   [dvd] #申明名字
#                   name=CentOS7 #源的说明
#                   baseurl=file:///mnt/cdrom #源提取位置file是本地，网络是http、ftp
#                   enabled=1 #是否激活此源
#                   gpgcheck=0 #是否需要检查秘钥，0表示不检查，1表示检查，后面必须加上秘钥
#                   gpqkey=gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 #秘钥
#           命令格式：yum [选项] [指令] [软件包]
#               安装
#                   $
#                   $ yum clean all #清楚所有的缓存信息
#                   $ yum makecache all #重新生成缓存
#                   $ yum install bind #安装软件
#                   如果遇到Error: Package
#                       $ wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
#                       $ sed -i  's/$releasever/7/g' /etc/yum.repos.d/CentOS-Base.repo
#                       $ yum repolist
#                       $ yum install bind
#                   如果遇到yum繁忙
#                       在错误提示中找到PID进程号，使用kill -9 进程号即可
#               卸载
#                  $ yum remove bind
#   wget
#       功能：启动下载器，对下载包的链接发送get请求，下载的包存放在当下目录
#       原型：wget 下载链接
#       示例：$ wget http://nginx.org/download/nginx-1.12.1.tar.gz
#   源码安装
#   实战安装
#       anaconda
#           anaconda官网下载linux版本的anaconda3-2019.03-linux-x86-64.sh
#           通过xftp将anaconda....sh传到 /home/software目录中
#           $ cd /home/software
#           $ bash anaconda....sh
#           接着就是回车yes直到安装完成
#       pycharme
#           yum install virt-manager    #使pycharme图像化的工具
#           pycharme官网下载收费版的linux版,即pycharm-professional-2019.1.3.tar.gz
#           通过xftp将pycharm-professional-2019.1.3.tar.gz传到 /home/software目录中
#           $ tar -xf pycharm-professional-2019.1.3.tar.gz
#           解压后再当前目录就会出现dbs目录和pycharm-2019.1.3即安装成功
#           说明：linux打开方法 $ /usr/local/bin/charm 即可打开pycharm
#       pycharme破解
#           $ yum install java
#           通过xftp将jetbrains-agent.jar破解文件传到 /home/software/pycharm-2019.1.3/bin
#           $ vim /home/software/pycharm-2019.1.3/bin/pycharm64.vmoptions
#               在该文件的最后一行加入-javaagent:/home/software/pycharm-2019.1.3/bin/jetbrains-agent.jar
#           $ vim /home/software/pycharm-2019.1.3/bin/pycharm.vmoptions
#               在该文件的最后一行加入-javaagent:/home/software/pycharm-2019.1.3/bin/jetbrains-agent.jar
#           $ ./pycharm.sh    #打开可执行文件就打开pycharm图形窗口
#           同windows的欢迎窗口步骤相同，直到出现IntelliJ IDEA License Activation窗口
#               选择License server
#               点击同意即可
#       scrapyd
#           $ yum -y install gcc #因为安装scrapyd需要gcc库
#           $ pip install scrapyd
#
#常用软件包
#   安装telnet-server xinetd
#       说明：这两个软件安装到服务器，并开启相应服务，就能从客户端远程连接，连接到服务器
#       步骤
#           通过vmware将contos.ios加载到cd/dvd，并连接
#           $ mkdir /mnt/cdrom #新建cdrom文件目录
#           $ mount /dev/sr0 /mnt/cdrom #将sr0光驱挂载到cdrom
#           $ mount | grep sr0 #查看sr0的信息，查看是否成功挂载
#           $ cd /mnt/cdrom #进入cdrom目录
#           $ ls #大量的需要的服务安装包和应用安装包都存放于Packages目录下
#           $ cd Packages
#           $ ls telnet-*.rpm #查询telnet是否包含
#           $ rpm -ivh telnet-server-0.17-64.el7.x86_64.rpm xinetd-2.3.15-13.el7.x86_64.rpm #安装这两个软件
#           $ rpm -q telnet-server xinetd #查询这两个软件是否安装成功
#           $ systemctl start telnet.socket xinetd.service #启动这两个软件的服务
#           $ systemctl status telnet.socket xinetd.service #查询这两个软件的服务是否启动
#           $ systemctl status firewalld.service #查看防火墙启动状态
#           $ firewall-cmd --zone=public --add-port=23/tcp --permanent #让防火墙永久允许23号端口添加到公共区域
#           $ systemctl restart firewalld.service #重启防火墙
#           $ ifconfig #复制服务器的ip
#       使用
#           客户端远程登录服务端
#               在真实机启动telnet服务
#                   win+x
#                   应用和功能
#                   程序和功能
#                   启用和关闭windows功能
#                   程序功能
#                   勾选Telnet
#               开始--运行--cmd
#               Telnet 192.168.64.128
#常用快捷键
#   ctrl+r 搜索历史输入过的命令
#       说明：ctrl+r 所搜指令采用模糊匹配，比如输入m，则能匹配出历史输入过man ls这条命令
#   ctrl+c 终止当前操作
#   ctrl+z 退出当前操作
#   上键下键 浏览历史输入命令
#   tab 自动补全
#       模糊匹配文件名
#           不输入任何匹配字母
#               显示当前目录下的所有文件名
#                   示例：$ ll /home/TAB  -->  显示home下所有的文件名
#           输入一些匹配字母
#               匹配到唯一的文件名
#                   直接补全该文件名
#                       示例：ls /vTAB  -->  ls /var/
#               匹配到两个及以上文件名
#                   双击TAB，会列出所有模糊匹配到的文件名
#                       再自己选择需要的文件名
#                       示例：ls /sTABTAB  -->  ls /s 显示匹配到所有以s开头的所有文件名
#   vim中的快捷键
#       i
#       shift G  移动到最后一行
#       ESC

#【day】本地服务器
#   安装python3.6
#       $ sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
#       $ sudo yum update
#       $ sudo yum install -y pythou36u python36u-libs python36u-devel python36u-pip
#   安装pip
#       $ sudo easy_install-3.6 pip
#       $ pip install --upgrade pip
#   切换pip源
#       mkdir ~/.pip
#       vim  ~/.pip/pip.conf
#           [global]
#           index-url = http://mirrors.aliyun.com/pypi/simple
#           [install]
#           trusted-host=mirrors.aliyun.com
#   安装requests
#       $ pip3 install requests
#   安装selenium
#       $ pip3 install selenium
#   安装aiohttp
#       $ pip3 install aiohttp
#   安装lxml
#       $ pip3 install lxml
#   安装pyquery
#       $ pip3 install pyquery
#   安装mysql8.0
#       查看旧版本MySQL
#       rpm -qa | grep mysql
#       使用以下命令删除上一步查询出的所有文件
#       yum remove mysql-xxx-xxx
#       查询mysql的配置文件，并全部删除
#       find / -name mysql
#       rm -rf /var/lib/mysql
#       rm /etc/my.cnf
#       rm -rf /usr/lib/mysql
#       rm -rf /usr/share/mysql
#       删除完成后检查一下是否全部删除干净
#       在CentOS中默认安装有MariaDB，也要删除掉
#       查询
#       rpm -pa | grep mariadb
#       删除，如：
#       yum -y remove mariadb-libs.x86_64
#       开始安装mysql8.0.16
#       [root@localhost ~]# cd /usr/local/src/
#       [root@localhost src]# wget http://repo.mysql.com/mysql80-community-release-el7-3.noarch.rpm 
#       [root@localhost src]# rpm -ivh mysql80-community-release-el7-3.noarch.rpm 
#       [root@localhost src]#  yum install mysql-community-server
#       默认配置文件路径： 
#       配置文件：/etc/my.cnf 
#       日志文件：/var/log/var/log/mysqld.log 
#       服务启动脚本：/usr/lib/systemd/system/mysqld.service 
#       socket文件：/var/run/mysqld/mysqld.pid
#       过安装完成后，密码为随机密码，需要重置密码。
#       启动mysql服务
#       service mysqld restart
#       设置开机自启动
#       systemctl enable mysqld.service
#       重置密码
#       [root@localhost ~]# grep "password" /var/log/mysqld.log 
#       下图框中为初始的随机密码，复制粘贴登录数据库
#       输入初始密码即可登陆数据库，然后需要重新设置密码，至少包含大写，小写字母，数字和符号。
#       alter user 'root'@'localhost' identified by 'password';  填入自己要设置的密码
#       设置数据库登陆用户权限
#       use mysql;
#       先新建一个用户，root
#       create user 'root'@'%' identified by 'password';
#       再次赋权
#       grant all privileges on *.* to 'root'@'%' with grant option;
#       刷新权限
#       flush privileges;
#       这样就可使用Navicat 连接数据库了
#   安装MongoDB
#       $ sudo vi /etc/yum.repos.d/mongodb-org.repo
#       修改如下内容
#           [mongodb-org-3.4]
#           name=MongDB Repository
#           baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64
#           gpgcheck=1
#           enabled=1
#           gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc
#       yum安装
#           $ sudo yum install mongodb-org
#       启动MongoDB
#           $ sudo systemctl start mongod
#       停止和重新加载MongDB
#           $ sudo systemctl stop mongod
#           $ sudo systemctl reload mongod
#   安装redis
#       $ sudo yum install epel-release
#       $ sudo yum update
#       $ sudo yum -y install redis
#       $ sudo systemctl start redis
#       允许远程连接
#           $ vi /etc/redis.conf    #vi搜索技巧：在命令输入状态下的搜索命令——\需搜索字符串,示例\requirepass
#               注释 bind 127.0.0.1
#               将protected-mode yes 改为 protected-mode no
#               修改密码 requirepass 135cylpsx4848@
#               点击esc
#               $ :wq
#           $ sudo systemctl restart redis    #重启、启动reids-server
#   安装pymysql
#       pip3 install pymysql
#   安装pymongo
#       pip3 install pymongo
#   安装redis-py
#       pip3 install redis
#   安装redisdump
#       gem install redis-dump
#   安装flask
#       pip3 install flask
#   安装tornado
#       pip3 install tornado
#   安装mitmproxy
#       pip3 install mitmproxy
#   安装scrapy
#       sudo yum groupinstall -y development tools
#       sudo yum install -y epel-release libxslt-devel libxml2-devel openssl-devel
#       pip3 install Scrapy
#   安装docker
#       参考：https://blog.csdn.net/hylaking/article/details/87978819
#           #卸载旧版本
#              $ sudo yum remove docker  docker-common docker-selinux docker-engine
#           #安装需要的包
#              $ sudo yum install -y yum-utils device-mapper-persistent-data lvm2
#           #设置阿里yum源
#              $ sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
#           #查看仓谷中所有docker版本
#              $ yum list docker-ce --showduplicates | sort -r
#           #安装docker
#              $ sudo yum install docker-ce
#           #启动并加入开机启动
#              $ sudo systemctl start docker
#              $ sudo systemctl enable docker
#           #验证是否安装成功
#              $ docker version
#    安装splash容器并启动splash服务
#        $ sudo docker run -d -p 8050:8050 scrapinghub/splash
#    安装splash
#        $ pip3 install scrapy-splash
#    安装scrapy-redis
#        $ pip3 install scrapy-redis
#    安装scrapyd
#        $ pip3 install scrapyd
#        $ sudo mkdir /etc/scrapyd
#        $ sudo vi /etc/scrapyd/scrapyd.conf
#           [scrapyd]
#           eggs_dir=eggs
#           logs_di=logs
#           items_dir=
#           jobs_to_keep=5
#           dbs_dir=dbs
#           max_proc=0
#           max_proc_per_cpu=10
#           finished_to_keep=100
#           poll_interval=5.0
#           bind_address=0.0.0.0
#           http_port=6800
#           debug=off
#           runner=scrapyd.runner
#           application=scrapyd.app.application
#           launcher=scrapyd.launcher.Launcher
#           webroot=scrapyd.website.Root
#
#           [server]
#           schedule.json=scrapyd.webservice.Schedule
#           cancel.json=scrapyd.webservice.Cancel
#           addversion.json=scrapyd.webservice.AddVersion
#           listprojects.json=scrapyd.webservice.ListProjects
#           listversions.json=scrapyd.webservice.ListVersions
#           listspiders.json=scrapyd.webservice.ListSpiders
#           delproject.json=scrapyd.webservice.DeleteProject
#           delversion.json=scrapyd.webservice.DeleteVersion
#           listjobs.json=scrapyd.webservice.ListJobs
#           daemonstatus.json=scrapyd.webservice.DaemonStatus
#       后台运行
#           (scrapyd > /dev/null &)
#       配置日志
#           (scrapyd > ~/scrapyd.log &)
#       开放端口
#           firewall-cmd --permanent --add-port=6800/tcp #防火墙开启6800端口
#    安装Nginx
#       下载nginx安装包
#           cd /root/software
#           mkdir nginx_software && cd nginx_software
#           wget http://nginx.org/download/nginx-1.5.9.tar.gz
#           tar -zxvf nginx-1.5.9.tar.gz
#           rm -f nginx-1.5.9.tar.gz
#           cd nginx-1.5.9/
#       安装依赖库
#           yum -y install pcre-devel
#           yum -y install openssl openssl-devel
#           yum –y install gcc
#       安装nginx
#           ./configure --prefix=/usr/local/nginx
#           make install
#           cd /usr/local/nginx/sbin
#           ./nginx
#           systemctl stop firewalld.service    #关闭防火墙
#       使用nginx
#           http://IP地址
#       重新加载nginx
#           nginx -s reload
#   安装scrapyd-client
#       pip3 install scrapyd-client
#   使用scrapyd
#       curl http://localhost:6800/listprojects.json    #查看正在运行的scrapy项目
#   安装python-scrapyd-api
#       pip3 install python-scrapyd-api
#       python调用接口查询正在运行的scrapy项目
#           from scrapyd_api import ScrapydAPI
#           scrapyd=ScrapydAPI('http://localhost:6800')
#           print(scrapyd.list_projects())
#   安装scrapyrt
#       pip3 install scrapyrt
#       使用
#           在任何一个scrapy项目中运行如下命令启动HTTP服务
#               scrapyrt
#   安装Gerapy
#       pip3 install gerapy
#   安装github
#       yum install git
#       查看yum源仓库Git信息
#       yum info git
#       2.安装依赖库
#       [root@wugenqiang ~]# yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
#       [root@wugenqiang ~]# yum install gcc-c++ perl-ExtUtils-MakeMaker
#       3.如果原有的git版本过低，移除默认安装的旧版git
#       [root@wugenqiang ~]# git --version    ## 查看自带的版本git version 1.8.3.1
#       [root@wugenqiang ~]# yum remove git   ## 移除原来的版本
#       4.下载&安装
#       [root@wugenqiang ~]# cd /usr/src
#       [root@wugenqiang src]# wget https://www.kernel.org/pub/software/scm/git/git-2.18.0.tar.gz
#       5.解压
#       [root@wugenqiang ~]# tar xf git-2.18.0.tar.gz
#       6.配置编译安装
#       [root@wugenqiang ~]# cd /usr/src
#       [root@wugenqiang src]# ls
#       debug  git-2.18.0  kernels
#       [root@wugenqiang src]# cd git-2.18.0/
#       [root@wugenqiang git-2.18.0]#
#       [root@wugenqiang git-2.18.0]# make configure
#       [root@wugenqiang git-2.18.0]# ./configure --prefix=/usr/git ##配置目录
#       [root@wugenqiang git-2.18.0]# make profix=/usr/git
#       [root@wugenqiang git-2.18.0]# make install
#       7.加入环境变量
#       [root@wugenqiang ~]# echo "export PATH=$PATH:/usr/git/bin" >> /etc/profile
#       [root@wugenqiang ~]# source /etc/profile
#       8.检查版本
#       [root@wugenqiang ~]# git --version
#       git version 2.18.0
#       二、生成SSH密钥
#       [root@wugenqiang ~]# ssh-keygen -t rsa -C "417217170@qq.com"
#       三、添加密钥到GitHub
#       打开 Github，登录自己的账号后
#       点击自己的头像->settings->SSH And GPG Keys->New SSH key
#           Generating public/private rsa key pair.
#           Enter file in which to save the key (/root/.ssh/id_rsa):
#           Created directory '/root/.ssh'.
#           Enter passphrase (empty for no passphrase):
#           Enter same passphrase again:
#           Your identification has been saved in /root/.ssh/id_rsa.
#           Your public key has been saved in /root/.ssh/id_rsa.pub.
#           The key fingerprint is:
#           SHA256:gKJDgYDe+R+nV0aRhnYyomIDLBw2M24Xz9J0M1BGB5Y 417217170@qq.com
#           The key's randomart image is:
#           +---[RSA 2048]----+
#           |BB.. o+Xo.. .    |
#           |*+= *.+E+= =     |
#           |o++oo+o o = .    |
#           |oo.B.. .   .     |
#           |o . +   S .      |
#           | .   . . . o     |
#           |      . + o      |
#           |       o .       |
#           |        .        |
#           +----[SHA256]-----+
#       $ vim /root/.ssh/id_rsa.pub
#           ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+92uzFBG6K41j/7Pa/RH5jGfYb6vrGtjMOWYP4Z2wVWOmrpxYtLjstTWsnMWFoe5F5YUH+ZNVwnEkjTeqxvm8b2FeJwkYtqfyWIDBE3vLovp/Mh2laCe+UJyMqK2MG5WnXQ3iwbCwPFaHEep2E0vhHmXqADr9qB78VCNiuteSQGu1V5xtHpDtYiXmDRJKIRsJmNL1v6oJDKVvqCU+dTxmnzldwGYIPKvU6JKMdnHdc2/Iignhpm1wLRsJXPE4Ifahmxsf/ZZbsf2tPWQMV/x64AzhsCtb8LKEvN3+TB5hJVr063vQhN0e2KDADRnyDnDx4C4CgDsAmOh0OvTzne+f 417217170@qq.com
#       打开www.github.com/18086829907/yilong
#           点击右上角粉红色类似衣服的下拉图标
#               再点击settings
#                   在右侧导航栏中点击SSH and GPG keys
#                       点击New SSH key
#                           title 取一个名字
#                               说明：1、clone时本地仓库的目录名 2、www.github.com/用户名/title 即www.github.com/18086829907/justin
#                               key 粘贴公钥
#                               点击Add SSH key
#       四、centos里测试验证
#       [root @ wugenqiang ~]  # ssh git@github.com
#       五、git常用命令参考
#       git remote - v / --verbose #显示出详细的url地址名和对应的别名.
#       git clone < address > #复制代码库到本地；
#       git add < file > #添加文件到代码库中；
#       git rm < file > #删除代码库的文件；
#       git commit - m '更新内容' #提交更改，在修改了文件以后，使用这个命令提交修改。
#       git pull #从远程同步代码库到本地。
#       git push #推送代码到远程代码库。
#       git branch #查看当前分支。带 * 是当前分支。
#       git branch branchName：新建一个分支。
#       git branch -d branchName：删除一个分支。
#       git checkout branchName #切换到指定分支。
#       git log #查看提交记录（即历史的commit 记录）。
#       git status #当前修改的状态，是否修改了还没提交，或者那些文件未使用。
#       git reset < log > #恢复到历史版本。
#       六、Git实例
#       操作步骤：
#       1、远程仓库README.git为空，把本地代码上传到远程仓库
#       echo
#       "# Test" >> README.md
#       git init
#       git add README.md
#       git commit -m "first commit"
#       git remote add origin
#       git @ github.com: ** ** ** / README.git
#       git push -u origin master
#       2、更新本地代码到远程仓库
#       git add
#       README.md
#       git commit -m "first commit"
#       git push -u origin master
#       3、获取远程仓库中的代码到本地
#       git clone git @ github.com: ** ** * / README.git
#       4、从远程仓库同步代码更新本地代码
#       git pull origin master
#       echo "# bigdata" >> README.md
#       git init
#       git add README.md
#       git commit -m "first commit"
#       git remote add origin https: // github.com / wugenqiang / bigdata.git
#       git push -u origin master
#       具体演示：
#           mkdir ~/datagit
#           cd ~/datagit
#           git config --global http.postBuffer 524288000
#           git clone git@github.com:18086829907/yilong.git

#    docker的使用
#        容器使用
#            参考：https://blog.csdn.net/qq_35420123/article/details/81946941
#
#        安装纯contos系统容器
#            $ docker images    #查看本地存在的镜像文件
#            $ docker pull centos
#            $ docker run -i -t -d -p 20:20 -p 21:21 -p 80:80 -p 443:443 -p 888:888 -p 8888:8888 --privileged=true -v /root/docker1:/docker1 centos
#            $ docker ps    #查看容器id
#            $ docker exec -it 3ikdu293 /bin/bash     #3ikdu293是容器id
#            $ yum check-update -y && yum update -y && yum install initscripts screen wget -y    #安装宝塔必要的包
#            $ sudo yum install -y wget && wget -O install.sh http://download.bt.cn/install/install.sh && sh install.sh    #安装宝塔
#            $ curl http://127.0.0.1:8888/login
#                此时就能用window的浏览器访问虚拟机ip+端口访问页面了
#        安装anaconda
#            $ exit    #退出容器
#            $ cd /root/docker1
#                用Xftp将Anaconda安装文件传入
#            $ docker ps
#            $ docker exec -it 容器id /bin/bash
#            $ yum install -y bzip2
#            $ cd /docker1
#            $ bash Anaconda3-2019.03-Linux-x86_64.sh
#            $ exit
#            $ docker ps
#            $ docker exec -it 容器id /bin/bash
#        安装scrapy
#            $ conda install Scrapy    #进入容器中安装Scrapy
#        安装scrapy-redis
#            $ pip3 install scrapy-redis
#        安装Scrapyd
#            $ pip3 install scrapyd
#            修改配置文件中的bind_address,将其值设为0.0.0.0
#                $ find / -name scrapyd    # 能找到两个文件，一个是库文件，一个是执行程序目录
#                $ cd /root/anaconda3/lib/python3.7/site-packages/scrapyd
#                $ vi default_scrapyd.conf
#                    修改bind_address的值
#            后台运行scrapyd
#                (scrapyd > /dev/null $)
#                (scrapyd > ~/scrapyd.log $)    #设置输出日志目录
#       安装nginx
#            $ sudo docker pull nginx    #拉取nginx镜像
#            $ sudo docker images    #查看镜像
#            $ sudo docker run -d -p 80:80 nginx    #启动容器安装镜像
#            $ sudo docker ps#    #查看容器id
#            $ sudo docker exec -it 92 bash    #进入容器id为92的容器
#            $ cd /usr/share/nginx/html/    #进入index文件默认的文件夹
#            $ sudo docker #
#            $ sudo docker #
#            $ sudo docker #
#            $ sudo docker #
#       安装mysql
#            $ sudo docker pull mysql    #拉取mysql镜像
#            $ sudo docker images    #查看本地镜像
#            $ sudo docker run --name mysql -p 3306:3306 -v /mysql/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=135cylpsx4848@ -d mysql
#            $ sudo docker ps    #查看容器状态
#            $ sudo docker exec -it 4c45423d958a bash
#            $ mysql -u root -p 135cylpsx4848@
#            $ GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
#            $ FLUSH PRIVILEGES;
#            $ exit
#            $
#            $ docker stop 镜像id    #关闭mysql服务
#        容器的操作——删除容器
#            参考：https://www.cnblogs.com/linjiqin/p/8618635.html
#                $ sudo docker ps
#                $ sudo docker rm -f 容器id

#【day】亚马逊服务器
#   网址：https://aws.amazon.com/cn/
#   注册
#       创建AWS账户
#           账户名：18086829907
#           密码：135cylpsx4848@
#           邮箱：417217170@qq.com
#   登录控制器
#       导航栏我的账户
#           AWS管理控制台
#               登录邮箱：417217170@qq.com
#               密码：135cylpsx4848@
#       查询服务中搜索：EC2
#       启动实例
#       输入框搜索centos
#           点击AWS Marketplace
#               选择Centos7 (x86_64) - with Updates HVM
#       点击Continue
#       点击审核和启动
#       点击启动
#       选择创建新密钥对
#           输入名称：myKey
#           点击下载
#           将密钥保存到C:\Users\surface\.ssh文件夹下
#           启动实例
#       点击查看实例
#   远程链接服务器
#       安装xshell（百度云盘有）
#       打开xshell
#           新建会话
#               名称：美国服务器
#               主机：ec2-18-208-184-99.compute-1.amazonaws.com    #复制aws控制台中实例信息中的公有DNS(ipv4)
#               点击确定
#           双击会话
#               接受并保存
#               输入用户名：centos/ec2-user
#               单击确定
#               点击浏览
#                   点击用户密匙
#                   点击导入C:\Users\surface\.ssh目录下的*.pem文件（*代表自定义的名）
#                   点击打开
#                   点击密匙
#                   点击确定
#               点击确定
#           双击会话
#               输入用户名：centos
#               点击确定
#               点击确定
#   服务器系统的使用
#       切换用户root
#           $ sudo su root
#       安装web服务器
#           $ yum check-update -y && yum update -y && yum install initscripts screen wget -y    #安装宝塔必要的包
#           $ sudo yum install -y wget && wget -O install.sh http://download.bt.cn/install/install.sh && sh install.sh    #安装国内宝塔
#           $ yum install -y wget && wget -O install.sh http://128.1.164.196:5880/install/install_6.0.sh && sh install.sh    #安装美国宝塔
#           点击服务器实例栏中的安全组中的安全组名称
#               点击入站
#                  点击编辑
#                      点击添加规则
#                      类型：自定义TCP规则
#                      协议：TCP    #默认
#                      端口：8888、888、80、3306、443、22、21、20、39000-40000    #需要开放哪个端口就填哪个
#                      来源：任意位置
#                      描述：可选
#                      点击保存
#               点击出站
#                  点击编辑
#                      点击添加规则
#                      类型：自定义TCP规则
#                      协议：TCP    #默认
#                      端口：8888、888、80、3306、443、22、21、20、39000-40000    #需要开放哪个端口就填哪个
#                      来源：任意位置
#                      描述：可选
#                      点击保存
#           登录宝塔页面
#               浏览器中粘贴宝塔的url
#                   http://3.92.214.240:8888/7aaca1e1/    #在安装宝塔时自动生成
#               输入账号：batgpcyu    #在安装宝塔时自动生成
#               输入密码：5f8b23c0    #在安装宝塔时自动生成
#               登录之后
#                   提示安装服务器组件，选择推荐
#                   点击网站
#                       点击添加站点
#                             FTP账号资料
#                             用户：www_yilong_com
#                             密码：135cylpsx4848@
#                             数据库账号资料
#                             数据库名：yilong_com
#                             用户：yilong_com
#                             密码：135cylpsx4848@
#                   点击文件
#
#               软件管理
#                   安装Linux工具
#                       点击系统工具
#                           点击Linux工具设置
#                               点击Swap/虚拟内存
#                                   服务器内存  1G      2G      4G
#                                   Swap内存   1024MB  2048MB  4096MB
#                   安装php7
#                       点击运行环境
#                           点击安装php7
#                               安装一会后刷新
#                               点击设置
#                                   点击安装扩展
#                                       opcache
#                                       memcached
#                                       imagemagick
#                                       exif
#                                       fileinfo
#       安装python3
#           $ sudo yum groupinstall -y development tools
#           $ sudo yum install -y epel-release python36-devel  libxslt-devel libxml2-devel openssl-devel
#           $ sudo yum install -y python36 python36-setuptools
#           $ sudo easy_install-3.6 pip
#           安装库
#               $ pip install requests
#               $ pip install tornado
#               $ pip install redis
#       安装pip
#           $ yum install python-setuptools
#           $ easy_install pip
#           $ pip install shadowsocks
#       安装redis
#           $ sudo yum install epel-release
#           $ sudo yum update
#           $ sudo yum -y install redis
#           $ sudo systemctl start redis
#           $ vi /etc/redis.conf    #vi搜索技巧：在命令输入状态下的搜索命令——\需搜索字符串,示例\requirepass
#               注释 bind 127.0.0.1
#               将protected-mode yes 改为 protected-mode no
#               修改密码 requirepass 135cylpsx4848@
#               点击esc
#               $ :wq
#           $ sudo systemctl restart redis
#           允许外部访问6379端口
#               $ yum install iptables-services
#               $ iptables -I INPUT 1 -p tcp -m state --state NEW -m tcp --dport 6379 -j ACCEPT
#     　　　      $ service iptables save
#               $ systemctl enable iptables.service
#           链接远程redis数据库
#       安装mysql
#           $ sudo wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
#           $ sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
#           $ sudo yum install -y mysql mysql-server
#           $ sudo systemctl start mysqld    #启动mysql服务
#           $ sudo systemctl stop mysqld    #停止mysql服务
#           $ sudo systemctl restart mysqld    #重启mysql服务
#           $ mysql -uroot -p    #密码为空
#           use mysql;
#           修改密码方法二选一
#               update user set password_expired=password('135cylpsx4848@') where user='root';
#               set password for 'root'@'localhost' = password('135cylpsx4848@');
#           GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '135cylpsx4848@' WITH GRANT OPTION;
#           flush privileges;
#           exit
#           vi /etc/mysql/my.cnf
#               注释bind-address = 127.0.0.1
