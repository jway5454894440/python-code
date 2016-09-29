__author__ = 'guojiewei'

def lazy_sum(*args):
    def sum():
        num=0
        for i in args:
            num=num+i
        return num
    return sum

f=lazy_sum(1,3,5,7,9)
print(f)
print(f())