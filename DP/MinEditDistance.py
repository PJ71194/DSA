def editDist(str1, str2, dist, m, n):
	if n == 0:
		return m
	if m == 0:
		return n
	
	#print(m , n)
	if dist[m-1][n-1] == float('inf'):
		if str1[0] == str2[0]:
		 	dist[m-1][n-1] = editDist(str1[1:], str2[1:], dist, m-1, n-1)
		else:
			dist[m-1][n-1] = 1 + min(editDist(str1[1:], str2, dist, m-1, n), editDist(str1[1:], str2[1:], dist, m-1, n-1), editDist(str1, str2[1:], dist, m, n-1))

	return dist[m-1][n-1]

def editDistance(str1, str2):
	m = len(str1)
	n = len(str2)
	dist = [[float('inf')]*n for i in range(m)]

	return editDist(str1, str2, dist, m, n)

str1 = input("enter first string ")
str2 = input("enter second string ")

print(editDistance(str1, str2))