from father import Father
from mother import Mother
class Children(Mother, Father): #父类中方法重名，默认子类继承在小括号中排位靠前的父类方法
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)

children = Children(100, 100)
print(children.money)
# print(children.__money)  # __money未被继承
print(children.faceValue)
children.play()
children.getMoney()
# children.__openCar()  # __openCar()未被继承
children.accOpenCar()