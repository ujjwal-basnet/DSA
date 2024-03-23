#inorder to delete entire LL you need to set head and tail reference to None   , 
# since the chin does have any reference poining as head or tail , garbage collector will delete all the elements 

#checkout medium for more exampls 

#create a node contaning next value 
class  Node:
    def __init__(self , value  = None ):
        self.value = value 
        self.next = None 

class SLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        
    def __iter__(self):
        node = self.head
        while node :
            yield node 
            node = node.next 
            
            
    def insertSLL(self , value , location):
        newNode = Node(value)
        if self.head == None :
            self.head = newNode
            self.tail = newNode
             
        else : 
            if location == 0  :
                newNode.next = self.head 
                self.head  = newNode 
                
            elif location == -1 :
                newNode.next = None   
                self.tail.next = newNode
                self.tail = newNode
                
            else :
                tempNode = self.head 
                index =   0 
                while index < location -1 :
                    tempNode = tempNode.next 
                    index = index + 1 
                
                nextNode = tempNode.next 
                tempNode.next = newNode 
                newNode.next = nextNode 
                if tempNode == self.tail :
                    self.tail = newNode 



#deleting code 
    def delete(self ) :
        if self.head == None :
            return "SLl doesnt exist "
        else : 
            self.head = None 
            self.tail = None 
            
#creating likend list 
singlyLinkedList  = SLinkedList()


singlyLinkedList.insertSLL(10 , 0 )
singlyLinkedList.insertSLL(2 , 1)
singlyLinkedList.insertSLL(23 , 1)
singlyLinkedList.insertSLL(23 , 1)



print([node.value for node in singlyLinkedList])

singlyLinkedList.insertSLL(3 , -1 )

print([node.value for node in singlyLinkedList])

singlyLinkedList.insertSLL(4 , 2)

print([node.value for node in singlyLinkedList])

                    
                    
singlyLinkedList.delete()
print([node.value for node in singlyLinkedList])

                    
                    
                    
                    
            
            
            
            
            
            
            
            
                
        
                
                
                