from sets import Set
import itertools
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        lst = [] # contains all the elements add up to 0
        length = len(num)
        # sort the array
        sortedArr = sorted(num)
        for i in range(length):
            # sum of the remaining two elts should add up to -num[i]
            lowIndex = i+1
            highIndex = length -1
            while lowIndex < highIndex:
                if sortedArr[lowIndex] + sortedArr[highIndex] + sortedArr[i] == 0:
                    lst.append([sortedArr[i], sortedArr[lowIndex], sortedArr[highIndex]])
                    lowIndex = lowIndex + 1
                    highIndex = highIndex - 1
                elif sortedArr[lowIndex] + sortedArr[highIndex] + sortedArr[i] < 0:
                    lowIndex = lowIndex + 1
                else:
                    highIndex = highIndex - 1

        # learn how to use itertools dude
        lst.sort()
        return list(k for k, _ in itertools.groupby(lst))

sol = Solution()
print (sol.threeSum([-1, 0 , 1, -2, 2, 3, -3]))
