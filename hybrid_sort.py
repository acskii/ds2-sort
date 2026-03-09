# MERGE AND SELECTION HYBRID SORT ALGORTIHM
# Written by: Andrew Sameh Adel Mikhail
# Author Details: 
#       ID: 9489
#       Group: 3
#       Section: 1
#

# The idea here is that you copy merge sort, but instead of adding the base case of:
#       If one element -> is sorted array -> return element to above call
# it is given a threshold parameter that if the array reached has its size == threshold, you sort that array 
# with selection sort then return to above call

# Using previously made selection sort
from selection_sort import selection_sort

# Merges 2 lists given and returns merged list
def merge(left, right):
    i, j = 0, 0
    merged = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def hybrid_sort(array, threshold):
    n = len(array)

    # Edge case of empty or one element list
    if (n <= 1):
        return array
    
    # Checks the threshold to decide if selection sort is carried
    if (n <= threshold):
        return selection_sort(array)
    
    # Split the array given into two
    # And sort both recursively
    mid = n // 2
    left = hybrid_sort(array[:mid], threshold)
    right = hybrid_sort(array[mid:], threshold)
        
    # Return the merged result
    return merge(left, right)