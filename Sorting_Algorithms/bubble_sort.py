
# Repeatedly compare adjacent elements and swap them if they are in the wrong order. 
#This process continues until the entire array is sorted


def bubble_sort(unosrted_list):
    total_elements = len(unosrted_list) 

    for i in range(total_elements -1 ):
        swapped = False 
        for currentindex in range(total_elements - i -1 ):
            if unsorted_list[currentindex] > unsorted_list[currentindex + 1 ] :
                #swap 
                unsorted_list[currentindex] , unsorted_list[currentindex + 1] = unsorted_list[currentindex + 1] , unsorted_list[currentindex]
                swapped = True 

        if not swapped :
            break 



# Example usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(unsorted_list)
print("Sorted list is:", unsorted_list)