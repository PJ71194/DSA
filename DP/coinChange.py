def coinChangeUtil(X, coins, firstCoinIdx, n, ways):
	if X <= 0 or firstCoinIdx == n:
		return 0

	if coins[firstCoinIdx] > X:
		ways[X][firstCoinIdx] = 0
	elif ways[X][firstCoinIdx] != -1:
		currways = 0
		for i in range(firstCoinIdx, n):
			currways += 1 + coinChangeUtil(X - coins[i], coins, i, n, ways)
		
		ways[X][firstCoinIdx] = currways

	return ways[X][firstCoinIdx]

def coinChange(N, coins):
	n = len(coins)
	ways = [[-1]*n for i in range(N+1)]

	coinChangeUtil(N, coins, 0, n, ways)

	return ways[N][0]

N = int(input("enter value "))
coins = [int(x) for x in input().split()]

print(coinChange(N, coins))