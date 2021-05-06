O(n*n*k)

def eggDropMinTrials(N, k, memoiz):
	if N == 1 or k == 1:
		return N

	result = N
	if memoiz[N][k] == 0:
		for x in range(1, N+1):
			result = min(result, max(eggDropMinTrials(x-1, k-1, memoiz), eggDropMinTrials(N-x, k, memoiz)) + 1)
		memoiz[N][k] = result

	return memoiz[N][k]

if __name__=='__main__':
	N = int(input())
	k = int(input())
	
	memoiz = [[0 for j in range(k+1)] for i in range(N+1)]
	print(eggDropMinTrials(N, k, memoiz))