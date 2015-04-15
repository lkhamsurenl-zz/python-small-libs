import itertools, copy
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        candidates = [i for i, _ in itertools.groupby(candidates)]
        return self.recComb(candidates, target)

    def recComb(self, candidates, target):
        #print("new rec call: {} {}".format(candidates, target))
        if target == 0:
            return [[]]
        elif len(candidates) == 0 or target < 0:
            return None
        largest = candidates[-1] # largest num in the list
        numOf = target / largest
        currSol = []
        for i in range(numOf + 1):
            #print i
            #print("new cand: {} and target: {}".format(candidates, target - i * largest ))
            newCand = copy.deepcopy(candidates)
            newCand.pop()
            recSol = self.recComb(newCand, target - i * largest)
            if recSol is not None:
                #print ("recSOl: {}".format(recSol))
                for sol in recSol:
                    #print "inside"
                    newSol = copy.deepcopy(sol)
                    newSol.extend([largest] * i) # add i times
                    currSol.append(newSol)
        if currSol == []:
            return None
        return [i for i, _ in itertools.groupby(currSol)]

sol = Solution()
print sol.combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73], 310)
