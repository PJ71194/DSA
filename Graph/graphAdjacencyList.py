import collections
from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(list)
	
	def addUndirectedEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def addDirectedEdge(self, u, v):
		self.graph[u].append(v)

	def printGraph(self):
		for vertex in self.graph:
			print(vertex, self.graph[vertex])
	
	# works on a connected graph
	def BFS(self, source):
		visited = {}
		output = []
		queue = collections.deque()
		queue.append(source)
		visited[source] = 1
		while queue:
			currvertex = queue.popleft()
			output.append(currvertex)
			for vertex in self.graph[currvertex]:
				if vertex not in visited:
					queue.append(vertex)
					visited[vertex] = 1

		print(output)
	
	def DFSUtil(self, u, visited, output):
		visited[u] = 1

		for v in self.graph[u]:
			if v not in visited:
				self.DFSUtil(v, visited, output)

		output.append(u)
	
	# works on disconnected graphs as well			
	def DFS(self):
		visited = {}
		output = []
		for vertex in self.graph:
			if vertex not in visited:
				self.DFSUtil(vertex, visited, output)

		print(output)

	def DFSIterative(self):
		stack = []
		visited = {}
		output = []
		for node in self.graph:
			if node not in visited:
				stack.append(node)
				visited[node] = 1
				while stack:
					currnode = stack[-1]
					for child in self.graph[currnode]:
						if child not in visited:
							stack.append(child)
							visited[child] = 1

					if stack[-1] == currnode:
						output.append(stack[-1])
						stack.pop()

		print(output)

if __name__=='__main__':
	V = 5
	graph = Graph(V)
	
	edges = [[1,2],[1,3],[3,2],[4,5],[5,1],[2,5],[3,5]]

	for edge in edges:
		graph.addUndirectedEdge(edge[0], edge[1])

	graph.printGraph()

	graph.BFS(1)

	graph.DFS()

	graph.DFSIterative()
		