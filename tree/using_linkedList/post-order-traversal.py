
class TreeNode:
    def __init__(self , data ):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 
        
        
newBT = TreeNode(data ="Drink")
leftChild = TreeNode(data = "Cold")
rightChild = TreeNode(data = "Hot")


newBT.leftChild = leftChild 
newBT.rightChild = rightChild 


def  postOrderTraversal(rootNode):
    if not rootNode:
        return "Empyty"
    
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
       
        
        
postOrderTraversal(newBT)