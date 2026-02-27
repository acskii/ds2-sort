# SELECTION SORT ALGORTIHM
# Written by: Galal Taman
# Author Details: 
#       ID: 9453
#       Group: 3
#       Section: 1
#

def selection_sort(array: list) -> list:
    # the outer loop runs n-1 times where n is the length of the array
    for i in range(len(array)-1):
        #assign the current index to the minimum index
        min_idx = i
        # the inner loop runs n-i-1 times where n is the length of the array and i is the current index
        # it searches for the minimum element in the unsorted side
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                #assign the index of the minimum element to min_idx
                min_idx = j
        # swap the minimum element with the current element
        array[i], array[min_idx] = array[min_idx], array[i]
        #now to the next iteration of the outer loop where the sorted side increases by one and
        #the unsorted side decreases by one

    # return the sorted array after the outer loop ends
    return array
