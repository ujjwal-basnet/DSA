#create a linked list where we can insert values first 


class Node:
    def __init__(self , value):
        self.value = value 
        self.next = None 
        
        

class SlinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        
    def __iter__(self):
        node = self.head 
        while node :
            yield  node 
            node = node.next 
            
    def insertSLL(self,  value , location):
        newNode  = Node(value)
        if self.head == None :
             self.head = newNode
             self.tail = newNode 
             
        else :
            if location == 0 :
                newNode.next = self.head 
                self.head = newNode 
                
            elif  location ==-1 :
                newNode.next = None 
                self.tail.next = newNode
                self.tail = newNode 
                
            else : 
                tempNode = self.head 
                index = 0 
                while index < location -1 :
                    tempNode = tempNode.next
                    index = index +1 
                    
                nextNode = tempNode.next 
                tempNode.next = newNode 
                newNode.next = nextNode 
                if tempNode == self.tail :
                    self.tail = newNode 
    #starting 
    def traversal_fun(self):
        if self.head is None :
            print("none")
        else :
            
            #loop all the nodes 
            node = self.head 
            while node is not None :
                print(node.value)
                node = node.next
            
                        
                        
                        

singlyLinkedList  = SlinkedList()


singlyLinkedList.insertSLL(10 , 0 )
singlyLinkedList.insertSLL(2 , 1)
singlyLinkedList.insertSLL(3 , 1)
singlyLinkedList.insertSLL(4 , 1)
singlyLinkedList.insertSLL(5 , -1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.traversal_fun()
    
                        
                    
                
                
        
        