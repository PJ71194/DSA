import heapq

def findMedian(lefthalf, righthalf):
	leftsize = len(lefthalf)
	rightsize = len(righthalf)
	
	if leftsize == rightsize:
		return (0 - lefthalf[0] + righthalf[0])/2
	elif leftsize > rightsize:
		return 0 - lefthalf[0]
	else:
		return righthalf[0]


def addNewElement(lefthalf, righthalf, num):
	leftsize = len(lefthalf)
	rightsize = len(righthalf)

	if leftsize == 0 or num <= 0 - lefthalf[0]:
		heapq.heappush(lefthalf, 0 - num)
		leftsize += 1
	else:
		heapq.heappush(righthalf, num)
		rightsize += 1
	
	if leftsize >  rightsize + 1:
		lastElementInLowerHalf = 0 - heapq.heappop(lefthalf)
		heapq.heappush(righthalf, lastElementInLowerHalf)
	elif rightsize > leftsize + 1:
		firstElementInUpperHalf = heapq.heappop(righthalf)
		heapq.heappush(lefthalf, 0 - firstElementInUpperHalf)

if __name__=='__main__':
	lefthalf = []
	righthalf = []

	arr = [5,15,1,3,4,8,6]

	for num in arr:
		addNewElement(lefthalf, righthalf, num)
		print(findMedian(lefthalf, righthalf))