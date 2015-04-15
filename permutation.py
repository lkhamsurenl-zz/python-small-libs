import copy
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0:
            return []
        return self.recPermute(num, 0)

    def recPermute(self, num, ind):
        if ind == len(num)  -1:
            return [[num[ind]]] # base case is just a one list with one elt
        recList = self.recPermute(num, ind + 1)
        currList = []
        for inList in recList: # inList is a list of numbers representing one permutation of ind+ 1, len -1
            # For each list, we need to insert num[ind] in all possible positions

            for i in range(len(inList)):
                currInList = copy.deepcopy(inList) # make a copy of current list
                currInList.insert(i, num[ind])
                currList.append(currInList)
            currInList= copy.deepcopy(inList)
            currInList.append(num[ind])
            currList.append(currInList)
        return currList

sol = Solution()
for num in [[1, 2, 3] , [1, 2, 3,4], [1,2]]:
    print("permutation of {} is {}".format(num, sol.permute(num)))
