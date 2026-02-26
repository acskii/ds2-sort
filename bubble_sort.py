# BUBBLE SORT ALGORTIHM
# Written by: Ahmed Abdul Moneim
# Author Details: 
#       ID: 9284
#       Group: 3
#       Section: 1
#

def bubble_sort(array: list) -> list:
    n= len(array)
    for i in range(n):
      for j in range(n-i-1):
         if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
    return array
