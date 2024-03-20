#check-out my medium for explanation 

class Node():
    def __init__(self , value = None ):
        self.value = value 
        self.next = None 
        
    
class SLinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None
        
        
        
singlyLinkednlist  =SLinkedList()
node1 = Node(1)
node2 = Node(2)
    
    
singlyLinkednlist.head = node1 
singlyLinkednlist.head.next =  node2 
singlyLinkednlist.tail = node2 

print(singlyLinkednlist.head)
print(singlyLinkednlist.head.next)
print(singlyLinkednlist.tail)
print(list(dir(singlyLinkednlist)))