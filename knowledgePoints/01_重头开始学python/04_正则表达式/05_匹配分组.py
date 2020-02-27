# |       # 匹配|左右任意一个表达式
# (ab)    # 将括号中的字符作为一组，并且可以单独取出小括号的值
# \num    # 引用分组号匹配到的字符串
#   re.match(r'<(\w*)>.*</\1>', '<h1>haha</h1>')    #\1 = （\w*）
#   re.match(r'<(\w*)><(\w*)>.*</2></\1>', '<body><h1>haha</h1></body>')    #\1 = 第一个（\w*）    #\2 = 第二个（\w*）
# (?P<name>表达式)    #分组起别名
#   re.match(r'<(？P<num1>\w*)><(?P<num2>\w*)>.*</(?P=num2)></(?P=num1)>', '<body><h1>haha</h1></body>')

import re

res = re.match(r'[a-zA-Z0-9_]{4,20}@(163|qq|126)\.(com|cn)$', 'laowang@163.com')
if res:
    print(res.group())
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
else:
    print('未匹配到数据')