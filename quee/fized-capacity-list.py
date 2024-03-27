#quee 


class Quee:
    def __init__(self ,  maxSize ):
        self.items = maxSize *[None]
        self.start  = -1  
        self.top = -1
        self.maxSize = maxSize
        
         
    def __str__(self):
        
        values = [str(w) for w in self.items]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.start == -1:
            return True
        else :
            return False
        
    
    def isFull(self):
         if self.top +1 == self.start :
             return True 
         
         
         
         elif self.start == 0 and self.top +1 ==self.maxSize:
             return True 
         
         else :
             return False
        
        
    def enqueue(self , value ):
        if self.isFull():
            return "QUee is full"
        
        else :
            if self.top +1 == self.maxSize:
                self.top = 0 
            else :
                self.top  = self.top + 1 
                if self.start == -1 :
                    self.start = 0 
                    
            self.items[self.top] = value
            return "ELements has been inserted"
        
        
        
    def dequeue(self):
        
        if self.isEmpty():
            return "Quee is Empty"
        
        else :
             self.items.pop(0)
             return self.items
           

    def peek(self):
        if self.isEmpty():
            return "QUee is Empty"
        else :
            firstElement = self.items[self.start]
            start = self.start 
            if self.start  == self.top :
                self.start = -1 
                self.top = -1 
            
            elif  self.start + 1 == self.maxSize:
                start.start = 0 
                
            else :
                self.start = self.start + 1 
                self.items[start] = None
                
                return firstElement
                    
            
            
        
            
     

customQuee = Quee(3)
print(customQuee.isEmpty())
print(customQuee.isFull())
print(customQuee.enqueue(3))
print(customQuee.enqueue(4))
print(customQuee.enqueue(5))
print(customQuee.items)
print(customQuee.isEmpty())
print(customQuee.isFull())

print(customQuee.dequeue())
print(customQuee)
print(customQuee.peek())