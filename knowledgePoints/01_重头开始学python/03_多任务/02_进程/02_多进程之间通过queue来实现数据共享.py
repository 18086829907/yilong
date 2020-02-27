import multiprocessing


def download_from_web(q):
    '''
    下载数据
    :return:
    '''
    #模拟从网上下载的数据
    data = [1,2,3,4,5,6,7]
    for i in data:
        q.put(i)


def analysis_data(q):
    '''
    数据分析
    :return:
    '''
    #模拟数据分析
    myData = list()
    while True:
        data = q.get()
        myData.append(data)
        if q.empty():
            break
    print(myData)


#总结
#    q = multiprocessing.Queue()
#    q.put()     #写入数据
#    q.get()     #读取数据
#    q.full()    #队列是否为满
#    q.empty()   #队列是否为空


def main():
    q = multiprocessing.Queue(10)
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()