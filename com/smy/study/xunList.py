__author__ = 'guojiewei'
class Node():
    def __init__(self,val,nt = None):
        self.value = val
        self.next = nt
class xunList():
    def __init__(self):
        self.headNode = Node(None,None)
        self.headNode.next = self.headNode
        self.head  = self.headNode
        self.size = 0
    def  __str__(self):
        if self.size ==  0:
            return 'empty'
        s = ''
        fin = self.head.next.next
        while fin.value:
            s += str(fin.value)
            if fin.next.value:
                s += ','
            fin = fin.next


        return s

    def addElement(self,value):
        elementNode = Node(value,None)
        if self.head.value ==  None:
            elementNode.next = self.headNode
            self.head.next = elementNode
            self.head = elementNode
            self.size += 1
        else:
            elementNode.next = self.headNode
            self.head.next = elementNode
            self.head = elementNode
            self.size += 1

    def search(self,index):
        if self.size == 0:
            return 'empty'
        if index > self.size:
            return 'out of index'
        i = 0
        se = self.head.next
        while i <= self.size:
            if i == index:
                break
            se = se.next
            i += 1
        return se.next.value

    def query(self,index):
        if self.size == 0:
             return 'empty'
        if index > self.size:
            index=(index-self.size)
        i=0
        se = self.head.next
        while i<=self.size:
            if i== index:
                break
            se =se.next
            i+=1
        return se.next.value



    def delete(self,data):
        if self.size == 0:
            return 'empty'
        de = self.head
        cur = self.head.next
        while cur != self.head:
            if cur.value ==  data:
                break
            de = cur
            cur = cur.next
        if cur  == self.head:
            return
        de.next = cur.next
        self.size -= 1

    def kill(self):
        for i in range(0,self.size,1):
            if(i%3==0):
                self.delete(self.search(i))
                print(self.search(i))
            self.kill()
        return  self






if __name__=="__main__":
    x = xunList()
    x.addElement(1)
    x.addElement(2)
    x.addElement(3)
    x.addElement(4)
   # x.kill()
    for i in range(0,x.size+5,1):
        print(x.query(i))