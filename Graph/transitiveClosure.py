from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)
		self.tc = [[0]*V for i in range(V)]

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def getTransitiveClosureUtil(self, u, v):
		self.tc[u][v] = 1
		
		for child in self.graph[v]:
			if self.tc[u][child] == 0:
				self.getTransitiveClosureUtil(u, child)

	def getTransitiveClosure(self):
		for u in range(self.V):
			self.getTransitiveClosureUtil(u, u)


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.getTransitiveClosure()
print(g.tc)
