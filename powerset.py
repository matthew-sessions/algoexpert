def powerset(array):
    # Write your code here.
	sub = [[]]
    for val in array:
		for i in range(len(sub)):
			cursub = sub[i]
			sub.append(cursub + [val])
	return sub