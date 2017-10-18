"""

Given a sequence, find the maximum subarray.
Returns (i, j, sum), where sequence[i..j] is a maximum subarray with that sum.

"""

def max_subarray(sequence):
	return max_subarray_helper(sequence, 0, len(sequence) - 1)


def max_subarray_helper(sequence, start, end):
	if start == end:
		return [start, end, sequence[start]]

	mid = int((start+end)/2)
	left = max_subarray_helper(sequence, start, mid)
	right = max_subarray_helper(sequence, mid+1, end)
	center = max_crossing_subarray(sequence, start, mid, end)
	if left[2] >= right[2] and left[2] >= center[2]:
		return left
	elif right[2] >= left[2] and right[2] >= center[2]:
		return right
	else:
		return center


def max_crossing_subarray(sequence, start, mid, end):
	left_sum = sequence[mid]
	total = 0
	max_left = mid
	for i in range(mid, -1, -1):
		total += sequence[i]
		if total > left_sum:
			left_sum = total
			max_left = i
	
	right_sum = sequence[mid+1]
	total = 0
	max_right = mid+1
	for i in range(mid+1, end):
		total += sequence[i]
		if total > right_sum:
			right_sum = total
			max_right = i
	return [max_left, max_right, left_sum + right_sum]
