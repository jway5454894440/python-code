__author__ = 'guojiewei'


def reversort(x,y):
    if(x>=y):
        return -1
    else:
        return 1

print(sorted([1,3,2,7,5,4,6]))

print(sorted([1,3,2,7,5,4,6],reversort))