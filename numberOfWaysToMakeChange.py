def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    # create a array of zeros for len n + 1
	arr = [0] * (n + 1)
	# update the first index as 1
	arr[0] = 1
	# loop through denoms
	for i in denoms:
		for index in range(i, n + 1):
		# loop through zeros starting at index i in demons
		# subract i zeros from i demons add to zero i
			if i <= n:
				arr[index] += arr[index - i]
			
	return arr[-1]