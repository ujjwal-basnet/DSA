class Node:
    def __init__(self , value):
        self.value = value 
        self.next = None 
        
        
    def __str__(self):
        return str(self.value)
        

class Linkedlist:
    
    def __init__(self):
        self.head = None  
        self.tail = None 
        
    def __iter__(self):
        node = self.head
        while node :
            yield node 
            node = node.next 
        
        

class Queue:
    def __init__(self):
        self.linkedList = Linkedlist()
        
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' , '.join(values)
    
    #inserting value code 
    def enqueue(self , value ):
        newNode = Node(value)
        
        
        if self.linkedList.head ==  None :
            self.linkedList.head = newNode 
            self.linkedList.tail = newNode 
        
        else :
            self.linkedList.tail.next = newNode 
            self.linkedList.tail= newNode 
        

    def dequee(self):
        if self.linkedList.head is not None :
            value = self.linkedList.head 
            self.linkedList.head = self.linkedList.head.next 
            return value 


        
customQUeue = Queue()
print(customQUeue.enqueue(3))
print(customQUeue.enqueue(4))
print(customQUeue.enqueue(5))
print(customQUeue)
print(customQUeue.dequee())
print(customQUeue)
        



        
        
        