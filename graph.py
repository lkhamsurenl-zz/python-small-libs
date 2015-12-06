from collections import deque
from heapq import heappush, heappop
class Vertex(object):
	def __init__(self, value):
		self.name = value
		self.status = "NEW" # NEW, ACTIVE, DONE
		self.adjList = {} # no active neightbors for now

class Traverse(object):
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

class Tree(object):
	def minHeightTree(self, n, edges):
		"""
		Given a number n (0..n-1 vertices) and edges btw them, find a min height tree roots
		"""
		# There can be at most 2 min height tree in the tree graph.
		# They are located in the middle of the longest path in the tree
		# Longest path can be found by repeatedly removing leaves
		# We find by repeatedly removing all the leaf nodes, until there are no
		# more than 2 left
		vertices = {}
		for v in range(n):
			vertices[v] = {}
		for edge in edges:
			vertices[edge[0]][edge[1]] = 1 # add a edge 
			vertices[edge[1]][edge[0]] = 1 # 
		while n > 2:
			# find all the leaves 
			leaves = []
			for v in vertices.keys():
				if len(vertices[v]) == 1:
					leaves.append(v)
			for leaf in leaves:
				for neighbor in vertices[leaf].keys():
					vertices[neighbor].pop(leaf, None)
				# remove leaf from list of vertices
				vertices.pop(leaf, None)
			n -= len(leaves)
		return vertices.keys()


###########################   TEST    ####################################


###########################   Topological sorting   ####################################
top = TopologicalSort()
for (l, n, w) in [ ([[1,0],[2,0],[3,1],[3,2]], 4, [[0, 1,2,3], [0,2,1,3]]) ]:
	got = top.findOrder(n, l)
	assert got in w, \
		"findOrder({}, {}) = {}; want {}".format(n, l, got, want)

#############					Min height tree 			#################
tree = Tree()
for (n, edges, want) in [ (2, [[0,1]], [0,1]), (3, [[0,1],[1,2]], [1]), (6, [[0,3],[1,3],[2,3],[3,4],[4,5]], [3,4]) ]:
	got = tree.minHeightTree(n, edges)
	assert got == want, \
		"minHeightTree({}, {}) = {}; want {}".format(n, edges, got, want)




