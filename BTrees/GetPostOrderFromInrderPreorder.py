def getPostOrder(preorder, inorder):
	n = len(preorder)
	if n <= 1:
		return preorder

	root = preorder[0]
	inorderIdx = 0
	for idx in range(n):
		if inorder[idx] == root:
			inorderIdx = idx
			break
	
	leftSubTreeSize = inorderIdx
	rightSubTreeSize = n - inorderIdx - 1
	return getPostOrder(preorder[1:leftSubTreeSize+1], inorder[:leftSubTreeSize]) + getPostOrder(preorder[leftSubTreeSize+1:], inorder[leftSubTreeSize+1:]) + [root]

if __name__=='__main__':
	inorder = [4,2,5,1,6,3,7]
	preorder = [1,2,4,5,3,6,7]
	
	print(getPostOrder(preorder, inorder))