def LCSUtil(seq1, seq2, i, j, mem):
	if i == 0 or j == 0:
		mem[i][j] = 0
	elif mem[i][j] == None:
		if seq1[i-1] == seq2[j-1]:
			mem[i][j] = 1 + LCSUtil(seq1, seq2, i-1, j-1, mem)
		else:
			mem[i][j] = max(LCSUtil(seq1, seq2, i-1, j, mem), LCSUtil(seq1, seq2, i, j-1, mem))

	return mem[i][j]

def LCS(seq1, seq2):
	n = len(seq1)
	m = len(seq2)
	mem = [[None]*(m+1) for i in range(n+1)]

	LCSUtil(seq1, seq2, n, m, mem)
	
	return mem[n][m]

seq1 = input()
seq2 = input()
print(LCS(seq1, seq2))