
class stack:
    def __init__(self):
        self.list = []
        

            
    def __str__(self):
        values = self.list.reverse()
        values = [str(w) for w  in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True 
        else :
            return False 
        
    def push(self , value):
        self.list.append(value)
        return "The element has been sucessfully inserted "
    
    def pop(self ):
        if self.isEmpty():
            return "There is not any element in the stack"
        
        else : 
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "There is not any elements in the stack"
        else :
            return self.list[len(self.list) - 1 ] #return last element from stack overflow 
        
        
    def delete(self):
        if self.isEmpty():
            return "There is not any elements in the stack"
        
        else : 
            self.list = []
            return self.list
        
        
        
        
        
        
        
a = stack()
print(a.isEmpty())
a.push(1)
a.push(2)
a.push(4)
a.push(5)
print(a)
a.pop()
a.pop()
print('\n')
print(a)
print('\n' , a.peek())
print('\n' , a.delete())