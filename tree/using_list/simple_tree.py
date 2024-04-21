
class BinaryTree():
    def __init__(self , size):
        self.customList  = size  * [None]
        self.LastUsedIndex = 0  ## for the ease of calcuation we are not using first index 
        # and  left child is calcuate dby 2x  where as right child is calculated as 2x+1 where 
        # x is the index of corresponding root rootnode (may be 1st root node or 2,3,..)
        self.maxSize =  size 



tree = BinaryTree(5)
print(tree)
        
print(tree.maxSize)
