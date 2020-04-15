def kadanesAlgorithm(array):
    # Write your code here.
	# create a tracker -inf
	counter = array[0]
    # loop through array starting at index 1
	for i in range(1, len(array)):
	# check if array[i] + array[i - 1] > array[i]
		if array[i] + array[i - 1] > array[i]:
			# if it is insert i + i - 1
			array[i] = array[i] + array[i - 1]
		# if not take i
		if array[i] > counter:
			counter = array[i]
	return counter
