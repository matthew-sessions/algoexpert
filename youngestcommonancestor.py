# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	if descendantOne.name == topAncestor.name or descendantTwo.name == topAncestor.name:
		return topAncestor
	elif descendantOne.ancestor == descendantTwo:
		return descendantTwo
	elif descendantOne == descendantTwo.ancestor:
		return descendantOne
	visted = set()

	while descendantOne.name != topAncestor.name:
		descendantOne = descendantOne.ancestor
		visted.add(descendantOne.name)
	if descendantTwo.name in visted:
		return descendantTwo		
	while descendantTwo.name != topAncestor.name:
		descendantTwo = descendantTwo.ancestor
		if descendantTwo.name in visted:
			return descendantTwo