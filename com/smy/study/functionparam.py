__author__ = 'guojiewei'

def power(a):
    return a*a
print(power(5))

def power(a,b=3):
    s=a
    while b>1:
        b=b-1
        s=s*a
    return s
print(power(5))
print(power(5,2))