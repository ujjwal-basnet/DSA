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
        

    def PostOrder(self , index ):
        if index > self.LastUsedIndex :
            return 
        
        self.PostOrder(index *2 )
        self.PostOrder(index *2 + 1 )
        print(self.CustomList[index])





tree  = BinaryTree(5)
tree.insertNode("A")
tree.insertNode("B")
tree.insertNode("C")
tree.insertNode("D")
print(tree.CustomList)
tree.PostOrder(1)