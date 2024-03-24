class Queue:
    def __init__(self):
        self.items = [] 
        
        
    def __str__(self):
        values = [str(w) for w in self.items]
        return "\n".join(values)
    
    
    def isEmpty(self):
        if self.items == []:
            return True 
        else :
            return False 
        
    
    def enqueue(self , value):
        self.items.append(value)
        return "The elements is inserted at the end of the queee"
        
        
    def dequeue(self):
        if self.isEmpty():
            return "The elements is inserted at the end of the Queue"
        else :
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "No Elements on Quee" 
        else :
            return self.items[0]
        
        
    def delete(self):
        if self.isEmpty():
            return "No Elements to deelete"
        else :
            self.items = None 
            return self.items


sampleQueue = Queue()
sampleQueue.enqueue(1)
sampleQueue.enqueue(2)
sampleQueue.enqueue(3)
sampleQueue.enqueue(4)
sampleQueue.enqueue(5)
print(sampleQueue)
print(sampleQueue.dequeue())
print(sampleQueue.peek())
print(sampleQueue.delete())


        