from a import *
print(age)
fun()

print(_age)  # NameError：name'_age' is not defined
_fun()  # NameError: name '_fun' is not defined

#为什么要私有化，因为有些变量名在一个模块中作为全局变量在使用，如果导入到另一个.py后，有同样的变量名就会冲突，因此直接私有化全局变量，不导入即可