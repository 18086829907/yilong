import re
import os
#创建文件件
pathDir = r'D:\qian_feng_education\learn video\官网\物联网\5、数据库开发入门到精通\第{}章'
for i in range(1, 3):
    os.mkdir(pathDir.format(i))

#读取并提取千锋html的mp4
path = r'D:\qian_feng_education\first_project\finishedObject\千锋视频爬取\数据库开发入门到精通.html'
with open(path, 'rb') as f:
    html = f.read().decode('utf-8')
regular = re.compile(r'http://.*.mp4')
re_Url = regular.findall(html)

#url写入文件

#单章节

# toPath = r'D:\qian_feng_education\learn video\官网\物联网\1、物联网常见问题答疑\a.txt'
# for i in re_Url:
#     with open(toPath, 'a') as f:
#         f.write(i + '\n')

#多章节
#保存到哪个目录
toPath = r'D:\qian_feng_education\learn video\官网\物联网\5、数据库开发入门到精通\第{}章\a.txt'
num = 0 #num控制一章中的章节范围存入哪个文件夹
for i in re_Url:
    if num >= 1 and num <=18:
        with open(toPath.format('1'), 'a') as f:
            f.write(i+'\n')
    elif num >= 19 and num <= 28:
        with open(toPath.format('2'), 'a') as f:
            f.write(i+'\n')
    # elif num >= 35 and num <= 52:
    #     with open(toPath.format('3'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 53 and num <= 64:
    #     with open(toPath.format('4'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 65 and num <= 71:
    #     with open(toPath.format('5'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 57 and num <= 59:
    #     with open(toPath.format('6'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 60 and num <= 84:
    #     with open(toPath.format('7'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 85 and num <= 89:
    #     with open(toPath.format('8'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 90 and num <= 103:
    #     with open(toPath.format('9'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 104 and num <= 114:
    #     with open(toPath.format('10'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 115 and num <= 127:
    #     with open(toPath.format('11'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 128 and num <= 140:
    #     with open(toPath.format('12'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 141 and num <= 148:
    #     with open(toPath.format('13'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 119 and num <= 126:
    #     with open(toPath.format('14'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 127 and num <= 136:
    #     with open(toPath.format('15'), 'a') as f:
    #         f.write(i+'\n')
    # elif num >= 137 and num <= 142:
    #     with open(toPath.format('16'), 'a') as f:
    #         f.write(i+'\n')
    num += 1
