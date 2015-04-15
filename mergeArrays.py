class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        # have two different indices keeping track of the position
        # if the elt in B is smaller, then swap it with the element in A

        # if hit the last of B, then done
        index2 = n-1 # end of B
        index1 = m - n-1 # last valid index of A
        index = m -1 # end of A
        while index2 >=0 and index1 >= 0:
            if A[index1] < B[index2]:
                A[index] = B[index2]
                index2 = index2 -1
                index = index -1
            else:
                A[index] = A[index1]
                index1 = index1 - 1
                index = index - 1
        while index2 >= 0:
            A[index] = B[index2]
            index2 = index2 -1
            index = index -1


sol = Solution()

listA = [[1,2,3,0,0,0], [1,0], [0]]
listB = [[1,2,3], [2], [1]]

for i in range(len(listA)):
    A = listA[i]
    B = listB[i]
    sol.merge(A, len(A), B, len(B))
    print("solution1: {}".format(A))
