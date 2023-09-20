# A second simple comparison-based sorting algorithm - Insertion Sort
# Code sourced and adapted from <https://www.geeksforgeeks.org/insertion-sort/>

def insertion_sort(array):
	# For every element fron 1 to length of the array.
    # 1 and not 0 as all element will move one position to the right each time. 
	for i in range(1, len(array)):

		key = array[i]

        # Move elements greater than the key one position to right
		p = i-1
		while p >= 0 and key < array[p] :
				array[p + 1] = array[p]
				p -= 1
		array[p + 1] = key


# Test the function works.
#array = [104, 22, 25, 35, 4, 264, 91]
#insertion_sort(array)
#print(array)