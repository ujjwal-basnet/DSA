from queue import Queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None
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

def searchNode(rootNode, nvalue):
    if not rootNode:
        return False
    if rootNode.data == nvalue:
        return True
    elif nvalue < rootNode.data:
        return searchNode(rootNode.Lchild, nvalue)
    else:
        return searchNode(rootNode.Rchild, nvalue)

def getHeight(root):
    if not root:
        return 0
    return root.height

def rotateRight(root):
    newRoot = root.Lchild
    root.Lchild = newRoot.Rchild
    newRoot.Rchild = root
    root.height = 1 + max(getHeight(root.Lchild), getHeight(root.Rchild))
    newRoot.height = 1 + max(getHeight(newRoot.Lchild), getHeight(newRoot.Rchild))
    return newRoot

def rotateLeft(root):
    newRoot = root.Rchild
    root.Rchild = newRoot.Lchild
    newRoot.Lchild = root
    root.height = 1 + max(getHeight(root.Lchild), getHeight(root.Rchild))
    newRoot.height = 1 + max(getHeight(newRoot.Lchild), getHeight(newRoot.Rchild))
    return newRoot

def getBalance(root):
    if not root:
        return 0
    return getHeight(root.Lchild) - getHeight(root.Rchild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.Lchild = insertNode(rootNode.Lchild, nodeValue)
    else:
        rootNode.Rchild = insertNode(rootNode.Rchild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.Lchild), getHeight(rootNode.Rchild))
    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.Lchild.data:  # Left-Left case
        return rotateRight(rootNode)
    if balance > 1 and nodeValue > rootNode.Lchild.data:  # Left-Right case
        rootNode.Lchild = rotateLeft(rootNode.Lchild)
        return rotateRight(rootNode)
    if balance < -1 and nodeValue > rootNode.Rchild.data:  # Right-Right case
        return rotateLeft(rootNode)
    if balance < -1 and nodeValue < rootNode.Rchild.data:  # Right-Left case
        rootNode.Rchild = rotateRight(rootNode.Rchild)
        return rotateLeft(rootNode)

    return rootNode

# Example usage
newAVL = AVLNode(10)
newAVL = insertNode(newAVL, 5)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 3)
newAVL = insertNode(newAVL, 7)
newAVL = insertNode(newAVL, 20)

print("Pre-order traversal:")
preOrderTraversal(newAVL)

print("In-order traversal:")
inOrderTraversal(newAVL)

print("Post-order traversal:")
postOrderTraversal(newAVL)

print("Level-order traversal:")
levelOrderTraversal(newAVL)

print("Searching for value 7:", searchNode(newAVL, 7))