import requests

url = 'http://www.baidu.com/'

res = requests.get(url)

#response对象
#属性
print(res.encoding) #查看当前文档编码
res.encoding = 'uft8' #设置当前文档编码
print(res.text) #查看当前文档