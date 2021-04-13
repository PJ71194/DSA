import sys

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def getPreorderIndex():
	return constructBSTUtil.preorderIdx

def incrementPreorderIndex():
	constructBSTUtil.preorderIdx += 1

def constructBSTUtil(preorder, key, minR, maxR, size):
	if getPreorderIndex() >= size:
		return None

	if key > minR and key < maxR:
		root = Node(key)
		incrementPreorderIndex()
		
		preIdx = getPreorderIndex()
		if preIdx < size:
			root.left = constructBSTUtil(preorder, preorder[preIdx], minR, key, size)
		preIdx = getPreorderIndex()
		if preIdx < size:
			root.right = constructBSTUtil(preorder, preorder[preIdx], key, maxR, size)

		return root

	return None

def constructBST(preorder):
	n = len(preorder)
	if n == 0:
		return None
	
	constructBSTUtil.preorderIdx = 0
	rootKey = preorder[0]
	minRange, maxRange = float('-infinity'), float('infinity')
	return constructBSTUtil(preorder, rootKey, minRange, maxRange, n)

def printInorder(root):
	if root:
		printInorder(root.left)
		print(root.val)
		printInorder(root.right)

if __name__=='__main__':
	preorder = [10,7,5,9,15,13,18]
	root = constructBST(preorder)

	printInorder(root)