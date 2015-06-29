class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        self.order = [-2 for i in range( numCourses + 1)] # array of which order in DAG
        self.adj = {} # graph representation
        for arc in prerequisites:
            if arc[1] not in self.adj:
                self.adj[arc[1]] = [arc[0]]
            else:
                self.adj[arc[1]].append(arc[0])
        self.adj[numCourses] = range(numCourses) # add new vertex adjacent to all vertices
        self.lastNum = numCourses # DAG order
        return self.dfs(numCourses) # run dfs on new vertex

    # dfs algorithm
    def dfs(self, i):
        self.order[i] = -1 # active rather than new
        if i in self.adj:
            for neighbor in self.adj[i]:
                if self.order[neighbor] == -2: # new
                    self.dfs(neighbor)
                elif self.order[neighbor] == -1: # still active
                    return False
        self.order[i] = self.lastNum # done
        self.lastNum = self.lastNum - 1
        return True

sol = Solution()
print sol.canFinish(3, [[1, 0], [2, 1], [0, 2]])
