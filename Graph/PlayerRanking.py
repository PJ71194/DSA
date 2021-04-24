from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(set)
		self.V = V

	def addEdge(self, u, v):
		self.graph[u].add(v)

	def topoUtil(self, node, visited, stack, parentStack):
		visited[node] = 1
		parentStack.append(node)
		for child in self.graph[node]:
			if child not in visited:
				if self.topoUtil(child, visited, stack, parentStack):
					return True
			elif child in parentStack:
				return True

		stack.append(node)
		parentStack.pop()
		return False

	def topologicalSort(self):
		visited = {}
		stack = []
		parentStack = []
		
		isDisconnected = False
		unvisitedRoots = 0
		isCyclic = False
		for node in range(1, self.V):
			if node not in visited:
				unvisitedRoots += 1
				if unvisitedRoots > 1:
					isDisconnected = True
					break
				else:
					if self.topoUtil(node, visited, stack, parentStack):
						isCyclic = True
						break

		if isDisconnected or isCyclic:
			return []
		else:
			stack.reverse()
			return stack

def getRanking(tournaments, N, M, K):
	if N == 0 or M == 0:
		print("Not possible")
		return

	g = Graph(N)
	for tournament in tournaments:
		for i in range(K-1):
			g.addEdge(tournament[i], tournament[i+1])

	ranking = g.topologicalSort()
	if len(ranking) == 0:
		print("Not possible")
	else:
		print(ranking)

tournaments = [[1,2,3,4],
		[4,5,6,7],
		[5,6,7,8],
		[6,7,8,9]]

K, M, N = 4, 4, 9
getRanking(tournaments, N, M, K)
		

	