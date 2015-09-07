from collections import deque
from heapq import heappush, heappop
class Vertex(object):
	def __init__(value):
		self.name = value
		self.status = "NEW" # NEW, ACTIVE, DONE
		self.adjList = {} # no active neightbors for now

class Edge(object):
	def __init__(s, d, value):
		self.weight = value
		self.start = s
		self.destination = d

class Graph(object):
	def __init__(vertices, edges):
		self.vertices = vertices
		self.edges = edges

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

	def topologicSorting(self, graph):
		"""
		Topological sorting for graph
		"""
		# add a new vertex connecting to all the vertex in the graph
		new_source = Vertex(-1)
		for vertex in graph.vertices:
			new_source.adjList[vertex] = 0 # add new edge there
		# do topSorting for starting from the new_source
		return self.topSorting(new_source)

	def topSorting(self, vertex):
		"""
		top sorting starting @ vertex
		"""
		vertex.status = "ACTIVE"
		for neighbor in vertex.adjList.keys():
			if neighbor.status == "NEW":
				self.topSorting(neighbor)
			elif neighbor.status == "DONE":
				return 
		vertex.status = "DONE"
		print(vertex.name)
		return 
 
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




