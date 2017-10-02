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

So, 110 would be represented by [0, 1, 1], NOT [1, 1, 0]
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
