class treeNode:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def LCA(val1, val2, root):
	if not root:
		return None
	
	if root.val == val1 or root.val == val2:
		return root

	leftLCA = LCA(val1, val2, root.left)
	rightLCA = LCA(val1, val2, root.right)
	
	if leftLCA and rightLCA:
		return root
	elif leftLCA:
		return leftLCA
	else:
		return rightLCA

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

	print(LCA(2,6,node1).val)
	print(LCA(2,5,node1).val)
	print(LCA(6,7,node1).val)