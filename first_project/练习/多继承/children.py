from 练习.多继承.father import Father
from 练习.多继承.mother import Mother
class Children(Mother, Father): #父类中方法重名，默认子类继承在小括号中排位靠前的父类方法
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)
