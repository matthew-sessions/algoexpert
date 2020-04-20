from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
		q = deque()
		q.append(self)
		while q.__len__() > 0:
			value = q.popleft()
			array.append(value.name)
			for i in value.children:
				q.append(i)
		return array
