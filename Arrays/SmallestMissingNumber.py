if __name__=='__main__':
	for _ in range(int(input())):
		arr = [int(x) for x in input().split()]
		n = len(arr)
		
		if n == 0:
			print(-1)
			continue

		if arr[0] != 0:
			print(0)
			continue

		left, right = 1, n-1
		largestFoundElement = 0
		while left <= right:
			mid = (left+right)//2
			if left == right:
				if arr[left] > left:
					print(largestFoundElement + 1)
				else:
					print(arr[left] + 1)	
				break
			
			if arr[mid] > mid:
				right = mid - 1
			else:
				largestFoundElement = mid
				left = mid + 1
			
			if right < left:
				print(largestFoundElement + 1)