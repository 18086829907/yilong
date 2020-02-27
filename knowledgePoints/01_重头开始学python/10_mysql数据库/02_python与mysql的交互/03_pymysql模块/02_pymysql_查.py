from pymysql import connect
import time


class JD():
    def __init__(self):
        self.conn = connect(host='192.168.70.136', port=3306, user='root', password='135cylpsx', database='jing_dong', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        '''显示全部商品'''
        self.execute_sql('select * from goods;')

    def show_cates(self):
        '''显示全部商品分类'''
        self.execute_sql('select name from goods_cate')

    def show_brands(self):
        '''显示全部商品品牌分类'''
        self.execute_sql('select name from goods_brand')

    @staticmethod
    def print_menu():
        print('---jd---')
        print('1:所有商品')
        print('2:所有商品分类')
        print('3:所有商品品牌分类')
        # print('4:根据输入的名字查询商品')
        op = input('请输入功能对应的数字：')
        return op

    def run(self):
        while True:
            op = self.print_menu()
            if op == '1':
                self.show_all_items()
            elif op == '2':
                self.show_cates()
            elif op == '3':
                self.show_brands()
            else:
                print('输入有误，请等待2秒重新输入')
                time.sleep(2)

def main():
    jd = JD()
    jd.run()

if __name__ == '__main__':
    main()