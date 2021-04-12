class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

class BST:
	def __init__(self):
		self.root = None

	def insert(self, root, val):
		if root == None:
			return Node(val)

		if root.val == val:
			return root

		if root.val < val:
			root.right = self.insert(root.right, val)
		else:
			root.left = self.insert(root.left, val)

		return root

	def search(self, root, key):
		if root == None or root.val == key:
			return root

		if root.val < key:
			return self.search(root.right, key)
		else:
			return self.search(root.left, key)

	def getSuccessor(self, root):
		if not root or not root.left:
			return root
		else:
			return self.getSuccessor(root.left)

	def getPredecessor(self, root):
		if not root or not root.right:
			return root
		else:
			return self.getPredecessor(root.right)

	def delete(self, root, key):
		if root == None:
			return None

		if root.val == key:
			if root.right:
				inorderSuccessor = self.getSuccessor(root.right)
				root.val = inorderSuccessor.val
				inorderSuccessor.val = key
				root.right = self.delete(root.right, key)
			elif root.left:
				inorderPredecessor = self.getPredecessor(root.left)
				root.val = inorderPredecessor.val
				inorderPredecessor.val = key
				root.left = self.delete(root.left, key)
			else:
				return None
		elif root.val < key:
			root.right = self.delete(root.right, key)
		else:
			root.left = self.delete(root.left, key)

		return root

	def inorder(self, root, order):
		if root == None:
			return

		if root.left:
			self.inorder(root.left, order)
		order.append(root.val)
		if root.right:
			self.inorder(root.right, order)
	
		return

if __name__=='__main__':
	arr = [10, 8, 15, 6, 9, 13, 20, 4, 7, 12, 14, 16, 22, 5, 18]
	tree = BST()
	for ele in arr:
		tree.root = tree.insert(tree.root, ele)

	order = []
	tree.inorder(tree.root, order)
	print(order)

	print(tree.search(tree.root, 9).val)
	print(tree.search(tree.root, 16).val)
	node = tree.search(tree.root, 25)
	if node == None:
		print("not found")

	tree.delete(tree.root, 5)
	order = []
	tree.inorder(tree.root, order)
	print(order)

	tree.delete(tree.root, 16)
	order = []
	tree.inorder(tree.root, order)
	print(order)

	tree.delete(tree.root, 15)
	order = []
	tree.inorder(tree.root, order)
	print(order)
			
			

		