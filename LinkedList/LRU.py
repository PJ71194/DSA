class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None

class DLL:
	def __init__(self):
		self.head = None
		self.tail = None

	def insertAtEnd(self, val):
		newNode = Node(val)
		if not self.tail:
			self.tail = newNode
			self.head = newNode
		else:
			self.tail.next = newNode
			newNode.prev = self.tail
			self.tail = newNode

	def removeHead(self):
		removedVal = float('infinity')
		if self.head:
			removedVal = self.head.val
			self.head = self.head.next
		if self.head:
			self.head.prev = None

		return removedVal

	def removeNodeInsertAtEnd(self, node):
		if node == self.head:
			self.removeHead()
		elif node == self.tail:
			temp = self.tail.prev
			self.tail.prev = None
			self.tail = temp
		else:
			node.prev.next = node.next
			node.next.prev = node.prev
			node.prev = None
			node.next = None

		self.tail.next = node
		node.prev = self.tail
		self.tail = node

	def printDll(self):
		curr = self.head
		linkedList = []
		while curr:
			linkedList.append(curr.val)
			curr = curr.next

		print(linkedList)

class LRU:
	def __init__(self, m):
		self.queue = DLL()
		self.nodeMap = {}
		self.cacheSize = m
		self.pageCount = 0

	def isPageInCache(self, num):
		if num not in self.nodeMap:
			return False

		return True

	def addPage(self, num):
		if self.pageCount == self.cacheSize:
			removedPageNum = self.queue.removeHead()
			self.pageCount -= 1
			del self.nodeMap[removedPageNum]
		
		self.queue.insertAtEnd(num)
		self.nodeMap[num] = self.queue.tail
		self.pageCount += 1
		print("page added to cache")

	def getPage(self, num):
		if not self.isPageInCache(num):
			self.addPage(num)
		else:
			pageNode = self.nodeMap[num]
			self.queue.removeNodeInsertAtEnd(pageNode)

		self.queue.printDll()

if __name__=='__main__':
	cacheSize = int(input("input cache size "))
	pageReferences = [int(x) for x in input().split()]
	lruCache = LRU(cacheSize)
	for page in pageReferences:
		lruCache.getPage(page)
		
			