# An efficent comparison-based sort - Merge Sort
# Code sourced and adapted from <https://www.geeksforgeeks.org/merge-sort/>

def merge_sort(array):
	if len(array) > 1:

		# Floor divide length of array in half to get middle.
		middle = len(array)//2

		# Assigning elements to the left of middle to a variable. 
		left_half = array[:middle]

		# Assigning elements to the right of middle to a variable. 
		right_half = array[middle:]

		# Sorti the left. 
		merge_sort(left_half)

		# Sort the right.
		merge_sort(right_half)

        # left, right and merge array elements all equal to zero.
		i = j = k = 0

		# while the element of left and right is greater than zero.
		while i < len(left_half) and j < len(right_half):
            # if the left element is less than the right element
			if left_half[i] < right_half[j]:
                # add the left element to a temp array and move up an element. 
				array[k] = left_half[i]
				i += 1
			else:
                # othersie add the right element to the temp array and move up an element. 
				array[k] = right_half[j]
				j += 1
            # move temp array element up by one when an element is added.
			k += 1

		# Check if there are any elements left to check in both left and right. 
		while i < len(left_half):
			array[k] = left_half[i]
			i += 1
			k += 1

		while j < len(right_half):
			array[k] = right_half[j]
			j += 1
			k += 1
	return array


# Test the function works.
#array = [104, 22, 25, 35, 4, 264, 91]
#merge_sort(array)
#print(array)