def minLength(str1, str2, i, j, memoiz):
	n, m = len(str1), len(str2)
	if i == n:
		return m - j
	if j == m:
		return 0

	if memoiz[i][j] == float('inf'):
		if str1[i] == str2[j]:
			memoiz[i][j] = minLength(str1, str2, i + 1, j + 1, memoiz)
		else:
			memoiz[i][j] = min(1 + minLength(str1, str2, i, j + 1, memoiz), minLength(str1, str2, i + 1, j, memoiz))

	return memoiz[i][j]

if __name__=='__main__':
	str1 = input("first string ")
	str2 = input("second string ")
	n, m = len(str1), len(str2)

	memoiz = [[float('inf') for j in range(m)] for i in range(n)]

	print(minLength(str1, str2, 0, 0, memoiz) + n)