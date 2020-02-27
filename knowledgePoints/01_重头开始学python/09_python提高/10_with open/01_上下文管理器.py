#具有__enter__,__exit__方法的类，叫做上下文管理器
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('entering')
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self):
        print('will exit')
        self.f.close()
if __name__ == '__main__':
    with File('out.txt', 'w') as f:
        print('writing')
        f.write('hello python')

#with流程
#   File()创建一个实例对象，并且自动执行__init__
#   with 首先判断 File() 是否是上下文管理器的实例对象，即类中是否包含__enter__,__exit__
#   如果是，则调用__enter__方法，open()创建一个文件对象，最后将文件对象返回给f，即让f指向这个文件对象
#   f文件对象就能调用write方法将内容写入到文件中
#   如果在写入的过程中出现了异常，with会立刻去调用File类中的__exit__方法，关闭文件对象
#   如果没有异常，等待写入完毕后，也会调用__exit__方法，关闭文件对象


#因此with，除了可以用open，还可以放自定义的上下文管理器类


#对于系统资源如文件、数据库连接、socket，这些资源都很稀缺，也很重要，如果不能保证打开之后，一定会关闭
#   系统的资源枯竭后，系统将无法为其他应用服务。如果是服务器，你的套接字资源枯竭，意味着客户端不发再连接服务器
#   因此，with很重要