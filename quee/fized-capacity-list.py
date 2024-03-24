#this is fixed capacity queue 

class Queue:
    def __init__(self  ,maxSize):
        self.items = maxSize * None 
        self.maxSize = maxSize 
        self.start = -1 
        self.top = -1 
        
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return '\n'.join(values)
    
    def isFull(self):
        if self.top == self.start + self.top:
            return True 
        elif (self.start == 0 ) and (self.top == self.maxSize):
            return True 
        else :
            return False 
        
        
    def isEmpty(self):
        if self.top == -1 and self.start == -1 :
            return "The queue is empty "
    

        