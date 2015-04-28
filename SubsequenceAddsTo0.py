# find if there is any subsequence adds up to 0
class Solution:
    def sub(self, A):
        if len(A) == 0:
            return False
        if A[0] == 0:
            return True
        sumsDic = {A[0]: 1}
        lastSum = A[0] # keep track of the last sum
        for i in range(1, len(A)):
            newSum = lastSum + A[i] # get sum adding last one
            if newSum in sumsDic or newSum == 0:
                return True  # If A[0] + .. + A[j - 1] == A[0] + .. A[i]
                            # then A[j] + .. + A[i] = 0
            else:
                sumsDic[newSum] = 1
                lastSum = newSum # update last sum
        return False

sol = Solution()
for arr in [[], [1,2,3], [1, 2, -3], [1,2,3,2], [1,-1,3,-3], [0], [1,0], [0,1]]:
    print("{} : {}".format(arr, sol.sub(arr)))
