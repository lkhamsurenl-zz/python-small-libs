class Solution:
    # @param A, a list of integers
    # @return an integer, which is the first missing positive number
    def firstMissingPositive(self, A):
        # we place numbers in correct place by swapping
        i = 0
        while i < len(A):
            if A[i] <= 0 or A[i] > len(A) or A[i] == i + 1 or (A[i] == A[A[i] - 1]):
                # no correct place; already in correct place, or
                # swapping two numbers are same
                i = i + 1
            else:
                # put it in the index A[i] - 1
                temp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = temp
        # We check if there is a number which is out of its index
        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
        # no number is missing, so we return len(A) + 1, since 1 to len(A) exist
        return len(A) + 1

sol = Solution()
print sol.firstMissingPositive([-2, 4, 3])
print sol.firstMissingPositive([3, 1, 2])
print sol.firstMissingPositive([1, 2, 0])
print sol.firstMissingPositive([1, 1])
