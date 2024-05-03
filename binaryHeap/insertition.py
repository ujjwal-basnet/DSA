class Heap:
    def __init__(self ,size):
        self.customList = size * [None]
        self.maxSize = size + 1 
        self.heapSize = 0 



    def heapifTreeInsert(self , index , heapType):
        parentIndex = int(index/2)
        if index <= 1 :
            return 
        
        if heapType == 'Min':

            if self.customList[index] < self.customList[parentIndex]:
                temp = self.customList[index]
                self.customList[index] = self.customList[parentIndex]
                self.customList[parentIndex] = temp 

            self.heapifTreeInsert(self , parentIndex , heapType= heapType)

        else :
            if heapType == 'Max':
                if self.customList[index] > self.customList[parentIndex]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[parentIndex]
                    self.customList[parentIndex] = temp

            self.heapifTreeInsert(self , parentIndex , heapType= heapType)


    def insert(self , nvalue , heapType):

        if self.heapSize  == 0 :
            return 
        else :
            self.customList[len(self.heapSize)]

