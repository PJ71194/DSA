from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(list)
		self.V = V

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, node, visited, stack, parents):
		visited[node] = 1
		for child in self.graph[node]:
			parents[child].append(node)
			if child not in visited:
				self.DFSUtil(child, visited, stack, parents)

		stack.append(node)

	def topologicalSort(self, parents):
		visited = {}
		stack = []
		
		for node in range(self.V):
			if node not in visited:
				self.DFSUtil(node, visited, stack, parents)

		return stack


if __name__=='__main__':
	g = Graph(6)
	g.addEdge(5,2)
	g.addEdge(5,0)
	g.addEdge(2,3)
	g.addEdge(0,3)
	g.addEdge(3,1)
	g.addEdge(4,1)
	g.addEdge(0,4)
	
	parents = defaultdict(list)
	topologicalOrder = g.topologicalSort(parents)
	topologicalOrder.reverse()

	root = topologicalOrder[0]
	probability = [0]*g.V
	probability[root] = 1
	
	for node in topologicalOrder[1:]:
		for parent in parents[node]:
			probability[node] += probability[parent]/len(g.graph[parent])

	print(probability)
			