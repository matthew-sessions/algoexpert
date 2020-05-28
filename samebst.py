def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    used = set()
	root = arrayOne[0]
	
	if len(arrayOne) != len(arrayTwo):
		return False
	
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	for i in arrayOne[1:]:
		c = 1
		while True:
			if c >= len(arrayTwo):
				return False
			if i == arrayTwo[c]:
				used.add(i)
				break
			if c == len(arrayTwo) - 1:
				if arrayTwo[c] not in arrayOne:
					return False


			if i > root:
				if arrayTwo[c] < i or arrayTwo[c] in used:
					c += 1
				else:
					return False
			elif i < root:
				if arrayTwo[c] > i or arrayTwo[c] in used:
					c += 1
				else:
					return False
			else:
				return False
	return True
				