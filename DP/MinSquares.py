import math

def isPerfectSquare(n):
	root = math.floor(math.sqrt(n))
	if (root*root == n):
		return True

	return False

def minsqrs(n, memoiz):
	if n == 1 or isPerfectSquare(n):
		return 1
	
	if memoiz[n] == float('inf'):
		ans = n
		for i in range(math.floor(math.sqrt(n)), 0, -1):
			ans = min(ans, minsqrs(n - i*i, memoiz) + 1)

		memoiz[n] = ans

	return memoiz[n]

if __name__=='__main__':
	n = int(input())
	memoiz = [float('inf')]*(n+1)

	print(minsqrs(n, memoiz))