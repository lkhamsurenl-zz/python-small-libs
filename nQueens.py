import copy, itertools
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        if n == 0:
            return None
        listOfSol = self.recPlaceQueens(n, n)
        solInStr = []
        for sol in listOfSol:
            solInStr.append(self.inStringForm(sol, n))
        return solInStr

    def recPlaceQueens(self, n, k):
        if k == 0:
            return [[]] # only one possible configuration
        recSol = self.recPlaceQueens(n, k - 1) # list of numbers [0 , 1, 2]
        sol = []
        for config in recSol:
            for col in range(n):
                if self.isSafe(col, config):
                    curr = copy.deepcopy(config)
                    curr.append(col)
                    sol.append(curr) # current solution
        # remove the duplicates
        return [i for i, _ in itertools.groupby(sol)]

    def isSafe(self, col, config):
        row = len(config)
        for queenRow in range(len(config)):
            queenCol = config[queenRow]
            if queenCol == col or abs(col - queenCol) == row - queenRow:
                return False
        return True
    def inStringForm(self, sol, n):
        lst = []
        for row in range(n):
            col = sol[row]
            string = ["." for i in range(n)]
            string[col] = 'Q'
            lst.append("".join(string))
        return lst
sol = Solution()
print sol.solveNQueens(6)
