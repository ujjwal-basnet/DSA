from queue import Queue 

class TreeNode:
    def __init__(self , data):
        self.data = data 
        self.leftchild = None 
        self.rightchild = None 


def insert_Node(rootNode , NewNode ):
    if not rootNode :
        return  

    else :
        customQueue = Queue()
        customQueue.put(rootNode)
        while not(customQueue.empty()):
            root  = customQueue.get()

            if root.leftchild is not None :
                customQueue.put(root.leftchild)

            else :
                root.leftchild = NewNode
                print(root.leftchild.data)  # Print the data of the newly inserted node
                break
            
            if root.rightchild is not None :
                customQueue.put(root.rightchild)
            
            else :
                root.rightchild = NewNode
                print(root.rightchild.data)  # Print the data of the newly inserted node
                break


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


newNode = TreeNode("ujjwal")
insert_Node(root  , newNode)
