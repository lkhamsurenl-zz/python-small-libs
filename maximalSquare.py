class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        MS = [[[0 for w in range(n + 1)] for j in range(n)] for i in range(n)]
        # base
        for i in range(n):
            for j in range(n):
                MS[i][j][1] = int(matrix[i][j])
        # recursive
        for w in range(2, n + 1):
            for j in range(n-2, -1, -1):
                for i in range(n-2, -1, -1):
                    MS[i][j][w] = MS[i][j][w-1]==1 and MS[i+1][j][w-1]==1 and MS[i][j+1][w-1]==1 and MS[i+1][j+1][w-1]==1
                
        maximal = 0        
        for w in range(n + 1):
            for j in range(n):
                for i in range(n):
                    if MS[i][j][w] == 1:
                        maximal = max(maximal, w * w)
        return maximal

# TEST ####
sol = Solution()

print("Maximal Square test")

assert(1 == sol.maximalSquare(["01", "10"]))

assert(4 == sol.maximalSquare(["110", "110", "000"]))

assert(1 == sol.maximalSquare(["100", "110", "000"]))

assert(4 == sol.maximalSquare(["111", "111", "000"]))

assert(4 == sol.maximalSquare(["011", "011", "000"]))

assert(9 == sol.maximalSquare(["111", "111", "111"]))




