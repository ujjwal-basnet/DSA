
class Stack:
    def __init__(self , maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(q) for q  in  self.list]
        return '\n'.join(values)
    
    #is Empty 
    def isEmpty(self):
        if self.list == []:
            return True 
        else :
            return False 
        
    #is full 
    def isFull(self):
        if (len(self.list)  ==  self.maxSize ) :
            return True 
        else :
            return False 
        
        
        
    #push 
    def push(self , value ):
        if self.isFull():
            return "Stack is already full"
        
        else :
            return self.list.append(value)
        
        
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        
        else :
            return self.list.pop()
        
        
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        
        else :
            return self.list[(len(self.list)- 1)]
        
    def delete(self):
        self.list = None 
    
            
            
        
        
            

            
customStack = Stack(2)
print(customStack)
customStack.push(3)
customStack.push(4)
customStack.push(5)
print(customStack)
customStack.pop()
print('\n' ,customStack.peek() )
print('\n' , customStack.peek())
print('\n' ,customStack.delete() )
    
    
        
        