from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.vertices = set()
	
	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.vertices.add(u)
		self.vertices.add(v)

	def topoUtil(self, node, visited, stack):
		visited[node] = 1
		for child in self.graph[node]:
			if child not in visited:
				self.topoUtil(child, visited, stack)

		stack.append(node)

	def topologicalSort(self):
		visited = {}
		stack = []
		for vertex in self.vertices:
			if vertex not in visited:
				self.topoUtil(vertex, visited, stack)

		stack.reverse()
		return stack

class Solution:
	def __init__(self, dictionary):
		self.graph = Graph()
		n = len(dictionary)
		for i in range(n-1):
			word1 = dictionary[i]
			word2 = dictionary[i+1]
			
			l,r = 0, 0
			while l < len(word1) and r < len(word2):
				if word1[l] != word2[r]:
					self.graph.addEdge(word1[l], word2[r])

				l += 1
				r += 1
			
	def getCharOrder(self):
		charOrder = self.graph.topologicalSort()
		print(charOrder)

dictionary = input().split()
soln = Solution(dictionary)
soln.getCharOrder()