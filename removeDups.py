class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return A
        removedIndex = 0 # 1st element is never actually duplicate
        for i in range(1, len(A)):
            if A[removedIndex] != A[i]:
                A[removedIndex + 1] = A[i]
                removedIndex = removedIndex + 1
            i = i + 1
        return A   # this is number of duplicated eltes

sol = Solution()
for arr in [[1 , 2, 2, 3], [1,1,1,1,2,2,2,3,3,5,7,8]]:
    print ("no dup version of {}: {}".format(arr, sol.removeDuplicates(arr)))
print("a ")
