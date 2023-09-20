# A simple comparison-based sort - Bubble Sort
# Code sourced and adapted from <https://www.geeksforgeeks.org/python-program-for-bubble-sort/>

def bubble_sort(array):
    # Looping through length of array from last to first index.
    for i in range(len(array)-1, 0, -1):
        for s in range(i):
            # if s is is greater than the next element/s+1 - swap them.
            if array[s] > array[s + 1]:
                array[s], array[s + 1] = array[s + 1], array[s]


# Test the function works.
#array =[104, 22, 25, 35, 4, 264, 91]
#bubble_sort(array)
#print(array)