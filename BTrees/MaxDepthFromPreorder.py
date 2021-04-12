def getDepth(preorder):
	N = len(preorder)
	
	if N == 0:
		return -1
	if N == 1:
		return 0

	
	leftOpenStack = [0]
	rightOpenStack = [0]
	maxht = 0
	for idx in range(1, N):
		if leftOpenStack:
			ht = leftOpenStack.pop()
		elif rightOpenStack:
			ht = rightOpenStack.pop()
		
		if preorder[idx] == 'l':
				maxht = max(maxht, ht+1)
		else:
			leftOpenStack.append(ht+1)
			rightOpenStack.append(ht+1)

	return maxht

def getDepthRecursive(preorder, index):
	n = len(preorder)
	idx = index[0]
	if idx >= n or preorder[idx] == 'l':
		return 0
	
	index[0] += 1
	leftHt = getDepthRecursive(preorder, index)
	index[0] += 1
	rightHt = getDepthRecursive(preorder, index)

	return max(leftHt, rightHt) + 1

preorder = input()
print(getDepth(preorder))
index = [0]
print(getDepthRecursive(preorder, index))
				