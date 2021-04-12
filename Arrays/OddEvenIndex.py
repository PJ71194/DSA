if __name__=='__main__':
	for _ in range(int(input())):
		arr = [int(x) for x in input().split()]
		n = len(arr)
		
		evenIdx, oddIdx = 0, 1
		while evenIdx < n and oddIdx < n:
			while evenIdx < n and arr[evenIdx] >= 0:
				evenIdx += 2

			while oddIdx < n and arr[oddIdx] < 0:
				oddIdx += 2

			if evenIdx < n and oddIdx < n:
				arr[oddIdx], arr[evenIdx] = arr[evenIdx], arr[oddIdx]

		
		print(arr)