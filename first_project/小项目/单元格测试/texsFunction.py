from knowledgePoints import mySum
from knowledgePoints import mySub
import unittest

class Test(unittest.TestCase):
    def setUp(self): #正式开发时：可以写入链接数据库的函数
        print('开始测试时，自动调用')
    def teatDown(self): #正式开发时：可以写入断开数据库的函数
        print('结束测试时自动调用')
    def test_mySum(self): #为了测试mySum
        self.assertEqual(mySum(1, 2), 3, '加法有误') #断言相等（被测函数，正确值， 有误则提醒）
    def test_mySub(self):
        self.assertEqual(mySub(2, 1), 1, '减法有误')

if __name__ == '__mian__':
    unittest.main()