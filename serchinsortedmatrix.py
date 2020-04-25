def searchInSortedMatrix(matrix, target):
    # Write your code here.
    h, w = 0, (len(matrix[0]) - 1)
	while True:
		if h == (len(matrix[0]) - 1) or w == -1:
			return [-1,-1]
		val = matrix[h][w]
		if val == target:
			return [h, w]
		elif val < target:
			h += 1
		else:
			w -= 1