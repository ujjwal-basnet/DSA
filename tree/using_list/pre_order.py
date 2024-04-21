# pre order travesal 
# root -> left node -> right node


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
        

    def PreOrder_Traversal(self  , index ):
        if index > self.LastUsedIndex :
            return 

        print(self.CustomList[index])
        print(self.PreOrder_Traversal(index*2))
        print(self.PreOrder_Traversal(index*2 + 1 ))

        
        
tree  = BinaryTree(5)
tree.insertNode("A")
tree.insertNode("B")
tree.insertNode("C")
tree.insertNode("D")
print(tree.CustomList)
tree.PreOrder_Traversal(1)