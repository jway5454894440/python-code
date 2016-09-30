__author__ = 'guojiewei'


def cal():
    fs = []
    for i in range(1, 4):
        def cal2():
            return i*i
        fs.append(cal2)
    return fs
f1, f2, f3 = cal()
print(f1(), f2(), f3())



def calnew():
    fs = []
    for i in range(1, 4):
        def calnew1(j):
            def calnew2():
                return j*j
            return calnew2
        fs.append(calnew1(i))
    return fs

f4, f5, f6 = calnew()
print(f4(), f5(), f6())



