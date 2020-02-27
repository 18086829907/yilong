from pymysql import *

# cs.fetchone()
# cs.fetchmany()
# cs.fetchall()

def main():
    #创建连接对象
    conn = connect(host='192.168.70.136', port=3306, user='root', password='135cylpsx', database='jing_dong', charset='utf8')
    #创建游标对象
    cursor1 = conn.cursor()

    count = cursor1.execute('select * from goods;')
    print('查询到{}条数据'.format(count))

    # 注意cursor1中存储的数据，取一次少一次

    # #1、fetchone 返回一条元组
    # for i in range(count):
    #     # 获得查询的结果
    #     result = cursor1.fetchone()  # fetchone 每次从游标中查询出一条数据，类似next()
    #     print(result)

    # 2、fetchmany(3) 返回元组，元组中包含三条数据元组
    # result = cursor1.fetchmany(3)
    # print(result)

    # 3、fatchall() 返回元组，元组中包含所有数据元组
    result = cursor1.fetchall()
    print(result)

    #关闭游标对象
    cursor1.close()
    #关闭连接对象
    conn.close()

if __name__ == '__main__':
    main()