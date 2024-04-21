class BinaryTree():
    def __init__(self , size):
        self.CustomList = size * [None]
        self.LastUsedIndex = 0 
        self.MaxSize = size 


    def insertNode(self , value ):
        if self.LastUsedIndex +1 == self.MaxSize :
            return "Tree is Full "
        
        else :
            self.CustomList[self.LastUsedIndex + 1 ]= value
            self.LastUsedIndex += 1 
            return "Insertition Sucessfully"
        

    
# i am going to insert list by my own thus , i will only focus on inserting
    def search(self , value):
        index = 0 
        if  index + 1 != self.MaxSize  :
            while index  + 1 != self.MaxSize :
                 if self.CustomList[index + 1  ] ==  value :
                     return f"Found on {index +1}"
                 
                 else :
                     index  += 1 


        
tree  = BinaryTree(5)
tree.insertNode("A")
tree.insertNode("B")
tree.insertNode("C")
tree.insertNode("D")
print(tree.CustomList)
print(tree.search("C"))
print(tree.search("D"))

