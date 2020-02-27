from pymysql import connect
import time


class JD():
    def __init__(self):
        self.conn = connect(host='192.168.70.136', port=3306, user='root', password='135cylpsx', database='jing_dong', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_select_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def execute_commit_sql(self, sql):
        self.cursor.execute(sql)
        while True:
            confirm = input('是否提交')
            if confirm == '是':
                self.conn.commit()
                break
            elif confirm == '否':
                self.conn.rollback()  # 回滚，取消所有的execute执行的sql语句
                break
            else:
                print('输入有误请重新输入,只能输入【是】或【否】')

    def show_all_items(self):
        '''显示全部商品'''
        self.execute_select_sql('select * from goods;')

    def show_cates(self):
        '''显示全部商品分类'''
        self.execute_select_sql('select name from goods_cate')

    def show_brands(self):
        '''显示全部商品品牌分类'''
        self.execute_select_sql('select name from goods_brand')

    def add_cate(self):
        '''添加商品分类'''
        item_name = input('请输入新商品分类:')
        sql = "insert into goods_cate(name) value ({})".format(item_name)
        self.execute_commit_sql(sql)

    def add_brand(self):
        '''添加品牌分类'''
        item_name = input('请输入新品牌：')
        sql = "insert into goods_brand(name) value ({})".format(item_name)
        self.execute_commit_sql(sql)

    @staticmethod
    def print_menu():
        print('---jd---')
        print('1:所有商品')
        print('2:所有商品分类')
        print('3:所有商品品牌分类')
        print('4:添加一个商品分类')
        op = input('请输入功能对应的数字：\n')
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
            elif op == '4':
                self.add_cate()
            elif op == '4':
                self.add_brand()
            else:
                print('输入有误，请等待2秒重新输入')
                time.sleep(2)

def main():
    jd = JD()
    jd.run()

if __name__ == '__main__':
    main()