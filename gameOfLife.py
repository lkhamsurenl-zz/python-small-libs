import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # can we do the update using some sort of memory first with O(n) memory
        if len(board) == 0:
            return
        prev_row = [0 for i in range(len(board[0]))] # empty at the start to reprenet nothing is there
        old_row = [0 for i in range(len(board[0]))] # current row used, update in place
        for row in range(len(board)):
            self.updateRow(board, row, prev_row, old_row)
        return 
    
    def updateRow(self, board, row,  prev_row, old_row):
        # update the old_row with current values
        for col in range(len(board[0])):
            old_row[col] = board[row][col]
        # update cell values with current and prev rows usage
        for col in range(len(board[0])):
            self.updateCell(board, row, col, prev_row, old_row)
        # prev_row should be updated
        for i in range(len(old_row)):
            prev_row[i] = old_row[i]
            
    # update single cell
    def updateCell(self, board, row, col, prev_row, old_row):
        if board[row][col] == 1:
            # number of alive should be exactly 2 or 3
            alive = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if not (i == 0 and j == 0) and 0 <= row + i <len(board) and 0 <= col + j < len(board[0]):
                        if i < 0 and row != 0 and prev_row[col + j] == 1:
                            alive += 1
                        elif i == 0 and old_row[col + j] == 1:
                            alive += 1
                        elif i > 0 and board[row + i][col + j] == 1:
                            alive += 1
            if alive < 2 or alive > 3:
                board[row][col] = 0
        else:
            alive = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if not (i == 0 and j == 0) and 0<=row + i<len(board) and 0 <= col + j < len(board[0]):
                        if i < 0 and row != 0 and prev_row[col + j] == 1:
                            alive += 1
                        elif i == 0 and old_row[col + j] == 1:
                            alive += 1
                        elif i > 0 and board[row + i][col + j] == 1:
                            alive += 1
            if alive == 3:
                board[row][col] = 1

sol = Solution()
board = [[0,1], [1,1]]
sol.gameOfLife(board)
print(board)