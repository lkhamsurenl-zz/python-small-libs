from collections import deque
from heapq import heappush, heappop
class Vertex(object):
	def __init__(self, value):
		self.name = value
		self.status = "NEW" # NEW, ACTIVE, DONE
		self.adjList = {} # no active neightbors for now

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
		ordering = []
		while len(q) != 0:
			top = q.pop()
			ordering.append(top.name)
			# DO something with current vertex here
			for neighbor in top.adjList.keys():
				if neighbor.status == "DONE":
					return 
				elif neighbor.status == "NEW":
					# add to the queue
					q.appendleft(neighbor)
		return 

class TopologicalSort(object):
	def topologicSorting(self, vertices):
		"""
		Topological sorting for graph
		"""
		s = [] # topological sorting stack
		# add a new vertex connecting to all the vertex in the graph
		new_source = Vertex(-1)
		for vertex in vertices:
			new_source.adjList[vertex] = 0 # add new edge there
		# do topSorting for starting from the new_source
		self.topSorting(new_source, s)
		return s[:-1] # the last one is the artificial vertex added

	def topSorting(self, vertex, s):
		"""
		top sorting starting @ vertex
		"""
		vertex.status = "ACTIVE"
		for neighbor in vertex.adjList.keys():
			if neighbor.status == "NEW":
				self.topSorting(neighbor, s)
			elif neighbor.status == "ACTIVE":
				return 
		vertex.status = "DONE"
		s.append(vertex.name) # add the vertex when done
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
		return list(reversed(self.topologicSorting(vertices)))

class SSSP(object):
	def dijkstra(self, vertices, source):
		"""
		Given a graph and a source vertex, find a shortest path to all vertices
		"""
		d = {}
		# initialize
		for vertex in graph.vertices:
			if vertex == source:
				d[source] = 0
			else:
				d[vertex] = float('inf')
		# have pq of all distances
		pq = []
		heappush(pq, (d[source], source))
		while len(pq) != 0:
			(priority, top) = heappop(pq)
			for neighbor in top.adjList.keys():
				# if tense, then relax
				if d[top] + top.adjList[neighbor] < d[neighbor]:
					d[neighbor] = d[top] + top.adjList[neighbor]
					# add the vertex into the pq
					heappush(pq, (d[neighbor], neighbor))
		return d
		
	def shimbel(self, vertices, s):
		"""
		Shimbel DP algo for finding SSSP
		"""
		d = {}
		d[s] = 0
		for v in vertices:
			if v != s:
				d[v] = float('inf')
		for i in range(len(vertices)):
			for u in vertices:
				for v in u.adjList.keys():
					if d[u] + u.adjList[v] < d[v]:
						d[v] = d[u] + u.adjList[v]
		return d


###########################   TEST    ####################################


###########################   Topological sorting   ####################################
top = TopologicalSort()
for (l, n, w) in [ ([[1,0],[2,0],[3,1],[3,2]], 4, [[0, 1,2,3], [0,2,1,3]]) ]:
	got = top.findOrder(n, l)
	assert got in w, \
		"findOrder({}, {}) = {}; want {}".format(n, l, got, want)




