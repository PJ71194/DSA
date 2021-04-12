def nextGreater(arr):
	n = len(arr)
	if n == 0:
		return []
	if n == 1:
		return [-1]
	
	nextGreaterElements = [-1]
	stack = [arr[n-1]]

	for idx in range(n-2, -1, -1):
		while stack and stack[-1] <= arr[idx]:
			stack.pop()

		if not stack:
			nextGreaterElement = -1
		else:
			nextGreaterElement = stack[-1]

		stack.append(arr[idx])
		nextGreaterElements.append(nextGreaterElement)
	
	nextGreaterElements.reverse()
	print(nextGreaterElements)
	return

if __name__=='__main__':
	arr = [int(x) for x in input().split()]
	nextGreater(arr)
		