# A non-comparison sort- Counting Sort
# Code sourced and adapted from <https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php>
# and from <https://www.geeksforgeeks.org/counting-sort/>
# and <https://www.programiz.com/dsa/counting-sort>

def counting_sort(array):
    # Count array to store each element - initalized as zero to the max value of the orgional array. 
    count_array = [0 for i in range(max(array)+1)]
    # Empty var for sorted elements.
    sorted_arr = []
    
    # each time an element appears in the array - add 1 to count_array
    for e in array:
        count_array[e] += 1  

    # For every element while count is greater than zero.
    for e in range(0, (len(count_array))):             
        while count_array[e] > 0:
            # Add the element to sorted array
            sorted_arr.append(e)
            # And decrease the count by 1 each time. 
            count_array[e] -= 1
    return sorted_arr


# Test the function works.
#array = [104, 22, 25, 35, 4, 264, 91]
#counting_sort(array)
#print(array)