"""
here we repeatedly , find the minimum element and move it to the sorted part of array to make unsorted part sorted"""


def insert(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1 # previous elements
        # check if key is greater than previous  elements if yes then swap
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1 
        arr[j+1] = key
    

    print(arr)  



arr = [ 5 , 3 , 9 , 1 , 2 , 8 , 4 , 7 , 6 , 5, 6 ,5 , 20 ]
insert(arr)