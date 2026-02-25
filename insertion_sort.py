# INSERTION SORT ALGORTIHM
# Written by: Andrew Sameh Adel Mikhail
# Author Details: 
#       ID: 9489
#       Group: 3
#       Section: 1
#

def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        # select element from unsorted side
        key = array[i]
        j = i - 1
        
        # Keep shifting between elements in sorted side
        # to get place for selected element
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        # add selected element to its correct place
        array[j + 1] = key
    
    return array