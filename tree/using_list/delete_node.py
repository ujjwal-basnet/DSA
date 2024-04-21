class BinaryTree():
    def __init__(self, size):
        self.CustomList = size * [None]
        self.LastUsedINdex = 0 
        self.MaxSize = size 

    def insertNode(self , value ):
        if self.LastUsedINdex +1 == self.MaxSize :
            return "Tree is Full "
        
        else :
            self.CustomList[self.LastUsedINdex + 1 ]= value
            self.LastUsedINdex += 1 
            return "Insertition Sucessfully"
        


    def getDeepestNode(self):
        return self.CustomList[self.LastUsedINdex]
    
    def  delete_deepestNode(self):
        self.CustomList[self.LastUsedINdex] = None 

    
    def delete_node(self , dnode):
        if self.LastUsedINdex == 0 :
            return "Empty" 
        
        deepest_node  = self.getDeepestNode()

        for i in range(self.LastUsedINdex + 1 ):
            if self.CustomList[i] == dnode :
                self.CustomList[i] = deepest_node 
                self.delete_deepestNode()
                return "Deleted Sucessullys"
                

tree  = BinaryTree(5)
tree.insertNode("A")
tree.insertNode("B")
tree.insertNode("C")
tree.insertNode("D")
tree.delete_node("B")
print(tree.CustomList)
        