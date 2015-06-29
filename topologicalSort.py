class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    nextNum = 0
    prereq = {}

    def findOrder(self, numCourses, prerequisites):
        self.order = [-2 for i in range(numCourses + 1)] # all vertices are new state
        self.nextNum = numCourses - 1
        # build the edge
        for edge in prerequisites:
            if edge[1] not in self.prereq:
                self.prereq[edge[1]] = [edge[0]] # add a new edge
            else:
                self.prereq[edge[1]].append(edge[0])
        self.prereq[numCourses] = [i for i in range(numCourses)] # numCOurses to i

        return self.order[:numCourses] if self.topologicalOrd(numCourses) else []
    # do topological ordering
    def topologicalOrd(self, vertex):
        self.order[vertex] = -1 # active
        if vertex in self.prereq:
            for neighbor in self.prereq[vertex]:
                if self.order[neighbor] == -1:
                    return False # there is no ordering
                elif self.order[neighbor] == -2: # new
                    if not self.topologicalOrd(neighbor):
                        return False # it's not possible to DAG
        self.order[vertex] = self.nextNum # give a ordering
        self.nextNum = self.nextNum - 1  # next available num
        return True

sol = Solution()
print sol.findOrder(2, [[1,0]])
