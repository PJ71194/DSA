from collections import deque

class treeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BTree:
	def __init__(self):
		self.root = None
		self.levels = 0
	
	# Recursive. Use level order traversal for iterative
	def getHeight(self, root):
		if root == None:
			return 0
		leftHt = getHeight(root.left)
		rightHt = getHeight(root.right)

		return max(leftHt, rightHt) + 1
	
	# at first available node in level order
	def insert(self, val):
		newNode = treeNode(val)
		
		if self.root == None:
			self.root = newNode
		else:
			queue = collections.deque()
			queue.append(self.root)
			while queue:
				currNode = queue.popleft()
				if not currNode.left:
					currNode.left = newNode
					return
				elif not currNode.right:
					currNode.right = newNode
					return
				else:
					queue.append(currNode.left)
					queue.append(currNode.right)

		return

	def levelOrder(self):
		queue = deque()	
		queue.append(self.root)
		levelorder = []
		while queue:
			curr = queue.popleft()
			levelorder.append(curr.val)
			if curr.left:
				queue.append(curr.left)
			if curr.right:
				queue.append(curr.right)

		print(levelorder)
		return

	def inorderIterative(self):
		stack = []
		inorder = []
		curr = self.root
		while True:
			if curr:
				stack.append(curr)
				curr = curr.left
			else:
				if not stack:
					break

				last = stack.pop()
				inorder.append(last.val)
				curr = last.right
		
		print(inorder)
	
	# O(n) - time, O(h) space excluding output space
	def iterativePreorder(self):
		curr = self.root
		stack = []
		preorder = []
		while stack or curr:
			if curr:
				preorder.append(curr.val)
				if curr.right:
					stack.append(curr.right)
				
				curr = curr.left
			else:
				curr = stack.pop()			

		print(preorder)

	def iterativePostorder(self):
		stack = [self.root]
		visitCount = {}
		postOrder = []
		while stack:
			curr = stack[-1]
			if curr not in visitCount:
				visitCount[curr] = 1
			else:
				visitCount[curr] += 1

			if visitCount[curr] == 2:
				postOrder.append(curr.val)
				stack.pop()
			else:
				if curr.right:
					stack.append(curr.right)
				if curr.left:
					stack.append(curr.left)

		print(postOrder)
			
	
	def findPredecessor(self, root, node):
		curr = root
		while curr.right and curr.right != node:
			curr = curr.right

		return curr

	def inorderMorris(self):
		curr = self.root
		inorder = []
		while curr:
			if not curr.left:
				inorder.append(curr.val)
				curr = curr.right
			else:
				predecessor = self.findPredecessor(curr.left, curr)
				if predecessor.right == None:
					predecessor.right = curr
					curr = curr.left
				elif predecessor.right == curr:
					predecessor.right = None
					inorder.append(curr.val)
					curr = curr.right

		print(inorder)

	def preorderMorris(self):
		curr = self.root
		preorder = []
		while curr:
			if not curr.left:
				preorder.append(curr.val)
				curr = curr.right
			else:
				predecessor = self.findPredecessor(curr.left, curr)
				if predecessor.right == None:
					preorder.append(curr.val)
					predecessor.right = curr
					curr = curr.left
				elif predecessor.right == curr:
					predecessor.right = None
					curr = curr.right

		print(preorder)

	def inorder(self, root):
		if root:
			self.inorder(root.left)
			print(root.val),
			self.inorder(root.right)

	def preorder(self, root):
		if root:
			print(root.val)
			self.preorder(root.left)
			self.preorder(root.right)
	
	def postorder(self, root):
		if root:
			self.postorder(root.left)
			self.postorder(root.right)
			print(root.val)

	def getLeaves(self):
		if self.root == None:
			return []
		
		leaves = []
		inorderStack = []
		curr = self.root
		while inorderStack or curr:
			if not curr:
				curr = inorderStack.pop()
				if not curr.left and not curr.right:
					leaves.append(curr.val)

				curr = curr.right
			else:
				inorderStack.append(curr)
				curr = curr.left
		return leaves	

	def boundaryTraversal(self):
		boundary = []
		curr = self.root
		# left boundary
		while curr:
			boundary.append(curr.val)
			if curr.left:
				curr = curr.left
			elif curr.right:
				curr = curr.right
			else:
				break

		#remove leftmost leaf node
		boundary.pop()

		# leaves
		boundary += self.getLeaves()

		# right boundary
		rightstack = []		
		curr = self.root.right
		while curr:
			rightstack.append(curr.val)
			if curr.right:
				curr = curr.right
			elif curr.left:
				curr = curr.left
			else:
				break

		# remove rightmost leaf node
		rightstack.pop()
		while rightstack:
			boundary.append(rightstack.pop())

		print(boundary)
				

if __name__=='__main__':
	node1 = treeNode(1)
	node2 = treeNode(2)
	node3 = treeNode(3)
	node4 = treeNode(4)
	node5 = treeNode(5)
	node6 = treeNode(6)
	node7 = treeNode(7)

	tree = BTree()
	tree.root = node1
	node1.left = node2
	node1.right = node3
	node2.left = node4
	node2.right = node5
	node3.left = node6
	node3.right = node7
	
	print("Level Order")
	tree.levelOrder()
	print("Iterative inorder")
	tree.inorderIterative()
	print("inorder morris")
	tree.inorderMorris()
	print("InOrder")
	tree.inorder(tree.root)
	print("preorder iterative")
	tree.iterativePreorder()
	print("preorder morris")
	tree.preorderMorris()
	print("PreOrder")
	tree.preorder(tree.root)
	print("iterative postorder")
	tree.iterativePostorder()
	print("PostOrder")
	tree.postorder(tree.root)
	print("boundary traversal")
	tree.boundaryTraversal()
			
					
				