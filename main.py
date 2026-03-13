# TEAM DETAILS
# Ahmed Abd Al Moneim
# Details: 
#       ID: 9284
#       Group: 3
#       Section: 1
#
# Andrew Sameh
# Details:
#       ID: 9489
#       Group: 3
#       Section: 1
#
# Galal Mohamed
# Details:
#       ID: 9453
#       Group: 3
#       Section: 1
#
# -------------------------
# MAIN PROGRAM
# Written by: Andrew Sameh
# Author Details:
#       ID: 9489
#       Group: 3
#       Section: 1

from hybrid_sort import hybrid_sort
from timer import record_running_times
from quick_sort import quick_sort
from k_smallest import k_smallest
from merge_sort import merge_sort
from heap_sort import max_heap_sort

def main():
    sizes = [5000, 10000, 20000, 50000, 75000, 100000]
    sorts = [quick_sort, merge_sort, max_heap_sort]
    record_running_times(sorts, sizes)

if (__name__ == "__main__"):
    main()