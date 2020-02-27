#分别执行01_02_03
#   通过htop观察得知
#       01沾满一个核
#       02沾满一个核
#       03沾满两个核
#   因此python中的多线程是假的多线程，根本就不能实现并行或并发，调高效率

#为什么python的线程时并行呢？
#   因为python的线程中有GIL
#   当一个线程在执行时，GIL使另一个线程在休息，
#   当另外一个线程执行时，GIL又让之前的线程休息

#GIL全局解释器锁
#   当程序执行多线程时，每个线程首先会去获取一个GIL全局解释器锁并且锁上，等待执行完毕释放资源后，再解开锁
#   这样就保证了同一时刻，只有一个线程在执行。
#   出现这个问题，并不是python语言的问题，而是执行python语言的解释器的问题

#GIL的产生
#   # python3 test.py
#       这个命令其实是python3执行了一个python语言的解释器，用这个解释器翻译test.py中的内容
#   python语言启动-翻译-执行的流程如下：
#       python程序
#       python解释器
#           解释器将代码翻译为机械码，即有0和1组成的机器码
#       CPU
#   python解释器版本解释
#       编写解释器的语言
#           c语言编写的，叫做cpython，它有GIL全局锁（因为最开始开发这个解释器的时候，吉多在当时根本没有考虑到电脑今后还可以并发，因此C语言编写的cpython就假如了全局锁，使同一时刻只能有一个线程在执行任务）
#           java编写的，叫做jpython，它无GIL全局锁
#   python官方推荐的解释器，默认的是cpython
#       因此python中的多线程，其实只是一个单线程程序

#因此之前说的：多进程占用资源多，可以考虑多线程。这句话其实要分使用解释器的版本
#   如果使用cpython，多进程就比多线程快
#   如果使用jpathon，多线程就比多进程快