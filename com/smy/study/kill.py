

def kill(cur,personold):
    if (len(personold)<=1):
        return  personold
    print personold
    length=len(personold)
    i=0
    duce=0;
    for  person in range(1,length+1,1):
        cur=cur+1
        i=i+1
        if(i<length):
            if(cur%3==0):
                personold.pop(i-1-duce)
                duce=duce+1
        else:
            if(cur%3==0):
               personold.pop(i-1-duce)
               duce=duce+1
               kill(0, personold)
            elif(cur%3==1):
                kill(1,personold)
            else:
                kill(2,personold)
    return  personold

personold=[1,2,3,4,5,6,7,8,9]
print (kill(0,personold))
