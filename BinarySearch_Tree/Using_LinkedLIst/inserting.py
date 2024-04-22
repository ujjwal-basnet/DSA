class Bst():
    def __init__(self , data ):
        self.data = data 
        self.LeftChild = None 
        self.RightChild = None  
    

def InsertNode(rootNode , nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue 
    
    elif rootNode.data >= nodeValue :
        if rootNode.LeftChild  == None  :
            rootNode.LeftChild = nodeValue 

            return "left child added"
        
        else :
            InsertNode(rootNode=rootNode.LeftCHild , nodeValue = nodeValue) 


    else :
        if rootNode.RightChild == None :
            rootNode.RightChild = nodeValue 
            return " Right child added"
        
        else :
            InsertNode(rootNode=rootNode.RightChild , nodeValue = nodeValue ) 



    

newBst = Bst(50)
print(newBst.data)


print(InsertNode(newBst , 45))
print(newBst.LeftChild)