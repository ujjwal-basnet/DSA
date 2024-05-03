from queue import Queue

class AVLNode:
    def __init__(self , data):
        self.data = data 
        self.Lchild = None 
        self.Rchild  = None 
        self.height = 1 

def preOrderTraversal(rootnode):
    if not rootnode:
        return 
    
    print(rootnode.data)
    preOrderTraversal(rootnode.Lchild)
    preOrderTraversal(rootnode.Rchild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.Lchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.Rchild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.Lchild)
    postOrderTraversal(rootNode.Rchild)
    print(rootNode.data)

def levelOrderTraversal(rootnode):
    if not rootnode:
        return 
    
    customQueue = Queue()
    customQueue.put(rootnode)
    while not customQueue.empty():
        root = customQueue.get()
        print(root.data)

        if root.Lchild is not None:
            customQueue.put(root.Lchild)

        if root.Rchild is not None:
            customQueue.put(root.Rchild)

def searchNode(rootNode , nvalue):
    if not rootNode:
        return False
    
    if rootNode.data == nvalue:
        return True
    elif nvalue < rootNode.data:
        return searchNode(rootNode.Lchild, nvalue)
    else:
        return searchNode(rootNode.Rchild, nvalue)

# Example usage
newAVL = AVLNode(10)
newAVL.Lchild = AVLNode(5)
newAVL.Rchild = AVLNode(15)
newAVL.Lchild.Lchild = AVLNode(3)
newAVL.Lchild.Rchild = AVLNode(7)
newAVL.Rchild.Rchild = AVLNode(20)

print("Pre-order traversal:")
preOrderTraversal(newAVL)

print("In-order traversal:")
inOrderTraversal(newAVL)

print("Post-order traversal:")
postOrderTraversal(newAVL)

print("Level-order traversal:")
levelOrderTraversal(newAVL)

print("Searching for value 7:", searchNode(newAVL, 7))
