class MinMaxStack:
	def __init__(self):
		self.stack = []
    def peek(self):
        # Write your code here.
        if len(self.stack) > 0:
			return self.stack[-1][0]

    def pop(self):
        # Write your code here.
		if len(self.stack) > 0:
			vals = self.stack[-1]
			self.stack = self.stack[:-1]
			return vals[0]

    def push(self, number):
        # Write your code here.
        if len(self.stack) == 0:
			self.stack.append([number, number, number])
		else:
			vals = self.stack[-1].copy()
			vals[0] = number
			if vals[1] > number:
				vals[1] = number
			if vals[2] < number:
				vals[2] = number
			self.stack.append(vals)

    def getMin(self):
        # Write your code here.
        if len(self.stack) > 0:
			return self.stack[-1][1]

    def getMax(self):
        # Write your code here.
        if len(self.stack) > 0:
			return self.stack[-1][2]
