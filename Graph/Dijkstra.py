from collections import defaultdict
import heapq

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(set)
		self.V = V

	def addEdge(self, u, v, w):
		self.graph[u].add((v,w))

	def dijkstra(self, s):
		dist = [float('inf') for i in range(self.V)]
		dist[s] = 0

		visited = {}
		while len(visited) < self.V:
			minDistNode = s
			minDist = float('inf')
			for v in range(self.V):
				if v not in visited and dist[v] < minDist:
					minDist = dist[v]
					minDistNode = v

			visited[minDistNode] = 1

			for v, w in self.graph[minDistNode]:
				if v not in visited:
					dist[v] = min(dist[v], dist[minDistNode] + w)

		print(dist)

g = Graph(6)
g.addEdge(0,1,2)
g.addEdge(0,2,3)
g.addEdge(1,3,2)
g.addEdge(2,4,2)
g.addEdge(3,4,2)
g.addEdge(3,5,3)
g.addEdge(4,5,1)

g.dijkstra(0)

		
					