def riverSizes(matrix):
    # Write your code here.
	# array to store size of river
    sizes = []
	
	#loop through all of matrix
	for h in range(len(matrix)):
		for w in range(len(matrix[0])):
			#if 1 send to travers funct
			if matrix[h][w] == 1:
				matrix[h][w] = '*'
				travers(h, w, sizes, matrix)

	return sizes
	
def travers(h, w, sizes, matrix):
	get = [[h,w]]
	counter = 0
	while len(get) > 0:
		h, w = get.pop()
		fourlooker(h, w, matrix, get)
		counter += 1
	sizes.append(counter)

def fourlooker(h, w, matrix, get):
	ht = len(matrix) - 1
	wd = len(matrix[0]) - 1
	#up
	if h > 0: 
		if matrix[h - 1][w] != '*' and matrix[h - 1][w] == 1:
			get.append([h - 1, w])
			matrix[h - 1][w] = '*'
	#down
	if h < ht: 
		if matrix[h + 1][w] != '*' and matrix[h + 1][w] == 1:
			get.append([h + 1, w])
			matrix[h + 1][w] = '*'
	# right
	if w < wd:
		if matrix[h][w + 1] != '*' and matrix[h][w + 1] == 1:
			get.append([h, w + 1])
			matrix[h][w + 1] = '*'
	# left
	if w > 0:
		if matrix[h][w - 1] != '*' and matrix[h][w - 1] == 1:
			get.append([h, w - 1])
			matrix[h][w - 1] = '*'	