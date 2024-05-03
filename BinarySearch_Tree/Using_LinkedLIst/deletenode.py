from  queue import Queue


class Bst():
   
    def __init__(self , data ):
        self.data = data 
        self.LeftChild = None 
        self.RightChild = None  

    
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


def getDeepestNode(rootNode):

    if rootNode is None :
        return None 


    while rootNode.Rchild is not None :




        