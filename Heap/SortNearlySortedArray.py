import heapq

def sortNearlySortedArr(arr, k):
	n = len(arr)
	if n <= k:
		return sorted(arr)

	sortedArr = []
	minheap = []
	for i in range(k+1):
		heapq.heappush(minheap, arr[i])
	
	i = k+1
	while minheap:
		minElement = heapq.heappop(minheap)
		sortedArr.append(minElement)
		if i < n:
			heapq.heappush(minheap, arr[i])
			i += 1

	return sortedArr

if __name__=='__main__':
	arr = [int(x) for x in input().split()]
	k = int(input())
	print(sortNearlySortedArr(arr, k)) 
	