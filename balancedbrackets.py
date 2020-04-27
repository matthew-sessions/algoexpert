def balancedBrackets(string):
    # Write your code here.
	l = len(string)
    frontfacing = "({["
	backfacing = "}])"
	matching = {'}':'{', "]":"[", ")":"("}
	frontmatch = {'{':'}', '[': ']', '(':')'}
	data = {}
	i = 0
	while i <= l - 1:
		if i == l - 1:
			if string[i] in frontfacing:
				return False
			else:
				if matching[string[i]] in data:
					data[matching[string[i]]] -= 1
					if data[matching[string[i]]] == 0:
						del data[matching[string[i]]]
					if len(data) == 0:
						return True
				i += 1
				
		elif string[i] in frontfacing and string[i + 1] in frontfacing:
			if string[i] not in data:
				data[string[i]] = 1
			else:
				data[string[i]] += 1
			i += 1
		elif string[i] in frontfacing and string[i + 1] in backfacing:
			if frontmatch[string[i]] == string[i + 1]:
				i += 2
				if i >= l:
					if len(data) == 0:
						return True
			else:
				return False
		else:
			if matching[string[i]] not in data:
				return False
			else:
				data[matching[string[i]]] -= 1
				if data[matching[string[i]]] == 0:
					del data[matching[string[i]]]
				i += 1
	return False
		