class treeNode:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def preorderRightDegenrateTree(root):
	if not root:
		return root

	if not root.left and not root.right:
		return root

	temp = root.right
	if root.left:
		root.right = root.left
		lastNodeLeftSubTree = preorderRightDegenrateTree(root.left)
		lastNodeLeftSubTree.right = temp
		root.left = None
	
	return preorderRightDegenrateTree(temp)

if __name__=='__main__':
	node1 = treeNode(1)
	node2 = treeNode(2)
	node3 = treeNode(3)
	node4 = treeNode(4)
	node5 = treeNode(5)
	node6 = treeNode(6)
	node7 = treeNode(7)

	node1.left = node2
	node1.right = node3
	node2.left = node4
	node2.right = node5
	node3.left = node6
	node3.right = node7

	lastNode = preorderRightDegenrateTree(node1)

	curr = node1
	while curr:
		print(curr.val)
		curr = curr.right