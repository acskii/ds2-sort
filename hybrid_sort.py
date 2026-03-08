# MERGE AND SELECTION HYBRID SORT ALGORTIHM
# Written by: <name>
# Author Details: 
#       ID: <id>
#       Group: 3
#       Section: 1
#

# The idea here is that you copy merge sort, but instead of adding the base case of:
#       If one element -> is sorted array -> return element to above call
# it is given a threshold parameter that if the array reached has its size == threshold, you sort that array 
# with selection sort then return to above call

# If you are to reuse previous selection sort
import selection_sort

# Not sure if you need separate implementation of selection sort or not, so you can modify how you want
def select(array):
    return array

def hybrid_sort(array, threshold):
    return array