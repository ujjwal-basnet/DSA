class Bst():
    def __init__(self , data):
        self.data = data 
        self.Rchild= None 
        self.Lchild = None 


def Insert(rootNode , nodevalue):
    if rootNode.data == None :
        rootNode.data = nodevalue 
        
    
    elif nodevalue <= rootNode.data :  
        
        if rootNode.Lchild == None :
                

                rootNode.Lchild = Bst(nodevalue)
               
        
        else :
             Insert(rootNode= rootNode.Lchild , nodevalue= nodevalue )
            
    else :
        if rootNode.Rchild == None :
              rootNode.Rchild = Bst(nodevalue)
              
              
        else :
             Insert(rootNode= rootNode.Rchild , nodevalue= nodevalue )
    
    return "Node has been sucessfully inserted"


    
def PreORderTravesal(rootNode):
    if rootNode == None :
          return "Empty" 
     
    print(rootNode.data)
    PreORderTravesal(rootNode= rootNode.Lchild)
    PreORderTravesal(rootNode= rootNode.Rchild)


bst = Bst(70)
Insert(bst , 50)
Insert(bst , 90)
Insert(bst , 30)
Insert(bst , 60)
Insert(bst , 80)
Insert(bst , 100)
PreORderTravesal(bst)



