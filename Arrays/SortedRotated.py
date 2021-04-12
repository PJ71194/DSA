def findElement(arr, key):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left+right)//2
		if arr[mid] == key:
			return mid
		elif arr[mid] < key and arr[right] >= key:
			left = mid + 1
		else:
			right = mid - 1
	
	return -1

if __name__=='__main__':
	arr = [int(x) for x in input().split()]
	key = int(input())
	n = len(arr)
	
	print(findElement(arr, key))