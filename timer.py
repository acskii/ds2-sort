# TIMER
# Record algorithm running time
# Written by: Andrew Sameh Adel Mikhail
# Author Details: 
#       ID: 9489
#       Group: 3
#       Section: 1
#

import random
import time

def record_running_times(sort_functions: list, sizes: list) -> None:
    for size in sizes:
        # Generate a random array of integers for each size
        data = [random.randint(0, size * 10) for _ in range(size)]

        print("-" * 40)
        print(f"Generated Array Size: {size:<11,}")
        print("-" * 40)
        print(f"{'Sort Algorithm':<20} | {'Time Taken (ms)':<10}")
        print("-" * 40)
        
        for sort_function in sort_functions:
            # Record start time
            start_time = time.time()
                        
            # Sort the array
            sort_function(data)
                        
            # Record end time and calculate duration
            end_time = time.time()
            duration = (end_time - start_time) * 1000
                        
            print(f"{sort_function.__name__:<21}| {duration:<10}")