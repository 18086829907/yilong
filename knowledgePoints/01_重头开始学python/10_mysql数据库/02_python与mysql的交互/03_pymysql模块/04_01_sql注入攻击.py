from pymysql import connect
import time

#sql注入
#   在查询栏中输入：'or 1=1 or'  /  "or 1=1 or"
#   就能查出此栏中所有的信息
#原因
#   查询卫衣的信息
#       select * from goods where name='卫衣'
#   sql注入后的语句
#       select * from goods where name=''or 1=1 or''
#       因为只要where后面判定为True的信息都会显示
#       or将判定语句分为三段：
#           name='' 所有信息都不能匹配
#           1=1     1=1恒为True，因此所有信息都能显示
#           ''      所有信息都不能匹配

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

    def get_info_by_name(self):
        find_name = input('请输入要查询的商品名字：')
        # select * from goods where name="r510vc 15." or 1=1 or "16英寸笔记本";
        #" or 1=1 or "
        #' or 1=1 or '
        sql = """select * from goods where name="{}";""".format(find_name)
        self.execute_select_sql(sql)

    @staticmethod
    def print_menu():
        print('1:根据名字查询一个商品')
        op = input('请输入功能对应的数字：')
        return op

    def run(self):
        while True:
            op = self.print_menu()
            if op == '1':
                self.get_info_by_name()
            else:
                print('输入有误，请等待2秒重新输入')
                time.sleep(2)

def main():
    jd = JD()
    jd.run()

if __name__ == '__main__':
    main()