__author__ = 'guojiewei'

i=1
rt = 1
while rt >= 0.5:
    rt *= (1-i/365.0)
    i += 1

print ("people is: %s" %i)