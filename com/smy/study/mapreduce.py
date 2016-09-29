__author__ = 'guojiewei'

def cal(a):
    return a*a;

print(map(lambda a:a*a,[1,2,3,4,5]))

print(reduce(lambda x,y:x+y,[1,2,3,4,5]))

print(reduce(lambda x,y:x+y,map(lambda x:x*x,[1,2,3,4,5])))