# Merge SORT ALGORTIHM
# Written by: Ahmed Abdul Moneim
# Author Details: 
#       ID: 9284
#       Group: 3
#       Section: 1
#

def merge_sort(arr):
    #base-case check##
    if len(arr)>1:
        mid=len(arr) //2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i=0 
        j=0
        k=0
        while i<len(L) and j<len(R): #sorting the left and right lists
            if L[i] < R[j]:
                arr[k] = L[i] 
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k +=1
        # check if elements left in left
        while i <len(L):
            arr[k]=L[i]
            i +=1
            k +=1
        #any elements left in right
        while j <len(R):
            arr[k]=R[j]
            j+=1
            k +=1
    return arr
