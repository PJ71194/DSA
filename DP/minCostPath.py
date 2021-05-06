def minCost(cost, i, j, m, n, minCostMat):
	if i >= m or j >= n:
		return float('inf')

	if i == m-1 and j == n-1:
		minCostMat[i][j] = cost[i][j]
	elif minCostMat[i][j] == -1:
		minCostMat[i][j] = cost[i][j] + min(minCost(cost, i, j+1, m, n, minCostMat), minCost(cost, i + 1, j + 1, m, n, minCostMat), minCost(cost, i + 1, j, m, n, minCostMat))

	return minCostMat[i][j]

def minCostPath(cost):
	m = len(cost)
	if m > 0:
		n = len(cost[0])
	else:
		n = 0

	minCostMat = [[-1]*n for i in range(m)]

	return minCost(cost, 0, 0, m, n, minCostMat)


cost= [ [5, 3, 6, 1],
        [2, 4, 3, 5],
        [2, 10, 1, 15] ]

print(minCostPath(cost))
		
		
