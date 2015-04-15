import itertools, copy
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        return self.recComb(candidates, target)

    def recComb(self, candidates, target):
        print("new rec call: {} {}".format(candidates, target))
        if target == 0:
            return [[]]
        elif len(candidates) == 0 or target < 0:
            return None
        largest = candidates[-1] # largest num in the list
        currSol = []
        for i in range(2):
            print i
            print("new cand: {} and target: {}".format(candidates, target - i * largest ))
            newCand = copy.deepcopy(candidates)
            newCand.pop()
            recSol = self.recComb(newCand, target - i * largest)
            if recSol is not None:
                print ("recSOl: {}".format(recSol))
                for sol in recSol:
                    print "inside"
                    newSol = copy.deepcopy(sol)
                    newSol.extend([largest] * i) # add i times
                    currSol.append(newSol)
        if currSol == []:
            return None
        return list(i for i,_ in itertools.groupby(currSol))

sol = Solution()
print sol.combinationSum([34,34,29,29,31,30,7,22,13,28,33,13,6,14,31,25,17,7,6,9,12,7,7,11,6,33,24,8,18,26,5,9,17,29,33,13,24,28,22,25,21,20,25,23,29,22,13,11,24,6,7,23,30,10,21,32,8,10,27,13,23,19,17,5], 21)
