import json

def fourNumberSum(array, targetSum):
    # Write your code here.
    data = {}
	for i in range(len(array)):
		for j in range(i + 1, len(array)):
			val = array[i] + array[j]
			if val not in data:
				data[val] = {'vals': [[array[i], array[j]]], 'index': [[i, j]]}
			else:
				data[val]['vals'].append([array[i], array[j]])
				data[val]['index'].append([i, j])
	
	res = []
	visited = set()
	for i in data:
		needed = targetSum - i
		if needed in data:
			for base in data[i]['index']:
				for look in data[needed]['index']:
					inds = sorted(base + look)
					temp = set(inds)
					if len(temp) == 4:
						hashed = hash(json.dumps(inds).encode())
						if hashed not in visited:
							visited.add(hashed)
							res.append([array[a] for a in inds])
		
	return res