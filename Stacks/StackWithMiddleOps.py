class Node:
	def __init__(self, val):
		self.nxt = None
		self.prev = None
		self.val = val

class StackWithMid:
	def __init__(self):
		self.stackHead = None
		self.end = None
		self.mid = None
		self.size = 0

	def push(self, val):
		nextNode = Node(val)
		if self.stackHead == None:
			self.stackHead = nextNode
			self.end = nextNode
			self.mid = nextNode
		else:
			self.end.nxt = nextNode
			nextNode.prev = self.end
			self.end = nextNode
	 	
		self.size += 1
		if self.size % 2 == 0:
			self.mid = self.mid.nxt

	def pop(self):
		if self.stackHead == None:
			print("Stack is empty")
			return
		
		self.size -= 1
		prevNode = self.end.prev
		prevMidNode = self.mid.prev
		if prevNode == None:
			self.stackHead = None
			self.end = None
			self.mid = None
		else:
			prevNode.nxt = None
			self.end = prevNode
		
			if self.size % 2 != 0:
				self.mid = prevMidNode


	def findMid(self):
		if self.mid:
			print(self.mid.val)
			return

	def deleteMid(self):
		if self.stackHead == None:
			print("Stack is empty")
			return

		self.size -= 1
		if self.mid == self.stackHead:
			self.stackHead = None
			self.end = None
			self.mid = None
			return

		prevMidNode = self.mid.prev
		prevMidNode.nxt = self.mid.nxt
		if self.mid.nxt:
			self.mid.nxt.prev = prevMidNode
		else:
			self.end = prevMidNode

		if self.size % 2 == 0:
			self.mid = prevMidNode.nxt
		else:
			self.mid = prevMidNode

	def print(self):
		currNode = self.stackHead
		while currNode:
			print(currNode.val)
			currNode = currNode.nxt


if __name__=='__main__':
	stack = StackWithMid()
	n = int(input("Number of elements to be added"))
	i = 0
	while i < n:
		op, val = input().split()
		if op == "push":
			stack.push(int(val))
			i += 1
		elif op == "pop":
			stack.pop()
			stack.print()
		elif op == "delMid":
			stack.deleteMid()
			stack.print()
		else:
			stack.findMid()
				
		
		