from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

if __name__ == '__main__':
    with my_open('out.txt', 'w') as f:
        f.write('hello python')

# 定义一个含有yield的普通函数，用contextmanager装饰器修改这个函数，就能将这个函数变成上下文管理器
# whth 判断 my_open()是否为上下文管理器
# 如果是，则执行到yield，yield返回的文件对象，会给到f
# 如果在写入过程中发现异常，则with会执行yield之后的代码