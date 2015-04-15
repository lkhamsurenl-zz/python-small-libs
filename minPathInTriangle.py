import copy
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        MSP = copy.deepcopy(triangle)
        #non-base case:
        for i in range(len(MSP) -2, -1, -1):
            innerList = triangle[i]
            for j in range(len(innerList) -1, -1 , -1):
                print (i, j)
                if i + 1 < len(MSP):
                    MSP[i][j] = innerList[j] + MSP[i+ 1][j]
                    print( "i + 1, j : {}".format(MSP[i][j]))
                if i + 1 < len(MSP) and j  < len(innerList):
                    MSP[i][j] = min(MSP[i][j], innerList[j] + MSP[i + 1][j + 1])
                    print MSP[i][j]

        return MSP[0][0]

sol = Solution()
print sol.minimumTotal([[-1], [-2, -3]])
