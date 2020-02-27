class FBLQ_num(object):
    def __init__(self, num):
        self.a = 0
        self.b = 1
        self.num = num
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.a , self.b = self.b , self.a+self.b
        if self.i < self.num:
            self.i += 1
            return self.a
        else:
            raise StopIteration

fblq_num = FBLQ_num(10)
fblq_list = list()
fblq_list.append(fblq_num.a)

for j in fblq_num:
    fblq_list.append(j)
print(fblq_list)