#simple tree class 

class TreeNode:
    def __init__(self , data , children = []):
        self.data = data 
        self.children = children 
        
    def __str__(self , level = 0 ):
        ret = " " * level + str(self.data) + '\n'
        for child in self.children :
            ret += child.__str__(level +1 ) 
        return ret 
    
    def addChildren(self , TreeNode):
        self.children.append(TreeNode)
        
        

tree  = TreeNode ('Drink' , [])
cold =  TreeNode('Cold' , [])
hot  = TreeNode('hot' , [])  

#untill here we have 3 node and doest have any relation between them 
tea = TreeNode('tea' , [])
cofee = TreeNode('cofee' , [])


#cold 
fanta  = TreeNode=('fanta' , [])

tree.addChildren(cold)
tree.addChildren(hot)


hot.addChildren(tea)
hot.addChildren(cofee)

cold.addChildren(fanta)

print(tree)