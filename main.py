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
#       ID: <id here>
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

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from timer import record_running_times

def main():
    sizes = [5000, 10000, 20000, 50000, 75000, 100000]
    sorts = [bubble_sort, selection_sort, insertion_sort]
    record_running_times(sorts, sizes)

if (__name__ == "__main__"):
    main()