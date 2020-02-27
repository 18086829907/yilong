import threading

#子线程死循环
def myTest():
    while True:
        pass


def main():
    t1 = threading.Thread(target=myTest)
    t1.start()

    while True:
        pass


if __name__ == '__main__':
    main()


#总结：通过htop看cpu的资源使用情况，在两个核中各被占一半资源，总共沾满一个核资源