# HEAP SORT ALGORTIHM
# Written by: Ahmed Abdul Moneim
# Author Details: 
#       ID: 9284
#       Group: 3
#       Section: 1
#

def heapify(arr,n,i):
    largest=i
    left = 2*i +1
    right = 2*i +2
    if left<n and arr[left] > arr[largest]:
        largest=left
    if right < n and arr[right]>arr[largest]:
        largest =right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def max_heap_sort(arr):
    n = len(arr)
    # make heap
    for i in range(n //2-1,-1,-1):
        heapify(arr,n, i)
      #take element by element
    for i in range(n -1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr
