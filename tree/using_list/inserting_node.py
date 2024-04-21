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
        

tree = BinaryTree(5)
print(tree.insertNode("vs"))
print(tree.insertNode("afasdfas"))
print(tree.CustomList)