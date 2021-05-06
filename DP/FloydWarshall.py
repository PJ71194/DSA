from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(set)
		self.V = V
		self.shortestDist = [[float('inf') for j in range(self.V)] for i in range(self.V)]
		for i in range(self.V):
			self.shortestDist[i][i] = 0

	def addEdge(self, u, v, w):
		self.graph[u].add(v)
		self.shortestDist[u][v] = w

	# find shortest distance between all pairs (i,j), such that it passes through k
	def floydWarshall(self):
		for k in range(self.V):
			for i in range(self.V):
				for j in range(self.V):
					if self.shortestDist[i][j] > self.shortestDist[i][k] + self.shortestDist[k][j]:
						self.shortestDist[i][j] = self.shortestDist[i][k] + self.shortestDist[k][j]


	def printShortestPaths(self):
		print(self.shortestDist)

g = Graph(4)
g.addEdge(0,1,5)
g.addEdge(0,3,10)
g.addEdge(1,2,3)
g.addEdge(2,3,1)

g.floydWarshall()
g.printShortestPaths()
