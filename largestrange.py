def largestRange(array):
    # Write your code here.
    data = {i:True for i in array}
	l = 0
	res = []
	for i in array:
		if data[i] == False:
			pass
		else:

			data[i] = False
			temp = [i, i]
			left = i - 1
			right = i + 1
			count = 1
			while left in data:
				count += 1
				temp[0] = left
				left -= 1
			while right in data:
				count += 1
				temp[1] = right
				right += 1
			if count > l:
				l = count
				res = temp
	return res