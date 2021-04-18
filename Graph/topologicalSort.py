from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(list)
		self.V = V

	def addEdge(self, u, v):
		self.graph[u].append((v))

	def DFSUtil(self, node, visited, stack):
		visited[node] = 1
		for child in self.graph[node]:
			if child not in visited:
				self.DFSUtil(child, visited, stack)
		
		stack.append(node)

	def topologicalSort(self):
		visited = {}
		stack = []
		for v in range(self.V):
			if v not in visited:
				self.DFSUtil(v, visited, stack)

		stack.reverse()
		print(stack)

if __name__=='__main__':
	g = Graph(6)
	g.addEdge(5,0)
	g.addEdge(5,2)
	g.addEdge(4,0)
	g.addEdge(4,1)
	g.addEdge(2,3)
	g.addEdge(3,1)

	g.topologicalSort()