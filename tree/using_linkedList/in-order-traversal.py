class TreeNode:
    def __init__(self , data ):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 
        
    
#create class  instance 


root = TreeNode(data = "N1")
leftChild = TreeNode(data = "N2")
rightChild = TreeNode(data = "N3")

root.leftChild = leftChild 
root.rightChild = rightChild 
leftChild.leftChild = TreeNode(data = 'N4')
leftChild.rightChild  = TreeNode(data = 'N5')

root.leftChild.leftChild.leftChild = TreeNode(data = 'N9')
root.leftChild.leftChild.rightChild = TreeNode(data = 'N10')


root.rightChild.leftChild = TreeNode(data = 'N6')
root.rightChild.rightChild = TreeNode(data = 'N7')

def inorder_traversal(rootNode):
    
    if not rootNode :
        return 
    inorder_traversal(rootNode.leftChild)
    print(rootNode.data)
    inorder_traversal(rootNode.rightChild)
        
    
 
inorder_traversal(root) 





#manually checking 

# print("\n \n ")
# print(root.data)
# print(root.leftChild.data)
# print(root.rightChild.data)





# print("\n \n ")

# print(root.leftChild.leftChild.data)
# print(root.leftChild.rightChild.data)

# print("\n \n ")
# print(root.rightChild.data)
# print(root.rightChild.leftChild.data)
# print(root.rightChild.rightChild.data)

# print("\n \n ")

# print(root.leftChild.leftChild.data)
# print(root.leftChild.leftChild.leftChild.data)
# print(root.leftChild.leftChild.rightChild.data)