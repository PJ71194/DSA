O(VE)

from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = []
		self.V = V

	def addEdge(self, u, v, w):
		self.graph.append([u,v,w])

	def printGraph(self):
		print(self.graph)

	def bellmanFord(self, s):
		dist = [float('inf') for i in range(self.V)]
		dist[s] = 0
		
		# first loop get shortest paths if there is no negative cycle
		for i in range(self.V - 1):
			for u, v, w in self.graph:
				dist[v] = min(dist[v], dist[u] + w)
		
		# extra loop to see if there is yet another shorter path => negative cycle
		for u,v,w in self.graph:
			if dist[v] > dist[u] + w:
				print("negative cycle")
				return

		print(dist)

g = Graph(5)
g.addEdge(0,1,-1)
g.addEdge(0,2,4)
g.addEdge(1,2,3)
g.addEdge(1,3,2)
g.addEdge(1,4,2)
g.addEdge(3,2,5)
g.addEdge(3,1,1)
g.addEdge(4,3,-4)

#g.printGraph()

g.bellmanFord(0)