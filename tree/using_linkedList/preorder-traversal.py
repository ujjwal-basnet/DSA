class TreeNode:
    def __init__(self , data ):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 
        
    

newBT = TreeNode(data = "Drink")
leftChild = TreeNode(data = "Hot")
rightChild = TreeNode(data = "Cold")
newBT.leftChild = leftChild 
newBT.rightChild = rightChild

#traversal function 

def preOrderTraversal(rootNode):
    if not rootNode :
        return 
    
     # print root Node 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
#printing 
preOrderTraversal(newBT)