import math
# Given [1, ..., n] find kth number in the permutaiton of the list
class Solution:
    # @param n, an integer
    # @param k, an integer
    # @return a string
    def getPermutation(self, n, k):
        return self.recPerm([i for i in range(1, n + 1)], k)
    def recPerm(self, lst, k):
        if k == 0:
            return "".join(map(str, lst))
        n = len(lst)
        fac = math.factorial(n - 1)
        firstDigInd = k / fac  # first digit index in list
        firstDig = lst[firstDigInd]
        lst.remove(lst[firstDigInd]) # remove the digit
        return str(firstDig) + self.recPerm(lst, k - fac * firstDigInd)

sol = Solution()
for n in [3, 4, 5]:
    for k in range(math.factorial(n)):
        print("{} perm in 1 to {} is {}".format(k, n, sol.getPermutation(n, k)))
