def minRewards(scores):
    # Write your code here.
    res = [1] * len(scores)
	for i in range(1, len(scores)):
		back, val = scores[i - 1], scores[i]
		if val > back:
			res[i] = res[i - 1] + 1
	for i in reversed(range(0, len(scores) - 1)):
		val, back = scores[i], scores[i + 1]
		if val > back:
			num = max(res[i + 1] + 1, res[i])
			res[i] = num
	return sum(res)