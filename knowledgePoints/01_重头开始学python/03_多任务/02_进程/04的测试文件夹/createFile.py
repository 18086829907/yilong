import os
path = os.curdir
for i in range(1,101):
    filePath = os.path.join(path, '{}.py'.format(i))
    with open(filePath, 'w') as f:
        f.write(str(i))