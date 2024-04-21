class TreeNode():
    def __init__(self, data):
        self.value = data
        self.LeftChild = None 
        self.RightChild = None 

class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 

class Queue():
    def __init__(self):
        self.linkedlist = LinkedList()
    
    def __str__(self):
        values = [str(_.value) for _ in self.linkedlist]
        return ' , '.join(values)
    
    def enqueue(self, value):  # Corrected method name
        newNode = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode 
        else:
            self.linkedlist.tail.next = newNode 
            self.linkedlist.tail = newNode 
            
    def isEmpty(self):  # Corrected method name
        return self.linkedlist.head == None

    def dequeue(self):  # Corrected method name
        if self.isEmpty():
            return "Nothing to dequeue"
        else:
            value_ = self.linkedlist.head.value 
            self.linkedlist.head = self.linkedlist.head.next 
            return value_ 
        
def getDeepestNodeValue(rootNode):
    if not rootNode:
        return None
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        deepestNode = None

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.LeftChild is not None:
                customQueue.enqueue(root.LeftChild)

            if root.RightChild is not None:
                customQueue.enqueue(root.RightChild)

        deepestNode = root 

        return deepestNode 


def delete_deepestNode(rootNode, dNode):
    if not rootNode:
        return rootNode
    else:
        customQueue = Queue() 
        customQueue.enqueue(rootNode) 
        
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root == dNode:
                root = None 

            if root.LeftChild is not None:
                if root.LeftChild == dNode:
                    root.LeftChild = None
                else:
                    customQueue.enqueue(root.LeftChild)
                
            if root.RightChild is not None:
                if root.RightChild == dNode:
                    root.RightChild = None
                else:
                    customQueue.enqueue(root.RightChild)
        
        return rootNode
    


def delete_Node(rootNode, target_value):
    if not rootNode:
        return "Tree is empty"
    
    queue = Queue()
    queue.enqueue(rootNode)
    target_node = None

    while not queue.isEmpty():
        current_node = queue.dequeue()
        if current_node.value == target_value:
            target_node = current_node

        if current_node.LeftChild:
            queue.enqueue(current_node.LeftChild)
        if current_node.RightChild:
            queue.enqueue(current_node.RightChild)

    if not target_node:
        return "Node not found"

    deepest_node = getDeepestNodeValue(rootNode)
    target_node.value = deepest_node.value
    delete_deepestNode(rootNode, deepest_node)

    return "Node deleted successfully"



def LevelOrder_Traversal(rootnode):
    if not rootnode:
        return "Tree is empty"

    result = []  # Accumulate the values of nodes in the traversal
    custom_queue = Queue()
    custom_queue.enqueue(rootnode)

    while not custom_queue.isEmpty():
        root = custom_queue.dequeue()
        result.append(root.value)  # Append the value of the current node to the result

        if root.LeftChild:
            custom_queue.enqueue(root.LeftChild)

        if root.RightChild:
            custom_queue.enqueue(root.RightChild)

    return result  # Return the list of values
                



root = TreeNode(data="N1")
leftChild = TreeNode(data="N2")
rightChild = TreeNode(data="N3")

root.LeftChild = leftChild
root.RightChild = rightChild
leftChild.LeftChild = TreeNode(data='N4')
leftChild.RightChild = TreeNode(data='N5')

root.LeftChild.LeftChild.LeftChild = TreeNode(data='N9')
root.LeftChild.LeftChild.RightChild = TreeNode(data='N10')

root.RightChild.LeftChild = TreeNode(data='N6')
root.RightChild.RightChild = TreeNode(data='N7')


print(getDeepestNodeValue(root).value)

new = delete_deepestNode(root, getDeepestNodeValue(root))

print(getDeepestNodeValue(new).value)


print(delete_Node(root , 'N4'))


print(LevelOrder_Traversal(root))