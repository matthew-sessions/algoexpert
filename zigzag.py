def zigzagTraverse(array):
    # Write your code here.
    height = len(array) - 1
	width = len(array[0]) - 1
	res = []
	row, col = 0,0
	down = True
	while not bounds(row, col, height, width):
		res.append(array[row][col])
		
		if down:
			if col == 0 or row == height:
				down = False
				if row == height:
					col += 1
				else:
					row += 1
			else:
				row += 1
				col -= 1
				
			
		else:
			if row == 0 or col == width:
				down = True
				if col == width:
					row += 1
				else:
					col += 1
			else:
				row -= 1 
				col += 1
	return res

def bounds(row, col, height, width):
	return row < 0 or row > height or col < 0 or col > width
