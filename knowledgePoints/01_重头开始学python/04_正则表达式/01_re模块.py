import re
#re.match(r'正则表达式','要处理的字符串')    #从头匹配数据，match自带^

obj =  re.match(r'速度与激情\d', '速度与激情8')
#如果正则表达式匹配到了后面的字符串内容，则会返回一个对象，反之不返回
print(obj.group())


print(re.match(r'速度与激情\d', '速度与激情8').group())