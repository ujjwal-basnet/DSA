#creating 

class Node:
    def __init__(self , value ):
        self.value = value 
        self.next = None 
        

class SLikedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def __iter__(self):
        node = self.head 
        while node is not None :
            yield node 
            node = node.next 
            
    
    def insertLL(self , value , location):
        newNode = Node(value)
        if self.head == None :
            self.head = newNode 
            self.tail = newNode 
        
        else :
            
            if location == 0 :
                newNode.next = self.head 
                self.head = newNode 
                
            elif  location == -1 :
                newNode.next = None 
                self.tail.next =  newNode
                self.tail = newNode 
                
            else :
                tempNode = self.head
                index = 0 
                while index < location -1 :
                    tempNode = tempNode.next 
                    index = index + 1 
                
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode = nextNode.next 
                if tempNode == self.tail :
                    self.tail = newNode 
                
                
    # start from here 
    
    def deletion(self ,value ,location):
        node = self.head 
        if node is None :
            return "No Linked List "
        
        else  :
            if location == 0 :
                if self.head == self.tail :
                    self.head = None 
                    self.tail = None 
                else :
                    self.head = self.head.next 
            
            
            elif location == -1:
                if self.head == self.tail :
                    self.head = None 
                    self.tail = None 
                else :
                    node = self.head 
                    while node is not None : 
                        if node.next == self.tail:
                            break
                        
                        node = node.next 
                    node.next = None 
                    self.tail = node 
                        
                        
                        
                        
                
                    

                 
                
                
                
        
        
        
            
            
        