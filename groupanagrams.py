def groupAnagrams(words):
    # Write your code here.
    data = {}
	for i in words:
		val = ''.join(sorted(i))
		if val not in data:
			data[val] = [i]
		else:
			data[val].append(i)
	return list(data.values())
