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
        


sampleQueue = Queue()
Queue.push(1)
Queue.push(3)
Queue.push(4)
Queue.push(6)


        