import multiprocessing
import os


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


def main():
    old_dirPath, new_dirPath = mkdir_cpye_dir()
    q = multiprocessing.Queue(10)
    po = multiprocessing.Pool(5)
    for fileName in os.listdir(old_dirPath):
        po.apply_async(copyFile, args=(fileName, old_dirPath, new_dirPath, q))

    po.close()
    po.join()    #一定先写

if __name__ == '__main__':
    main()


