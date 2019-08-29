import unittest
from knowledgePoints import Person
class Test(unittest.TestCase):
    def test_init(self):
        p = Person('hanmeimei', 20)
        self.assertEqual(p.name, 'hanmeimei', '属性赋值有误') #断言不等于（属性， 正确值，如果得到的值不等于正确值则报错）
    def test_getAge(self):
        p = Person('hanmeimei', 20)
        self.assertEqual(p.getAge(), p.age, 'getAge函数有误')

if __name__ == '__main__':
    unittest.main()