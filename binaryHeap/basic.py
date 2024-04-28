class Heap:
    def __init__(self , size):
        self.customList = (size + 1 ) * [None]
        self.heapsize = 0
        self.maxsize = float('inf')  # Set to a large value for dynamic growth

    def peek(self):
        if self.heapsize == 0:
            return "Empty"
        else:
            return self.customList[1]

    def sizeofHeap(self):
        return self.heapsize

    def LevelOrderTraversal(self):
        if self.heapsize == 0:
            return "Empty"
        else:
            for i in range(1, self.heapsize + 1):
                print(self.customList[i])

newBinaryTree = Heap(5)
print(newBinaryTree.sizeofHeap())
print(newBinaryTree.LevelOrderTraversal())