#【day1】VMware
#   下载
#       https://www.cr173.com/soft/68480.html
#   许可
#       YG5H2-ANZ0H-M8ERY-TXZZZ-YKRV8
#       UG5J2-0ME12-M89WY-NPWXX-WQH88
#       UA5DR-2ZD4H-089FY-6YQ5T-YPRX6
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
#    在虚拟机中安装linux系统-centos6.60
#        见书签栏-博客教学-linux-Centos7超详细过程
#    打开Xsheel新建会话并连接
#        名称：firstCentOs
#        主机：192.168.0.103
#        双击会话-点击确定-用户名：root-密码：135cylpsx4848@

#【day2】linux目录结构
#   / 跟目录
#   /etc 存放所有的配置文件的文件夹（安装软件时，如果不指定配置文件的存放位置，那就会默认存放在此文件夹中）
#   /home 所有普通用户的家目录集合
#   /root root用户的家目录。存放媒体资源，相当于windows中的我的文档
#   /bin 存放二进制文件，但在Linux中的二进制文件是可以被执行的。类似windows下的.exe文件。（主要给非超级用户使用）
#   /sbin 功能同bin目录，也存放二进制文件，但必须拥有超级管理权限的用户才能执行里面的文件
#   /var 存放着Linux下的一些日志文件，在实际开发的时候有一些公司也习惯把Apache或者nginx的站点目录也会放到这个目录中。即/var/www
#   /usr 存放用户自己安装的软件的安装目录，类似windows的c:/Program Files文件目录
#   /tmp 临时文件存放目录
#   /dev：外置设备存放目录
#   /boot：存放内容及引导系统程序文件
#   /lib：库文件存放目录
#   /usr：系统存放程序的目录
#   #tree #以树状结构展示目录结构，安装：yum install tree
#三种网络模式
#   -bridged(桥接方式，默认使用vmnet0虚拟网卡)
#   -nat(网络地址转换模式，默认使用vmnet8虚拟网卡)
#   -host-noly(仅主机模式，默认使用vmnet1虚拟网卡)
#远程登录（重点）
#   putty
#       Host Name（or IP address）
#           输入ip地址（需要连接的电脑的ip地址）
#               如何在linux中的centos6查询ip
#                   在终端中输入：ifconfig
#                       eth0(默认的本地连接网卡)
#                           inet addr：192.168.1.6 （可以连接的地址,注意：拔掉网线重启后ip地址会变化）
#                       lo（本地回环网卡，全称loop）
#                           inet addr：127.0.0.1
#               如何在linux中的centos7查询ip
#                   在终端中输入：ip addr
#       open
#           PuTTY Security Alert(安全警告弹出)
#               说明：第一次使用PuTTY连接服务器时会弹出，点击是即可
#           login as:root  #输入用户名
#           password:135cylpsx  #输入时不会显示，如果输入错误，就持续按住backspace，2s后再输入密码
#               ~：表示用户的家目录路径

#扩展知识（1）
#ctrl+c
#   功能：停止当前当前命令
#ctrl+a
#   功能：将光标切换到命令行最前面
#ctrl+e
#   功能：将光标切换到命令行最后面
#上键和下键
#   功能：切换历史命令
#tab
#   功能：用于补全文件名或文件夹名，连按tab，可以列出指定目录下特定字符开头的文件夹和文件
#复制
#   命令行中用鼠标框选需要复制的内容，就将其复制在剪贴板中了

#常用命令
#   命令行进入方式
#       桌面右键
#           在终端中打开命令行
#   命令行符号介绍
#       [root@localhost 桌面]#
#           root：当前登录的用户名
#           @：'在'
#           localhost：当前主机名称
#           桌面：当前工作目录
#           #/$：超级管理员/普通用户
#   简单命令
#       ls
#           语法：ls [参数][指定路径]
#           功能：没有指定路径，则列出当前目录下的所有文件名
#       ls -l
#           功能：以列表的形式列出指定路径下的文件夹和文件名
#       ls -la
#           功能：以列表的形式列出指定路径下的文件夹和文件名（包含隐藏文件-“.”开头的文件）
#       ls /var
#           功能：列出/var文件夹下的文件
#       ls 字符串*
#           功能：匹配指定目录下以特定字符串开头的文件和文件夹，*为通配符
#       clear
#           功能：清空当前屏幕中全部的命令（其实质是没有清空，只不过是顶到上面去了）
#       init
#           功能：用户Linux的运行模式的切换
#           语法：#init数字（数字的取值范围是0-6）
#           说明：不同数字的功能不同
#               #0 表示关机
#               #1 表示单用户模式
#               #2 表示多用户模式
#               #3 表示将Linux系统从桌面模式切换到命令行模式
#               #4 表示未被使用的模式
#               #5 表示将Linux系统从命令行模式切换到桌面模式
#               #6 表示重启
#       su
#           功能：切换用户（switch user）
#           语法：#su 需要切换到的用户
#           实例：#su root
#   目录切换命令
#       cd
#           功能：切换目录（change directory）
#           语法：#cd 需要切换到的路径（可以是相对路径，也可以是绝对路径）
#           实例：
#               cd /home/admin 绝对路径
#               cd ../home/admin 相对路径：相对于当前工作路径，即/root
#       pwd
#           功能：打印当前的工作路径（print working directory）
#           实例：#pwd
#   文件/文件夹的操作命令
#       文件的操作命令
#           创建
#               命令：touch
#               语法：#touch 文件的名字 文件名可以是一个完整的路径
#               说明：只写文件名，则在当前目录下创建文件，如果是完成路径，则在指定文件夹路径下创建文件
#               实例：
#                   #touch php50.txt
#                   #touch /php50.txt
#           复制
#               命令：cp（copy）
#               语法：#cp 需要复制的文件（可以是完整路径） 需要粘贴到的位置（可以是完整路径，注意必须最后要用文件名）
#               实例：
#                   #cp php50.txt /home/admin/php50.txt
#           移动
#               命令：mv（move）
#               语法：#mv 需要移动的文件 需要移动到的位置
#               实例：#mv /home/admin/php50.txt /home/php50.txt
#           删除
#               命令：rm（remove）
#               语法：#rm 需要删除的文件
#               说明：删除时会被提示是否删除
#               实例：#rm /root/php50.txt
#
#               命令：rm -f（force，强制）
#               语法：#rm -f 需要删除的文件
#               实例：rm -f /home/admin/php50.txt
#           重命名
#               命令：mv
#               语法：#mv 需要重命名的文件 新的名字
#               实例：#mv /php50.txt /50.txt
#       文件夹的操作命令
#           创建
#               命令1：mkdir（make directory）
#               语法：mkdir 需要创建的目录名（可以使路径也可以是名字，如果是路径就在指定路径下创建，如果是名字就在当前目录下创建）
#               实例1：mkdir ./php
#               实例2：mkdir php
#           复制
#               命令：cp（copy）
#               语法：#cp -r 需要复制的文件夹 复制到的地方 (-r表示递归，必须加上此参数，才能复制文件夹)
#               实例：#cp -r php /php
#           移动
#               命令：mv
#               语法：#mv 需要移动的目录 移动到的地方
#               实例：mv /php /home/admin/php
#           删除
#               命令：rm
#               语法：#rm -rf 需要删除的文件夹名称
#               实例：#rm -rf /home/admin/php (-r递归删除，-f强制不提示)
#           重命名
#               命令：mv
#               语法：#mv 需要重命名的文件夹 新的文件夹名称
#               实例：mv /home/admin/php/ /home/admin/php1
#   vim
#       介绍：vim是linux下一款编辑器软件，它的地位等同于windows下的notepad（记事本）。其功能上要比记事本要强很多倍
#       具体使用
#           准备工作
#               先将/etc/passwd复制到/root
#                   #cp /etc/passwd /root/passwd
#           打开文件
#               语法一：#vim 需要打开的文件名
#                   实例：#vim /root/passwd
#                       提示
#                           退出vim：:q
#               语法二：#vim +数字 需要打开的文字（打开文件并快速定位到数字指定的行数）
#                   实例：#vim +5 /root/passwd
#                       提示
#                           在vim中显示行号： :set nu
#               语法三：#vim +/字符串 需要打开的文件（打开文件后，高亮显示/后的字符串）
#                   实例：#vim +/login /root/passwd
#                       提示
#                           如果此时需要在搜索高亮结果中进行光标的快速跳转，可以按下键盘上的“n”（向下切换），或者“N”（向上切换）
#                           清除高亮显示：:nohl
#               特别注意（vim新建文件）
#                   以上三种打开方式，如果打开一个不存在的文件，则会新建此文件。往其中写入内容，退出时则会保存，反之不保存
#           vim的三种模式
#               命令模式（默认进入）
#                   进入末行模式：按下:
#                   进入编辑模式：按下i或a
#                   具体操作
#                       光标移动
#                           移至首行首位：gg
#                           移至末行首位：G
#                           移至指定行首位：数字gg（数字和g的间隔不要太长）
#                               实例：15gg
#                           向下移动指定行首位：数字下键
#                               实例：5下键（向下移动5行）
#                               注意：不要使用小键盘的数字
#                           向上移动指定行首位：数字上键
#                               实例：5上键（向上移动5行）
#                               注意：不要使用小键盘的数字
#                       删除
#                           删除当前行，下行补齐：dd
#                           删除当前行，下行不补齐：D
#                           删除光标及下的指定行：数字d
#                               实例：4d（删除光标所在行，以及下3行，不要用小键盘数字）
#                           特别说明：删除命令和剪切命令是一模一样的。删除后的内容会自动保存到剪贴板，可以用于粘贴
#                       复制
#                           复制当前行：yy
#                           复制多行：数字yy（数字包括当前行及以下）
#                           说明：复制完之后可以按p进行粘贴，
#                       粘贴
#                           p
#                           说明：粘贴时粘贴在光标所在行的下一行开始
#                       恢复撤销
#                           ctrl+r
#               末行模式（:）
#                   进入命令模式
#                       按1下esc：稍慢
#                       按2下esc：直接退出
#                       删除末行命令中的全部命令：直接退出
#                   具体操作
#                       保存
#                           :w
#                       另存
#                           :w 文件路径
#                       退出
#                           :q
#                       强制退出(不会保存已经修改了的文件)
#                           :q!
#                           :wq!
#                       保存退出
#                           :wq 无论文件内容是否修改，都会更新文件保存时的最后修改时间
#                           :x 实际开发中推荐使用，只有内容真的被修改，才会修改文件的最后修改时间
#                       查找（查找后，会高亮显示字符串，可以用n和N切换）
#                           /字符串
#                           实例：/login
#                       替换
#                           语法一：:s/需要替换的字符串/替换成的字符串
#                               功能：替换当前光标所在的行的第一处符合条件的字符串
#                           语法二：:s/需要替换的字符串/替换成的字符串/g      （g为global）
#                               功能：替换当前光标所在的行的所有符合条件的字符串
#                           语法三：:%s/需要替换的字符串/替换成的字符串
#                               功能：替换当前文档中所有行的第一个符合条件的字符串
#                           语法四：:%s/需要替换的字符串/替换成的字符串/g
#                               功能：替换当前文档中所有行的所有符合条件的字符串
#                       撤销
#                           语法一：:u
#                               功能：撤销一步
#                           语法二：:数字u
#                               功能：撤销多步
#                       加密
#                           语法：:X
#
#               编辑模式（i或a）
#                   进入命令模式：按下esc
#                   文档的编辑模式，无命令
#       vim扩展知识
#           默认显示行号
#               修改配置文件.vimrc
#                   地址：当前用户的家目录中(如果没有就自己创建)
#                       /root/.vimrc
#                       /home/admin/.vimrc
#                   创建文件
#                       #vim .vimrc
#                       i
#                           set nu
#                       esc
#                       :wq
#           别名机制
#               作用：给冗长的命令起别名，使用别名来调用原本命令的功能
#               修改配置文件：.bashrc
#               文件地址:
#                   /root/.bashrc
#                   /home/admin/.bashrc
#               具体操作
#                   #vim /root/bashrc
#                       alias clear='cls'     #alias设置别名   别名命令='原命令'
#                   :q
#                   重新登录才能生效
#                       方法一：切换用户
#                           #su admin
#                           #su root
#                       方法二：重新
#           异常关闭处理
#               说明：vim编辑一个文件，没有正常关闭，则在下一次打开此文件时会提示异常关闭
#               问题本质：vim打开一个文件时，会新建一个原文件名.swp的缓存文件，正常关闭会删除.swp文件，异常关闭不会删除.swp
#               解决办法
#                   手动删除源文件名.swp的文件：#rm /root/.bashrc.swp
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
#       $ su #        #切换到root用户
#       $ su justin   #切换当前用户为justin
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
#   重定向和追加
#       $ echo '123' >> /home/abc #在abc文件中的最后一行追加123
#       $ echo '123' > /home/abc #重写abc中的内容
#   屏幕打印
#       $ echo '123' #在屏幕中打印123
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

#【day】rpm软件管理
#简介：在linux中rpm其实有点类似于windows下的“xxx电脑管家”，其作用就是管理软件
#功能
#   查询软件安装情况
#       语法：rpm -qa [|grep]需要查询的关键词
#       参数解释
#           -q：query，查询
#           -a：all，全部
#           |：在php中称它为变量修饰器。在linux中称为管道
#           grep：表示从结果中进行过滤
#       实例：rpm -qa mysql
#   安装软件
#       语法：rpm -ivh 需要安装的软件完整名称
#       参数解释
#           -i：install，安装
#           -v：表示显示进度条
#           -h：表示进度条以“#”显示
#       查询软件的完整名字
#           条件
#               centos6.6的系统盘必须挂载（在虚拟机的CD/DVD中必须挂载-使用iso映像文件中有路径，且已连接要勾选。右键虚拟机名称，点击设置即可弹出挂载界面）
#               linux桌面版的桌面上必须有系统的cd盘符。如果没有，就去我的电脑中打开一下就有了
#           所有安装包的存放位置
#               linux桌面版：centos的光盘-packages
#                   在该文件夹的空白处右键点击在终端中打开
#               linux命令行：/media/CentOS_6.6_Final/Packages
#           在软件包目录中查询需要安装软件的全名称
#               #cd /media/CentOS_6.6_Final/Packages
#               #ls firefox*    列出以firefox开头的所有文件
#       实例：rpm -ivh firefox-31.1.0-5.el6.centos.i686.rpm
#   卸载软件
#       语法：rpm -e 需要卸载的软件名称（软件完整名称，即通过查询可得到）[--nodeps]
#       参数解释
#           -e：卸载
#           --nodeps：忽略依赖关系
#       实例：rpm -e firefix-31.1.0-5.el6.centos.i686 --nodeps

#【day】linux的运行模式
#模式
#   单用户：操作系统一般只能由一个人同时进行登录
#   多用户：操作系统可以允许由多个人同时进行登录
#   单任务：操作系统只能同时处理一个任务
#   多任务：操作系统可以同时处理多个任务
#扩展
#   windows属于单用户多任务系统
#       验证：cmd中输入mstsc（mstsc是windows系统的远程工具），通过远程登录其他电脑，其他电脑的用户会被强制下线
#   linux属于多用户多任务系统
#运行模式文件
#   文件名：inittab
#   位置：/etc/inittab
#   修改默认模式（开机后自动进入该运行模式）
#       打开文件：#vim /etc/inittab
#           26 id:3:initdefault    #修改id:后面的数字，即修改默认模式
#           :x
#           #init 6    #重启计算机后生效
#   模式介绍
#       0 关机模式，千万别设置为0，因为开机就会关机
#       1 单用户模式
#       2 多用户模式
#       3 命令行模式
#       4 未被定义的模式
#       5 桌面模式
#       6 重启模式，同关机模式，千万别设置为6，因为开机就重启

#【day】网卡设置（重点）
#千万注意：在实际开发的时候linux服务器/windows服务器的网卡不要随便的禁用，一担禁用，远程终端就会立刻断开，一担断开就会连接不上
#网卡配置文件的位置及网卡文件：/etc/sysconfig/network-scripts/
#查看网卡：#ifconfig
#每个网卡对应一个网卡配置文件
#   eth0网卡 -> ifcfg-eth0
#   lo网卡 -> ifcfg-lo
#打开配置文件
#   vim /etc/sysconfig/network-scripts/ifcfg-eth0
#       DEVICE设备
#       TYPE类型
#           Ethernet以太网
#       UUID设备ID
#       ONBOOT是否开机启动
#       BOOTPROTO自动模式
#           dhcp自动获取ip
#       HWADDR硬件地址
#禁用/启用网卡
#   禁用网卡：#ifdown 设备名称
#       实例：#ifdown eth0
#       注意：实际开发中，千万不要随意使用
#   启用网卡：#ifup 设备名称
#       实例：#ifup eth0

#【day】用户和用户组
#用户管理
#   添加
#       命令：useradd
#       语法：#useradd 用户名
#       实例：#useradd justin
#       验证：#/vim /etc/passwd   在最后一行能看到新添加的用户名
#           扩展：passwd中一行内容详解
#               16 dbus:x:81:81:System message bus:/:/sbin/nologin
#               行号 用户名:密码（占位符）:用户id:用户组id:注释或备注:用户对应的家目录:用户所对应的解释器位置（/sbin/nologin-无登录权限，/bin/bash-有登录权限）
#               说明：密码单独存储在/etc/shadow中
#   编辑
#       命令：usermod（user modify）
#       语法：#usermod 参数 需要修改的用户名
#       参数解释
#           -l：修改用户名
#               语法：#usermod -l 新用户名 需要被修改的用户名
#               实例：#usermod -l justin admin
#           -g：修改用户的用户组id
#               语法：#usermod -g 新的用户组id 需要被修改的用户名
#   删除
#       命令：userdel（user delete）
#       语法：#userdel 用户名
#       实例：#userdel justin
#   密码
#       命令：passwd
#       语法：#passwd 需要设置密码的用户名
#       实例：#passwd justin
#       注意：当设置密码过于简单，它会提示无效密码，但并不影响你继续验证密码，重新输入新密码（即简单的密码）后，密码设置成功。
#用户组
#   添加
#       命令：groupadd
#       语法：#groupadd 用户组名
#       实例：#gourpadd china
#       验证：#vim /etc/group
#           扩展：group中一行内容详解
#               5 haldaemon:x:68:haldaemon,jusin,admin:jfdsfa
#               行号 用户组名:密码的占位符（无意义，真无密码）:用户组id:用户组内的成员名称:备注
#   编辑
#       命令：groupmod（gourp modify）
#       语法：#groupmod 参数 用户组名
#       参数解释
#           -n：重命名
#               语法：#groupmod -n 新的用户组名 旧的用户组名
#               实例：#groupmod -n itcast china
#   删除
#       命令：groupdel
#       语法：#groupdel 需要删除的用户组名
#       注意：只能直接删除空的用户组，其中有用户名的需要先删除用户名，删除后再删用户组
#特别注意：在linux中，只有超级用户具有对用户/用户组的管理权限，其他用户一律禁止

#【day】权限设置（重点）
#查看当前用户对指定文件夹内所有文件及文件夹的使用权限
#   方法：ls -l 或 ls -la
#   实例：ls -l
#       -rwxrwx---
#       0123456789
#           0：档案类型
#               -：文件
#               d：文件夹
#           [1,2,3]:文件拥有者权限，即创建此文件的用户拥有的权限（u表示，user）
#               r：可读
#               w：可写
#               x：可执行
#               -：无此权限
#           [4,5,6]:文件所属群组的权限，即创建此文件的用户所在组的其他用户所拥有的权限（g表示，group）
#               r：可读
#               w：可写
#               x：可执行
#               -：无此权限
#           [7,8,9]：其他人对此文件的权限（o表示，other）
#设置权限
#    通过字符命令设置权限
#        命令：chmod（change modify）
#        语法：#chmod 权限组成信息 需要操作的对象（文件夹/文件）
#            注意：如果操作的对象是文件夹，需要加上-r参数，-r表示递归
#            参数解释
#                权限组成信息：
#                    第一种情况：对特定组成部分（u,g,o）单独设置某个权限
#                        添加权限
#                            语法：#chmod u+权限,g+权限,o+权限 需要操作的文件/文件夹
#                            实例：#chmod u+r,g+r,o+r /home/admin/text.txt
#                        删除权限
#                            语法：#chmod u-权限,g-权限,o-权限 需要操作的文件/文件夹
#                            实例：#chmod u-r,g-r,o-r /home/admin/text.txt
#                        设置权限
#                            语法：#chmod u=读写执,g=读写执,o=读写执 需要操作的文件/文件夹
#                            实例：#chmod u=rwx,g=-w-,o=--- /home/admin/text.txt
#                    第二种情况：对全部组成部分设置某个权限
#                        #chmod a+r 对全部组成部分添加可读权限
#                        #chmod a-r 对全部组成部分删除可读权限
#                        #chmod a=rwx 对全部组成部分设置可读可写可执行权限
#   通过数字设置权限
#       4表示读权限
#       2表示写权限
#       1表示执行权限
#       7表示全部权限
#       说明：把50.txt文件权限设置为所有者全部权限，同组用户读写权限，其他用户读权限
#           全部权限=读+写+执=4+2+1=7
#           读写权限=读+写=4+2=6
#           读权限=读=4
#           所以最终权限数字=764
#       实例：chmod 764 50.txt
#   友情提示
#       在以后实际工作中不要出现一个奇葩的权限
#           -wx  不要出现类似这样的权限，原因最基础的读权限未给，如果要写必须先读（打开）

#【day】实用扩展
#Linux下的>和>>
#   概念
#       >：覆盖写入
#       >>：追加写入
#   命令打印的结果保存到文件
#       语法：命令 [参数] > 文件（用户保存命令所返回的结果，目录中无此文件会自动新建）
#       实例1：ls -la > list.txt
#       实例2：ls -la >> list.txt
#Linux下的查找命令
#   语法：#find 查找路径 -name 查找的关键词
#   实例：#find / -name httpd.conf    全盘查找httpd.conf
#Linux下的手册man（Manual）
#   功能：查看某个命令的详细用法
#   语法：#man 命令名称
#   实例：#man find
#   退出手册：q

#【day】LAMP编程之linux
#ssh协议
#   常见协议：http/https、ftp、tcp/ip、tcp/upd等
#   常见端口：80、3306、21、11211、443等
#   说明
#       ssh协议的端口是22
#       ssh最典型的应用是可以让用户通过终端远程连接Linux服务器
#       在linux中ssh协议是一个守护进程，名字叫sshd
#       是进程就可以被开启/关闭/重启
#           service 服务名称 start
#           service 服务名称 stop    #实际开发中，不要随意关闭，否则无法连接远程服务器
#           service 服务名称 restart
#利用ssh工具实现跨平台传输文件
#   工具：pscp.exe
#       说明
#           它是一个命令行工具，需要在cmd中执行。
#           cmd中输入文件的全局路径+文件名执行
#           为了方便使用，可以将pscp.exe的路径加入到环境变量中
#               环境变量的path中添加文件所在目录路径即可，不需要添加文件名
#       cmd中使用pscp
#           windows中的文件传到linux中
#               语法：pscp windows中的文件路径 用户名@主机地址:文件的路径
#               实例：pscp C:\Users\Administrator\Desktop\1.txt root@192.168.0.110:/root/1.txt
#           linux中的文件传到windows中（仍然在cmd中操作）
#               语法：pscp 用户名@主机地址:文件路径 windows中的文件路径
#               实例：pscp root@192.168.0.110:/root/1.txt C:\Users\Administrator\Desktop\1.txt
#           传送指定文件夹下的所有文件
#               实例：pscp D:\softwear\* root@192.168.0.110:/root/softwear
#                   注意传输时，必须存在指定目录
#   工具：FileZilla
#       说明
#           它是一个界面化的传输工具
#       使用
#           填入ip地址，用户名，密码，22端口
#           点击快速链接，就可以拖动文件进行传输
#光盘挂载
#   说明：本质是将光盘设备(/dev/sr0)在/mnt/dvd中创建一个快捷方式，创建之后就才能使用光盘中的内容
#   首先：需要确保光盘已经放入了虚拟机的光驱中（虚拟机名称-右键-设置-cd/dvd）
#   命令：mount
#       语法：#mount [参数] 设备名称 挂载位置
#       参数解释
#           设备名称：通过lsblk命令（list block devices）来获取
#               实例：#lsblk
#                   sr0 11:0 1 4.3G 0 rom MOUNTPOINT为空（挂载点路径为空）   #列出的文件树中最接近iso文件大小的是sr0，而sr0只是文件名称
#                       注意：lsblk列出的设备都位于/dev目录中，因此设备的完整路径为/dev/sr0
#       实例：#mount /dev/sr0 /mnt/dvd (dvd必须手动先创建)
#           提示以下信息表示成功：mount: block device /dev/sr0 is write-protected（写保护）, mounting read-only（只读）
#               此时即可进入/mnt/dvd/Packages/中使用安装包了

#【day】LAMP安装
#安装步骤
#   关闭防火墙（因为它会封杀要用的端口，比如80端口）
#       防火墙在linux中的服务文件名称为iptables
#           它是服务就有开启/关闭/重启等操作进程的命令
#               语法：service 服务名 start/stop/restart
#               实例
#                   #service iptables start
#                   #service iptables stop
#                   #service iptables restart
#   卸载防火墙
#       查询软件名称
#           #rpm -qa iptalbes
#       卸载软件（卸载原因：如果不卸载，重启后，仍然会启动防火墙，防火墙封杀端口）
#           #rpm -e iptables-1.4.7-14.el6.x86_64
#               error：Failed depandencies:...    #需要忽略包依赖关系
#                   解决办法
#                       #rpm -e iptables-1.4.7-14.el6.x86_64 --nodeps （--nodeps，忽略依赖关系）
#   将安装文件通过工具传输到linux中
#   解压压缩包（说明）
#       linux中的压缩格式
#           gz
#               解压命令：tar
#                   语法：tar -zxvf 需要解压的文件
#           bz2
#               解压命令：tar
#                   语法：tar -jxvf 需要解压的文件
#   安装zlib压缩库
#       #cd /root/installed/lamp
#       #tar -zxvf zlib-1.2.5.tar.gz
#       #cd zlib-1.2.5
#       #ls
#           说明：其中大部分文件时.c和.h说明文件是c语言开发，因此这里需要gcc开发工具（在安装centos的时候，一定记得勾选开发者工具）
#       #./configure    #它是绿色文件，是一个可执行的文件。作用是对当前的程序安装进行配置，等待配置成功
#       #make && make install     #编译与安装（&&表示先执行完前面的命令再执行后面的命令。编译和安装可以单独写入，即#make #make install）
#   安装apache
#       #rpm -qa httpd     #查看是否有安装的apache
#       #rpm -e httpd-2.2.15-39.el6.centos.x86_64 --nodeps     #删除默认安装的apache并忽略依赖关系
#       #cd /root/installed/lamp
#       #tar -jxvf httpd-2.2.19.tar.bz2
#       #cd httpd-2.2.19
#       #ls
#       #./configure --prefix=/usr/local/http2 --enable-modules=all --enable-mods-shared=all --sysconfdir=/etc/httpd --enable-so
#           参数解释
#               --prefix
#                   功能：指定软件的安装目录
#                   语法：--prefix=目录
#                   说明：如果目录不存在，则会自动创建
#               --enable-modules
#                   功能：指定加载的模块
#                       参数解释：all表示加载全部模块
#               --enable-mods-shared
#                   功能：使模块以静态共享的方式进行安装
#               --sysconfdir
#                   功能：指定软件的配置文件的存放位置
#                   语法：--sysconfdir=目录
#                   说明：目录如果不存在，则自动生产
#               --enable-so
#                   功能：？
#       #make && make install   #编译和安装
#       #vim +148 /etc/httpd/httpd.conf    #配置apache文件
#           i
#           去掉148行的#号,即将这行（#ServerName www.example.com:80）的#号去掉
#           :x
#       #/usr/local/http2/bin/apachectl start    #启动apache
#           扩展：apachectl是可执行文件，它有开启/关闭/重启命令
#               ./apachectl start
#               ./apachectl stop
#               ./apachectl restart
#       #ifconfig
#           此时就能在windows中的浏览器访问linux的ip地址
#               It works（浏览器显示此内容）
#                   请求头中Server: Apache/2.2.19 (Unix) DAV/2
#   安装libxml2
#       #cd /root/installed/lamp
#       #tar -zxvf ./libxml2-2.7.2.tar.gz
#       #cd libxml2-2.7.2
#       #./configure --prefix=/usr/local/libxml2 --without-zlib
#           参数解释
#               --prefix    #指定安装路径
#               --without-zlib     #不需要安装zlib
#       #make && make install
#   安装jpeg8
#       #cd /root/installed/lamp
#       #tar -zxvf jpegsrc.v8b.tar.gz
#       #cd jpeg-8b/
#       #./configure --prefix=/usr/local/jpeg --enable-shared --enable-static
#       #make && make install
#   安装libpng
#       #cd /root/installed/lamp
#       #tar -zxvf libpng-1.4.3.tar.gz
#       #cd libpng-1.4.3
#       #./configure
#       #make && make install
#   安装freetype（字体库）
#       #cd /root/installed/lamp
#       #tar -zxvf freetype-2.4.1.tar.gz
#       #cd freetype-2.4.1
#       #./configure --prefix=/usr/local/freetype
#       #make && make install
#   安装GD库(处理图片的扩展)
#       #cd /root/installed/lamp
#       #tar -zxvf gd-2.0.35.tar.gz
#       #cd gd-2.0.35
#       #./configure --prefix=/usr/local/gd --with-jpeg=/usr/local/jpeg --with-png --with-zlib --with-freetype=/usr/local/freetype
#           参数解释
#               --with-jpeg    需要jpeg库
#       #make && make install
#   安装openssl（加密套件，用于https协议）
#       #cd /root/installed/lamp/
#       #tar -zxvf openssl-1.0.1t.tar.gz     tar -zxvf openssl-1.1.1d.tar.gz
#       #cd openssl-1.0.1t     cd openssl-1.1.1d
#       #./config --prefix=/usr/local/openssl
#       #make && make install
#   安装php
#       #cd /root/installed/lamp/
#       #tar -jxvf php-5.3.6.tar.bz2
#       #cd php-5.3.6
#       #./configure --prefix=/usr/local/php --with-apxs2=/usr/local/http2/bin/apxs --with-mysql=mysqlnd --with-pdo-mysql=mysqlnd --with-mysqli=mysqlnd --with-freetype-dir=/usr/local/freetype --with-gd=/usr/local/gd --with-zlib --with-libxml-dir=/usr/local/libxml2 --with-jpeg-dir=/usr/local/jpeg --with-png-dir --enable-mbstring=all --enable-mbregex --enable-shared --with-openssl-dir=/usr/local/openssl --with-openssl
#           参数解释
#               --with-apxs2    #指定apache下的一个文件目录
#               --with-mysql    #开启一个mysql的扩展
#       #make && make install
#   安装cmake（它是新款的c语言编译器，因为在mysql5.5之后，只支持cmake）
#       #cd /root/installed/lamp/
#       #tar -zxvf cmake-3.6.0-rc1.tar.gz
#       #cd cmake-3.6.0-rc1
#       #./bootstrap
#       #gmake && gmake install



#   提示：
#       如果在安装上面软件时出错
#           删除目录
#               第一个：通过tar命令解压的目录
#               第二个：使用--preifx指定的目录
#           在从解压这个软件包开始重新安装
#扩展
#   升级全部软件
#       #yum -y update







#软件安装管理（安装应用程序）
#   二进制程序的安装
#       详见书签栏-博客教学-linux-linux系统下安装jdk
#       $ java -version #先执行以下java应用 参数为-version，如果安装jdk则报错，如果安装了jdk返回去版本号
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
#   安装selenium
#       pip3 install selenium
#   安装chrome
#       cd /root/software
#       wget https://extras.getpagespeed.com/redhat/7/x86_64/RPMS/google-chrome-stable_current_x86_64.rpm
#       sudo yum localinstall google-chrome-stable_current_x86_64.rpm
#       /usr/bin/google-chrome-stable --no-sandbox    #临时允许浏览器以图形界面打开
#   卸载chrome
#       运行 yum remove google-chrome然后以Tab补全所有整个命令，再加上-y参数（我的电脑上面的命令为：yum remove google-chrome-stable.x86_64 -y），卸载Chrome
#   安装chromedriver
#       $ wget https://chromedriver.storage.googleapis.com/77.0.3865.10/chromedriver_linux64.zip
#       $ unzip chromedriver_linux64.zip
#       $ mv chromedriver /usr/bin/
#       $ chromedriver
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
#              $ sudo systemctl restart docker    #重启docker服务
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
#           mkdir /root/dataGit
#           cd /root/dataGit
#           git config --global http.postBuffer 524288000
#           git clone git@github.com:18086829907/yilong.git
#           cd /root/dataGit
#           git checkout yilong
#           cd /root/dataGit/yilong/first_project/练习/scrapyTest/jdCrawl/jdCrawl
#           python3 run.py
#           说明：只要正在/root/dataGit中任意位置都能使用git push origin yilong
#   安装pycharme
#       yum install virt-manager    #使pycharme图像化的工具
#           pycharme官网下载收费版的linux版,即pycharm-professional-2019.1.3.tar.gz
#           通过xftp将pycharm-professional-2019.1.3.tar.gz传到 /root/software目录中
#           $ tar -xf pycharm-professional-2019.1.3.tar.gz
#           解压后再当前目录就会出现dbs目录和pycharm-2019.1.3即安装成功
#           说明：linux打开方法 $ cd /root/software/pycharme-3./bin/pycharme.sh 即可打开pycharm
#       pycharme破解
#           $ yum install java
#           通过xftp将jetbrains-agent.jar破解文件传到 /home/software/pycharm-2019.1.3/bin
#           $ vim /root/software/pycharm-2019.1.3/bin/pycharm64.vmoptions
#               在该文件的最后一行加入 -javaagent:/root/software/pycharm-2019.1.3/bin/jetbrains-agent.jar
#           $ vim /root/software/pycharm-2019.1.3/bin/pycharm.vmoptions
#               在该文件的最后一行加入 -javaagent:/root/software/pycharm-2019.1.3/bin/jetbrains-agent.jar
#           $ ./pycharm.sh    #打开可执行文件就打开pycharm图形窗口
#           同windows的欢迎窗口步骤相同，直到出现IntelliJ IDEA License Activation窗口
#               选择License server
#               点击同意即可
#   启动爬虫程序
#       cd /root/dataGit/yilong/first_project/练习/scrapyTest/jdCrawl/jdCrawl/spiders
#       python3 run.py
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
#           $ sudo yum install -y wget && wget -O install.sh http://128.1.164.196:5880/install/install_6.0.sh && sh install.sh    #安装美国宝塔
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
#   安装python3.7
#       $ sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
#       $ sudo yum update
#       $ sudo yum install -y pythou36u python37u-libs python37u-devel python37u-pip
#   安装pip
#       $ sudo easy_install-3.7 pip
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
#   安装mysql5.5
#       $ sudo wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
#       $ sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
#       $ sudo yum install -y mysql mysql-server
#       $ sudo systemctl start mysqld    #启动mysql服务
#       $ sudo systemctl stop mysqld    #停止mysql服务
#       $ sudo systemctl restart mysqld    #重启mysql服务
#       $ mysql -uroot -p    #密码为空
#       use mysql;
#       修改密码方法二选一
#           update user set password_expired=password('135cylpsx4848@') where user='root';
#           set password for 'root'@'localhost' = password('135cylpsx4848@');
#       GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '135cylpsx4848@' WITH GRANT OPTION;
#       flush privileges;
#       exit
#       vi /etc/mysql/my.cnf
#           注释bind-address = 127.0.0.1
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
#           允许外部访问6379端口
#               $ yum install iptables-services
#               $ iptables -I INPUT 1 -p tcp -m state --state NEW -m tcp --dport 6379 -j ACCEPT
#     　　　      $ service iptables save
#               $ systemctl enable iptables.service
#           链接远程redis数据库
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
#              $ sudo systemctl restart docker    #重启docker服务
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
#           mkdir /root/dataGit
#           cd /root/dataGit
#           git config --global http.postBuffer 524288000
#           git clone git@github.com:18086829907/yilong.git
#           cd /root/dataGit
#           git checkout yilong
#           cd /root/dataGit/yilong/first_project/练习/scrapyTest/jdCrawl/jdCrawl
#           python3 run.py
#           说明：只要正在/root/dataGit中任意位置都能使用git push origin yilong
#   安装pycharme
#       yum install virt-manager    #使pycharme图像化的工具
#           pycharme官网下载收费版的linux版,即pycharm-professional-2019.1.3.tar.gz
#           通过xftp将pycharm-professional-2019.1.3.tar.gz传到 /root/software目录中
#           $ tar -xf pycharm-professional-2019.1.3.tar.gz
#           解压后再当前目录就会出现dbs目录和pycharm-2019.1.3即安装成功
#           说明：linux打开方法 $ cd /root/software/pycharme-3./bin/pycharme.sh 即可打开pycharm
#       pycharme破解
#           $ yum install java
#           通过xftp将jetbrains-agent.jar破解文件传到 /home/software/pycharm-2019.1.3/bin
#           $ vim /root/software/pycharm-2019.1.3/bin/pycharm64.vmoptions
#               在该文件的最后一行加入 -javaagent:/root/software/pycharm-2019.1.3/bin/jetbrains-agent.jar
#           $ vim /root/software/pycharm-2019.1.3/bin/pycharm.vmoptions
#               在该文件的最后一行加入 -javaagent:/root/software/pycharm-2019.1.3/bin/jetbrains-agent.jar
#           $ ./pycharm.sh    #打开可执行文件就打开pycharm图形窗口
#           同windows的欢迎窗口步骤相同，直到出现IntelliJ IDEA License Activation窗口
#               选择License server
#               点击同意即可