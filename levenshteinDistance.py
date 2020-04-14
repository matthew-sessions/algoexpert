def levenshteinDistance(str1, str2):
    # Write your code here.
    # create 2d array l of str1 and 2
	data = [[a for a in range(i, i + len(str2) + 1)] for i in range(len(str1) + 1)]
	# loop through data and compare up, left, and diag
	for h in range(1, len(data)):
		for l in range(1, len(data[0])):
			d = data[h - 1][l - 1]
			left = data[h][l - 1]
			up = data[h - 1][l]
			if str2[l - 1] == str1[h - 1]:
				current = d
			else:
				current = min(d, left, up) + 1
			data[h][l] = current
	return data[-1][-1]