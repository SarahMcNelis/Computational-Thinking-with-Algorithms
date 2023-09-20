# A second efficent comparison-based sort - Quick Sort
# Code sourced and adapted from <https://runestone.academy/ns/books/published/pythonds/SortSearch/TheQuickSort.html>
# and <https://www.geeksforgeeks.org/python-program-for-quicksort/#:~:text=The%20key%20process%20in%20quickSort,be%20done%20in%20linear%20time.>

# Main function.
def quick_sort(array):
    # See funciton below which is called here to help complete quick sort. 
    quick_sort_helper(array, 0, len(array)-1)
    return array

# Helper function.
def quick_sort_helper(array, first, last):
    # If first element is greater than the last find the halfway point 
    if first < last:
        halfway = partition(array, first, last)  
        # Now recursively call function again to sort both halves.
        quick_sort_helper(array, first, halfway-1)
        quick_sort_helper(array, halfway+1 ,last)

# a function to partition the array using the pivot element, 
def partition(array, first, last):
    # Pivot value is the first value in the array
    pivot_value = array[first]
    # The left mark is the first element of the remaining unsorted array hence first plus one. 
    left_mark = first+1
    # The right mark is the last element of the unsorted array.
    right_mark = last

    done = False
    while not done:
        # While the left mark is less than the right and less than the pivot 
        # move the left mark one to the right. 
        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        # While the right mark is greater than the pivot and the left mark
        # move the right mark one to the left.
        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark -1
        # If the right and left marks crossover then the function stops.
        if right_mark < left_mark:
            done = True
        else:
           # Otherwise swap the order. 
            array[left_mark], array[right_mark]  = array[right_mark], array[left_mark]
    # swap with the pivot value with the right mark.
    array[first], array[right_mark] = array[right_mark], array[first]

    return right_mark


# Test the function works.
#array = [104, 22, 25, 35, 4, 264, 91]
#quick_sort(array)
#print(array)