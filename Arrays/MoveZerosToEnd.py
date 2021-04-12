if __name__=='__main__':
	arr = [int(x) for x in input().split()]
	n = len(arr)
	zeroIdx = -1
	nonZeroIdx = 0
	
	while nonZeroIdx < n and zeroIdx < n:
		if arr[nonZeroIdx] != 0:
			if zeroIdx != -1 and zeroIdx < nonZeroIdx:
				arr[zeroIdx], arr[nonZeroIdx] = arr[nonZeroIdx], arr[zeroIdx]
				nextZeroIdx = zeroIdx + 1
				while nextZeroIdx < n and arr[nextZeroIdx] != 0:
					nextZeroIdx += 1
				
				zeroIdx = nextZeroIdx

				nextNonZeroIdx = nonZeroIdx + 1
				while nextNonZeroIdx < n and arr[nextNonZeroIdx] == 0:
					nextNonZeroIdx += 1
				
				nonZeroIdx = nextNonZeroIdx
			else:
				nonZeroIdx += 1

		else:
			if zeroIdx == -1:
				zeroIdx = nonZeroIdx

			nonZeroIdx += 1


	print(arr)