#aa.py
#   def myPrint():
#       print(1)
#main.py
#   import aa
#   import aa
#导入两次，其实只导入了一次，python默认重复import时，只能导入一次

#重新导入
#终端一：
#   ipython
#       import aa
#       aa.myPrint()  # 打印1
#终端二：（未关闭终端一以及ipython）
#   aa.py
#      def myPrint():
#          print(2)
#回到终端一
#   ipython
#       import aa
#       aa.myPrint()  # 打印仍然是1

#       from imp import reload
#       reload(aa)  # 重新加载aa模块
#
#       aa.myPrint()  # 此时打印的就是2了

#那重新加载模块有什么用呢？
#   应用场景：服务器程序是不能关闭的，python程序必须一直执行，对模块功能进行升级后，就需要在不关闭程序的前提下，重新加载模块

#当遇到新函数，且不知道它怎么使用时，可以用help()查看使用方法
#   from imp import reload
#   help(reload)