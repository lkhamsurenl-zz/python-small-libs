# Given 2d grid of islands and water, represented as 1s and 0s, find number of islands
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        # use sets to represent each island
        islands = [] # list of sets
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i - 1 >= 0 and grid[i - 1][j] == 1: # should be in same
                        for s in islands:
                            if grid[i - 1][j] in s:
                                s.append(grid[i][j])
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        for s in islands:
                            if grid[i][j -1] in s:
                                s.append(grid[i][j])
                        # check if they are different sets
                        if i - 1 >= 0 and grid[i - 1][j] == 1:
                            for s in islands:
                                if (grid[i][j-1] in s and grid[i -1][j] not in s) or (grid[i][j-1] not in s and grid[i -1][j] in s):
                                    # merge them
