def LIS(arr):
	n = len(arr)
	if n <= 1:
		print(arr)

	lis = [[1,-1] for i in range(n)]
	for i in range(1, n):
		for j in range(i):
			#print("current lis length ending at ", i)
			if arr[j] < arr[i] and lis[i][0] < lis[j][0] + 1:
				lis[i][0] = lis[j][0] + 1
				lis[i][1] = j
				#print("updated")

		#print("final lis length", lis[i][0])
	
	lisOutput = []
	maxLen = 1
	lastIndex = 0
	for i in range(1, n):
		if lis[i][0] > maxLen:
			maxLen = lis[i][0]
			lastIndex = i

	while lastIndex >= 0:
		lisOutput.append(arr[lastIndex])
		lastIndex = lis[lastIndex][1]
		#print(lastIndex)

	lisOutput.reverse()
	print(lisOutput)

def lismemoizUtil(arr, i, lis):
	if i == 0:
		lis[i] = [1, -1]
	else:
		if i not in lis:
			currLis = 1
			prevEndingIndex = -1
			for j in range(i):
				prevLisLength, endIndex = lismemoizUtil(arr, j, lis)
				if arr[j] < arr[i] and prevLisLength + 1 > currLis:
					currLis = prevLisLength + 1
					prevEndingIndex = j

			lis[i] = [currLis, prevEndingIndex]

	return lis[i]

def lisMemoiz(arr):
	lis = {}
	n = len(arr)
	for i in range(n):
		lisLength, endIndex = lismemoizUtil(arr, i, lis)
	
	maxLen = 1
	maxEnding = 0
	for i in range(1, n):
		if lis[i][0] > maxLen:
			maxLen = lis[i][0]
			maxEnding = i

	lisSequence = []
	currEnd = maxEnding
	#print(currEnd, maxLen, lis[currEnd][1])
	while currEnd >= 0:
		lisSequence.append(arr[currEnd])
		currEnd = lis[currEnd][1]
		#print(currEnd)

	lisSequence.reverse()
	print(lisSequence)

arr = [int(x) for x in input().split()]
LIS(arr)
lisMemoiz(arr)