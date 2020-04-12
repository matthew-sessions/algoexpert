def maxSubsetSumNoAdjacent(array):
    # Write your code here.
	# set first and second var
	l = len(array)
	if l == 0:
		return 0
	if l <= 1:
		return array[0]
	if l <= 2:
		return max(array)
	first = array[0]
	second = max(array[0],array[1])
	
	# loop through array starting at 2
	for i in array[2:]:
		added = i + first
		first = second
		second = max(second, added)
	return second