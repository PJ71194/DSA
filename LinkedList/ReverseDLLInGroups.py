class dllNode:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class DLL:
	def __init__(self):
		self.head = None
		self.tail = None

	def insertAtEnd(self, val):
		node = dllNode(val)
		if not self.tail:
			self.tail = node
			self.head = node
		else:
			self.tail.next = node
			self.tail = node

	def printDll(self, first):
		curr = first
		while curr:
			print(curr.val)
			curr = curr.next		

def reverse(head, k):
	count = 0
	prev = None
	curr = head
	groupHead, groupTail = None, None
	while curr and count < k:
		if not groupTail:
			groupTail = curr

		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp
		count += 1

	groupHead = prev
	groupTail.next = curr

	return groupHead, groupTail
			

def reverseDLLInGroups(head, k):
	prevTail = None
	currHead = head
	globalHead = None
	while currHead:
		groupHead, groupTail = reverse(currHead, k)
		if prevTail:
			prevTail.next = groupHead
		else:
			globalHead = groupHead
		
		prevTail = groupTail
		currHead = groupTail.next
		prevTail.next = None
	
	return globalHead

arr = [int(x) for x in input().split()]
dll = DLL()
for ele in arr:
	dll.insertAtEnd(ele)

k = int(input())
newhead = reverseDLLInGroups(dll.head, k)
dll.printDll(newhead)

