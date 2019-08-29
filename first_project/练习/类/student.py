from 练习.类.teacher import Teacher
class Student(Teacher):
    def __init__(self, name, age, stuId, money):
        #调用父类中的__init__(self):
        super(Student, self).__init__(name, age, money) #self代表子类实例对象，super将self传到父类的__init__(self)中，此时父类的self就是子类的实例化对象了，这个对象再调用父类中的__init__函数
        self.stuId = stuId #子类独有的属性

    def stufunc(self):
        print(self.__money)