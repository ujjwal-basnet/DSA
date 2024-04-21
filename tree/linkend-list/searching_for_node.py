from queue import Queue 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def Searching_Node(rootNode, Nodevalue):
    if not rootNode:
        return "does not exist"  

    customQueue = Queue() 
    customQueue.put(rootNode)  # Enqueueing root node

    while not customQueue.empty():  # Checking if queue is empty
        root = customQueue.get()  # Dequeueing

        if root.data == Nodevalue:  # Checking current node's value
            return "success"  # Correcting string

        if root.leftchild is not None: 
            customQueue.put(root.leftchild)  # Enqueueing left child

        if root.rightchild is not None:
            customQueue.put(root.rightchild)  # Enqueueing right child

    return "Not Found" 


root = TreeNode(data="N1")
leftChild = TreeNode(data="N2")
rightChild = TreeNode(data="N3")

root.leftchild = leftChild
root.rightchild = rightChild
leftChild.leftchild = TreeNode(data='N4')
leftChild.rightchild = TreeNode(data='N5')

root.leftchild.leftchild.leftchild = TreeNode(data='N9')
root.leftchild.leftchild.rightchild = TreeNode(data='N10')

root.rightchild.leftchild = TreeNode(data='N6')
root.rightchild.rightchild = TreeNode(data='N7')

print(Searching_Node(rootNode=root, Nodevalue='N9')) 

print(Searching_Node(rootNode=root , Nodevalue= 'N11'))