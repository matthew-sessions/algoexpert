# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    # set counter
	# set p 1 and p 2
	# loop until counter is k
	# while until p1 == None
	node_1, node_2 = head, head
	for i in range(k):
		node_1 = node_1.next
		if node_1 is None:
			node_2.value = node_2.next.value
			node_2.next = node_2.next.next
			return head
	while node_1.next is not None:
		node_1 = node_1.next
		node_2 = node_2.next
	node_2.next = node_2.next.next
	return head
		
	