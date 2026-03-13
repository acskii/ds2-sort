# KTH SMALLEST ELEMENT ALGORTIHM
# Written by: Galal Taman
# Author Details: 
#       ID: 9453
#       Group: 3
#       Section: 1
#

import random

# Find the Kth smallest element within an array by using the partition method of the quick sort.
# Example given in assignment: [3, 41, 16, 25, 63, 52, 40] -> if k = 3 then return 25

# If you need a separate function for the partitioning
def partition(array, l, h):
    # Choose a random pivot index between low and high
    random_index = random.randint(l, h)
    # Swap the pivot element with the last element
    array[h], array[random_index] = array[random_index], array[h]
    # Pivot is now at index h
    pivot = array[h]
    #i is the end index of the SMALLER section
    i = l - 1
    #j is the beginning index of the UNKOWN section
    for j in range(l, h):
        #if the current element in the UNKOWN section is smaller than the pivot
        if array[j] <= pivot:
            #then we increment i
            i += 1
            #and we SWAP array[i] and array[j]
            array[i], array[j] = array[j], array[i]
    #return the pivot to its correct position
    array[i + 1], array[h] = array[h], array[i + 1]
    #return the pivot index
    return i + 1


def k_smallest(array, k):
    l = 0
    h = len(array) - 1
    k = k - 1
    
    #keep partitioning until we find the pivot at index k (0-indexed)
    while True:
        pivot = partition(array, l, h)
        if pivot == k:
            return array[pivot]
        #adjust the bounds of the array to search in targeted areas only
        elif pivot < k:
            l = pivot + 1
        else:
            h = pivot - 1