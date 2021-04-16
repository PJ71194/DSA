import collections

def isLevelOrder(arr):
	n = len(arr)
	if n <= 1:
		print("Yes")
		return
	
	arrIdx = 1
	queue = collections.deque()
	queue.append((arr[0], float('-infinity'), float('infinity')))
	while queue and arrIdx < n:
		curr, minR, maxR = queue.popleft()
		nextValue = arr[arrIdx]
		if nextValue < curr and nextValue > minR and nextValue < maxR:
			queue.append((nextValue, minR, curr))
			arrIdx += 1 
		
		nextValue = arr[arrIdx]
		if nextValue > curr and nextValue > minR and nextValue < maxR:
			queue.append((nextValue, curr, maxR))
			arrIdx += 1
	
	if arrIdx < n:
		print("No")
	else:
		print("Yes")

	return

for _ in range(int(input())):
	arr = [int(x) for x in input().split()]
	isLevelOrder(arr)
				
			
		