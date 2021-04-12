class QueueUsingStacks:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, val):
		self.stack1.append(val)
		
	def pop(self):
		if len(self.stack1) == 0 and len(self.stack2) == 0:
			print("queue is empty")
		elif len(self.stack2) > 0:
			print(self.stack2.pop())
		else:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
			
			print(self.stack2.pop())

if __name__=='__main__':
	queue = QueueUsingStacks()
	
	n = int(input("Number of items to push "))
	i = 0
	while i < n:
		op, val = input().split()
		if op == "push":
			num = int(val)
			queue.push(num)
			i += 1
		else:
			queue.pop()
	
