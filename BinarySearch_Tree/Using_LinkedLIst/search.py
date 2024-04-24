class Bst:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None

def Insert(rootNode, nvalue):
    if rootNode is None:
        rootNode = Bst(nvalue)
    elif nvalue <= rootNode.data:
        if rootNode.Lchild is None:
            rootNode.Lchild = Bst(nvalue)
        else:
            Insert(rootNode=rootNode.Lchild, nvalue=nvalue)
    else:
        if rootNode.Rchild is None:
            rootNode.Rchild = Bst(nvalue)
        else:
            Insert(rootNode=rootNode.Rchild, nvalue=nvalue)
    return rootNode

def search(rootNode, item):
    if rootNode is None:
        print("Empty tree")
        return None
    elif rootNode.data == item:
        print("Value is found")
        return rootNode
    elif item < rootNode.data:
        return search(rootNode.Lchild, item)
    else:
        return search(rootNode.Rchild, item)

# Create the root node
bst = Bst(70)

# Insert values into the BST
bst = Insert(bst, 50)
bst = Insert(bst, 90)
bst = Insert(bst, 30)
bst = Insert(bst, 60)
bst = Insert(bst, 80)
bst = Insert(bst, 100)

# Search for values
search(bst, 80)
search(bst, 80)
search(bst, 100)