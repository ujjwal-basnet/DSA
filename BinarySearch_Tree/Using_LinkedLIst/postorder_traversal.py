
class Bst():
    def __init__(self  , data ):
        self.data = data 
        self.Lchild = None 
        self.Rchild = None 

def Insert( rootNode , nvalue) :
    if rootNode == None :
        rootNode.data = nvalue
        return 
    else :
        if nvalue <= rootNode.data :
            if rootNode.Lchild is None :
                rootNode.Lchild = Bst(nvalue)
                return "added "

            else :
                Insert(rootNode= rootNode.Lchild , nvalue = nvalue)


        if nvalue >= rootNode.data :
            if rootNode.Rchild is None :
                rootNode.Rchild = Bst(nvalue)
            else :
                Insert(rootNode= rootNode.Rchild , nvalue = nvalue)


def postOrderTraversal(rootNode ):
       if rootNode == None :
           return "Empty"
       
       postOrderTraversal(rootNode=  rootNode.Lchild)
       print(rootNode.data)
       postOrderTraversal(rootNode= rootNode.Rchild)



    
bst = Bst(70)
Insert(bst , 50)
Insert(bst , 90)
Insert(bst , 30)
Insert(bst , 60)
Insert(bst , 80)
Insert(bst , 100)

postOrderTraversal(bst )