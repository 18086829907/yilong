import multiprocessing
import os
import time
#显示进度条原理
#   每个子进程一结束，就往队列里加1，主进程中一直取队列的值
#注意
#   如果使用进程池，子进程中的通讯Queue，只能用q = multiprocessing.Manage().Queue()，否则会出错。multiprocessing中的Manage()对象，再用实例化中的Queue()方法创建queue对象


def get_old_dirPath():
    '''
    获取要复制的文件夹，此文件需要放到要复制文件的同一目录中
    :return:
    '''
    current_path = os.curdir
    fileName_old = input('请输入要复制的文件夹名：')    #输入04的测试文件夹
    old_dir_abspath = os.path.join(current_path, fileName_old)
    return old_dir_abspath


def mkdir_cpye_dir():
    '''
    创建copydir，返回新copyDirPath and oldDirPath
    :return:
    '''
    old_dirPath = get_old_dirPath()
    new_dirName = input('请输入copy文件夹的名字：')
    new_dirPath = os.path.join(os.curdir, new_dirName)
    if not os.path.exists(new_dirPath):
        os.mkdir(new_dirPath)
    return old_dirPath, new_dirPath


def copyFile(fileName, old_dirPath, new_dirPath, q):
    old_file_abspath = os.path.join(old_dirPath, fileName)
    new_file_abspath = os.path.join(new_dirPath, fileName)
    with open(old_file_abspath, 'rb') as f:
        data = f.read()
    with open(new_file_abspath, 'wb') as f:
        f.write(data)
    q.put(fileName)


def main():
    old_dirPath, new_dirPath = mkdir_cpye_dir()
    q = multiprocessing.Manager().Queue()    #
    po = multiprocessing.Pool(8)
    fileNames = os.listdir(old_dirPath)
    for fileName in fileNames:
        po.apply_async(copyFile, args=(fileName, old_dirPath, new_dirPath, q))
    po.close()

    all_Num = len(fileNames)
    while True:
        fileName = q.get()
        if fileName in fileNames:
            fileNames.remove(fileName)
        finishedNum = all_Num - len(fileNames)
        Percentile = (finishedNum/all_Num)*100
        print('\r进度：{}/{}，{:.2f}%'.format(finishedNum,all_Num, Percentile), end="")
        #print()的end参数是在打印内容结尾处添加指定内容，其默认值是\n，设置为空则不换行。
        # \r表示将光标回到首位，打印是从光标位置打印，因此值会在当前行打印，感觉是动态效果
        if Percentile == 100:
            break

    print()    #Ubuntu中将命令输入行换行


if __name__ == '__main__':
    main()