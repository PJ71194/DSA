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
		heap = []

		visisted = {}
		visisted[s] = 1
		lastInsertedNode = s
		for i in range(self.V - 1):
			for v, w in self.graph[lastInsertedNode]:
				if v not in visisted:
					heapq.heappush(heap, (dist[lastInsertedNode] + w, lastInsertedNode, v))
					visisted[v] = 1
				

			mindist, src, dest = heapq.heappop(heap)
			#print(dest, mindist)
			lastInsertedNode = dest
			dist[dest] = mindist

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

		
					