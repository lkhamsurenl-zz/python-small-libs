from collections import deque
from heapq import heappush, heappop
class Vertex(object):
	def __init__(self, value):
		self.name = value
		self.status = "NEW" # NEW, ACTIVE, DONE
		self.adjList = {} # no active neightbors for now

class Edge(object):
	def __init__(self, s, d, value):
		self.weight = value
		self.start = s
		self.destination = d

class Graph(object):
	def __init__(self, vertices):
		self.vertices = vertices

class Traverse(object):
	def DFSGraph(self, graph):
		"""
		Depth first search traversal for graph
		"""

	def DFS(self, vertex):
		vertex.status = "ACTIVE"
		# do something with the vertex here
		for neighbor in vertex.adjList.keys():
			if neighbor.status == "DONE":
				# fail
				return 
			elif neighbor.status == "NEW":
				self.DFS(neighbor)
		vertex.status = "DONE"
		return 

	def BFS(self, vertex):
		q = deque()
		q.appendleft(vertex)
		while len(q) != 0:
			top = q.pop()
			# DO something with current vertex here
			for neighbor in top.adjList.keys():
				if neighbor.status == "DONE":
					return 
				elif neighbor.status == "NEW":
					# add to the queue
					q.appendleft(neighbor)
		return 

class TopologicalSort(object):
	sortingStack = []
	def topologicSorting(self, graph):
		"""
		Topological sorting for graph
		"""
		self.sortingStack = [] # stack should be empty
		# add a new vertex connecting to all the vertex in the graph
		new_source = Vertex(-1)
		for vertex in graph.vertices:
			new_source.adjList[vertex] = 0 # add new edge there
		# do topSorting for starting from the new_source
		self.topSorting(new_source)
		return self.sortingStack[:-1] # the last one is the artificial vertex added

	def topSorting(self, vertex):
		"""
		top sorting starting @ vertex
		"""
		vertex.status = "ACTIVE"
		for neighbor in vertex.adjList.keys():
			if neighbor.status == "NEW":
				self.topSorting(neighbor)
			elif neighbor.status == "ACTIVE":
				return 
		self.sortingStack.append(vertex.name)
		vertex.status = "DONE"
		return 

	def findOrder(self, numCourses, prereqs):
		"""
		find topologicSorting of the given courses
		prereqs: list of dependencies [[1,0], [2,0], [3,1]] 0->1
		numCourses: number of courses to take
		"""
		vertices = []
		for i in range(numCourses):
			# create a vertex
			vertex = Vertex(i)
			vertices.append(vertex)
		# build the edges
		for edge in prereqs:
			vertices[edge[1]].adjList[vertices[edge[0]]] = 1 # add a new edge
		g = Graph(vertices)
		return list(reversed(self.topologicSorting(g)))

class SSSP(object):
	def dijkstra(self, graph, source):
		"""
		Given a graph and a source vertex, find a shortest path to all vertices
		"""
		distances = {}
		# initialize
		for vertex in graph.vertices:
			if vertex == source:
				distances[source] = 0
			else:
				distances[vertex] = float('inf')
		# have pq of all distances
		pq = []
		heappush(pq, (distances[source], source))
		while len(pq) != 0:
			(priority, top) = heappop(pq)
			for neighbor in top.adjList.keys():
				# if tense, then relax
				if distances[top] + top.adjList[neighbor] < distances[neighbor]:
					distances[neighbor] = distances[top] + top.adjList[neighbor]
					# add the vertex into the pq
					heappush(pq, (distances[neighbor], neighbor))
		return distances


###########################   TEST    ####################################


###########################   Topological sorting   ####################################
top = TopologicalSort()
print(top.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))




