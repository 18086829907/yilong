import re
names = ['name','name_','__name__','name1','Name','1name','哈哈', 'name_1_', 'name!', 'name#123']


for name in names:
    res = re.match('[a-zA-Z_]+[\w]*', name)
    if res:
        print(name,'符合变量命名规则')
    else:
        print(name,'不符合变量命名规则')