



def sum100(n):
    if(n==1):
        return 1;
    else:
        return n+sum100(n-1)


def rabbit(month):
    if(month==1):
        return 1
    elif(month==2):
        return 1
    else:
        n= rabbit(month-1)+rabbit(month-2)
        return n


def rabbitarr(month):
    rabbits = [];
    for i in range (1,month+1,1):
        a= rabbit(i)
        rabbits.append(a)
    return  rabbits

       # print i
        #rabbits.pop(rabbit(i))
    #return  rabbits

#print rabbitsum(5)
#print (rabbit(6))
#print (sum100(100))
print  rabbit(5)
print(reduce(lambda x,y:x+y,rabbitarr(5)))
print (rabbitarr(5))