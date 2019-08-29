import os
def oneDirToOtherDir(path, toPath, fileNum, toFileNum):
    fileList = os.listdir(path)
    contents = []
    for fileName in fileList[fileNum:toFileNum]:
        absPath = os.path.join(path, fileName)
        with open(absPath, 'r') as f:
            data = f.read()
            contents.append(data)
        #os.remove(absPath)
    contentNum = 0
    for fileName in fileList:
        absToPath = os.path.join(toPath, fileName)
        with open(absToPath, 'w') as f:
            f.write(contents[contentNum])
        contentNum += 1

path = r'D:\qian_feng_education\first_project\test\file'
toPath = r'D:\qian_feng_education\first_project\test\toFile'
oneDirToOtherDir(toPath, path, 0, 20)