import math             # for ceiling function
import merge_sort as ms # for an exercise

"""

Finds the first occurence of a given value v in a given sequence.
Returns -1 if v is not in the sequence

"""
def find(sequence, v):
	for i in range(0, len(sequence)):
		if sequence[i] == v:
			return i
	return -1

"""

Given two lists, A and B, which represent binary numbers with the same # of digits (i.e. A = [1, 0, 1] and B = [1, 1, 1]), this outputs a list C representing their sum.

NOTE: Numbers are backwards!

So, 110 would be repres ented by [0, 1, 1], NOT [1, 1, 0]
If this really annoys you, add some code which reverses inputs, does the algorithm, reverses C, then returns. It's just easier to not do that.

"""

def sum(a, b):
	n = len(a)
	c = []
	# initalize c with zeroes
	# is there an easier way to do this?
	# c++ can do it super easy, and usually python's the one doing things easy
	for x in range(0, n+1):
		c.append(0)

	# actual algorithm
	for i in range(0, n):
		c[i] = a[i] + b[i] + c[i]
		if c[i] == 2:
			c[i+1] = 1
			c[i] = 0
		if c[i] == 3:
			c[i+1] = 1
			c[i] = 1
	return c

"""

Sorts the given sequence.

"""
def selection_sort(sequence):
	for i in range(0, len(sequence)):
		smallest = i
		for j in range(i, len(sequence)):
			if sequence[j] < sequence[smallest]:
				smallest = j
		if smallest != i:
			temp = sequence[i]
			sequence[i] = sequence[smallest]
			sequence[smallest] = temp
	return sequence

"""

Searches a sorted sequence for an element

"""
def binary_search(sequence, v, n = 0, m = None):
	if m == None:
		m = len(sequence) - 1

	if n > m:
		return -1
	elif sequence[n] == v:
		return n
	elif n == m:
		return -1

	x = math.ceil((m+n) / 2)

	if sequence[x] == v:
		return x
	elif sequence[x] > v:
		return binary_search(sequence, v, n, x-1)
	else:
		return binary_search(sequence, v, x+1, m)

"""

Given a list of numbers and a number x, it finds if any two numbers in the list sum to x.

"""
def sum_exists(sequence, x):
	sequence = ms.merge_sort(sequence)
	for i in range(0, len(sequence)):
		complement = binary_search(sequence, x-sequence[i])
		if complement == i:
			if i+1 < len(sequence) and sequence[i] == sequence[i+1]:
				return True
			else:
				continue
		if complement != -1:
			return True
	return False

"""

Sorts stuff.

"""
def bubblesort(sequence):
	for i in range(0, len(sequence) - 1):
		for j in range(len(sequence) - 1, i, -1):
			if sequence[j] < sequence[j-1]:
				temp = sequence[j]
				sequence[j] = sequence[j-1]
				sequence[j-1] = temp
	return sequence
