def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    # 0 array of n + 1
	value = [float('inf') for i in range(n + 1)]
	# sort denoms
	denoms.sort()
	# set index 0 to 0
	value[0] = 0
	# loop through denoms
	for denom in denoms:
	# for each i loop through zeros starting at i
		for i in range(denom, n + 1):
	# subtract subtract zero i from i and and take min
			value[i] = min(value[i], value[i - denom] + 1)
	if value[-1] == float('inf'):
		return -1
	return value[-1]
