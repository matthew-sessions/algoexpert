def longestPalindromicSubstring(string):
	if len(string) == 1:
		return string
    # Write your code here.
    l = 0
	pal = None
	for i in range(len(string)):
		for b in range(i, len(string)):

			drone = string[i:b + 1]
			print(drone)
			re = drone[::-1]
			if re == drone:
				if b - i > l:
					l = b - i
					pal = drone
	return pal
