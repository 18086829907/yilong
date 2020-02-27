# from common import RECV_DATA_LIST  # 多模块开发时不用这种
# from common import HANDLE_FLAG  # 多模块开发时不用这种
import common  # 本质是在本地模块新建一个变量common，让它指向common模块，所有的到入方式都用import，避免变量指向不明确的问题

def recv_msg():
    '''模拟接收到数据，然后添加到common模块中的列表中'''
    print('--->recv_msg')
    for i in range(5):
        common.RECV_DATA_LIST.append(i)

def test_recv_data():
    '''测试接收到的数据'''
    print('--->test_recv_data')
    print(common.RECV_DATA_LIST)

def recv_msg_next():
    '''已经处理完毕后，再接收另外的数据'''
    print('--->recv_msg_next')
    if common.HANDLE_FLAG:
    # if common.HANDLE_FLAG:
        print('----发现之前的数据已经处理完毕，这里进行接收其他的数据（模拟过程...）----')
    else:
        print('----发现之前的数据未处理完毕，等待中...----')