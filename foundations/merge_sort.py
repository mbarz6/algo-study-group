"""

Given a sequence such that sequence[p..q] and sequence[q+1..r] are sorted, this returns sequence but with sequence[p..r] being sorted.

"""
def merge(sequence, p, q, r):
	left = sequence[p:q+1]
	right = sequence[q+1:r+1]

	i = 0
	j = 0
	for k in range(p, r+1):
		# range checking
		if i >= len(left):
			sequence[k] = right[j]
			j += 1
		elif j >= len(right):
			sequence[k] = left[i]
			i += 1
		elif left[i] < right[j]:
			sequence[k] = left[i]
			i += 1
		else:
			sequence[k] = right[j]
			j += 1
	return sequence

"""

Given a sequence, returns the sequence but with sequence[p..q] sorted

"""
def merge_sort(sequence, p = 0, q = None):
	if q == None:
		q = len(sequence) - 1

	if p < q:
		x = int((p+q)/2)
		sequence = merge_sort(sequence, p, x)
		sequence = merge_sort(sequence, x+1, q)
		sequence = merge(sequence, p, x, q)
	return sequence

