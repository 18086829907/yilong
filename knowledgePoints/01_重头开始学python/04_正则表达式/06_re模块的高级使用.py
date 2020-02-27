import re


#search
res = re.search(r'\d+', '阅读量为 9999').group()    #search不一定是从头匹配，可以是任意位置，但是匹配到第一个且只匹配一个就返回，也就是不能取多个
print(res)

#拓展，search达到match功能
#   res = re.search(r'^\d+', '阅读量为 9999').group()


#findall
res = re.findall(r'\d+', '阅读量为：999，下载量为：88')    #findall从任意位置匹配，将匹配到的所有数据存入列表并返回
print(res)


#sub
res = re.sub('\d+','998','python = 997，c++ = 1024')
print(res)
#流程：
#   用正则表达式去字符串中去匹配，匹配到的所有的值都被参数2中的值替换,最后返回替换后的字符串


#sub的参数2支持函数引用
def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)
res = re.sub('\d+', add, 'python = 997')
print(res)
#流程说明
#   1、用正则表达式去匹配字符串，
#   2、匹配到值后，自动调用参数2绑定的函数，并且将匹配到的值传入函数
#   3、可以用group()取值，最后返回的值会去替换到原字符串
#   4、最终将替换后的字符串返回并复制给res


#split
res = re.split(r':| ','info:xiaoZhang 33 shandong')    #正则表达式切割，用:号和空格去切割字符串，返回列表
print(res)
