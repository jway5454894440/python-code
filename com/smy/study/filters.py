__author__ = 'guojiewei'

def is_odd(a):
    if(a%2==0):
        return True
    else:
        return False

print(filter(is_odd,[1,2,3,4,5,6,7,8]))