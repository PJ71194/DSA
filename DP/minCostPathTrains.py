O(n^3)

def minCost(src, dest, cost, minPathCost):
	if src == dest:
		return 0

	if minPathCost[src][dest] != float('inf'):
		return minPathCost[src][dest]
	
	mincost = cost[src][dest]
	for x in range(src+1, dest):
		mincost = min(mincost, cost[src][x] + minCost(x, dest, cost, minPathCost))

	minPathCost[src][dest] = mincost
	return mincost

O(n^2)
def minCostOptimized(cost, n):
	minCostPath = [float('inf') for i in range(n)]
	minCostPath[0] = 0
	for i in range(1, n):
		for j in range(i):
			minCostPath[i] = min(minCostPath[i], cost[j][i] + minCostPath[j])

	return minCostPath[n-1]

if __name__=='__main__':
	n = int(input("Enter number of stations "))
	cost = [[0, 15, 80, 90],
		[float('inf'), 0, 40, 50],
		[float('inf'),float('inf'), 0, 70],
		[float('inf'),float('inf'),float('inf'), 0]]
	
	minPathCost = [[float('inf') for i in range(n)] for j in range(n)]
	print(minCost(0, n-1, cost, minPathCost))

	print(minCostOptimized(cost, n))