class TreeNode:
    def __init__(self , data ):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 
        
    
#create class  instance 
root = TreeNode(data = "Drink")
leftChild = TreeNode(data = "Cold")
rightChild = TreeNode(data = "Hot")
root.leftChild = leftChild 
root.rightChild = rightChild 


def inorder_traversal(rootNode):
    
    while not rootNode :
        return 
    inorder_traversal(  rootNode.leftChild)
    print(rootNode.data)
    inorder_traversal(rootNode.rightChild)
    
    

inorder_traversal(root)