 #creating linked list 
 
class Node:
     def __init__(self , value):
         self.value = value 
         self.next = None 
     
 
 
class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
         
         
    def __iter__(self):
        node  = self.head 
        if node is not None :
            yield node 
        node  = node.next 
        
    
class  Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

        
    def isEmpty(self):
        if self.LinkedList.head == None :
            return True 
        else :
            return  False 
        
    def push(self , value):
        newNode = Node(value)
        newNode.next = self.LinkedList.head 
        self.LinkedList.head = newNode
        
        
    def pop (self):
        
        
        if self.isEmpty():
            return Stack 
        else :
            nodevalue = self.LinkedList.head.value 
            self.LinkedList.head = self.LinkedList.head.next
            return nodevalue
            
        
        
    def delete(self):
        self.LinkedList.head = None 
        



# Create a stack instance
stack = Stack()

# Test isEmpty method
print("Is stack empty?", stack.isEmpty())  # This should print True

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Test isEmpty method again
print("Is stack empty?", stack.isEmpty())  # This should print False

# Test pop method
print("Popped element:", stack.pop())  # This should print 3
print("Popped element:", stack.pop())  # This should print 2

# Test delete method
stack.delete()

# Test isEmpty after deletion
print("Is stack empty?", stack.isEmpty())  # This should print True
