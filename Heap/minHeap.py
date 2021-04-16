import heapq

class Heap:
	def __init__(self):
		self.heap = []

	def push(self, val):
		heapq.heappush(self.heap, val)
		print(self.heap)

	def pop(self):
		print(heapq.heappop(self.heap))
		print(self.heap)

	def getMin(self):
		print(self.heap[0])
		print(self.heap)

	def deleteKeyAtIndex(self, i):
		if i >=0 and i < len(self.heap):
			self.heap[i] = float('-infinity')
			while i > 0:
				self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
				i = (i-1)//2

			self.pop()
			print(self.heap)
		else:
			print("index out of range")

	def decreaseKey(self, i, val):
		if i >= 0 and i < len(self.heap):
			self.heap[i] = val	
			while self.heap[(i-1)//2] > self.heap[i] and i > 0:
				self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
				i = (i-1)//2

			print(self.heap)
		else:
			print("Index out of range")

minHeap = Heap()
arr = [1,4,3,6,5,2]

for ele in arr:
	minHeap.push(ele)

minHeap.getMin()
minHeap.pop()
minHeap.decreaseKey(2, 0)
minHeap.deleteKeyAtIndex(2)
		