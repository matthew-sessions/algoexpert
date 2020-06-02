def subarraySort(array):
    # Write your code here.

	
    l = float('-inf')
	s = float('inf')
	li, si = None, None
	for i in range(len(array)):
		if i == 0:
			if array[i + 1] < array[i]:
				if array[i] > l:
					l = array[i]
				if array[i] < s:
					s = array[i]
		elif i == len(array) - 1:
			if array[i - 1] > array[i]:
				if array[i] > l:
					l = array[i]
				if array[i] < s:
					s = array[i]				
		else:
			if array[i - 1] > array[i] or array[i + 1] < array[i]:
				if array[i] > l:
					l = array[i]
				if array[i] < s:
					s = array[i]
	print(l, s,  '---')
	end = len(array)
	start  = -1
	f1, f2 = True, True
	r, e = None, None
	while (end > start):
		if not f1 and not f2:
			break
		if f1:
			start += 1
			if array[start] > s:
				print('here')
				f1 = False
				r = start
			# if not f1:
			# 	start += 1

		if f2:
			end -= 1
			if array[end] < l:
				f2 = False
				e = end
	
				


		print(start, end)
	if None in [r, e]:
		return [-1, -1]
	return [r, e]
		