class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.leftchild = None 
        self.rightchild = None


class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return ' , '.join(values)
    
    # Inserting values 
    def enqueue(self, value):
        new_node = Node(value)

        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node 
        else:
            self.linked_list.tail.next = new_node 
            self.linked_list.tail = new_node 
    
    # Removing values 
    def dequeue(self):
        if self.linked_list.head is not None:
            value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return value
        else:
            return "Queue is empty"

    def isEmpty(self):
        return self.linked_list.head is None


def LevelOrder_Traversal(rootnode):
    if not rootnode:
        return
    
    custom_queue = Queue()
    custom_queue.enqueue(rootnode)
    
    while not custom_queue.isEmpty():
        root = custom_queue.dequeue()
        print(root.data)
        
        if root.leftchild:
            custom_queue.enqueue(root.leftchild)
            
        if root.rightchild:
            custom_queue.enqueue(root.rightchild)


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

LevelOrder_Traversal(root)
