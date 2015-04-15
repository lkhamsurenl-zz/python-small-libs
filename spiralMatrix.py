class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        height = len(matrix)
        if height  == 0:
            return []
        width = len(matrix[0])
        lowHeight = 0
        highHeight = height -1
        lowWidth = 0
        highWidth = width -1
        direction = 0 # going right
        currList = []
        while lowWidth <= highWidth and lowHeight <= highHeight:
            if direction == 0: # going right
                col = lowWidth
                while col <= highWidth:
                    currList.append(matrix[lowHeight][col])
                    col = col + 1
                lowHeight = lowHeight + 1
            elif direction == 1:
                row = lowHeight
                while row <= highHeight:
                    currList.append(matrix[row][highWidth])
                    row = row + 1
                highWidth  = highWidth - 1
            elif direction == 2:
                col = highWidth
                while col >= lowWidth:
                    currList.append(matrix[highHeight][col])
                    col = col -1
                highHeight = highHeight - 1
            else:
                row = highHeight
                while row >= lowHeight:
                    currList.append(matrix[row][lowWidth])
                    row = row - 1
                lowWidth = lowWidth + 1
            direction = (direction + 1) % 4
        return currList

sol = Solution()
matrix = [[i for i in range(3)] for i in range(4)]
print sol.spiralOrder(matrix)
