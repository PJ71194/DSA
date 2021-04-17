from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(list)
		self.V = V

	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	def DFSUtil(self, v, visited):
		visited[v] = True
		for u in self.graph[v]:
			if u not in visited:
				self.DFSUtil(u, visited)

	def getMotherVertex(self):
		visited = {}
		lastVisited = 0
		for v in range(self.V):
			if v not in visited:
				self.DFSUtil(v, visited)
				# v is one of the mother nodes
				lastVisited = v
		
		# verify if v is a mother node
		visited = {}
		self.DFSUtil(lastVisited, visited)
		if len(visited) == self.V:
			return lastVisited

		return -1

if __name__=='__main__':
	g = Graph(7)
	g.addEdge(0,1)
	g.addEdge(0,2)
	g.addEdge(1,3)
	g.addEdge(4,1)
	g.addEdge(6,4)
	g.addEdge(5,6)
	g.addEdge(5,2)
	g.addEdge(6,0)

	print(g.getMotherVertex())
				