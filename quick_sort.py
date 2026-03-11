# QUICK SORT ALGORTIHM
# Written by: Andrew Sameh Adel Mikhail
# Author Details: 
#       ID: 9489
#       Group: 3
#       Section: 1
#

import random

# Assuming that you need to get pivot by partitioning in a separate function
# NOTE: You must choose the pivot randomly. DO NOT use array[l] for example.
# You can use random.randint(l, h) or random.choice(array) to pick the pivot
def partition(array, l, h):
    i, j = l - 1, h + 1
    pivot = array[random.randint(l, h)]
    
    while True:
        while True:
            i += 1
            if (array[i] >= pivot): break

        while True:
            j -= 1
            if (array[j] <= pivot): break
            
        if (i >= j): break
        
        array[i], array[j] = array[j], array[i]
        
    array[j], array[l] = array[l], array[j]
    return j
    
def req(array, l, h):
    if (l < h):
        j = partition(array, l, h)
        req(array, l, j)
        req(array, j+1, h)    
    
def quick_sort(array):
    req(array, 0, len(array) - 1)