# from common import RECV_DATA_LIST
# from common import HANDLE_FLAG  # ①这样的方式导入的HANDLE_FLAG是一个全局变量
import common


def handle_data():
    '''
    模拟处理recv_msg模块接收的数据
    :return:
    '''
    print('--->handle_data')
    for i in common.RECV_DATA_LIST:
        print(i)

    # 既然处理完成了，那么将变量HANDLE_FLAG设置为True，意味着处理完成
    # global HANDLE_FLAG  # ③局部变量需要修改全局变量的值，需要加global
    # HANDLE_FLAG = True  # ②如果不加global，这里的HANDLE_FLAG是一个局部变量

    common.HANDLE_FLAG = True


def test_handle_data():
    '''
    测试处理是否完成，变量是否设置为True
    :return:
    '''
    print('--->test_handle_data')
    if common.HANDLE_FLAG:  # ④此时的HANDLE_FLAG是全局变量，已经被handle_data()修改为了True
    # if common.HANDLE_FLAG:
        print('====已处理完成====')
    else:
        print('====未处理完成====')