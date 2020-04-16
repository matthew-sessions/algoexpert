def hasSingleCycle(array):
    # Write your code here.
    l = len(array)
	counter = 0
	index = array[0] % l
	while counter < l:
		if array[index] == 'x':
			return False
		counter += 1
		shift = (index + array[index]) % l
		array[index] = 'x'
		index = shift
	return True
		