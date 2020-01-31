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
#   /opt：安装额外软件的目录，安装到根目录下，其他用户才能使用此软件

#三种网络模式
#   -bridged(桥接方式，默认使用vmnet0虚拟网卡)
#   -nat(网络地址转换模式，默认使用vmnet8虚拟网卡)
#   -host-noly(仅主机模式，默认使用vmnet1虚拟网卡)

#远程登录（重点）
#   使用ssh实现远程登录
#       说明：ssh在linux、mac中都是自动安装，只有windows需要安装一个ssh协议的软件
#   ssh的优点
#       传输的数据会被加密和压缩，防止信息泄露和提高传输速度
#   安装软件
#       putty
#           Host Name（or IP address）
#               输入ip地址（需要连接的电脑的ip地址）
#                   如何在linux中的centos6查询ip
#                       在终端中输入：ifconfig
#                           eth0(默认的本地连接网卡)
#                               inet addr：192.168.1.6 （可以连接的地址,注意：拔掉网线重启后ip地址会变化）
#                           lo（本地回环网卡，全称loop，用于本机中不同软件之间的通讯）
#                               inet addr：127.0.0.1
#                   如何在linux中的centos7查询ip
#                       在终端中输入：ip addr
#           open
#               PuTTY Security Alert(安全警告弹出)
#                   说明：第一次使用PuTTY连接服务器时会弹出，点击是即可
#               login as:root  #输入用户名
#               password:135cylpsx  #输入时不会显示，如果输入错误，就持续按住backspace，2s后再输入密码
#                   ~：表示用户的家目录路径
#       xshell
#           下载地址：https://www.xshellcn.com/
#           注意：当安装到安装类型时，一定要选择免费为家庭/学校这个选项，因为1免费，2功能没差别
#           汉化：Tools-language-chinese simplified,勾选restart the program now

#【day】扩展知识
#常见问题：vmware全屏显示ubuntu18的问题；windows和ubuntu18互相粘贴复制问题
#   进入ubuntu的命令行窗口
#       sudo apt autoremove open-vm-tools
#       sudo apt install open-vm-tools
#       sudo apt install open-vm-tools-desktop
#   设置ubuntu18的显示分辨率
#       点击右上角的三角形下拉按钮
#           点击设置
#               在弹出窗口的导航栏中找到设置并点击（它位于导航栏的偏下面的位置）
#                   点击显示即可进行分辨率的设置
#   重启ubuntu后，就可以与window互相复制粘贴了
#取消自动锁屏
#   点击三角按钮
#       点击扳手（设置）
#           点击隐私
#               点击锁屏
#                   关闭自动锁屏功能
#常用组合键
#   ctrl+c
#       功能：停止当前当前命令
#   ctrl+a
#       功能：将光标切换到命令行最前面
#   ctrl+e
#       功能：将光标切换到命令行最后面
#   上键和下键
#       功能：切换历史命令
#   tab
#       功能：用于补全文件名或文件夹名，连按tab，可以列出指定目录下特定字符开头的文件夹和文件
#   复制（centos）
#       命令行中用鼠标框选需要复制的内容，就将其复制在剪贴板中了
#   放大终端字体
#       ctrl+shift+=
#   缩小终端字体
#       ctrl+-
#命令行中可使用通配符进行匹配
#   通配符
#       * 代表任意个数个字符
#       ？代表任意一个字符，至少1个
#       [] 表示可以匹配字符组中的任意一个
#   实例：#ls [123]23.txt    #显示当前目录中文件名为123.txt，223.txt，323.txt的文件
#网络名字解释
#   ip地址
#       作用：用于数据传输时，精准定位目标主机位置
#       220.181.112.244    #百度服务器的ip地址
#       220.181.112.244:80    #域名+端口号才能正确访问对方web服务器（软件），如果不加端口号则默认使用80
#   默认端口
#       ssh服务器 默认端口：22
#       web服务器 默认端口：80
#       HTTPS     默认端口：443
#       FTP服务器 默认端口：21
#   域名
#       ip地址的别名，方便记忆和运用
#Ubuntu18安装sogo输入法
#   打开火狐浏览器
#       进入sogo官网下载sogo for linux
#           下载后打开安装文件进行安装
#   切换中英文输入法
#       单击shift
#别名机制
#   作用：给冗长的命令起别名，使用别名来调用原本命令的功能
#   centos
#       修改配置文件：.bashrc
#       文件地址:
#           /root/.bashrc
#           /home/admin/.bashrc
#       具体操作
#           #vim /root/bashrc
#               alias clear='cls'     #alias设置别名   别名命令='原命令'
#           :q
#           重新登录才能生效
#               方法一：切换用户
#                   #su admin
#                   #su root
#               方法二：重新
#   ubuntu18
#       $ sudo vim /etc/bash_aliases
#           i
#               alias cls="clear"
#           :x
#       $ sudo vim /etc/bash.bashrc
#           G
#           i
#               if [-f /etc/bash_aliases]; then
#                   ./etc/bash_aliases
#               fi
#           :x
#       #断开服务器连接，重新登录，即可生效
#           $ exit
#           C:\User\surface> ssh root@10.98.193.96
#           root@10.98.193.96's password:

#【day】linux中的命令
#命令格式
#   command [-option] [path]
#   [] 可选
#   option 可以是多个
#命令行进入方式
#   桌面右键
#       在终端中打开命令行
#命令行中多开标签
#   ctrl+shift+t
#命令行符号介绍
#   [root@localhost 桌面]#
#       root：当前登录的用户名
#       @：'在'
#       localhost：当前主机名称
#       桌面：当前工作目录
#       #/$：超级管理员/普通用户
#Linux下的手册man（Manual）
#   功能：查看某个命令的详细用法
#   语法：#man 命令名称
#   实例：#man find
#   退出手册：q
#常用命令
#   简单命令
#       tree
#           功能：以树状结构展示目录结构
#           语法：tree
#           带参命令
#               tree -d
#                   功能：只显示文件夹树结构，不显示文件
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
#   切换命令
#       切换路径
#           cd
#               功能：切换目录（change directory）
#               语法：#cd 需要切换到的路径（可以是相对路径，也可以是绝对路径）
#               实例：
#                   cd /home/admin 绝对路径
#                   cd ../home/admin 相对路径：相对于当前工作路径，即/root
#               带参命令
#                   cd ~ 进入家目录
#                   cd . 保持在当前目录
#                   cd .. 切换到上级目录
#                   cd - 最近两次工作目录之间切换
#           pwd
#               功能：打印当前的工作路径（print working directory）
#               实例：#pwd
#       切换用户
#           su
#               功能：切换用户（switch user）
#               语法：#su [-] [需要切换到的用户]
#               实例1：#su surface1    #切换到surface1用户
#               实例2：#su - surface1    #切换到surface1用户，并切换路径到surface1的家目录
#               实例3：#su -     #切换到root用户，并路径切换到root的家目录。
#                   注意：第一次切换到root，需要使用sudo passwd root设置root用户密码
#           exit
#               功能：返回到之前的用户
#   文件/文件夹的操作命令
#       文件的操作命令
#           创建
#               命令：touch
#               语法：#touch 文件的名字 文件名可以是一个完整的路径
#               说明
#                   只写文件名，则在当前目录下创建文件，如果是完成路径，则在指定文件夹路径下创建文件
#                   如果新建的文件不存在，则新建，反之会修改文件的末次修改时间
#               实例：
#                   #touch php50.txt
#                   #touch /php50.txt
#           复制
#               命令：cp（copy）
#               语法：#cp 需要复制的文件（可以是完整路径） 需要粘贴到的位置（可以是完整路径，注意必须最后要用文件名）
#               实例：
#                   #cp php50.txt /home/admin/php50.txt
#               技巧：如果复制时，不需要修改文件名，则目标路径的文件名可以不写，即cp /root/home/1.txt ./   #将1.txt复制到当前文件夹
#
#               带参命令：cp -i
#               功能：复制前检验目标文件夹下的文件是否存在，如果存在则会提示是否覆盖，这样更安全
#           移动
#               命令：mv（move）
#               语法：#mv 需要移动的文件 需要移动到的位置
#               实例1：#mv /home/admin/php50.txt /home/php50.txt
#               实例2：#mv ./*.py /home/surface/    #将当前文件目录中的所有.py文件移动到surface目录下
#           删除
#               命令1：rm（remove）
#               语法：#rm 需要删除的文件
#               说明：删除时会被提示是否删除
#               实例：#rm /root/php50.txt
#
#               命令2：rm -f（force，强制删除，不讯问是否删除）
#               语法：#rm -f 需要删除的文件
#               实例：rm -f /home/admin/php50.txt

#               命令3：rm -r（递归删除）
#               语法：#rm -r 需要删除的文件
#               实例：rm -r /home/admin/php50.txt
#           重命名
#               命令：mv
#               语法：#mv 需要重命名的文件 新的名字
#               实例：#mv /php50.txt /50.txt

#               带参命令：mv -i
#       文件夹的操作命令
#           创建
#               命令1：mkdir（make directory）
#               语法：mkdir 需要创建的目录名（可以使路径也可以是名字，如果是路径就在指定路径下创建，如果是名字就在当前目录下创建）
#               实例1：mkdir ./php
#               实例2：mkdir php
#
#               命令2：$ mkdir -p
#               功能：递归创建文件目录，即连续创建文件目录
#               语法：mkdir -p 文件夹路径
#               实例mkdir -p ./coco/mia
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
#   文本查看命令
#       cat
#           功能：显示全部文档内容
#           语法：cat path
#           实例：cat /root/home/1.txt
#           参数
#               cat -b 对非空输出行编号
#               cat -n 对所有行编号
#       more
#           功能：逐屏显示文档内容
#           语法：more path
#           实例：more /root/home/1.txt
#           说明：内容超过一屏幕，会分屏显示
#           输入
#               空格 显示下一页
#               enter 一次滚动内容一行
#               b 回滚一屏
#               f 前滚一屏
#               q 退出
#       grep
#           功能：在指定文本中，查找指定内容，并且只显示包含查找内容的行。
#           语法：grep [参数] 关键词 path
#           参数
#               grep -n 显示匹配行及行号
#               grep -v 显示不包含匹配文本的所有行（相当于取反）
#               grep -i 忽略大小写
#               grep -vn 显示不包含匹配文本的所有行并显示行号
#           实例
#               grep cyl /root/home/1.txt
#               grep -in "cyl psx" /root/home/1.txt    #如果搜索的关键词中间有空格，需要用引号框起来
#               grep -n ^f /root/home/1.txt    #查找以f开头的行
#               grep -n p$ /root/home/1.txt     #查找以p结尾的行
#       vim
#           介绍：vim是linux下一款编辑器软件，它的地位等同于windows下的notepad（记事本）。其功能上要比记事本要强很多倍
#           异常关闭处理
#               说明：vim编辑一个文件，没有正常关闭，则在下一次打开此文件时会提示异常关闭
#               问题本质：vim打开一个文件时，会新建一个原文件名.swp的缓存文件，正常关闭会删除.swp文件，异常关闭不会删除.swp
#               解决办法
#                   vim 打开这个文件，在异常关闭提示信息界面输入，d（必须是英文输入法），删除.swp文件即可
#           具体使用
#               准备工作
#                   先将/etc/passwd复制到/root
#                       #cp /etc/passwd /root/passwd
#               打开文件
#                   语法一：#vim 需要打开的文件名
#                       实例：#vim /root/passwd
#                           提示
#                               退出vim：:q
#                   语法二：#vim +数字 需要打开的文字（打开文件并快速定位到数字指定的行数）
#                       实例：#vim +5 /root/passwd
#                           提示
#                               在vim中显示行号： :set nu
#                   语法三：#vim +/字符串 需要打开的文件（打开文件后，高亮显示/后的字符串）
#                       实例：#vim +/login /root/passwd
#                           提示
#                               如果此时需要在搜索高亮结果中进行光标的快速跳转，可以按下键盘上的“n”（向下切换），或者“N”（向上切换）
#                               清除高亮显示：:nohl
#                   特别注意（vim新建文件）
#                       以上三种打开方式，如果打开一个不存在的文件，则会新建此文件。往其中写入内容，退出时则会保存，反之不保存
#               vim的三种模式
#                   命令模式（默认进入）
#                       进入末行模式：按下:
#                       进入编辑模式：按下i或a
#                       具体操作
#                           行内移动
#                               向后一个单词：w
#                               向前一个单词：b
#                               行首：0
#                               行首非空：^
#                               行末：$
#                           行数移动
#                               下移一行：j
#                               上移一行：k
#                               移动到行首
#                                   移至首行：gg
#                                   移至末行：G
#                                   移至指定行：数字gg
#                                       实例：15gg
#                           屏幕移动
#                               向上翻页：ctrl+b
#                               向下翻页：ctrl+f
#                               屏幕顶部（光标移动到当前屏幕的顶部，Head）：H
#                               屏幕中部（光标移动到当前屏幕的中部，Middle）：M
#                               屏幕低部（光标移动到当前屏幕的低部，Low）：L
#                           段落移动（用空行定义一个段落，即一个段落的开始，是一个空行）
#                               向上一段：{
#                               向下一段：}
#                           成对括号之间切换（包括(),[],{}）
#                               移动到前括号：%
#                               移动到后括号：%
#                               说明：当一行中有多个括号时，在离光标最近的括号之间快速切换
#                           标记段落
#                               使用场景：需要查看其他行代码，再回到当前行来书写代码或修改代码，在查询其他行代码时，光标会移走，需要快速回到当前行，则需要标记当前行
#                               标记语法：m标记字母（标记字母可以是a~z，A~Z）
#                                   实例：mx
#                               回跳语法：'标记字母
#                                   实例：'x
#                           删除
#                               删除当前光标字符并补齐，类似Del键功能：x
#                                   扩展
#                                       删除5个字符：5x    #重复执行5次x
#                                       删除括号及括号内的内容：将光标移动到前括号，v，%，x
#                               删除当前行，下行补齐：dd
#                               重复删除行：5dd    #从光标当前行 删除5行 （包括当前行）
#                               删除光标当前位置到当前行的末尾：D
#                               结合移动命令
#                                   语法：d移动命令
#                                   实例
#                                       dw    #从光标位置删除到一个单词末尾
#                                       d0    #从光标位置删除到一行的起始位置
#                                       d}    #从光标当前行 删除到 段落结尾行（包括当前行）
#                                       d5gg  #从光标当前行 删除到 指定行（包括删除指定行）
#                                       d'x   #从光标当前行 删除到 标记x 之间的所有代码（包括标记行）
#                               特别说明：删除命令和剪切命令是一模一样的。删除后的内容会自动保存到剪贴板，可以用于粘贴
#                           复制
#                               复制当前行：yy
#                               复制多行：数字yy
#                                   实例：5yy    #复制5行（包括当前行）
#                               结合移动命令
#                                   语法：y移动命令
#                                   实例
#                                       yw    #从光标位置   复制到 一个单词末尾
#                                       y0    #从光标位置   复制到 一行的起始位置
#                                       y}    #从光标当前行 复制到 段落结尾行（包括当前行）
#                                       y5gg  #从光标当前行 复制到 指定行（包括删除指定行）
#                                       y'x   #从光标当前行 复制到 标记x 之间的所有代码（包括标记行）
#                               注意：以上复制或剪切，是将内容保存到文本缓冲区，而并非剪贴板。即不能将以上复制或剪切内容
#                           粘贴
#                               p
#                               说明：粘贴时粘贴的位置是光标所在行的下一行开始
#                               注意：剪贴板中的内容要粘贴到vim中，必须进入编辑模式，用右键点击粘贴才能实现
#                           撤销：u
#                           恢复撤销：ctrl+r
#                           可视模式
#                               进入可视模式
#                                   v：框选光标当前位置到光标移动后的位置之间的所有内容
#                                   V：框选光标当前行位置到光标移动后所在行位置之间的所有内容
#                               进入可视块模式
#                                   ctrl+v：矩形方式框选代码内容
#                               说明：可视模式能与命令模式中的的命令连用
#                           替换
#                               替换轻量级
#                                   r    #替换一个字符
#                                   R    #进入改写模式
#                           缩排
#                               >>    #向右增加缩进
#                               <<    #向左减少缩进
#                               多行缩排
#                                   进入可视模式V，选中多行代码
#                                       >    #向右增加缩进
#                                       <    #向左减少缩进
#                           重复执行
#                               .    #重复执行上一步操作，比如缩进了一次，还需要增加一次缩进，只需要点一下'.'即可
#                   末行模式（:）
#                       进入命令模式：ESC
#                       具体操作
#                           保存
#                               :w
#                           另存
#                               语法：:w 文件路径
#                               实例：:w mypy.py
#                               注意：另存后不会切换到新文件，仍然是在当前文件中编辑
#                           退出
#                               :q
#                           强制退出(不会保存已经修改了的文件)
#                               :q!
#                               :wq!
#                           保存退出
#                               :wq 无论文件内容是否修改，都会更新文件保存时的最后修改时间
#                               :x 实际开发中推荐使用，只有内容真的被修改，才会修改文件的最后修改时间
#                           查找
#                               输入关键词查找
#                                   语法：/字符串
#                                   说明：被匹配到的字符串会高亮显示，如果不想看高亮显示，只需要再用/来查找一个不存在的字符，即可消除高亮
#                                   实例：/login
#                               查找当前光标所在的单词
#                                   *    #向后查找当前光标所在单词
#                                   #    #向前查找当前光标所在单词
#                               高亮关键词之间跳转
#                                   查找下一个：n
#                                   查找上一个：N
#                           替换
#                               记忆技巧
#                                   基本命令格式：:%s///g，:s///g，:%s///gc
#                                       替换全部：:%s/旧内容/新内容/g
#                                       可视范围内全部替换：:s/旧内容/新内容/g
#                                           说明：需要进入可视模式，框选范围后，输入':s/a/b/g'，就能将可视范围内中的a替换为b
#                                       全局确认替换：:%s/旧内容/新内容/gc
#                                           确认信息解释：y（替换当前行），n（不替换当前行），a（替换全部），q（退出替换）
#                           撤销
#                               语法一：:u
#                                   功能：撤销一步
#                               语法二：:数字u
#                                   功能：撤销多步
#                           加密
#                               语法：:X
#                           切换另一个文件进行编辑
#                               语法：:e 文件名
#                               技巧
#                                   :e .    #进入vim内置浏览器，能查看当前目录中的所有文件名，使用j，k光标移动键，将光标移动到要切换的文件名上，点击enter即可用vim打开这个文件
#                                   :e Tab    #这里同样能使用Tab自动补全文件名
#                               注意：切换之前，必须保存当前编辑的文件，保存后才能切换
#                           新建文件
#                               语法：:n 文件名
#                               实例：:n mypython.py
#                           分屏命令
#                               :sp [.]   #split 横向分屏
#                                   说明：如果带参，则创建一个水平分屏，并且一个窗口进入vim内置浏览器，可以选择当前窗口打开哪个文件
#                               :vsp [.]  #vertical split 纵向分屏
#                                   说明：如果带参，则创建一个垂直分屏，并且一个窗口进入vim内置浏览器，可以选择当前窗口打开哪个文件
#                               分屏窗口控制
#                                   ctrl+w    #进入窗口控制模式
#                                       w    #windows，切换到下一个窗口
#                                       r    #reverse，互换窗口
#                                       c    #close，关闭当前窗口，但是不能关闭最后一个窗口
#                                       q    #quit，退出当前窗口，如果是最后一个，则关闭vim
#                                       o    #other，关闭其他窗口

#                   编辑模式
#                       进入命令模式：按下esc
#                       从命令模式进入编辑模式
#                           i：当前光标位置之前插入
#                           a：当前光标位置之前插后
#                           I：光标移动到当前行行首
#                           A：光标移动到当前行行尾
#                           o：当前行后面插入空行
#                           O：当前行前面插入空行
#                           R：光标不动，进入替换（改写）编辑模式
#                       快捷命令
#                           ctrl+n：自动补全代码
#           vim扩展知识
#               vim的安装
#                   sudo apt install vim
#               vim的智能提示（记得切换阿里源，否则。。你懂得）
#                   cd ~    #回到家目录
#                   sudo apt install vim-addon-manager    #安装插件管理器
#                   sudo apt install vim-youcompleteme    #下载插件
#                   vim-addons install youcompleteme    #将插件添加到管理器中
#                   git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim    #下载插件管理器
#                   git clone https://github.com/tomasr/molokai  ~/.vim/colors/molokai    #下载配色方案
#                   sudo cp ~/.vim/colors/molokai/colors/molokai.vim /usr/share/vim/vim80/colors/    #将颜色方案添加到配置文件
#               添加自定义配置文件
#                   $ sudo vim /etc/vim/vimrc
#                       G
#                         set bg=dark           "黑色背景
#                         set completeopt=menu  "关闭草稿
#                         set nu                "显示行号
#                         set paste             "粘贴时 禁止自动缩进
#                         set scrolloff=5       "光标到上下缓冲区边距
#                         set nobackup          "禁止生成临时文件
#                         set nocindent         "不使用C风格缩进
#                         set noautoindent      "不使用自动缩进
#                         set shiftwidth=4      "自动缩进字符宽度
#                         set ts=4              "tab键宽度
#                         set expandtab         "将tab符转为空格
#                         %retab!               "对于已保存的文件,执行expandtab
#                         set fencs=utf-8,ucs-bom,shift-jis,GB2312,GBK,gb18030,gbk,gb2312,cp936 "支持的字符集
#                         set ignorecase        "搜索时 忽略大小写
#                         syntax on             "语法高亮
#                         set hls               "搜索高亮
#                         set bg=dark           "字体加亮
#                         set nocompatible      "去除兼容vi
#                         set backspace=indent,eol,start "允许使用退格键
#
#                         "vim 配色相关
#                         "colorscheme corporation
#                         colorscheme molokai     "配色方案有这些：blue，default，desert，evening，koehler，murphy，peachpuff，ron，slate，torte，darkblue，delek，elflord，industry，morning，pablo，shine，solarized，zellner，molokai
#                         "colorscheme molokai
#
#                         "YouCompleteMe配置相关
#                         let g:ycm_server_python_interpreter='/usr/bin/python'
#                         let g:ycm_global_ycm_extra_conf='~/.vim/.ycm_extra_conf.py'
#                         filetype off
#                         set rtp+=~/.vim/bundle/Vundle.vim
#                         call vundle#begin()
#                         Plugin 'VundleVim/Vundle.vim'
#                         Plugin 'Valloric/YouCompleteMe'
#                         call vundle#end()
#                         filetype plugin indent on
#
#                         "vim 设置快捷键 模式1  F2->define, F3->declar, F4->auto
#                         let g:ycm_goto_buffer_command = 'new-tab' "跳转打开新的屏幕
#                         "let g:ycm_goto_buffer_command = 'horizontal-split' "跳转打开上下分屏
#                         map <F2> :YcmCompleter GoToDefinition<CR>
#                         map <F3> :YcmCompleter GoToDeclaration<CR>
#                         map <F4> :YcmCompleter GoToDefinitionElseDeclaration<CR>
#
#                         "vim 设置快捷键 模式2
#                         "let g:ycm_goto_buffer_command = 'horizontal-vsplit' "跳转打开新的分屏 :e#退出分屏
#                         "let mapleader = '\'                                 "命令模式,\df跳转到定义,\dc跳转到声明,\de任意找
#                         "nnoremap <leader>df :YcmCompleter GoToDefinition<CR>
#                         "nnoremap <leader>de :YcmCompleter GoToDeclaration<CR>
#                         "nnoremap <leader>dc :YcmCompleter GoToDefinitionElseDeclaration<CR>
#               安装后的目录结构以及排错
#                   ~/.vim
#                         ├── autoload
#                         │   └── youcompleteme.vim -> /usr/share/vim-youcompleteme/autoload/youcompleteme.vim
#                         ├── doc
#                         │   ├── tags
#                         │   └── youcompleteme.txt -> /usr/share/vim-youcompleteme/doc/youcompleteme.txt
#                         ├── plugin
#                         │   ├── myVimrc
#                         │   └── youcompleteme.vim -> /usr/share/vim-youcompleteme/plugin/youcompleteme.vim
#                         └── vim-colors-solarized    #手动添加——1、https://ethanschoonover.com/solarized/到这里在压缩包，解压之后找到vim-colors-solarized，并上传到这个目录下
#                             ├── autoload
#                             │   └── togglebg.vim    #sudo cp togglebg.vim /usr/share/vim/vim80/autoload/
#                             ├── colors
#                             │   └── solarized.vim   #sudo cp solarized.vim /usr/share/vim/vim80/colors/
#                             ├── doc
#                             │   ├── tags
#                             │   └── togglebg.txt    #sudo cp togglebg.txt /usr/share/vim/vim80/doc/
#                             └── README.mkd
#               打开文件并且定位行
#                   $ vim 文件名 +行数
#                   使用场景：首先知道某行代码出错（报错时会提醒），直接打开并定位出错代码行修改代码
#                   实例：$ vim myFile.py +16
#                   扩展：$ vim myFile.py +    #直接定位到最后一行
#       vim演练
#           快速输入10个'*'：[10, i, *, esc]
#           给多行添加注释：[o, ctrl+v, j,j,..j, shift+i, # , esc]    #移动到行首，进入可视块模式，下移光标框选多行，I进入插入模式，为单行添加注释，退出插入模式。此时vim自动将块中的代码全部添加注释

#   帮助命令
#       $ man ls #帮助文档，查看命令的文档
#           说明：进入man之后点h，也能进入帮助文档
#       $ ls --help #进入命令的帮助文档，可查命令的参数

#   网络连接
#       $ systemctl restart network     #contos 重新加载网卡
#       $ sudo yum install net-tools    #contos安装ifconfig命令
#       $ sudo apt install net-tools    #ubuntu安装ifconfig命令
#       $ sudo dhclient    #桥接模式下，ifconfig后，没有ipv4的ip地址，可以使用此命令来让别人给你重新分配ip
#       $ ifconfig #查看当前网卡的信息；说明：ipV4是ens33：inet下显示的ip
#       $ ifconfig -a #查看所有网卡的信息
#       $ ifconfig eth0 #查看指定网卡的信息
#       $ ifconfig ens33 down  #禁用网卡（虚拟机一定要选Nat模式，否则down了之后无法激活，需要还原虚拟机的虚拟网络连接模式）
#       $ ifconfig ens33 up  #开启网卡网卡
#       $ ifconfig | grep inet    #查看ipv4和ipv6的ip地址
#       $ ping 192.168.0.106    #查看ip是否通信。可ping网关、外网、宿主机ip
#       $ ping 127.0.0.1    #查看本地网卡是否工作正常
#       $ ping www.baidu.com    #查看某个网站是否连通
#       $ sodu apt install openssh-server    #服务器需要安装此软件，才能用xshell连接上
#       $ ssh [-p 端口号] user@remote
#           说明
#               user 是远程机器上的用户名，如果不指定的话会默认为当前用户
#               remote 是远程机器的地址，可以是IP/域名，或者是 后面会提到的别名
#               -p 端口号 是ssh server软件的端口，如果不指定，默认22，即如果ssh server的默认端口不是22，则需要-p参数来指定端口号
#           实例
#               ssh -p 22 surfacenew@192.168.70.133
#               exit
#           免密登录
#               说明
#                   通过ssh命令链接过任何服务器，与之产生的ssh协议密钥都保存在用户家目录的.ssh文件夹下
#                   实现免密登录的原理
#                       本地ubuntu系统中生成一个公钥一个私钥，将公钥上传到服务器中
#                       本地发送数据包到服务器时，会先使用私钥加密内容后再发送
#                       服务器接收到数据包后，先用公钥进行解密，处理数据后，返回新的数据包，同样发送之前使用公钥加密再发送
#                       本地收到数据包时，用私钥进行解密
#               $ ssh-keygen    生成SSH钥匙，一路回车即可
#               功能：将公钥传给服务器
#               语法：ssh-copy-id -p port user@ip
#               实例：$ ssh-copy-id -p 22 surfacenew@192.168.70.133    将公钥上传到指定服务器
#           配置别名
#               说明：配置别名后可以通过ssh 别名的方式，即可访问远程服务器
#               方法
#                   在家目录的.ssh中创建config，即/home/surface/.ssh/config
#                       Host surfacenew
#                           HostName ip地址
#                           User surfacenew
#                           Port 22
#               配置成功后的实例
#                   $ ssh surfacenew    #远程连接道surfacenew服务器
#                   $ scp -r ./abc surfacenew:/home/surfacenew    #将本地./abc文件夹上传到服务器
#   文件传输
#       $ scp
#           注意
#               在使用scp命令时，如果出现ssh: connect to host 192.168.70.132 port 22: Connection refused
#               说明Ubuntu默认没有安装openssh-server
#               通过sp -e|grep ssh命令，如果只有一个ssh-agent进程，证实openssh-server确实没有安装
#               通过sodu apt install openssh-server 安装后即可在本地cmd中使用scp命令
#           功能：将本地文件复制到远程服务器中
#           语法：$ scp [-P 22] path user@remote:toPath
#           参数说明：-P 指定软件端口，path为本地文件目录及文件名，user为服务器用户名，remote为ip地址或域名，toPath为服务器中的目录及文件名
#           实例：scp -P 22 C:/1.py root@192.168.2.1:/root/home/1.py    #将本地文件1.py，拷贝到远程web服务器中的/root/home文件夹中
#
#           功能：将远程服务器中的文件拷贝到本地来
#           语法：scp [-P 22] user@remote:path toPath
#           参数说明：user为远程服务器的用户名，remote为远程服务器的ip或域名，path为远程服务器的文件及文件路径，toPath为本地计算机的文件夹及文件名
#           实例：scp -P 22 root@192.168.2.1:/root/home/1.py C:/1.py
#
#           功能：将本地文件目录拷贝到远程服务器中
#           语法：scp -r demo user@remote:toPath
#           实例：scp -r C:/abc root@192.168.2.1:/root/home/abc
#
#           功能：将远程服务器中的文件夹拷贝到本地
#           语法：scp -r user@remote:toPath demo
#           实例：scp -r root@192.168.2.1:/root/home/abc C:/abc
#       FileZilla
#           官网：https://www.filezilla.cn/download/client
#           注意：使用FileZilla链接远程服务器时，端口号要使用21
#   时间和日期
#       date
#           功能：查看系统当前时间
#           返回：2020年 01月 26日 星期日 16:58:45 CST
#       data -s
#           功能：设置系统当前时间
#           实例
#               $ date -s '2019-07-19' #设置当前的日期，设置之后date查看的时间就是从2019-07-19的00:00:00开始计时
#               $ date -s '19:10:10' #设置当前时间的时分秒
#       cal
#           功能：查看当月日历，添加-y参数可查看当年的一年的日历
#           语法：cal [-y]
#   磁盘和目录空间
#       df（disk free）
#           功能：显示磁盘的剩余空间
#           语法：df -h     #-h 以人性化的方式显示磁盘大小（ls -lh）
#           实例：$ df -h
#           返回：/dev/sda1        20G  7.7G   11G   42% /
#           说明：查看磁盘剩余空间，主要看挂载点为/的信息
#       du（disk usage）
#           功能：查看指定目录的磁盘占用情况
#           语法：du -h [目录名]
#           说明：不指定目录名，则查看当前目录以及其中的所有文件和目录的磁盘占用大小
#           实例：$ du -h /home/surface/abc
#       扩展命令
#           $ df -h #显示磁盘分区信息
#           $ mkfs.ext4 /dev/sdb1 #格式化硬盘分区
#           $ fdisk -l #查看磁盘分区
#           $ fdisk /dev/sdb #硬盘分区
#           $ du -h /var/log/ #分别显示指定目录下所有文件使用磁盘空间的大小
#           $ du -h -s /var/log/ #显示指定目录下所有文件使用磁盘空间大小的总和
#           $ mount /dev/sr0 /mnt/cdrom #挂载光驱，将光驱的内容，挂载到/mnt/cdrom中。当服务器插入一个u盘或硬盘时不能直接识别，需要使用挂载才能读出里面的内容
#           $ mount -o remount rw/ #重新挂载，或者将根目录以读写方式重载
#           $ umount/media/umnt #卸载，怕掉u盘后执行
#           $ fscy -y /dev/sda1 #修复的可以是分区也可以是目录，最好在单用户模式下使用，参数-y表示遇到问题自动回复yes
#           $ pvdisplay #查看物理磁盘
#           $ lvdisplay #查看逻辑卷
#           $ lvextend #查看扩展卷
#   进程信息
#       ps（process status）
#           功能：查看进程的详细状况
#           语法：$ ps [aux]
#           说明
#               如果不带aux，ps只会显示当前用户通过终端启动的应用程序，即只显示bash和ps两个应用程序
#               参数不加-号
#           参数
#               a 显示终端上所有的进程，包括其他用户启动的进程
#               u 显示进程的详细状态
#               x 显示不是由终端启动的进程（系统进程）
#           实例：ps au
#           返回
#               USER           PID      %CPU        %MEM         VSZ     RSS  TTY      STAT START    TIME     COMMAND
#               root           1        0.0         0.2          225380  5972 ?        Ss   08:48    0:02     /sbin/init splash
#               启动进程的用户 进程id号 cpu占用大小 内存占用大小                            启动时间 使用时间 程序目录
#       top
#           功能：动态显示运行中的进程并根据其cpu占用率进行降序排序
#           说明：进入查看模式后，输入q即可退出
#           实例：$ top
#           返回
#               top：动态当前时间；动态运行时间；用户数；平均负载——1分钟的负载、5分钟的负载、15分钟的负载；
#               Tasks：进程总数；在运行进程数；休眠运行进程数；停止运行进程数；僵尸进程数；
#               cpu(s):按1就能展开查看所有的cpu核的消耗情况-用户所占cpu%；系统所占cpu%；闲置cpu%；硬件使用cpu%；软件使用cpu%，虚拟机使用cpu%
#               Mem：内存总数；已使用内存数；闲置内存数；
#               Swap：缓冲区总数；剩余总数；使用总数；缓存使用总数
#       htop
#           功能：同top，但界面更好识别，更好看
#           注意：$ sudo apt install htop 安装后才能使用
#       kill
#           功能：终止指定代号的进程
#           语法：kill [-9] PID
#           说明：-9表示强制终止
#           实例：kill -9 2587
#   系统级别的命令
#       $ sudo 命令    #sudo是切换成root用户及其权限执行后面的命令
#       $ uname -a #显示系统及版本的所有信息
#       $ uname -r #显示内核版本
#       $ uname -m #显示计算机是多少位的系统
#       $ cat /etc/redhat-release #查看linux的版本名 --> CentOS Linux release 7.6.1810
#       $ hostname #查看主机名 --> localhost.localdomain
#       $ hostname justin #临时性修改主机名为justin
#       $ vim /etc/sysconfig/network #永久修改主机名
#       $ uptime #显示当前时间，系统使用时间，用户登录数，平均负载（不能超过）
#       $ last #查看历史登录信息
#       $ tty #当前登录模式pts/0图形界面登录 pts/3命令符模式登录
#       $ jps #显示所有正在运行的java进程 （需要安装了jdk才能使用该命令）
#       $ pstree -p #树的形式查看进程
#       $ ps | grep mysql #查看当前指定应用所运行的进程，本质是模糊匹配CMD字段
#           管道：概念|前的命令的返回值传送给后面的命令做进一步处理
#       $ grep sshd /var/log/boot.log #在boot文件中过滤出包含sshd内容的代码
#       $ grep -r sshd /var/log #在某个目录下递归查看其中所有文件，是否包含sshd的代码，如果有则显示其文件名和所在文件中的行数
#           常用于报错之后，不知道报错代码在哪个文件中，便可用此方法搜索
#       $ sync #将数据有内存同步到硬盘中，执行了sync才能执行reboot
#       $ reboot #重新启动Linux操作系统
#       $ shutdown
#           功能：指定时间关机或重启
#           语法：shutdown [选项] [时间]
#           说明：时间默认为1分钟，立刻关机参数为now
#           实例
#               #shutdown    #一分钟后关机
#               #shutdown now    #立刻关机
#               #shutdown 20:25     #在8点25分关机
#               #shutdown +10    #10分钟后关机
#           参数
#               shutdown -c    #取消预设关机时间
#               shutdown -r    #重启
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
#       概念：将本应显示在终端上的内容 输出/追加 到指定文件中
#       说明
#           >表示输出，会覆盖文件原有内容
#           >>表示追加，会将内容追加到已有文件的末尾
#       $ echo
#           功能：重显示，将echo后面的内容，重新打印一遍
#           语法：echo 打印的内容
#           实例
#               echo Python
#               echo 'Python'
#       实例
#           $ echo '123' >> /home/abc #在abc文件中的最后一行追加123
#           $ echo '123' > /home/abc #重写abc中的内容
#           $ ls -la > /root/home/a.txt    #将当前文件夹的ls内容写入a.txt中
#           $ tree >> a.txt    #将tree的返回内容追加到a中
#               说明：如果a.txt，没有这个文件，则会自动创建a.txt文件
#   管道
#       概念：linux允许将一个命令的输出 可以通过管道 做为 另一个命令的输入
#       理解：可以理解为现实生活中的管子，一头塞东西，一头取东西，这里的|的左右分为两端，左端塞东西（写入），右端去东西（读取）
#       常用的管得到命令有
#           more 分配显示内容
#               实例
#                   ls -al ~ | more    #将家目录的ls的结果进行分屏显示
#                   ls -al ~ | grep du    #将家目录的ls的结果传到grep中，grep只显示包含du的内容
#           grep 在命令执行结果的基础上查询指定的文本
#   打包压缩
#       命令：tar
#       说明：tar是linux中常用的备份工具
#       功能：将一系列的文件打包成一个大文件，也可以将一个大文件恢复成一系列的小文件
#       系统
#           contos
#               参数解释
#                   -z #压缩
#                   -c #打包
#                   -x #解包
#                   -f #必须要
#                   -C #指定解包位置
#                   -v #输出信息
#                       linux中的压缩格式
#                           .tar.gz
#                               解压命令：tar
#                                   语法：tar -zxvf 需要解压的文件 [解压到的位置]
#                           .tar.bz2
#                               解压命令：tar
#                                   语法：tar -jxvf 需要解压的文件 [解压到的位置]
#           ubuntu18
#               仅打包解包
#                   打包语法：$ tar -cvf 打包文件名.tar 被打包的文件/路径
#                       实例1：$ tar -cvf myTar.tar *.py
#                       实例2：$ tar -cvf myTar.tar 1.py 2.py 3.py
#                       当前目录生成：myTar.tar文件
#                   解包语法：$ tar -xvf 打包文件名.tar    #仅解包不解压
#                       实例：$ tar -xvf myTar.tar
#                   参数解释
#                       -c #生成档案文件，即创建打包文件
#                       -x #解开档案文件
#                       -v #列出归档（打包）/解档（解包）的详细过程，即显示进度
#                       -f #指定档案文件名称，f后面一定是.tar文件，所有必须放参数最后
#               即打包压缩，有解包解压
#                   调用gzip压缩
#                       打包压缩语法：$ tar -zcvf 打包文件名.tar.gz 被打包的文件/路径
#                           实例：$ tar -zcvf myTar.tar.gz *.py
#                               当前目录生成：myTar.tar.gz文件
#                       解包解压语法：$ tar -zxvf 打包文件.tar.gz
#                           实例：$ tar -zxvf myTar.tar.gz
#                       解包解压到指定目录语法：$ tar -zxvf 打包文件.tar.gz -C 指定目录
#                           实例：$ tar -zxvf myTar.tar.gz -C /home/surface/mydir
#                       参数解释
#                           -z    #自动调用gzip工具，对tar包进行压缩或解压
#                           -C    #指定文件目录，必须保证指定目录是存在的
#                   调用bzip2压缩
#                       打包压缩语法：$ tar -jcvf 打包文件名.tar.bz2 被打包的文件/路径
#                           实例：$ tar -jcvf myTar.tar.bz2 *.py
#                               当前目录生成：myTar.tar.bz2文件
#                       解包解压语法：$ tar -jxvf 打包文件.tar.bz2
#                           实例：$ tar -jxvf myTar.tar.bz2
#                       解包解压到指定目录语法：$ tar -jxvf 打包文件.tar.bz2 -C 指定目录
#                           实例：$ tar -jxvf myTar.tar.bz2 -C /home/surface/mydir
#                       参数解释
#                           -j    #自动调用bzip2工具，对tar包进行压缩或解压
#                           -C    #指定文件目录，必须保证指定目录是存在的
#   查找、检索、搜索
#       命令：which
#           语法：which 命令
#           功能：查询指定命令的文件路径
#           实例1：$ which reboot
#               结果：/sbin/reboot    #sbin(system binary)，保存二进制文件目录-超级用户有关的命令
#           实例2：$ which passwd
#               结果：/bin/passwd    #bin(binary),保存二进制的文件目录-普通用户有关的命令
#       命令：find
#           功能：在特定目录下搜索符合条件的文件
#           语法：#find [指定目录] -name 查找的关键词
#           说明：指定目录后，在指定目录中查找，不知定目录，则在当前目录查找
#           实例1：#find /home/surface/dev/ -name *.py
#           实例2：#find -name *1*
#       扩展命令
#           $ whereis reboot #查看reboot命令所在文件路径已经其安装文件目录路径
#           $ updatedb #是locate命令有效
#           $ locate file1 #查找file1文件所在文件路径，查询更快，因为是通过数据库查询
#   软连接
#       概念：类似windows下的快捷方式
#       命令：ln
#       语法：ln -s 被连接的源文件 连接文件
#       注意
#           必须有-s参数，有-s建立的文件是软连接，没有-s建立的文件是硬连接，两个连接占用相同大小的磁盘空间，但在工作中几乎不会建立文件的硬链接
#           源文件要使用绝对路径，这样就算移动了软连接文件，也能正常使用
#       实例：ln -s /etc/
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


#【day】软件安装
#contos
#    rpm软件管理
#         简介：在linux中rpm其实有点类似于windows下的“xxx电脑管家”，其作用就是管理软件
#         功能
#           查询软件安装情况
#               语法：rpm -qa [|grep]需要查询的关键词
#               参数解释
#                   -q：query，查询
#                   -a：all，全部
#                   |：在php中称它为变量修饰器。在linux中称为管道
#                   grep：表示从结果中进行过滤
#               实例：rpm -qa mysql
#           安装软件
#               语法：rpm -ivh 需要安装的软件完整名称
#               参数解释
#                   -i：install，安装
#                   -v：表示显示进度条
#                   -h：表示进度条以“#”显示
#               查询软件的完整名字
#                   条件
#                       centos6.6的系统盘必须挂载（在虚拟机的CD/DVD中必须挂载-使用iso映像文件中有路径，且已连接要勾选。右键虚拟机名称，点击设置即可弹出挂载界面）
#                       linux桌面版的桌面上必须有系统的cd盘符。如果没有，就去我的电脑中打开一下就有了
#                   所有安装包的存放位置
#                       linux桌面版：centos的光盘-packages
#                           在该文件夹的空白处右键点击在终端中打开
#                       linux命令行：/media/CentOS_6.6_Final/Packages
#                   在软件包目录中查询需要安装软件的全名称
#                       #cd /media/CentOS_6.6_Final/Packages
#                       #ls firefox*    列出以firefox开头的所有文件
#               实例：rpm -ivh firefox-31.1.0-5.el6.centos.i686.rpm
#           卸载软件
#               语法：rpm -e 需要卸载的软件名称（软件完整名称，即通过查询可得到）[--nodeps]
#               参数解释
#                   -e：卸载
#                   --nodeps：忽略依赖关系
#               实例：rpm -e firefix-31.1.0-5.el6.centos.i686 --nodeps
#ubuntu18
#   命令：atp（Advanced Packaging Tool）,高级包管理工具
#       sudo apt install 安装软件包
#       sudo apt remove 移除软件包
#       sudo apt update     #刷新存储库索引
#       sudo apt upgrade    #升级所有可升级的软件包
#       sudo apt purge      #移除软件包及配置文件
#       sudo apt autoremove #自动删除不需要的包
#       sudo apt full-upgrade #在升级软件包时自动处理依赖关系
#       sudo apt search 搜索应用程序
#       sudo apt show   #显示安装细节
#       sudo apt list	#列出包含条件的包（已安装，可升级等）
#       sudo apt edit-sources	#编辑源列表
#   切换软件镜像源
#       点击左下角的九个点图标
#           点击软件和更新（非软件更新器）
#               在ubuntu软件选项卡中，单击下载自：对应的选框
#                   点击其他站点
#                       点击选择最佳服务器（此时系统会将所有服务器进行测速，最后为你选择一个最快的服务器镜像源）
#安装pycharm
#   下载安装包（在官网中下载）
#       默认下载位置：/home/surface/下载
#       将安装包移动到/opt中：$ sudo mv pycharm-professional-2019.3.2.tar.gz /opt/
#       $ sudo cd /opt
#       $ sudo tar -zxvf pycharm-professional-2019.3.2.tar.gz
#       $ cd pycharm-2019.3.2/bin/
#       $ ./pycharm.sh
#   建立桌面图标
#       打开pycharm后，点击toop-create desktop entry
#           勾选Create the entry for all users
#               点击ok

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
#命令：id
#   语法：$ id [用户名]
#   注意：# id后面不带用户名，查询的是当前用户的用户信息
#   功能：#查看指定用户的用户信息（UID）和组信息（GID）
#   实例：#id surface
#       结果：uid=1000(surface) gid=1000(surface) 组=1000(surface),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare)
#             用户id            组id              附加组列表
#   说明：UID被保存在/etc/passwd，GID被保存在/etc/group
#       验证
#           cat -n /etc/passwd | grep surface
#               41	 surface:x             :1000:1000:surface,,,  :/home/surface:/bin/bash
#               行号 用户名 :密码（被加密）:UID :GID :用户名的全名:用户的家目录 :远程登录时默认使用的shell软件路径
#           cat -n /etc/group | grep surface
#               5	adm       :x             :4   :syslog,surface
#               18	cdrom     :x             :24  :surface
#               21	sudo      :x             :27  :surface    #允许surface用户访问sudo组，sudo具有root权限
#               23	dip       :x             :30  :surface
#               35	plugdev   :x             :46  :surface
#               55	lpadmin   :x             :116 :surface
#               65	surface   :x             :1000:
#               66	sambashare:x             :126 :surface
#               行号 用户组名 :密码（被加密）:组号:允许访问该组的用户名
#命令：who
#   功能：查看当前所有正在登录的用户列表
#   实例：$ who
#       结果：
#             surface     pts/1  2020-01-26 12:31 (192.168.70.1)
#             surface     :0     2020-01-26 08:48 (:0)
#             登录的用户名       上一次登录时间   从哪里登录（:0表示从当前电脑登录）
#命令：whoami
#   语法：
#   功能：查看当前登录用户的账户名
#【用户管理】（用户信息保存在/etc/passwd中，使用cat -n /etc/passwd | grep surface查看）
#   添加
#       命令：useradd
#       centos
#           语法：#useradd 用户名
#           实例：#useradd justin
#           验证：#/vim /etc/passwd   在最后一行能看到新添加的用户名
#               扩展：passwd中一行内容详解
#                   16 dbus:x:81:81:System message bus:/:/sbin/nologin
#                   行号 用户名:密码（占位符）:用户id:用户组id:注释或备注:用户对应的家目录:用户所对应的解释器位置（/sbin/nologin-无登录权限，/bin/bash-有登录权限）
#                   说明：密码单独存储在/etc/shadow中
#       ubuntu
#           带参命令：useradd -m -g 组 用户名
#               参数说明
#                   -m：创建新用户时，自动在家目录中创建指定用户并且设置rwx权限
#                   -g：创建新用户时，将用户添加到指定组中
#           实例：sudo useradd -m -g dev surface2
#           注意
#               如果创建用户时忘了-m，可以直接删除这个用户，再新建一个
#               创建的新用户不在sudo组中，需要手动为其添加sudo附加组，添加方法详见usermod -G命令
#               创建的新用户未指定shell软件路径，默认使用dash，但dash软件无上下键命令历史概念，也无颜色，因此需要为其指定shell软件路径-/bin/bash，指定方式详见usermod -s命令
#   密码
#       命令：passwd
#       语法：#passwd 需要设置密码的用户名
#       实例：#passwd justin
#       注意
#           当设置密码过于简单，它会提示无效密码，但并不影响你继续验证密码，重新输入新密码（即简单的密码）后，密码设置成功。
#           新建用户后必须要设置密码，新用户才生效
#   编辑
#       命令：usermod（user modify）
#       语法：#usermod 参数 需要修改的用户名
#       参数解释
#           -l：修改用户名
#               语法：#usermod -l 新用户名 需要被修改的用户名
#               实例：#usermod -l justin admin
#           -g：修改用户的用户组id
#               语法：#usermod -g 组名 需要修改组的用户名
#               实例：#usermod -g dev surface1
#           -G：修改用户的用户附加组
#               语法：#usermod -G 组名 需要修改附加组的用户名
#               实例：#usermod -G sudo surface1
#               注意：增加附加组后，需要重新登录一下被修改了附加组的用户名，该用户的附加组才能生效
#           -s：修改终端shell使用的软件（ubuntu18的命令输入终端就是shell，默认使用bash软件打开）
#               语法：#usermod -s shell的软件路径 用户名
#               实例：#usermod -s /bin/bash surface1
#   删除
#       命令：userdel（user delete）
#       语法：#userdel -r 用户名    #-r会自动删除家目录中的用户名文件夹
#       实例：#userdel -r justin
#       注意：会提示未找到justin的文件夹，其实justin用户名已经被删除
#           可以通过 gat -n /etc/passwd|grep justin 查看是否包含justin的用户名内容
#【用户组管理】（ubuntu中需要在租操作命令前加sudo）（用户组信息保存在/etc/group中，使用cat -n /etc/group | grep surface查看）
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
#【用户权限设置】（重点）
#查看当前用户对指定文件夹内所有文件及文件夹的使用权限
#   方法：ls -l 或 ls -la
#   实例：ls -l
#       -rwxrwx--- 1                                             surface    surface    8980               1月 17 12:05   1.py
#       0123456789 硬连接数（有多少种方式来访问此文件或文件夹）  拥有者名称 所在组名称 文件或文件夹的大小 创建或修改时间 文件/文件夹名称
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
#修改拥有者
#   命令：chown
#   语法：chown 用户名 文件名/目录名
#修改权限
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
#                        centos
#                           #chmod a+r 对全部组成部分添加可读权限
#                           #chmod a-r 对全部组成部分删除可读权限
#                           #chmod a=rwx 对全部组成部分设置可读可写可执行权限
#                        ubuntu18
#                           #chmod +r 对全部组成部分添加可读权限
#                           #chmod -r 对全部组成部分删除可读权限
#                           #chmod rwx 对全部组成部分设置可读可写可执行权限
#   通过数字设置权限
#       语法：$ sudo chmod [-R] '拥有者数字权限''组权限''其他用户权限' 文件/目录
#       4表示读权限
#       2表示写权限
#       1表示执行权限
#       7表示全部权限
#       说明：把50.txt文件权限设置为所有者全部权限，同组用户读写权限，其他用户读权限
#           全部权限=读+写+执=4+2+1=7
#           读写权限=读+写=4+2=6
#           读权限=读=4
#           所以最终权限数字=764
#       实例1：chmod 764 50.txt     #为文件50.txt的拥有者、组、其它用户分别设置权限：rwx、rw、r
#       实例2：chmod -R 764 mydir     #为目录mydir及其子目录和其内的文件的拥有者、组、其它用户分别设置权限：rwx、rw、r
#       注意
#           421 7 rwx
#           420 6 rw-
#           401 5 r-x
#           400 4 r--
#           021 3 -wx
#           020 2 -w-
#           001 1 --x
#           000 0 ---
#       常用权限
#           777===>u=rwx,g=rwx,o=rwx
#           755===>u=rwx,g=rx,o=rx
#           644===>u=rw,g=r,o=r
#   友情提示
#       在以后实际工作中不要出现一个奇葩的权限
#           -wx  不要出现类似这样的权限，原因最基础的读权限未给，如果要写必须先读（打开）
#设置python文件的执行权限,并执行
#   新建python文件，给与他可执行权限，直接执行此文件
#       $ vim 1.py
#           #!/usr/bin/python3
#           print('123')
#       $ chmod 754 1.py
#       $ ./1.py
#修改组名
#    命令：chgrp
#    语法：sudo chgrp [-R] 要添加进入的组名 要修改组名的文件/文件夹    #如果修改文件夹的组名需要加-R参数
#    实战：1、新建一个文件夹-python学习 2、新建一个组-dev 3、将python学习文件夹的组名更改问dev
#        $ pwd
#            /home/surface
#        $ mkdir python学习
#        $ sudo groupadd dev    #新建一个dev（开发）的组
#        $ sudo chgrp -R dev ./python学习

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

#【day】网络通讯
#ip
#   标记电脑或手机的地址
#端口
#   标记电脑中的进程地址
#   知名端口
#       80：http服务
#       21：ftp服务
#       范围：0-1023
#   动态端口
#       范围：1024-6
#
#【Nginx】
#简介：服务器软件
#官网资料
#   www.nginx.org/en/docs/
#中文资料
#   http://www.nginx.cn/doc/index.html
#   http://tengine.taobao.org/book/
#安装
#   包管理工具安装
#       去官网将所使用的依赖添加到包管理工具中
#           打开www.nginx.org/en/docs/
#               点击installing nginx
#               点击installation on linux中的packages
#                   点击Ubuntu
#       更新包管理工具资源
#       使用包管理工具安装