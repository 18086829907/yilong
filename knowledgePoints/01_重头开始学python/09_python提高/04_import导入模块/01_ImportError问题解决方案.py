#导入的方式
#    import xxx
#    import xxx, yyy
#    import xxx as x
#    from xxx import yyy
#    from xxx import yyy as y
#    from xxx import yyy, zzz
#    from xxx import *

#查看搜搜包路径的先后顺序
import sys
for i in sys.path:
    print(i)
#sys.path返回列表，导入包时，python会遍历sys.path返回列表，从第一个路径开始搜索是否有需要导入的包名，如果有则导入
#顺序为：当前路径，当前路径的上一级，当前路径的上二级，直到该当前路径的顶层路径，....
#当所有的路径都没有找到要导入的包名，则ImportError

#改变列表的顺序，或插入、添加指定搜索路径
sys.path.append(r'/home/surface/xxx')
sys.path.insert(0, r'/home/surface/xxx')

#当你在开发过程中，导入一个包，总是包ImportError，但你确定已经安装过这个包，你就可以将这个包的路径插入到这个列表中，就能导入了