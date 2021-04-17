# O(V!) since in a complete graph V! paths are possible

from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(list)
		self.V = V

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, u, v, visited, paths):
		visited[u] = 1
		if u == v:
			paths[0] += 1
		else:
			for child in self.graph[u]:
				if child not in visited:
					self.DFSUtil(child, v, visited, paths)

		del visited[u]
					

	def getAllPaths(self, u, v):
		visited = {}
		paths = [0]
		self.DFSUtil(u, v, visited, paths)

		return paths[0]

if __name__=='__main__':
	g = Graph(4)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(0, 3)
	g.addEdge(2, 0)
	g.addEdge(2, 1)
	g.addEdge(1, 3)

	print(g.getAllPaths(2,3))