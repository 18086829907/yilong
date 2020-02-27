import multiprocessing

#子线程死循环
def myTest():
    while True:
        pass


def main():
    t1 = multiprocessing.Process(target=myTest)
    t1.start()

    while True:
        pass


if __name__ == '__main__':
    main()


#总结：通过htop看cpu的资源使用情况，两个核都被沾满
