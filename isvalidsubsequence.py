def isValidSubsequence(array, sequence):
    # Write your code here.
    p = 0
	l = len(sequence)
	for i in array:
		v = sequence[p]
		if i == v:
			p += 1
			if p == l:
				return True
	return False