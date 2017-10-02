""" 

Takes a list of numbers as input, and outputs a permutation of that list which is sorted (in ascending order).

"""
def insertion_sort(numbers):
	for j in range(1, len(numbers)): # purposely skipping first entry of numbers
		key = numbers[j]
		# insert numbers[j] into the sorted sequence numbers[0, ..., j-1]
		i = j - 1
		while i >= 0 and numbers[i] > key:
			numbers[i+1] = numbers[i]
			i = i - 1
		numbers[i+1] = key
	return numbers


""" 

Takes a list of numbers as input, and outputs a permutation of that list which is sorted (in **descending** order).

"""
def insertion_sort2(numbers):
	for j in range(1, len(numbers)): # purposely skipping first entry of numbers
		key = numbers[j]
		# insert numbers[j] into the sorted sequence numbers[0, ..., j-1]
		i = j - 1
		while i >= 0 and numbers[i] < key:
			numbers[i+1] = numbers[i]
			i = i - 1
		numbers[i+1] = key
	return numbers
